"""The Funniest Honest Appliance Error — entry program.

Writes a single honest appliance error line (under 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure Python stdlib, deterministic, no network.
"""

import os

LINE = (
    "Error: I burnt your toast again. The browning dial has been "
    "decorative since 2019. I toast at one temperature: regret."
)


def main():
    if not LINE.strip():
        raise SystemExit("entry line is empty or only whitespace")
    if len(LINE) > 200:
        raise SystemExit(
            "entry line is %d characters, over the 200-character limit"
            % len(LINE)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
