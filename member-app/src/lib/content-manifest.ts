import manifest from '@/data/content-manifest.json';

export type ContentManifestItem = {
  id: string;
  grade: string;
  domain: string;
  unit: string;
  previewUrl: string;
  memberAssetPath: string;
  launchIncluded: boolean;
};

export const contentManifest = manifest as ContentManifestItem[];

export function getLaunchLibraryItems() {
  return contentManifest.filter((item) => item.launchIncluded);
}
