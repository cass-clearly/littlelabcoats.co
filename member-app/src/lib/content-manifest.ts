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
