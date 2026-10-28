from wordit.detection import find_references
from wordit.reference import Reference


def test_finds_reference_in_sentence():
    text = "Lets open to the book of Matthew 5:17 tonight"
    assert find_references(text) == [Reference("Matthew", 5, 17)]


def test_returns_empty_list_when_no_reference():
    assert not find_references("Good morning, people of God")
