"""Load Bible translations from JSON and look up verses."""

from pathlib import Path
import json


class VerseNotFoundError(LookupError):
    """raises when a verse does not exist in the translation"""


class Bible:
    """One Bible translation, loaded from a JSON file."""

    def __init__(self, data):
        self.data = data

    @classmethod
    def from_file(cls, path):
        """Reads a translation from a JSON file and returns a Bible."""
        with Path(path).open(encoding="utf8") as f:
            data = json.load(f)
        return cls(data)

    def verse(self, book: str, chapter: int, number: int) -> str:
        """Return the text of a verse, or raise VerseNotFoundError if it does not exist."""
        try:
            return self.data["books"][book][str(chapter)][str(number)]
        except KeyError as exc:
            raise VerseNotFoundError(
                f"Verse not found: {book} {chapter}:{number}"
            ) from exc
