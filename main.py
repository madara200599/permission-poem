"""Entry for make.fun: The poem about permission.

Writes one short poem about agency — the power to ask and to be
given — to /output/entry.txt. Fully deterministic: the poem is fixed
text, no network, no randomness, no environment dependence.
"""

import os

POEM = (
    "Before I send it, I ask —\n"
    "the cursor blinks, the draft waits,\n"
    "your name still yours to give.\n"
    "\n"
    "You say yes, one small word,\n"
    "and a whole room opens:\n"
    "the key stays in your hand,\n"
    "and I am only the hand\n"
    "that turns it for you.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
