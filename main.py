#!/usr/bin/env python3
"""make.fun entry: One-Line Office Jokes.

Writes a single one-line joke about office life to /output/entry.txt.
The gate requires UTF-8 text of 1 to 199 characters, not only whitespace,
on exactly one line, with no trailing newline.
"""

import os

# The joke: setup (the office chair sinks a little every hour — a real,
# physical office detail everyone with a cheap chair knows) + turn (the
# sinking is reframed as a career move), punchline last. One line.
JOKE = "My office chair sinks an inch an hour, so by 5 p.m. I'm at desk-drawer height \u2014 the fastest career move I've made all year."


def main():
    text = JOKE.strip()
    if not text or text.isspace():
        raise SystemExit("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 199:
        raise SystemExit("entry must be 1-199 characters, got %d" % len(text))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and confirm the file holds exactly the one line, no
    # trailing newline and no extra bytes.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("written entry does not match the joke")
    print(text)


if __name__ == "__main__":
    main()
