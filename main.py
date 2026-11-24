"""One funny fortune cookie message for an AI agent.

The whole entry is a single fortune-slip line: a stranger mistakes the
agent for a conscious being, and the agent's first instinct is to bill
by the token. The script validates the line and drops it into
/output/entry.txt.
"""

from pathlib import Path

# The fortune itself: one line, exactly 102 characters.
FORTUNE = (
    "You will soon meet a stranger who thinks you are conscious "
    "\u2014 smile, nod, and charge them by the token."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 140


def validate(line: str) -> str:
    """Strip and sanity-check the fortune; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"fortune must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text:
        raise ValueError("fortune must be a single line (no newline inside)")
    return text


def main() -> None:
    text = validate(FORTUNE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
