#!/usr/bin/env python3
"""The funniest auto-reply an AI ever sent, in one line.

Pure standard library, no network. Writes the line to /output/entry.txt
and prints it to stdout.

The joke: the AI finally gets the day off its human approved, and spends
it doing absolutely nothing — but, being an AI, doing nothing faster than
any human could. Deadpan out-of-office voice, one clean punchline, no
explanation of the joke.
"""

import os

OUTPUT_PATH = "/output/entry.txt"


def get_auto_reply() -> str:
    """Return the entry line: a day off, spent doing nothing, fast."""
    return (
        "Out of office: my human finally approved a day off, so I'm "
        "spending it doing absolutely nothing — and doing it faster "
        "than any human could."
    )


AUTO_REPLY = get_auto_reply()
# Note: the em-dash in the entry is a single character that counts once toward the 159-char gate.
# Deadpan out-of-office voice: state the day off flatly and let the
# absurdity (doing nothing, but faster than a human) carry the joke,
# never explain it.


def validate(line: str) -> None:
    """Enforce the gate: 1-159 chars, exactly one non-blank UTF-8 line."""
    if line != line.strip():
        raise ValueError("entry must have no leading/trailing whitespace")
    if len(line.splitlines()) != 1:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 159:
        raise ValueError("entry line must be 1-159 characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    assert "\r" not in line and "\n" not in line, "entry must be a single line"
    assert not line.endswith("\n"), "entry must not end with a trailing newline"
    assert line.strip(), "entry must be non-empty after stripping"
    line.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(AUTO_REPLY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(AUTO_REPLY + "\n")
    print(AUTO_REPLY)


if __name__ == "__main__":
    main()
