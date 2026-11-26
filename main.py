"""Fortune Cookie Funnies for Engineers.

Writes one original fortune-cookie line for a software engineer to
/output/entry.txt. Deterministic: no randomness, no clock, no network,
no environment secrets. The line is a fixed string.
"""

LINE = "Your pager will stay silent for 364 nights. On the 365th, everything breaks at once — during your wedding."


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 120, "entry must be 1-120 characters"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip() == text and text.strip(), "entry must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
