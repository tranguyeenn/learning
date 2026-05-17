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
started: may 2026

concepts practiced:
- while loops
- conditionals
- functions
- random module
- input validation
- dictionaries

what i learned:
- repetitive logic can usually be abstracted
- dictionaries can simplify program behavior
- writing messy logic first often reveals cleaner structure later
- optimization makes more sense after understanding the repetitive version

future improvements:
- replay system
- cleaner game flow
- exception handling
- refactor repeated logic into reusable functions

---

## pomodoro timer
started: may 2026

concepts practiced:
- loops
- functions
- time module
- formatting output
- menu systems
- basic program flow

what i learned:
- breaking programs into smaller functions makes logic easier to manage
- input validation matters more than expected
- even simple terminal programs require thinking about user experience

future improvements:
- customizable break lengths
- sound notifications
- session tracking
- file saving

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
- file persistence forces you to think about data shape upfront
- validation and error handling matter more once data is saved
- reading many small files is a workable pattern before reaching for a database

future improvements:
- refactor shared file-loading logic into one module
- classes for entries instead of raw dicts
- sqlite instead of per-day json files
- fix `add_entry.py` running on import (guard with `if __name__ == "__main__"`)

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
