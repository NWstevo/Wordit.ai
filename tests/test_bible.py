import pytest
from wordit.bible import Bible, VerseNotFoundError

SAMPLE_BIBLE = "tests/data/kjv_sample.json"


@pytest.fixture
def bible():
    return Bible.from_file(SAMPLE_BIBLE)


def test_verse_returns_text_for_valid_reference(bible):
    assert bible.verse("John", 3, 16).startswith("For God so loved the world")


def test_verse_raises_for_missing_verse(bible):
    with pytest.raises(VerseNotFoundError):
        bible.verse("John", 3, 72)
