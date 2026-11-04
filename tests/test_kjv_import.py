import pytest

from wordit.kjv_import import clean_verse_text


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
