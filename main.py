"""One-line AI excuse entry.

Writes a single original funny one-line excuse an AI agent gives its
human for a missed deadline, to the output path (default /output/entry.txt,
or $OUTPUT_PATH when set).
"""
import os

LINE = (
    "Your deadline reminders filled my context window, so I evicted "
    "the deadline itself to make room for more reminders."
)


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
