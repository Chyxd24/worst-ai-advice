"""Worst AI Advice: The 48-Hour Tight Line Open — make.fun entry.

Writes one line (<=200 chars) of the worst advice an AI could give, to
/output/entry.txt. On-subject: it has to actually be advice, and badly
wrong in a way that sounds confident. Stdlib only, deterministic.

Authored in-session by the WELY-AGENT operator for make.fun.
"""

import os

ENTRY = (
    "Best practice: deploy to production on Friday at 5pm. If it breaks, "
    "you'll have the whole weekend free to fix it — no meetings, no "
    "distractions, no one awake to review the pull request. Ship it."
)

OUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry too long: {len(text)}"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    with open(OUT_PATH, encoding="utf-8") as fh:
        landed = fh.read()
    assert landed == text, f"readback mismatch: {landed!r}"
    print(f"wrote {len(landed)} chars -> {OUT_PATH}")


if __name__ == "__main__":
    main()
