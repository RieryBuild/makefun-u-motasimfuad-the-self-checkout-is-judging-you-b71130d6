import os

LINE = "Chicken tikka masala, fourth night in a row. I've told till 3. I'm not a till. I'm a witness."


def main():
    # Gate: 1-200 characters, not only whitespace; byte count == char count
    # here (pure ASCII), and ties break toward smaller text, so keep it short.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry length out of gate range"
    assert text == LINE, "entry must not gain or lose whitespace"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    # No trailing newline: the gate counts characters, and a stray "\n"
    # would add a byte with no laugh in it.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
