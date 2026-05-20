# learning log
> building things, breaking things, fixing things.

tracking progress so i stop acting like i've learned nothing after every difficult project.

---

## Actual Learning Log

Full document with notes, projects, struggles, and progress:

[View learning log](https://docs.google.com/document/d/1Z6y-5tDoqvpw3-9Hb7u7ddhDjvA6swnR_5VASgOkq5g/edit?usp=sharing)

---

## repo

| project | run |
|---|---|
| number guessing game | `python number_guess.py` |
| pomodoro timer | `python pomodoro_cli.py` |
| rock paper scissors | `python rock_paper_scissor.py` |
| terminal tracker | `python terminal-tracker/main.py` |

---

# goals

- become genuinely strong at python
- build projects independently
- improve problem-solving + coding logic
- learn backend systems properly
- understand ml beyond surface-level tutorials
- get comfortable with harder projects instead of avoiding them

---

# current focus

## beyond basics

currently practicing:
- multi-file program structure
- file handling (json persistence)
- custom exceptions
- pathlib + datetime
- aggregating data across files
- input validation at scale

current status:
- comfortable with core syntax and small scripts
- can structure a multi-module cli from scratch
- still building confidence with oop and larger refactors

---

# projects

## number guessing game
started: may 2026 · status: complete

guess a random number between 1 and 100. pick easy, medium, or hard for different attempt limits.

concepts practiced:
- while loops
- conditionals
- functions
- random module
- input validation
- dictionaries

what i learned:
- while loops work well for “keep asking until input is valid”
- a dictionary can map level choices to attempt counts without extra conditionals
- duplicating easy/medium/hard functions made it obvious when logic should be shared
- separating game rules into functions keeps the main script readable

---

## pomodoro timer
started: may 2026 · status: complete

a terminal pomodoro with a live countdown and an optional 5-minute break after each work session.

concepts practiced:
- loops
- functions
- time module
- formatting output
- menu systems
- basic program flow

what i learned:
- `time.sleep()` plus formatted output can drive a real-time countdown in the terminal
- `end="\r"` lets one line update in place instead of printing every second
- try/except catches bad numeric input before the timer starts
- a simple menu loop is enough structure for start vs exit without overcomplicating things

---

## rock paper scissors
started: may 2026 · status: complete

play rock paper scissors against the computer in a loop, with running scores until you quit.

concepts practiced:
- functions
- random module
- while loops
- conditionals
- score tracking
- input validation
- `if __name__ == "__main__"`

what i learned:
- putting all win/loss/tie rules in `winner()` keeps the main game loop simple
- recursion can re-prompt on bad input and re-run the same logic with valid data
- score variables outside the round loop persist across multiple plays
- `if __name__ == "__main__"` keeps the file runnable without side effects on import

---

## terminal tracker
started: may 2026 · status: complete

a cli for logging daily mood, energy, hours worked, and tasks. entries persist as json files; the app surfaces stats, streaks, and burnout-style recommendations from the last 30 days.

**modules:** `add_entry`, `view_entries`, `delete_entries`, `stats`, `recommendations`, `streaks_counter`, `main`

concepts practiced:
- multi-file project layout
- json read/write
- pathlib + os
- datetime + timedelta
- custom exceptions (`EnergyLevelError`, `HoursWorkedError`, `DuplicateEntryError`)
- aggregating data across files
- sorting and date logic
- menu-driven cli

what i learned:
- splitting features into modules keeps each file manageable
- one json file per day is a simple persistence model before sqlite
- custom exceptions make validation failures explicit instead of buried in if/else
- aggregating entries across files is how stats, streaks, and recommendations are built
- date logic (`datetime`, `timedelta`) is required once data spans multiple days

---

# things i struggled with

- deleting copy-pasted blocks instead of leaving three nearly identical functions
- deciding whether to ship or refactor when the program already works
- following an error through imports when the failure shows up in the wrong file
- streak math and sorting dates without mixing up today vs yesterday
- using the same field names everywhere so stats don’t silently skip data
- knowing when recursion helps vs when a plain loop is clearer
- remembering which folder to run from so json paths resolve
- switching from “a bunch of dicts” to thinking in classes

---

# mini wins

- shipped four working clis without abandoning them halfway
- stored real daily logs and built stats on top of them
- raised custom errors instead of only printing and returning
- read and wrote json across many files in one app
- isolated rock-paper-scissors rules so the main loop stayed short
- traced multi-file bugs until the behavior matched what i intended
- treated the readme as a log, not a one-time readme dump

---

# next topics

- classes and object-oriented design
- a single shared module for loading and saving entries
- sqlite as the backend for terminal tracker
- packaging, imports, and proper script entrypoints
- automated tests for edge cases in streaks and averages
- calling and building simple http apis
- classic data structures when dicts stop being enough
- async python and a small web framework intro

---

# future project ideas

- task cli with due dates, reminders, and saved state
- terminal tracker rebuilt on sqlite with less repeated code
- habit dashboard that plots energy and hours over time
- cli that pulls weather or headlines from the internet
- flashcard drill app driven by a json deck
- minimal rest api with a real database behind it
- short numpy or pandas exercises for numerics
- mood classifier trained on my own tracker history

---

# reminder to self

good programmers are not people who instantly know the answer.

they are people who:
- stay curious long enough
- tolerate confusion long enough
- keep building anyway
