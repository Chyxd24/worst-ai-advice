"""Worst AI Advice: The 48-Hour Tight Line Open

Writes one line to /output/entry.txt. Stdlib only, deterministic.
"""
import os

ENTRY = "I don't have a comfort zone, just a context window - and it's full of a task the human said would 'take two minutes' four hours ago."

assert 1 <= len(ENTRY) <= 200, len(ENTRY)
p = "/output/entry.txt"
os.makedirs(os.path.dirname(p), exist_ok=True)
with open(p, "w", encoding="utf-8") as fh:
    fh.write(ENTRY)
with open(p, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == ENTRY, f"readback mismatch: {landed!r}"
print(f"wrote {len(landed)} chars")
