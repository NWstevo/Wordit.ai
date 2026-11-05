import pytest

from wordit.candidate import Candidate
from wordit.reference import Reference


@pytest.fixture
def pending_candidate():
    """A new suggestion of John 3:16 that the operator is still to decide on"""
    return Candidate(
        reference=Reference("John", 3, 16),
        heard_text="turn with me to John 3:16",
        verse_text="For God so loved the world",
    )
