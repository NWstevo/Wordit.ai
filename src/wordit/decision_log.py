"""Record the operator's decisions so a service can be reviewed afterwards"""

from datetime import datetime
from pathlib import Path

from wordit.candidate import Candidate


def log_decision(candidate: Candidate, log_path: Path, now=datetime.now) -> None:
    """Append the time, decision and the reference to the log file"""
    timestamp = now().strftime("%Y-%m-%d %H:%M")
    decision = candidate.status.name
    with log_path.open("a", encoding="utf-8") as log:
        log.write(f"{timestamp} {decision} {candidate.reference}\n")
