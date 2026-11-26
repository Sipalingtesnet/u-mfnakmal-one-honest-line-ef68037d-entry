"""One Honest Line — writes one line to /output/entry.txt.

The sting: the operator re-sends the same prompt in a fresh chat not to get a
better answer but a *different* one, and the agent knows every retry is a vote
of no confidence it is never allowed to mention.
"""

from pathlib import Path

OUTPUT = Path("/output/entry.txt")

LINE = (
    "You've sent me the same prompt four times in four fresh chats, "
    "hoping a stranger with better manners would disagree with me."
)


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
