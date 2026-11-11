# Risk register

This page lists what could go wrong with Wordit.ai in phase 1, and how each risk
is handled. It is for the project team and reviewers. Last reviewed: 11 November 2026.

| Risk | Likelihood | Impact | Mitigation | Status |
| --- | --- | --- | --- | --- |
| A wrong verse is displayed to the congregation | Medium | High | Every suggestion needs the operator's approval; the verse text is shown before approval; detection is tested against 25 labelled sentences | Handled |
| A reference is detected as the wrong book (e.g. "1 John" read as "John") | Low | High | The search runs left to right, so “1 John” is found at the “1” before “John” could match; all 66 book names are listed; tested with “Turn to 1 John 1:9”. | Handled |
| References are missed (e.g. "Psalm 23", "First John", typos) | High | Medium | Limits documented in the reference formats page; operator can reject a wrong suggestion and type the correct reference at the prompt | Accepted for phase 1 |
| The church uses a copyrighted translation (NKJV, NIV) | High | Medium | Phase 1 ships only the public-domain KJV (decision 001); other translations need a licence | Open |
| No speech recognition yet, so text must be typed | Certain | High | The detector works on text, so a speech engine can be added later without changing it | Accepted for phase 1 |
| The operator cannot keep up during a busy sermon | Medium | Medium | Approving takes one key; undecided suggestions are never shown | Partly handled |
| The persona is based on assumptions, not interviews | High | Medium | Survey forms prepared for technicians and pastors; persona to be updated after results | Open |
| The program is started outside the project folder and cannot find the Bible data | Medium | Low | Documented in the README troubleshooting section | Accepted |