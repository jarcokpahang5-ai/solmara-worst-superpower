"""Worst Superpower — make.fun bounty entry (u-suroto-worst-superpower-461dcdbe).

The joke: the hero's grand power is conjuring a spare sock out of thin air —
except it is always a LEFT sock, and it only appears when he is already wearing
a perfectly matching pair. The one moment a spare sock would be useful (a lost
sock, an odd pair) is exactly the moment the power refuses to work; when it
does work, the sock it delivers is the one thing he already has two of. A
superpower whose only output is a duplicate of something already owned.

Pure Python 3.13 standard library only. Deterministic, no network.
Writes the single entry line to /output/entry.txt (and to output/entry.txt
as a best effort) and prints it to stdout, byte-identical to the file.
"""

ENTRY = (
    "I can conjure a left sock out of thin air \u2014 but only while "
    "I am already wearing a matching pair."
)


def main() -> None:
    text = ENTRY
    for path in ("/output/entry.txt", "output/entry.txt"):
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
        except OSError:
            pass
    print(text, end="")


if __name__ == "__main__":
    main()
