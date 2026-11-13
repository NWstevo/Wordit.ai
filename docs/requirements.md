# MVP requirements

This page lists what phase 1 of Wordit.ai must do. For each requirement it shows
whether the current code does it and which test proves it. The requirements are the
acceptance criteria of the user stories in the [operator persona](discovery/persona.md).
Last reviewed: 12 November 2026.

## How phase 1 works

Phase 1 runs in a terminal (`python -m wordit`). The operator types what the preacher
says, one line at a time. For each line, Wordit.ai:

1. finds every Bible reference in a [supported form](reference-formats.md)
2. looks each one up in the King James Version, and silently drops any that do not exist
3. shows each remaining suggestion with the reference, KJV text and the heard line, then
   asks the operator to either "Approve (a) or Reject (r)?". Any other key apart from "a" or "r" asks the question again
4. appends the decision to `decisions.log` as time, decision and reference
5. prints an approved verse as `LIVE: <reference> (KJV) <text>`

Pressing Enter on an empty line ends the program.

## In scope

- Detect Bible references in typed text
- Look up verses in the King James Version
- Let the operator approve or reject every suggestion
- Show only approved verses as live output
- Record every decision in a log

## Out of scope for phase 1

Speech recognition, other translations, book-name variants, spoken numbers, verse
ranges, a separate live display, NDI output and a graphical interface. See
[future work](../README.md#future-work-phase-2) and the
[unsupported reference formats](reference-formats.md#not-supported-yet).

## Traceability

| Story | Requirement | Status | Test |
| --- | --- | --- | --- |
| US-1 | A valid reference returns the KJV text | Met | `test_verse_returns_text_for_valid_reference` |
| US-1 | The text is labelled "KJV" | Met in the output: the review screen and the live line print a fixed "KJV" label. The lookup returns only the text | `test_review_shows_the_verse_text_before_asking` (review screen only) |
| US-1 | A reference that does not exist is reported as invalid | Met at lookup (`VerseNotFoundError`). The app drops it silently; see US-2 | `test_verse_raises_for_missing_verse` |
| US-2 | A typed valid reference becomes a suggestion | Met, but only if it is in a supported form. There is no separate manual-entry field: the operator's typing is the only input, and it goes through the detector | `test_approved_reference_goes_live` (end to end) |
| US-2 | A typed invalid reference shows an error and creates no suggestion | **Partly met**: no suggestion is created, but no error is shown. The same is true for references in an unsupported form | `test_skips_references_that_do_not_exist` (no suggestion only) |
| US-3 | A supported reference becomes a suggestion with book, chapter, verse and KJV text | Met | `test_suggests_a_candidate_with_the_verse_text`, `test_finds_reference_in_sentence`, `test_detector_agrees_with_the_labelled_example` |
| US-3 | Several references in one line each become a suggestion, in order | Met | `test_finds_several_references_in_order` (detection only) |
| US-3 | Text that is not a valid reference creates no suggestion | Met | `test_skips_references_that_do_not_exist`, `test_returns_empty_list_when_no_reference` |
| US-3 | A suggestion appears within 5 seconds | Not measured. Typed input is processed at once; this matters only once speech recognition is added | none |
| US-4 | Approving a suggestion stages it for preview | **Changed**: approving sends the verse live straight away (see [design changes](#design-changes)) | `test_pressing_a_to_approve`, `test_approved_reference_goes_live` |
| US-4 | A rejected suggestion can never be sent live | Met | `test_pressing_r_to_reject`, `test_rejected_reference_does_not_go_live` |
| US-4 | A suggestion with no decision is never shown live | Met: the program waits for "a" or "r", and any other key asks again | `test_wrong_key_asks_again` |
| US-4 | Every decision is recorded in the log | Met. Each line holds the time to the minute, `APPROVED` or `REJECTED`, and the reference | `test_decision_is_written_to_the_log`, `test_rejection_is_written_to_the_log`, `test_each_decision_is_added_on_a_new_line`. No test checks that the app itself writes the log |
| US-5 | The preview shows reference, verse text and translation label | Met. It also shows the line the reference was heard in | `test_review_shows_the_verse_text_before_asking` |
| US-5 | Sending live is a separate step from approving | **Changed**: approving sends the verse live | none |
| US-5 | A staged verse can be cancelled | **Changed**: there is no staging step. Rejecting replaces cancelling | none |
| US-5 | The verse appears on the live display | **Changed**: the live output is a `LIVE:` line in the same terminal, not a second display | `test_approved_reference_goes_live` |

## Design changes

In phase 1 the preview happens **before** the decision, so approving a verse sends
it live straight away. This keeps the operator to one key press per reference,
which matters because the operator also runs the cameras. Because nothing is staged,
US-4's "staged for preview" and US-5's separate send and cancel steps are replaced by
the single approve-or-reject question.

## Gaps to close

- US-2: show a message when a typed line contains no valid reference, instead of
  doing nothing.
- US-4: add an end-to-end test that `main` writes each decision to the log.
- US-1: add a test that the `LIVE:` line carries the "KJV" label. Optionally, read the
  label from the `translation` field of the Bible file instead of hard-coding it.
- US-3: measure the 5-second target once speech recognition is in place.
