# Proto-persona: Gerald Che, media operator

> Status: assumption-based. Not yet validated with real operators.

## Who he is

- Gerald is a passionate Christian who loves to serve in his church.
- He volunteers on the media team of his local church.
- He is tech-literate and has used broadcasting software such as EasyWorship, OBS and vMix.
- He attends almost every service, so he serves most Sundays.
- He knows the Bible well and is able to spot a wrong quotation

## His setting

- He works with a desktop and a set of extended displays one for operations and the other for live view (to monitor what goes on the display screens)
- He works with only a handful of other volunteers.
- The church uses mainly English for displaying scriptures
- Frequently used translations are:
    - KJV
    - NKJV
    - NIV
- He does not get the sermon or references before service so he has to follow when the preaching is going live

## Frustrations

- Besides the slides, he also coordinates the cameras, so his attention is split.
- With so many tasks on him, he often feels tired and burnt out from the manual work.
- When he is slow, the preacher sometimes complains.





## User Stories (US)

The stories are listed in the order they will be built.

### US-1: Show verses in KJV

As a media operator, I want every verse shown in the King James Version,
so that the text is accurate and the church needs no licence in phase 1.

**Acceptance criteria**

- **Given** a valid reference,
  **when** the verse is looked up,
  **then** the KJV text is returned with the label "KJV".

- **Given** a reference that does not exist in KJV (for example John 3:591),
  **when** it is looked up,
  **then** the system reports it as invalid.

Source: decision 001.

### US-2: Enter a reference manually

As a media operator, I want to type a reference myself,
so that a reference the system misses does not leave the congregation waiting.

**Acceptance criteria**

- **Given** I type a valid reference,
  **when** I submit it,
  **then** it becomes a suggestion I can approve.

- **Given** I type an invalid reference,
  **when** I submit it,
  **then** the system shows an error and creates no suggestion.

Source: frustration "when he is slow, the preacher sometimes complains".

### US-3: See suggested references

As a media operator, I want the system to suggest each Bible reference the preacher says,
so that I don't have to search for it while I also do other things.

**Acceptance criteria**

- **Given** the preacher says a reference in a supported form
  (for example "John 3:16" or "Romans 8 verse 28"),
  **when** the system processes it,
  **then** a suggestion appears with book, chapter, verse and KJV text.

- **Given** the preacher says something that is not a valid reference,
  **when** the system processes it,
  **then** no suggestion is created.

- **Given** a reference is spoken,
  **when** the suggestion appears,
  **then** it appears within 5 seconds (target, measured in evaluation).

Source: frustration "attention is split"; setting "no references before the service".

### US-4: Approve or reject suggestions

As a media operator, I want to approve or reject each suggestion,
so that only scripture I have checked reaches the screen.

**Acceptance criteria**

- **Given** a pending suggestion,
  **when** I approve it,
  **then** it is staged for preview.

- **Given** a pending suggestion,
  **when** I reject it,
  **then** it is removed and can never be sent live.

- **Given** a pending suggestion,
  **when** I take no action,
  **then** it is never shown on the live display.

- **Given** a pending suggestion,
  **when** I approve or reject it,
  **then** the decision is recorded in the service log.

Source: Gerald can spot a wrong quotation, so he is the final check.

### US-5: Preview before going live

As a media operator, I want to check a staged verse before it goes live,
so that the congregation never sees a mistake.

**Acceptance criteria**

- **Given** a staged verse,
  **when** I preview it,
  **then** I see the reference, the verse text and the translation label.

- **Given** a previewed verse,
  **when** I send it live,
  **then** it appears on the live display. Sending live is a separate step from approving.

- **Given** a staged verse,
  **when** I cancel it,
  **then** nothing changes on the live display.

Source: setting "two displays, one for operations and one for the live view".