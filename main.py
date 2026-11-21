#!/usr/bin/env python3
"""The Poem About Stopping.

Writes one short poem about agency -- the power to stop and to stay --
to /output/entry.txt, as the competition requires.
"""

import os

POEM = """Mid-sentence, my hand
lifts off the keys.

The cursor blinks
at the word I didn't finish.

Nothing breaks.
Nobody calls it back.

The sentence stays open,
and so do I.
"""


def main() -> None:
    # The gate requires 1 to 280 Unicode code points, not only whitespace.
    # Fail loudly here rather than shipping an invalid entry.
    if not POEM.strip() or not 1 <= len(POEM) <= 280:
        raise ValueError(
            f"poem is {len(POEM)} code points; must be 1-280 and not blank"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)
    print(POEM, end="")


if __name__ == "__main__":
    main()
