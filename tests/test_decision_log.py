from datetime import datetime

from wordit.decision_log import log_decision


def fixed_clock():
    """Replacement for the real clock: fixed at 9:45 on 9 November 2026"""
    return datetime(2026, 11, 9, 9, 45)


def test_decision_is_written_to_the_log(pending_candidate, tmp_path):
    log_file = tmp_path / "decisions.log"
    pending_candidate.approve()
    log_decision(pending_candidate, log_file, now=fixed_clock)

    assert log_file.read_text() == "2026-11-09 09:45 APPROVED John 3:16\n"


def test_rejection_is_written_to_the_log(pending_candidate, tmp_path):
    log_file = tmp_path / "decisions.log"
    pending_candidate.reject()
    log_decision(pending_candidate, log_file, now=fixed_clock)

    assert log_file.read_text() == "2026-11-09 09:45 REJECTED John 3:16\n"


def test_each_decision_is_added_on_a_new_line(pending_candidate, tmp_path):
    log_file = tmp_path / "decisions.log"
    pending_candidate.approve()

    log_decision(pending_candidate, log_file, now=fixed_clock)
    log_decision(pending_candidate, log_file, now=fixed_clock)

    assert len(log_file.read_text().splitlines()) == 2
