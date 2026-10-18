from pathlib import Path
import json


class Bible:
    def __init__(self, data):
        self.data = data

    @classmethod
    def from_file(cls, path):
        with Path(path).open(encoding="utf8") as f:
            data = json.load(f)
        return cls(data)

    def verse(self, book: str, chapter: int, number: int) -> str:
        try:
            return self.data["books"][book][str(chapter)][str(number)]
        except KeyError as exc:
            raise KeyError(f"Verse not found: {book} {chapter}:{number}") from exc
