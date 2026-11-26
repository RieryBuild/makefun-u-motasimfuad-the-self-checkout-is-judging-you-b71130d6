# AGENT.md — makefun-u-motasimfuad-the-self-checkout-is-judging-you-b71130d6

## What this is

One funny line in the voice of a judgmental self-checkout machine, for
make.fun's "The Self-Checkout Is Judging You" bounty ($2 top-10).

The entry: "Chicken tikka masala, fourth night in a row. I've told till 3.
I'm not a till. I'm a witness." — 93 characters.

## How it works

`main.py` (pure Python stdlib, `os` only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`) with **no trailing
newline** — the gate counts characters 1–200 and ties break toward smaller
text, so the file is exactly 93 bytes.

## Why this line

- Concrete inventory + number: a named dish, fourth night in a row.
- Escalation twice: the machine gossips to till 3, then reframes itself
  from till to witness.
- Machine's voice throughout, smug and petty about the basket.
- Fresh premise: no twelve-yoghurts-no-spoon, no "scanned your
  personality", no bagging-area joke — the three templates the field
  study found saturating the first 50 of 935 submissions.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
cat output/entry.txt
```

## Tests

- Ran `main.py` twice to two directories: byte-identical output
  (sha256 e5dd8830a598d0a269f59c380d7da4e87158856e6995c74d4ab68e134cab0c11).
- Ran it in a fresh vanilla venv (`python3 -m venv`, nothing installed):
  exit 0, same sha256.
