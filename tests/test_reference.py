import pytest

from wordit.reference import Reference, parse_reference


@pytest.mark.parametrize(
    "text, expected",
    [
        ("John 3:16", Reference("John", 3, 16)),
        ("1 Corinthians 2:1", Reference("1 Corinthians", 2, 1)),
        ("Song of Solomon 3:9", Reference("Song of Solomon", 3, 9)),
    ],
)
def test_parse_simple_reference(text, expected):
    assert parse_reference(text) == expected


def test_reference_prints_like_a_bible_reference():
    assert str(Reference("Romans", 8, 28)) == "Romans 8:28"
