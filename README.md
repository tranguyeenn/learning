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

- designing loop conditions cleanly
- recognizing when logic should become a function
- avoiding repetitive code
- thinking through program flow before coding
- organizing logic across multiple files without duplication
- file paths and where the program expects to run from

---

# mini wins

- completed programs independently
- debugged logic without copying solutions
- started understanding *why* abstractions help
- becoming less intimidated by blank files
- shipped a multi-module project with persistence and analytics

---

# next topics

- classes + object-oriented programming
- refactoring duplicated logic into shared modules
- sqlite
- modules and packaging
- APIs
- data structures
- async python
- backend architecture basics

---

# future project ideas

- task/reminder CLI
- terminal music player
- recommendation system (beyond rule-based)
- scientific computing mini-projects
- ML-based stress detection

---

# reminder to self

good programmers are not people who instantly know the answer.

they are people who:
- stay curious long enough
- tolerate confusion long enough
- keep building anyway
