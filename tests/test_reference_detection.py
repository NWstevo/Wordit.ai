import pytest

from wordit.detection import find_references
from wordit.reference import Reference


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Lets open to the book of Matthew 5:17 tonight", Reference("Matthew", 5, 17)),
        ("Romans 8 verse 28 says all things work together", Reference("Romans", 8, 28)),
        ("Turn to John chapter 3 verse 16", Reference("John", 3, 16)),
    ],
)
def test_finds_reference_in_sentence(text, expected):
    assert find_references(text) == [expected]


def test_returns_empty_list_when_no_reference():
    assert not find_references("Good morning, people of God")


def test_finds_several_references_in_order():
    text = "Lets read John 3:16 and then move to Romans 8 verse 28"
    assert find_references(text) == [
        Reference("John", 3, 16),
        Reference("Romans", 8, 28),
    ]
