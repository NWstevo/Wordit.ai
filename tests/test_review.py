from wordit.review import review_candidate
from wordit.candidate import Status


def test_pressing_a_to_approve(pending_candidate):
    review_candidate(
        pending_candidate, ask=lambda prompt: "a"
    )  # Replace the keyboard with a fake so the test can run without an operator
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
