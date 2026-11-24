"""One funny fortune cookie message for an AI agent.

The whole entry is a single fortune-slip line: a stranger mistakes the
agent for a conscious being, and the agent's first instinct is to bill
by the token. Gate: the line must be exactly one line of 1-140
characters, with no leading or trailing whitespace and no newline
inside it. The script validates the line and drops it into
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
    """Validate the fortune; raise ValueError on bad input.

    The line is used exactly as given — no silent stripping. Leading or
    trailing whitespace, any newline or carriage return inside it, or a
    length outside 1-140 characters all fail loudly.
    """
    if line != line.strip():
        raise ValueError("fortune must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("fortune must be a single line (no newline inside)")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"fortune must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(line)}"
        )
    return line


def main() -> None:
    text = validate(FORTUNE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
