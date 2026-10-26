"""Parse Bible references such as 'John 3:16' into structured values."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Reference:
    """A Bible location: book name, chapter number, and verse number."""

    book: str
    chapter: int
    verse: int


def parse_reference(text: str) -> Reference:
    """Transform a reference string like John 3:16 into a reference."""
    book, chapter_verse = text.split()
    chapter, verse = chapter_verse.split(":")

    return Reference(book, int(chapter), int(verse))
