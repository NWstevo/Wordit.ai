import pytest

from wordit.kjv_import import clean_verse_text, build_books


@pytest.mark.parametrize(
    "raw, expected",
    [
        ("# For God so loved the world", "For God so loved the world"),
        ("The LORD [is] my shepherd", "The LORD is my shepherd"),
        ("In the beginning God created", "In the beginning God created"),
    ],
)
def test_clean_verse_text_removes_source_markers(raw, expected):
    assert clean_verse_text(raw) == expected


def test_build_books_uses_the_detector_name_for_song_of_solomon():
    source = {"Solomon's Song 1:1": "The song of songs"}
    assert "Song of Solomon" in build_books(source)


def test_build_books_nests_verses_by_book_chapter_and_verse():
    source = {"John 3:16": "#For God so loved the world"}
    assert build_books(source) == {"John": {"3": {"16": "For God so loved the world"}}}
