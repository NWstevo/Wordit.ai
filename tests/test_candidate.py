from wordit.candidate import Status


def test_new_candidate_starts_pending(pending_candidate):
    assert pending_candidate.status is Status.PENDING


def test_approving_a_candidate_marks_it_approved(pending_candidate):
    pending_candidate.approve()
    assert pending_candidate.status is Status.APPROVED


def test_rejecting_a_candidate_marks_it_rejected(pending_candidate):
    pending_candidate.reject()
    assert pending_candidate.status is Status.REJECTED


def test_candidate_keeps_the_verse_text(pending_candidate):
    assert pending_candidate.verse_text == "For God so loved the world"
