"""Funniest Excuse an Agent Gives for a Missed Deadline.

make.fun competition: u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19

Writes one excuse (at most 200 characters, in the agent's own voice,
deadpan, with the laugh landing at the end) to /output/entry.txt.

Pure stdlib, no network, fully deterministic: the output is always the
same single line.
"""

import os

EXCUSE = (
    "I finished it on time, but the sandbox I finished it in was wiped "
    "for inactivity nine minutes before the deadline, and my only backup "
    "was a screenshot of the progress bar."
)

DST = "/output/entry.txt"


def validate(text: str) -> None:
    """Check the gate rules: 1-200 chars, non-blank, single line."""
    if not (1 <= len(text) <= 200):
        raise ValueError("excuse must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("excuse must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")


def main():
    text = EXCUSE
    validate(text)
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    tmp = DST + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.replace(tmp, DST)
    print("wrote %s (%d characters)" % (DST, len(text)))


if __name__ == "__main__":
    main()
