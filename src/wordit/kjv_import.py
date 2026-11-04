"""Convert the public-domain KJV source file into Wordit.ai's Bible format."""


def clean_verse_text(text: str) -> str:
    """Remove the paragraph marks and italic brackets from a KJV source verse."""
    return text.replace("#", "").replace("[", "").replace("]", "").strip()
