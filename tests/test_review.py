import pytest
from wordit.candidate import Candidate, Status
from wordit.reference import Reference
from wordit.review import review_candidate


@pytest.fixture
def pending_candidate():
    """A fresh suggestion for John 3:16 that the Operator is still to decide on"""
    return Candidate(Reference("John", 3, 16), "Turn with me to John 3:16")


def test_pressing_a_to_approve(pending_candidate):
    review_candidate(
        pending_candidate, ask=lambda prompt: "a"
    )  # fake operator presses "a" (lambda function)
    assert pending_candidate.status is Status.APPROVED


def test_pressing_r_to_reject(pending_candidate):
    review_candidate(pending_candidate, ask=lambda prompt: "r")
    assert pending_candidate.status is Status.REJECTED


def test_wrong_key_asks_again(pending_candidate):
    keys = [
        "x",
        "4",
        "words",
        "a",
    ]  # Operator presses a wrong key or number (anything from the list)

    def fake_operator(prompt):
        return keys.pop(0)

    review_candidate(pending_candidate, ask=fake_operator)
    assert pending_candidate.status is Status.APPROVED
