# learning
> building things, breaking things, fixing things.

personal repo for python practice, java practice, and studying orbit enough to understand the architecture — not just run it.

progress lives in the readmes below so it’s obvious what’s actually been built.

---

## structure

| folder | what it is | detailed log |
|---|---|---|
| `python/` | terminal clis and small projects | [python/README.md](python/README.md) |
| `java/` | jvm programs — packages, compile, run | [java/app/README.md](java/app/README.md) |

---

## actual learning log

full notes, struggles, and longer-form progress:

[View learning log](https://docs.google.com/document/d/1Z6y-5tDoqvpw3-9Hb7u7ddhDjvA6swnR_5VASgOkq5g/edit?usp=sharing)

---

## quick run

run from the repo root unless noted.

### python

| project | command |
|---|---|
| number guessing game | `python python/number_guess.py` |
| pomodoro timer | `python python/pomodoro_cli.py` |
| rock paper scissors | `python python/rock_paper_scissor.py` |
| terminal tracker | `python python/terminal-tracker/main.py` |

### java

| project | command |
|---|---|
| calculator | `javac java/app/Calculator.java && java -cp java/app app.Calculator` |

---

# goals

- get strong at fundamentals in more than one language
- build small projects independently before reaching for frameworks
- improve problem-solving and program structure
- learn backend and desktop architecture on purpose, not by accident
- understand orbit deeply enough to explain and rebuild its features
- stay comfortable with harder projects instead of avoiding them

---

# current focus

## python
- classes and object-oriented design
- less duplicated logic across modules
- sqlite as a step up from json files

see [python/README.md](python/README.md) for projects, struggles, and next steps.

## java
- packages, compile/run workflow, and jdk errors
- extracting logic out of `main`
- matching folder layout to package names

see [java/app/README.md](java/app/README.md).

## orbit
- one concept, one tiny build, one orbit connection per session
- mapping visible features before reading the whole codebase

see [orbit/README.md](orbit/README.md).

---

# projects at a glance

| project | track | started | status |
|---|---|---|---|
| number guessing game | python | may 2026 | complete |
| pomodoro timer | python | may 2026 | complete |
| rock paper scissors | python | may 2026 | complete |
| terminal tracker | python | may 2026 | complete |
| calculator | java | may 2026 | complete |

write-ups, concepts practiced, and what i learned for each project are in the track readmes.

---

# things i struggled with

- refactoring copy-pasted code instead of shipping three versions of the same function
- multi-file debugging when the error points at the wrong file
- date and streak logic without off-by-one mistakes
- knowing when to stop polishing and move to the next project
- java package rules vs folder names — especially reserved `java.*` packages
- switching between python’s run-anytime flow and compile-then-run in java
- reading a large codebase without a feature map first

---

# mini wins

- four finished python terminal projects
- terminal tracker with json persistence, stats, streaks, and recommendations
- first java program compiles and runs with proper `app` package layout
- reorganized the repo into `python/`, `java/`, and `orbit/` instead of one flat mess
- keeping readmes updated as a real learning log, not a one-time dump

---

# next topics

**python:** classes · shared modules · sqlite · pytest · simple apis

**java:** methods outside `main` · loops and menus · `ArrayList` · try/catch · junit

**orbit:** js fundamentals → react → typescript → tauri → per-feature architecture notes

---

# future project ideas

- task cli with due dates and persistence
- terminal tracker v2 on sqlite
- port a python cli game to java
- orbit mini-widgets rebuilt in isolation before touching the real app
- small rest api with a database
- habit charts from tracker data

track-specific ideas live in [python/README.md](python/README.md) and [java/app/README.md](java/app/README.md).

---

# reminder to self

good programmers are not people who instantly know the answer.

they are people who:
- stay curious long enough
- tolerate confusion long enough
- keep building anyway
