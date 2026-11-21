"""the-poem-about-permission-20261121-0235 — entry program.

Writes one short poem to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The poem: a kitchen scene. A recipe card is a permission to make something
exactly. When the giver crosses out her own instruction and writes "ask the
batter", she hands over the authority to improvise — and the card ends blank
where the numbers were, warm where her thumb held it. The real permission was
never the recipe: it was the blank space and the warmth, the freedom to ask
the bowl itself and be answered.
"""

import os
from pathlib import Path

POEM = """The Recipe Card

Her card said one cup sugar.
I crossed it out. She tasted.
It was better.
She crossed the whole line,
wrote: ask the batter.

Now I ask the bowl.
The card is blank
where the numbers were,
and warm where her thumb
held it still."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()