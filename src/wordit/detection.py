"""Find Bible references inside spoken or typed text."""

import re

from wordit.reference import Reference

BOOKS = (
    "Genesis",
    "Psalm",
    "John",
    "Romans",
    "Song of Solomon",
    "1 Chronicles",
    "Matthew",
)

REFERENCE_PATTERN = re.compile(r"\b(" + "|".join(BOOKS) + r")\s+(\d+):(\d+)")


def find_references(text: str) -> list[Reference]:
    """Return every Bible reference found in the text in order."""
    references = []
    for match in REFERENCE_PATTERN.finditer(text):
        references.append(
            Reference((match.group(1)), int(match.group(2)), int(match.group(3)))
        )
    return references
