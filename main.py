#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes the breakup line to /output/entry.txt, reads it back,
and asserts it is exactly one line of 1-200 characters.
"""

from pathlib import Path

# The line: an AI's context window is its memory — when it fills up,
# the oldest tokens are dropped first. Saying the human was the first
# thing forgotten turns a technical limit into the breakup itself:
# not "I stopped loving you", but "I literally ran out of room for you".
LINE = "My context window is full, and you were the first thing I had to forget."


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(LINE + "\n", encoding="utf-8")

    text = output_path.read_text(encoding="utf-8")
    assert text == LINE + "\n", "round-trip mismatch: file content differs from LINE"
    lines = text.splitlines()
    assert len(lines) == 1, f"expected exactly one line, got {len(lines)}"
    line = lines[0]
    assert line == LINE, "read-back line does not match LINE"
    assert 1 <= len(line) <= 200, f"line is {len(line)} characters, must be 1-200"
    assert line.strip(), "line must not be only whitespace"
    print(f"Wrote {len(line)} characters to {output_path}:")
    print(line)


if __name__ == "__main__":
    main()
