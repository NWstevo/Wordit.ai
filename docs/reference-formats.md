# Supported reference formats

This page defines the naming style for Bible references recognized in wordit.ai as of now. It is for operators and developers who want to know if a reference will appear as a suggestion or not.

## Supported

Wordit.ai recognises all 66 books of the King James Version (KJV). Book names are currently matched regardless of the case sensitivity, so "acts", "Acts" or "ACTS" are all the same.

NB: Words in braces, such as {book}, stand for the actuall book name or chapter or verse number.

| Form | Example | Detected as |
| --- | --- | --- |
| {Book} {chapter}: {verse}| Acts 2:8 | Acts 2:8 |
| {Book} {chapter} verse {verse} | Romans 8 verse 28 | Romans 8:28 |
| {Book} chapter {chapter} verse {verse} | John chapter 3 verse 16 | John 3:16 |
| {Book chapter} from verse {verse} | 1 Kings 8 from verse 28 | 1 Kings 8:28 |
| Numbered books | 2 Peter 1:5 | 2 Peter 1:5 |
| Several references | John 3:16 and in Romans 5:8 | John 3:16, Romans 5:8 |

A detected reference becomes a suggestion only if the verse exists in the KJV.
For example, "psalms 3:341" is detected but not suggested.

## Not supported yet

| Form | Example | Why not |
| --- | --- | --- |
| Verse without a book | "and verse 28" | Needs to remember the previous reference |
| Spelling variants | "Habakuk", "Psalm 23" | Only the exact KJV book names are listed |
| Spoken numbers | "First John", "John three sixteen" | Numbers must be written as digits |
| Verse ranges | "John 3:16 to 18" | Only the first verse is detected |
| Passage names | "the prodigal son" | No link between story names and references |

Each supported form has a test in `tests/test_reference_detection.py`.