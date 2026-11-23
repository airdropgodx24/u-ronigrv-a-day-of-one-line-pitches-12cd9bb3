"""One-line pitch entry for "A Day of One-Line Pitches".

The entry pitches a kettle that texts you "done boiling" in the voice
of a tired butler. Running this program writes that single pitch line
to /output/entry.txt.
"""

import os
import sys

PITCH = 'A kettle that texts you "done boiling" in the voice of a tired butler, because even water deserves a dramatic exit.'


def main() -> int:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
