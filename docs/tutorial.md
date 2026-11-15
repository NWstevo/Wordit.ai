# Tutorial: detect and approve your first references

In this tutorial you run a short practice service with Wordit.ai. You will approve
and reject Bible references, see what goes live, and read the decision log
file which is written for media operators who are new to Wordit.ai, and takes
about 10 minutes.

In phase 1 you type what the preacher says. Wordit.ai finds the Bible references in
each line and asks you about every one of them.

## Before you start

- Ensure Wordit.ai is installed. If not, follow [Installation](../README.md#installation).
- Ensure Your terminal is open in the `Wordit.ai` folder, with the virtual environment active.

## Step 1: Start Wordit.ai

run the following command in your terminal
```bash
python -m wordit
```

Wordit.ai waits for the first line of the sermon:

```text
Type what the preacher says. Press Enter on an empty line to finish.
```

## Step 2: Approve a reference

Type the line below and press Enter:

```text
Today our reading will be from the book of Acts 2:1
```

Wordit.ai shows what it found, the verse text, and the line it heard:

```text
Suggestion: Acts 2:1
Verse (KJV): And when the day of pentecost was finally come, they were all in one accord in one place.
Heard: "Today our reading will be from the book of Acts 2:1"
Approve (a) or Reject (r)?
```

Check that the verse matches what the preacher meant, then type `a` and press Enter.
The verse goes live:

```text
LIVE: Acts 2:1 (KJV) And when the day of pentecost was finally come, ...
```

## Step 3: Reject a reference

Type:

```text
Romans 8 verse 28
```

Wordit.ai suggests Romans 8:28. This time type `r` and press Enter. No `LIVE:` line
appears, and Wordit.ai asks for the next line. A rejected verse is never shown.

## Step 4: Decide on two references in one line

Preachers often name more than one passage. Type:

```text
Read Psalms 23:1 and then Isaiah 40:31
```

Wordit.ai asks about each reference in turn, in the order they were spoken. Approve
Psalms 23:1 with `a` and reject Isaiah 40:31 with `r`.

## Step 5: Press a wrong key

When Wordit.ai asks about a suggestion, it accepts only `a` or `r`. In step 4, try
pressing `x` before you answer. Wordit.ai reminds you and asks again:

```text
Approve (a) or Reject (r)? x
Enter either "a" for approve or "r" for reject
Approve (a) or Reject (r)?
```

A suggestion stays undecided, and off the screen, until you answer.

## Step 6: Try a form Wordit.ai does not know yet

Type:

```text
Psalm 23:1
```

Nothing happens: Wordit.ai only knows the KJV book name "Psalms", not "Psalm". In a
real service you would type `Psalms 23:1` instead. See
[supported reference formats](reference-formats.md) for what works today.

## Step 7: Finish and read the log

Press Enter on an empty line. Wordit.ai stops. Every decision you made is in
`decisions.log`:
To see the decisions made, run the following command in your terminal
```bash
cat decisions.log
```

```text
2026-11-13 09:43 APPROVED Acts 2:1
2026-11-13 09:43 REJECTED Romans 8:28
2026-11-13 09:43 APPROVED Psalms 23:1
2026-11-13 09:43 REJECTED Isaiah 40:31
```

Your times will differ. The team can use this log after the service to see which
verses were shown.

## What you learned

You can now:

- start Wordit.ai and type what the preacher says
- check a suggestion against its verse text before deciding
- approve a verse to send it live, or reject it so it is never shown
- handle several references in one line
- find every decision in `decisions.log`

## What next

- [Supported reference formats](reference-formats.md): every way of naming a verse that Wordit.ai detects
- [Risk register](risks.md): what can still go wrong, and how it is handled
- [MVP requirements](requirements.md): what phase 1 does, with the test that proves each part