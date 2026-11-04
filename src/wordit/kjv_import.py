"""Convert the public-domain KJV source file into Wordit.ai's Bible format."""

import json
from pathlib import Path

from wordit.reference import parse_reference

SOURCE_BOOK_NAMES = {"Solomon's Song": "Song of Solomon"}


def clean_verse_text(text: str) -> str:
    """Remove the paragraph marks and italic brackets from a KJV source verse."""
    return text.replace("#", "").replace("[", "").replace("]", "").strip()


def build_books(verses: dict[str, str]) -> dict[str, dict[str, dict[str, str]]]:
    """Turn the flat source verses into nested book, chapter and verse dictionaries."""

    books: dict[str, dict[str, dict[str, str]]] = {}

    for key, raw_text in verses.items():
        reference = parse_reference(key)
        book = SOURCE_BOOK_NAMES.get(reference.book, reference.book)
        chapter = str(reference.chapter)
        verse = str(reference.verse)
        if book not in books:
            books[book] = {}
        if chapter not in books[book]:
            books[book][chapter] = {}
        books[book][chapter][verse] = clean_verse_text(raw_text)
    return books


def convert_file(source_path: Path, target_path: Path) -> None:
    """read the raw Kjv source and write it as a wordit.ai Bible file."""
    with source_path.open(encoding="utf-8") as source:
        verses = json.load(source)
    bible = {"translation": "KJV", "books": build_books(verses)}

    with target_path.open("w", encoding="utf-8") as target:
        json.dump(bible, target, ensure_ascii=False)


if __name__ == "__main__":
    convert_file(Path("data/raw/kjv-verses-1769.json"), Path("data/kjv.json"))
