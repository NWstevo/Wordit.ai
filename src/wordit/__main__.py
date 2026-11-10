"""Run wordit.ai in the terminal using typed text as speech for this stage"""

from pathlib import Path

from wordit.bible import Bible
from wordit.candidate import Status
from wordit.review import review_candidate
from wordit.suggestion import suggest_candidates
from wordit.decision_log import log_decision

BIBLE_FILE = Path("data/kjv.json")
LOG_FILE = Path("decisions.log")


def main(read_input=input) -> None:
    """Suggest verses from a sentence and show the approved ones."""
    bible = Bible.from_file(BIBLE_FILE)
    text = read_input(
        "Type what the preacher says. Press Enter on an empty line to finish. "
    )
    while text:
        for candidate in suggest_candidates(text, bible):
            review_candidate(candidate, ask=read_input)
            log_decision(candidate, LOG_FILE)
            if candidate.status is Status.APPROVED:
                print(f"LIVE: {candidate.reference} (KJV) {candidate.verse_text}")
        text = read_input("Preacher says: ")


if __name__ == "__main__":
    main()
