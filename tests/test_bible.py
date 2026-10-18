import pytest
from wordit.bible import Bible

sample_bible = "tests/data/kjv_sample.json"


def test_verse_returns_text_for_valid_reference():
    bible = Bible.from_file(sample_bible)
    assert bible.verse("John", 3, 16).startswith("For God so loved the world")


def test_verse_raises_for_missing_verse():
    bible = Bible.from_file(sample_bible)
    with pytest.raises(KeyError):
        bible.verse("John", 3, 72)
