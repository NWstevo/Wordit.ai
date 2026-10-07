# 1. Bible translation for phase 1

## Status

Accepted on 7 October 2026.

## Context

Wordit.ai stores the Bible text on the operator's computer and shows verses
on screen during a service. The project repository is public, and the final
demonstration will be recorded.

The translation must therefore be one whose full text we can store,
publish in the repository and display in recordings without violating any copyright laws.

## Options considered

Translation <Rights> <Outcome> 

King James Version (KJV) <Public domain>  <Chosen as the default >
Berean Standard Bible (BSB)  <Public domain since 30 April 2023>  <Approved, added as second> 
American Standard Version (ASV)  <Public domain>  <Approved, lower priority> 
World English Bible (WEB) <Public domain> <Approved, lower priority>


NKJV was the preferred translation, because many churches use it. It is
under copyright, so we cannot store the full text in a public repository
or show it in recordings without a licence. We deferred it until we
obtain permission from the publisher.

## Decision

We use the KJV as the default translation for phase 1. It is the closest
public-domain text to the NKJV and uses the same verse numbering.

Each translation is one JSON file. All files have the same structure, so
the rest of the program does not depend on which translation is loaded.

The screen shows the translation's abbreviation beside every reference,
for example "John 3:16 (KJV)".

Data source: to be confirmed on 9 October, with its licence.

## Consequences

- We can add a translation by adding a data file. No code changes.
- A reference is valid for a particular translation, not in general,
  because translations do not all contain the same verses. Validation
  must use the selected translation's data.
- The KJV's older vocabulary is harder to read quickly on screen. BSB is
  the planned modern alternative.
- NKJV needs a licence before we can add it. This is recorded in the
  risk register.