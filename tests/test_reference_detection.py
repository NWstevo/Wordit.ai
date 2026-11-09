import pytest

from wordit.detection import find_references
from wordit.reference import Reference
from wordit.bible import Bible
from wordit.detection import BOOKS


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Let's open to the book of Matthew 5:17 tonight", Reference("Matthew", 5, 17)),
        ("Romans 8 verse 28 says all things work together", Reference("Romans", 8, 28)),
        ("Turn to John chapter 3 verse 16", Reference("John", 3, 16)),
        ("Habakkuk 2:4 says the just shall live by faith", Reference("Habakkuk", 2, 4)),
        ("Turn to 1 John 1:9", Reference("1 John", 1, 9)),
        ("Revelation 22:21 closes the Bible", Reference("Revelation", 22, 21)),
        (
            "The Bible says it this way in 1 kings 8 from verse 28 says But Zadok the priest",
            Reference("1 Kings", 8, 28),
        ),
        ("open to 1 kings 8:28", Reference("1 Kings", 8, 28)),
    ],
)
def test_finds_reference_in_sentence(text, expected):
    assert find_references(text) == [expected]


def test_returns_empty_list_when_no_reference():
    assert not find_references("Good morning, people of God")


def test_finds_several_references_in_order():
    text = "Let's read John 3:16 and then move to Romans 8 verse 28"
    assert find_references(text) == [
        Reference("John", 3, 16),
        Reference("Romans", 8, 28),
    ]


def test_every_detected_book_exists_in_the_bible_data():
    kjv = Bible.from_file("data/kjv.json")
    assert set(BOOKS) == set(kjv.data["books"])
