"""Turn spoken text into candidates that the operator can approve or reject"""

from wordit.bible import Bible, VerseNotFoundError
from wordit.candidate import Candidate
from wordit.detection import find_references


def suggest_candidates(text: str, bible: Bible) -> list[Candidate]:
    """Return a candidate for every reference in the text that exists in the Bible"""
    candidates = []
    for reference in find_references(text):
        try:
            verse_text = bible.verse(reference.book, reference.chapter, reference.verse)
        except VerseNotFoundError:
            continue
        candidates.append(Candidate(reference, text, verse_text))
    return candidates
