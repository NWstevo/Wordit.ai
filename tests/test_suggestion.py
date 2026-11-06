from wordit.reference import Reference
from wordit.suggestion import suggest_candidates


def test_suggests_a_candidate_with_the_verse_text(bible):
    candidates = suggest_candidates("Turn t" "with me to John 3:16", bible)

    assert len(candidates) == 1
    assert candidates[0].reference == Reference("John", 3, 16)
    assert candidates[0].verse_text.startswith("For God so loved")


def test_skips_references_that_do_not_exist(bible):
    assert not suggest_candidates("Read John 3:99 tonight", bible)
