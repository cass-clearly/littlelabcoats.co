#!/usr/bin/env python3
import json
import re
import subprocess
import sys
from html import unescape
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LESSON_DIR = REPO_ROOT / "lesson-plans"
OUTPUT_PATH = LESSON_DIR / "_generated" / "lesson-index-data.json"

EXCLUDED_NAME_SUBSTRINGS = {
    "refcard",
    "quiz",
    "worksheet",
    "competitor-analysis",
    "daario-",
    "mia-",
    "audit",
    "review",
    "manifest",
    "document-id-manifest",
    "shareable-manifest",
    "style-guide",
    "public-mapping-and-publish-prep",
}

EXCLUDED_SLUGS = {
    "gr4-ls1-unit1-l1-food-webs",
    "how-to-save-and-print",
    "index",
    "landing-page",
    "science-curriculum-business-plan",
    "template",
}

GRADE_LABELS = {
    "k": "Kindergarten",
    "1": "Grade 1",
    "2": "Grade 2",
    "3": "Grade 3",
    "4": "Grade 4",
    "5": "Grade 5",
}

DOMAIN_LABELS = {
    "ps": "Physical Science",
    "ls": "Life Science",
    "ess": "Earth & Space Science",
    "ets": "Engineering",
}

GRADE_ORDER = {"k": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
DOMAIN_ORDER = {"ps": 0, "ls": 1, "ess": 2, "ets": 3}

TITLE_TAG_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
WHITESPACE_RE = re.compile(r"\s+")
STRUCTURED_RE = re.compile(
    r"^(?P<prefix>k|gr\d+)-(?P<domain>ps|ls|ess|ets)\d*-(?:unit(?P<unit>\d+)-)?(?:lesson|l)(?P<lesson>\d+)-(?P<rest>.+)$",
    re.IGNORECASE,
)
UNIT_OVERVIEW_RE = re.compile(
    r"^(?P<prefix>k|gr\d+)-(?P<domain>ps|ls|ess|ets)\d*-(?:unit(?P<unit>\d+)-)?(?P<rest>.+)$",
    re.IGNORECASE,
)
LEGACY_UNIT_RE = re.compile(r"^unit(?P<unit>\d+)-(?:lesson|l)(?P<lesson>\d+)-(?P<rest>.+)$", re.IGNORECASE)
FREE_RE = re.compile(r"^free-(?:(?P<freeprefix>k|gr\d+|\d+th)-)?(?P<rest>.+)$", re.IGNORECASE)
FIFTH_RE = re.compile(r"^(?P<grade>\d+)th-(?P<rest>.+)$", re.IGNORECASE)


def should_include(path: Path) -> bool:
    if path.suffix.lower() != ".html":
        return False
    slug = path.stem.lower()
    if slug in EXCLUDED_SLUGS:
        return False
    return not any(token in slug for token in EXCLUDED_NAME_SUBSTRINGS)


def read_title(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    match = TITLE_TAG_RE.search(text)
    if not match:
        return None
    title = unescape(match.group(1)).strip()
    title = WHITESPACE_RE.sub(" ", title)
    return title or None


def humanize_slug(rest: str) -> str:
    return " ".join(part.capitalize() if part.lower() not in {"and", "or", "the", "a", "an", "of", "to", "for", "in", "on", "with"} else part.lower() for part in rest.split("-"))


def is_metadata_title_chunk(chunk: str) -> bool:
    normalized = chunk.strip().lower()
    metadata_markers = [
        "lesson",
        "unit",
        "grade",
        "kindergarten",
        "little lab coats",
        "physical science",
        "life science",
        "earth science",
        "earth & space science",
        "engineering",
        "free lesson",
        "freebie",
        "k-ps",
        "k-ls",
        "k-ess",
        "k-ets",
    ]
    return any(marker in normalized for marker in metadata_markers)


def clean_display_title(title: str | None, slug: str) -> str:
    if not title:
        return humanize_slug(slug)

    cleaned = title.strip()

    if "|" in cleaned:
        cleaned = cleaned.split("|", 1)[0].strip()

    parts = [part.strip() for part in cleaned.split(" — ") if part.strip()]
    while len(parts) > 1 and is_metadata_title_chunk(parts[-1]):
        parts.pop()
    cleaned = " — ".join(parts)

    cleaned = re.sub(r"^Archived\s+", "", cleaned, flags=re.IGNORECASE)
    cleaned = WHITESPACE_RE.sub(" ", cleaned).strip(" -—|")
    return cleaned or humanize_slug(slug)


def parse_grade_prefix(prefix: str | None) -> tuple[str | None, str | None]:
    if not prefix:
        return None, None
    normalized = prefix.lower()
    if normalized == "k":
        return "k", GRADE_LABELS["k"]
    if normalized.startswith("gr"):
        grade_number = normalized[2:]
        return grade_number, GRADE_LABELS.get(grade_number, f"Grade {grade_number}")
    if normalized.endswith("th") and normalized[:-2].isdigit():
        grade_number = normalized[:-2]
        return grade_number, GRADE_LABELS.get(grade_number, f"Grade {grade_number}")
    return None, None


def parse_metadata(slug: str) -> dict:
    metadata = {
        "gradeKey": None,
        "gradeLabel": "Other Lessons",
        "domainKey": None,
        "domainLabel": "Other Lessons",
        "unitNumber": None,
        "lessonNumber": None,
        "isFreeSample": slug.startswith("free-"),
        "bucket": "other-lessons",
        "sourcePattern": "standalone",
    }

    match = STRUCTURED_RE.match(slug)
    if match:
        grade_key, grade_label = parse_grade_prefix(match.group("prefix"))
        domain_key = match.group("domain").lower()
        unit_number = int(match.group("unit")) if match.group("unit") else None
        lesson_number = int(match.group("lesson"))
        metadata.update(
            {
                "gradeKey": grade_key,
                "gradeLabel": grade_label or "Other Lessons",
                "domainKey": domain_key,
                "domainLabel": DOMAIN_LABELS.get(domain_key, "Other Lessons"),
                "unitNumber": unit_number,
                "lessonNumber": lesson_number,
                "bucket": f"{(grade_key or 'other')}-{domain_key}",
                "sourcePattern": "structured",
            }
        )
        return metadata

    match = LEGACY_UNIT_RE.match(slug)
    if match:
        metadata.update(
            {
                "gradeKey": "k",
                "gradeLabel": GRADE_LABELS["k"],
                "unitNumber": int(match.group("unit")),
                "lessonNumber": int(match.group("lesson")),
                "bucket": "k-other",
                "sourcePattern": "legacy-kindergarten-unit",
            }
        )
        return metadata

    match = FREE_RE.match(slug)
    if match and match.group("freeprefix"):
        grade_key, grade_label = parse_grade_prefix(match.group("freeprefix"))
        metadata.update(
            {
                "gradeKey": grade_key,
                "gradeLabel": grade_label or "Other Lessons",
                "bucket": f"{(grade_key or 'other')}-free-samples",
                "sourcePattern": "free-sample",
            }
        )
        return metadata

    match = UNIT_OVERVIEW_RE.match(slug)
    if match:
        grade_key, grade_label = parse_grade_prefix(match.group("prefix"))
        domain_key = match.group("domain").lower()
        unit_number = int(match.group("unit")) if match.group("unit") else None
        metadata.update(
            {
                "gradeKey": grade_key,
                "gradeLabel": grade_label or "Other Lessons",
                "domainKey": domain_key,
                "domainLabel": DOMAIN_LABELS.get(domain_key, "Other Lessons"),
                "unitNumber": unit_number,
                "bucket": f"{(grade_key or 'other')}-{domain_key}",
                "sourcePattern": "unit-overview",
            }
        )
        return metadata

    match = FIFTH_RE.match(slug)
    if match:
        grade_key, grade_label = parse_grade_prefix(f"gr{match.group('grade')}")
        metadata.update(
            {
                "gradeKey": grade_key,
                "gradeLabel": grade_label or "Other Lessons",
                "bucket": f"{(grade_key or 'other')}-other",
                "sourcePattern": "legacy-grade-slug",
            }
        )
        return metadata

    return metadata


def sort_key(entry: dict):
    grade_rank = GRADE_ORDER.get(entry["gradeKey"], 999)
    domain_rank = DOMAIN_ORDER.get(entry["domainKey"], 999)
    unit_rank = entry["unitNumber"] if entry["unitNumber"] is not None else 999
    lesson_rank = entry["lessonNumber"] if entry["lessonNumber"] is not None else 999
    free_rank = 1 if entry["isFreeSample"] else 0
    return (
        grade_rank,
        domain_rank,
        unit_rank,
        lesson_rank,
        free_rank,
        entry["displayTitle"].lower(),
        entry["slug"],
    )


def build_groups(entries: list[dict]) -> list[dict]:
    groups = {}
    for entry in entries:
        key = (entry["gradeLabel"], entry["domainLabel"])
        groups.setdefault(key, []).append(entry)

    grouped = []
    for (grade_label, domain_label), group_entries in sorted(
        groups.items(),
        key=lambda item: (
            GRADE_ORDER.get(next((e["gradeKey"] for e in item[1] if e["gradeKey"] is not None), None), 999),
            DOMAIN_ORDER.get(next((e["domainKey"] for e in item[1] if e["domainKey"] is not None), None), 999),
            item[0][0].lower(),
            item[0][1].lower(),
        ),
    ):
        grouped.append(
            {
                "gradeLabel": grade_label,
                "domainLabel": domain_label,
                "count": len(group_entries),
                "entries": group_entries,
            }
        )
    return grouped


def main() -> None:
    entries = []
    scanned_files = sorted(path for path in LESSON_DIR.glob("*.html") if should_include(path))

    for path in scanned_files:
        slug = path.stem
        title = read_title(path)
        metadata = parse_metadata(slug)
        display_title = clean_display_title(title, slug)
        entry = {
            "slug": slug,
            "sourcePath": str(path.relative_to(REPO_ROOT)),
            "canonicalUrl": f"/lesson-plans/{slug}.html",
            "reviewUrl": f"/lesson-plans/{slug}.html?review=1",
            "title": title or display_title,
            "displayTitle": display_title,
            **metadata,
        }
        entries.append(entry)

    entries.sort(key=sort_key)
    groups = build_groups(entries)

    output = {
        "sourceDirectory": "lesson-plans",
        "sourcePattern": "lesson-plans/*.html",
        "excludedNameSubstrings": sorted(EXCLUDED_NAME_SUBSTRINGS),
        "entryCount": len(entries),
        "entries": entries,
        "groups": groups,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    render_script = REPO_ROOT / "scripts" / "render-lesson-index-page.py"
    subprocess.run([sys.executable, str(render_script)], check=True)
    print(f"Wrote {len(entries)} lesson entries to {OUTPUT_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
