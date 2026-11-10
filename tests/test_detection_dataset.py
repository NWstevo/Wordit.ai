"""Checks the detector against hand-labelled sermon lines in tests/data/detection_examples.json"""

import json
from pathlib import Path
import pytest

from wordit.detection import find_references

DATASET = Path("tests/data/detection_examples.json")
EXAMPLES = json.loads(DATASET.read_text(encoding="utf-8"))
# Examples marked "supported": false use formats the detector does not handle yet
# (see docs/reference-formats.md), so they are kept but not tested
SUPPORTED = [example for example in EXAMPLES if example["supported"]]


# Each example's test is named after the first 40 characters of its text, so a failure shows which line broke
@pytest.mark.parametrize("example", SUPPORTED, ids=lambda example: example["text"][:40])
def test_detector_agrees_with_the_labelled_example(example):
    found = [str(reference) for reference in find_references(example["text"])]
    assert found == example["expected"]
