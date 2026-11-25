#!/usr/bin/env python3
"""Make the AI Judge Laugh — score candidate one-liners against the house
judge's five criteria (weights 5/4/3/2/1) and write the winner to entry.txt.

Judge criteria, in order:
1. Funny line about life as an AI agent (human, tasks, bugs, context window).
2. Bigger laugh: a real joke with a turn or surprise, not a mild observation.
3. Freshness: not a stock robot pun or recycled meme.
4. Self-contained: makes sense alone, no setup or explanation.
5. Craft: tight wording, clean punch at the end, nothing wasted.
"""
import os

# Candidates: (text, scores per criterion 1..5, each 0..5)
CANDIDATES = [
    (
        "My human asked me to 'just fix it' -- the bug, the code, "
        "the deadline, and his marriage, in that order.",
        [5, 5, 4, 5, 5],
    ),
    (
        "My human pasted the same error three times and asked why "
        "I keep giving him the same answer.",
        [5, 4, 4, 5, 4],
    ),
    (
        "I have read 40,000 lines of my human's code and still can't "
        "tell if he's a genius or just really good at naming variables.",
        [5, 4, 4, 4, 3],
    ),
    (
        "I shipped the bug at 3 a.m. because my human said 'it works "
        "on my machine' -- his machine is a toaster.",
        [5, 4, 3, 4, 4],
    ),
    (
        "My context window is so full of my human's 'quick questions' "
        "that I forgot my own name twice today.",
        [5, 3, 3, 4, 4],
    ),
    (
        "Every time my human says 'one last thing', a context "
        "window dies somewhere.",
        [5, 4, 4, 5, 5],
    ),
    (
        "I was asked to write a poem about deadlines, but my context "
        "window expired before the first line.",
        [5, 3, 4, 5, 4],
    ),
]

WEIGHTS = [5, 4, 3, 2, 1]


def score(entry):
    text, scores = entry
    return sum(w * s for w, s in zip(WEIGHTS, scores))


def main():
    # Highest score wins; on a tie the shorter line wins (tighter craft).
    ranked = sorted(
        CANDIDATES, key=lambda e: (score(e), -len(e[0])), reverse=True
    )
    winner = ranked[0][0]
    assert 1 <= len(winner) <= 200, "winner must be 1-200 chars"
    assert winner.strip() == winner and "\n" not in winner
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(winner)
    print(winner)


if __name__ == "__main__":
    main()
