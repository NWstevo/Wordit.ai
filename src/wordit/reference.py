"""Parse Bible references such as 'John 3:16' into structured values."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Reference:
    """A Bible location: book name, chapter number, and verse number."""

    book: str
    chapter: int
    verse: int

    def __str__(self) -> str:
        """Return the reference the way people would normally write it,
        for example "Romans 8:28"."""
        return f"{self.book} {self.chapter}:{self.verse}"


def parse_reference(text: str) -> Reference:
    """Transform a reference string like John 3:16 into a Reference."""
    book, chapter_verse = text.rsplit(" ", 1)
    chapter, verse = chapter_verse.split(":")

    return Reference(book, int(chapter), int(verse))
