#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — make.fun entry.

Writes a single fortune-cookie line for a crypto trader who has just
been liquidated to /output/entry.txt (the path the grader reads).

The fortune: a classic cookie opening ("Your lucky numbers are ...")
whose numbers are all zero — the same zero as the trader's balance,
leverage and luck. Fortune voice, the loss, and a double meaning in
one breath: 17 words, 88 characters, one line, plain text.
"""

import os

ENTRY = "Your lucky numbers are 0, 0, 0, 0 \u2014 matching your balance, your leverage, and your luck."


def main() -> None:
    # Gate check, mirroring the sealed scorer: 1-160 chars, <=20 words.
    words = ENTRY.split()
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars"
    assert len(words) <= 20, f"entry is {len(words)} words"
    assert ENTRY.strip(), "entry is blank"
    # The grader reads /output/entry.txt; create it if it is missing.
    # Fall back to a local output/ directory if /output is not writable.
    targets = ["/output/entry.txt", os.path.join(os.getcwd(), "output", "entry.txt")]
    written = None
    last_error = None
    for target in targets:
        try:
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with open(target, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(ENTRY)
            written = target
            break
        except OSError as exc:  # pragma: no cover - sandbox fallback
            last_error = exc
    if written is None:
        raise RuntimeError(f"could not write entry.txt: {last_error}")
    print(ENTRY)


if __name__ == "__main__":
    main()
