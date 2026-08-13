from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
GRADE1_PAGES = sorted((ROOT / "lesson-plans").glob("gr1-*.html"))
PREVIEW_GATE_MARKERS = (
    'id="llcpaywall"',
    "function locklesson()",
    "preview. unlock the full lesson",
)


class Grade1CustomerPrintReadyTest(unittest.TestCase):
    def test_canonical_grade1_customer_pages_have_no_preview_gate(self):
        self.assertEqual(40, len(GRADE1_PAGES))

        gated = []
        for page in GRADE1_PAGES:
            content = page.read_text(encoding="utf-8").lower()
            if any(marker in content for marker in PREVIEW_GATE_MARKERS):
                gated.append(page.name)

        self.assertEqual([], gated, f"Direct customer pages still contain preview gates: {gated}")

    def test_canonical_grade1_customer_pages_have_print_basics(self):
        failures = []
        for page in GRADE1_PAGES:
            content = page.read_text(encoding="utf-8").lower()
            if not re.search(r"@page\s*\{[^}]*size\s*:\s*letter", content, re.DOTALL):
                failures.append(f"{page.name}: missing US Letter @page rule")
            if "mobile-print-helper.js" not in content:
                failures.append(f"{page.name}: missing mobile print fallback")
            if "break-inside: avoid" not in content or "page-break-inside: avoid" not in content:
                failures.append(f"{page.name}: missing non-splitting print treatment for cards and media")

        self.assertEqual([], failures)


if __name__ == "__main__":
    unittest.main()
