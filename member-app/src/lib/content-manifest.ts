import fs from 'node:fs';
import path from 'node:path';
import manifest from '@/data/content-manifest.json';

export type ContentManifestStatus = 'launch-ready' | 'coming-soon' | 'free-preview';

export type ContentManifestItem = {
  id: string;
  slug: string;
  title: string;
  grade: string;
  domain: string;
  unit: string;
  summary: string;
  lessonCount: number;
  format: string;
  previewUrl: string;
  memberAssetPath: string;
  launchIncluded: boolean;
  status: ContentManifestStatus;
};

export type LibraryGroup = {
  grade: string;
  items: ContentManifestItem[];
  domains: string[];
};

export type UnitLessonPreview = {
  slug: string;
  title: string;
  objective: string;
};

export const contentManifest = manifest as ContentManifestItem[];

function gradeSortValue(grade: string) {
  const match = grade.match(/(\d+)/);
  return match ? Number(match[1]) : -1;
}

export function getLaunchLibraryItems() {
  return contentManifest.filter((item) => item.launchIncluded);
}

export function getDeferredLibraryItems() {
  return contentManifest.filter((item) => !item.launchIncluded);
}

export function getLibraryOverview() {
  const launchIncluded = getLaunchLibraryItems();
  const deferredItems = getDeferredLibraryItems();
  const gradeCount = new Set(contentManifest.map((item) => item.grade)).size;

  return {
    totalItems: contentManifest.length,
    launchIncludedItems: launchIncluded.length,
    deferredItems: deferredItems.length,
    totalLessons: contentManifest.reduce((sum, item) => sum + item.lessonCount, 0),
    launchLessons: launchIncluded.reduce((sum, item) => sum + item.lessonCount, 0),
    gradeCount,
  };
}

function decodeHtml(html: string) {
  return html
    .replace(/&amp;/g, '&')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&nbsp;/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function stripTags(html: string) {
  return decodeHtml(html.replace(/<[^>]+>/g, ' '));
}

function escapeRegex(value: string) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

export function getUnitLessonPreviews(item: ContentManifestItem): UnitLessonPreview[] {
  if (!item.previewUrl.startsWith('/lesson-plans/')) {
    return [];
  }

  const lessonFile = item.previewUrl.replace('/lesson-plans/', '');
  const lessonMatch = lessonFile.match(/^(.*?)(?:lesson|l)1([^-a-z0-9].*|-.+)$/i);

  if (!lessonMatch) {
    return [];
  }

  const unitPrefix = lessonMatch[1];
  const lessonsDir = path.resolve(process.cwd(), '..', 'lesson-plans');

  if (!fs.existsSync(lessonsDir)) {
    return [];
  }

  const lessonFiles = fs
    .readdirSync(lessonsDir)
    .filter((name) => name.endsWith('.html') && new RegExp(`^${escapeRegex(unitPrefix)}(?:lesson|l)\\d+`, 'i').test(name))
    .sort((left, right) => left.localeCompare(right, undefined, { numeric: true }));

  return lessonFiles.map((name) => {
    const filePath = path.join(lessonsDir, name);
    const html = fs.readFileSync(filePath, 'utf8');
    const titleMatch = html.match(/<h1>(.*?)<\/h1>/i);
    const objectiveMatch = html.match(/<h2>[^<]*Learning Objective<\/h2><div class="objective-box"><p>(.*?)<\/p><\/div>/i);

    return {
      slug: name,
      title: stripTags(titleMatch?.[1] ?? name),
      objective: stripTags(objectiveMatch?.[1] ?? 'Learning objective coming soon.'),
    };
  });
}

export function getLibraryGroups(items: ContentManifestItem[] = contentManifest): LibraryGroup[] {
  const grouped = new Map<string, ContentManifestItem[]>();

  items.forEach((item) => {
    const existing = grouped.get(item.grade) ?? [];
    existing.push(item);
    grouped.set(item.grade, existing);
  });

  return Array.from(grouped.entries())
    .map(([grade, gradeItems]) => ({
      grade,
      items: gradeItems.sort((left, right) => left.title.localeCompare(right.title)),
      domains: Array.from(new Set(gradeItems.map((item) => item.domain))).sort(),
    }))
    .sort((left, right) => gradeSortValue(left.grade) - gradeSortValue(right.grade));
}
