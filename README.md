# Signal Locator

A number guessing game with a twist — instead of plain "too high / too low" text, a live signal-locator gauge shows how close you are to the target number in real time.

## How it works

Pick a difficulty, and the game picks a hidden number in that range. Guess your way to it before you run out of lives. A needle gauge swings from cold (far off) to hot (close) with every guess, so you get instant visual feedback instead of just reading a message.

## Difficulty levels

| Difficulty | Range  | Lives | Max Score |
|------------|--------|-------|-----------|
| Easy       | 1–50   | 10    | 100       |
| Medium     | 1–100  | 7     | 200       |
| Hard       | 1–200  | 5     | 300       |

## Features

- **Signal gauge** — a needle shows how close your guess is, with a hot/cold reading and a direction hint (aim higher / aim lower)
- **Scoring** — based on how many lives you have left when you win; using a hint costs you points
- **Hints** — offered if you're struggling (parity, divisibility, or a narrowed range), at the cost of some score
- **Session stats** — tracks games played, wins/losses, best score, and win streak across rounds
- **Input validation** — rejects non-numbers and out-of-range guesses without crashing

## Versions

- `NumberGuessing.py` — command-line version, built in Python
- `signal_locator.html` — browser version with the interactive gauge UI

## Running it

**Python (CLI):**
```bash
python NumberGuessing.py
```

**Browser:**
Just open `signal_locator.html` in any browser — no install needed.
