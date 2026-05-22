# learning log
> building things, breaking things, fixing things.

a repo for tracking what i actually build — not what i vaguely intend to learn someday.

terminal projects live in python. the browser dashboard lives in javascript. each folder has its own readme with project details, struggles, and notes.

---

## learning log

longer notes and reflections:

[View learning log](https://docs.google.com/document/d/1Z6y-5tDoqvpw3-9Hb7u7ddhDjvA6swnR_5VASgOkq5g/edit?usp=sharing)

---

## repo layout

```
learning/
├── python/                          → [python/README.md](python/README.md)
│   ├── number_guess.py
│   ├── pomodoro_cli.py
│   ├── rock_paper_scissor.py
│   └── terminal-tracker/
└── javascript/
    └── personal-dashboard/          → [javascript/personal-dashboard/README.md](javascript/personal-dashboard/README.md)
```

---

## quick run

from the repo root:

| project | command |
|---|---|
| number guessing game | `python python/number_guess.py` |
| pomodoro timer | `python python/pomodoro_cli.py` |
| rock paper scissors | `python python/rock_paper_scissor.py` |
| terminal tracker | `python python/terminal-tracker/main.py` |

the personal dashboard is browser-based — see the javascript readme when the app is runnable.

---

# goals

- build small projects independently before reaching for frameworks
- improve problem-solving and how i structure programs
- get strong at python fundamentals and apply them without tutorials
- learn javascript through real features on a dashboard i actually use
- understand data flow, state, and persistence on the frontend
- get comfortable with harder projects instead of avoiding them

---

# current focus

## python
- classes and object-oriented design
- shared modules instead of duplicated file-loading logic
- sqlite as the next step after json files

full write-ups → [python/README.md](python/README.md)

## javascript
- personal dashboard built feature by feature
- dom, events, localStorage, and rendering before reaching for react
- small modules: calendar, tasks, focus timer, daily check-in

full plan → [javascript/personal-dashboard/README.md](javascript/personal-dashboard/README.md)

---

# projects

| project | track | status |
|---|---|---|
| number guessing game | python | complete |
| pomodoro timer | python | complete |
| rock paper scissors | python | complete |
| terminal tracker | python | complete |
| personal dashboard | javascript | in progress |

concepts practiced and what i learned for each finished project are in [python/README.md](python/README.md).

---

# things i struggled with

- copy-pasting logic instead of refactoring when three functions do the same thing
- debugging across multiple files when the traceback points somewhere unhelpful
- streak and date math without off-by-one mistakes
- knowing when the program is good enough to ship vs polish forever
- keeping json field names consistent so stats don’t silently skip data
- starting a frontend project without defaulting to tutorial-shaped code

---

# mini wins

- four finished python terminal projects
- built terminal tracker with json storage, stats, streaks, and recommendations
- split the repo into `python/` and `javascript/` so tracks stay separate
- documented progress in readmes instead of treating them as one-time files
- defined a real dashboard project plan tied to actual study habits

---

# next topics

**python:** classes · shared data layer · sqlite · pytest · simple apis

**javascript:** dom and events · localStorage · `setInterval` · `fetch` · date logic for calendar and streaks

---

# future project ideas

- terminal tracker v2 with sqlite
- task cli with due dates and saved state
- habit charts from tracker data
- weather or quote widgets on the dashboard
- port a python game logic pattern into javascript
- small rest api backed by a real database

more ideas per track → [python/README.md](python/README.md) · [javascript/personal-dashboard/README.md](javascript/personal-dashboard/README.md)

---

# reminder to self

good programmers are not people who instantly know the answer.

they are people who:
- stay curious long enough
- tolerate confusion long enough
- keep building anyway
