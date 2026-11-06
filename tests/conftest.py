import pytest

from wordit.candidate import Candidate
from wordit.reference import Reference
from wordit.bible import Bible

SAMPLE_BIBLE = "tests/data/kjv_sample.json"


@pytest.fixture
def pending_candidate():
    """A new suggestion of John 3:16 that the operator is still to decide on"""
    return Candidate(
        reference=Reference("John", 3, 16),
        heard_text="turn with me to John 3:16",
        verse_text="For God so loved the world",
    )


@pytest.fixture
def bible():
    """The small KJV sample with Genesis 1:1, Psalms 23:1, John 3:16 and Acts 8:37."""
    return Bible.from_file(SAMPLE_BIBLE)
