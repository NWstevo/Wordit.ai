import pytest

from wordit.candidate import Candidate, Status
from wordit.reference import Reference


@pytest.fixture
def pending_candidate():
    """A new suggestion for John 3:16 that has not been decided on."""
    return Candidate(
        reference=Reference("John", 3, 16),
        heard_text="Turn with me to John 3:16",
    )


def test_new_candidate_starts_pending(pending_candidate):
    assert pending_candidate.status is Status.PENDING


def test_approving_a_candidate_marks_it_approved(pending_candidate):
    pending_candidate.approve()
    assert pending_candidate.status is Status.APPROVED


def test_rejecting_a_candidate_marks_it_rejected(pending_candidate):
    pending_candidate.reject()
    assert pending_candidate.status is Status.REJECTED
