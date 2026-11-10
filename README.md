# Wordit.ai

![CI](https://github.com/NWstevo/Wordit.ai/actions/workflows/ci.yml/badge.svg)

**Wordit.ai** suggests Bible references from a sermon on screen, and a church operator approves which verses go live.

Created by Stephen Wiendoh Ntah (NWstevo), CODE University of Applied Sciences, Berlin.

---

## Key Features at the moment

Wordit.ai is currently in phase 1. It runs in the terminal and uses a text as sample input for the preacher's voice or sermon.

- Finds Bible references in a sentence, such as "Romans 8:28" or "John chapter 3 verse 16".
- Looks up each verse using the King James Version of the Bible.
- Shows each suggestion to the operator, who decides to either approve or reject it.
- Shows approved verses as live output.
- Logs every decision in a log file.

Nothing is displayed on the screen without the operator's approval.

## Requirements

- Python 3.11 or newer
- Git

## Installation

```bash
git clone https://github.com/NWstevo/Wordit.ai.git
cd Wordit.ai
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Getting started

Start Wordit.ai and type a sentence as the preacher would say it:

```bash
python -m wordit
```

```text
Type what the preacher says. Press Enter on an empty line to finish.
Preacher says: Turn with me to John 3:16
Suggestion: John 3:16
Verse (KJV): For God so loved the world, that he gave his only begotten Son, ...
Heard: "Turn with me to John 3:16"
Approve (a) or Reject (r)? a
LIVE: John 3:16 (KJV) For God so loved the world, ...
```

Press Enter on an empty line to stop. Each decision is saved in `decisions.log`.

## Troubleshooting

**`FileNotFoundError: ... 'data/kjv.json'`**: run Wordit.ai from the project folder (`cd Wordit.ai`), because it looks for the Bible data relative to where you start it.

## Future Work (phase 2)

Planned: speech recognition, so Wordit.ai listens to the sermon directly.

Planned: NDI output for OBS Studio, vMix, EasyWorship and ProPresenter.

---


## Contributing

We welcome contributions from developers, media directors, and tech enthusiasts passionate about enhancing church media production. Please read our [Contributing Guidelines](CONTRIBUTING.md) to get started.

## License

Distributed under the [MIT License](LICENSE).
