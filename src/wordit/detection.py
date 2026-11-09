"""Find Bible references inside spoken or typed text."""

import re

from wordit.reference import Reference

BOOKS = (
    "Genesis",
    "Exodus",
    "Leviticus",
    "Numbers",
    "Deuteronomy",
    "Joshua",
    "Judges",
    "Ruth",
    "1 Samuel",
    "2 Samuel",
    "1 Kings",
    "2 Kings",
    "1 Chronicles",
    "2 Chronicles",
    "Ezra",
    "Nehemiah",
    "Esther",
    "Job",
    "Psalms",
    "Proverbs",
    "Ecclesiastes",
    "Song of Solomon",
    "Isaiah",
    "Jeremiah",
    "Lamentations",
    "Ezekiel",
    "Daniel",
    "Hosea",
    "Joel",
    "Amos",
    "Obadiah",
    "Jonah",
    "Micah",
    "Nahum",
    "Habakkuk",
    "Zephaniah",
    "Haggai",
    "Zechariah",
    "Malachi",
    "Matthew",
    "Mark",
    "Luke",
    "John",
    "Acts",
    "Romans",
    "1 Corinthians",
    "2 Corinthians",
    "Galatians",
    "Ephesians",
    "Philippians",
    "Colossians",
    "1 Thessalonians",
    "2 Thessalonians",
    "1 Timothy",
    "2 Timothy",
    "Titus",
    "Philemon",
    "Hebrews",
    "James",
    "1 Peter",
    "2 Peter",
    "1 John",
    "2 John",
    "3 John",
    "Jude",
    "Revelation",
)

REFERENCE_PATTERN = re.compile(
    r"\b("
    + "|".join(BOOKS)
    + r")\s+(?:chapter\s+)?(\d+)(?::|\s+(?:from\s+)?verse\s+)(\d+)",
    re.IGNORECASE,
)
OFFICIAL_NAMES = {book.lower(): book for book in BOOKS}


def find_references(text: str) -> list[Reference]:
    """Return every Bible reference found in the text in order."""
    references = []
    for match in REFERENCE_PATTERN.finditer(text):
        references.append(
            Reference(
                OFFICIAL_NAMES[match.group(1).lower()],
                int(match.group(2)),
                int(match.group(3)),
            )
        )
    return references
