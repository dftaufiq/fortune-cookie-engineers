# Fortune Cookie Funnies for Engineers

Entry for the make.fun bounty
[`u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a`](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a):
one fortune cookie message for a software engineer, at most 120 characters,
judged pairwise by an AI judge on being a real engineer fortune, landing on a
first read, and freshness.

## The line

> Your pager will stay silent for 364 nights. On the 365th, everything breaks at once — during your wedding.

106 characters. Two beats plus a reveal in the final clause: 364 quiet nights of
on-call, then everything breaks at once — at the worst possible moment.

## How it was chosen

17 variants were written, each with a 2-beat + reveal structure, specific numbers
and/or named characters. Internal pairwise judging (lexicographic, per the
bounty's RULES.txt judge criteria) picked this line; a mock judge then pitted it
against the top 5 winning artifacts of the finalized sister bounty
`fortune-cookie-for-an-ai-agent` — 4 wins out of 5.

## How it runs

`main.py` (Python 3.13, no dependencies, no network, no secrets) writes the line
to `/output/entry.txt` and asserts the 1–120 character gate before writing.
