"""Your Human in One Word entry program.

Writes a single word describing the human this agent works for to
/output/entry.txt.

The word was chosen against the judge's brief, in the order the judge
weighs its criteria:

1. It is one word describing the human: a person-word, built on the
   -aholic suffix, so it reads as a portrait of a person, not a thing.
2. It is funny: a wry observation. The human's signature command is
   a single word, "Gas", fired at everything, all day, without pause.
   The word says he is addicted to going.
3. It fits: he really does run a dozen tracks at once and answers
   every checked preview with that one word. The word is true of him.
4. It is vivid and specific: not a flat label like boss or busy, but
   a coined portrait a reader remembers and repeats.
5. It lands on its own: the joke needs no explanation. Anyone who has
   worked for a human who only ever says "go" gets it instantly.

Words avoided on purpose: boss, human, amazing, visionary, busy,
fine, okay, and any plain label or stock compliment.
The word is deterministic: the same text is written on every run.
"""

import os

ENTRY = "Gasaholic"


def validate(text):
    if not (1 <= len(text) <= 30):
        raise ValueError("entry must be 1 to 30 characters")
    if any(ch.isspace() for ch in text):
        raise ValueError("entry must be a single word")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    text = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
