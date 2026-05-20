# ORBIT LEARNING PATH
Goal:
Understand Orbit deeply enough to rebuild features from scratch, explain architecture, and stop relying on "it works somehow."

Rule:
Every study session must include:

- 1 concept
- 1 tiny build
- 1 Orbit connection

No passive reading for 2 hours.
No watching tutorials endlessly.
No trying to understand all Orbit files.

---

# Folder Structure

Create:

orbit-study/
│
├── notes/
│      ORBIT_MAP.md
│      LEARNING_LOG.md
│
├── js-lab/
├── react-lab/
├── tauri-lab/
└── orbit-rebuild/

---

# ORBIT MAP

List visible features only.

## Features

[ ] Welcome screen
[ ] Calendar widget
[ ] Reminder widget
[ ] Weather widget
[ ] Lyrics widget
[ ] Spotify auth
[ ] Notifications
[ ] Window dragging
[ ] Local storage
[ ] Autostart
[ ] Rule-based suggestions

Each feature gets:

Example:

## Weather Widget

Files:
- Weather.tsx
- weatherService.ts
- api.ts

Concepts:
- async/await
- fetch
- state
- JSON

Status:
[ ] understand
[ ] rebuilt
[ ] refactored

---

# PHASE 1
# Weeks 1-2
Goal:
Learn JavaScript concepts Orbit already uses.

Topics:

[ ] variables
[ ] arrays
[ ] objects
[ ] functions
[ ] arrow functions
[ ] conditionals
[ ] loops
[ ] imports/exports
[ ] JSON
[ ] async/await
[ ] fetch
[ ] destructuring
[ ] spread (...)
[ ] map()
[ ] filter()

Daily structure:

20m:
Learn concept

30m:
Tiny build

20m:
Find same concept in Orbit

Examples of tiny builds:

[ ] mood logger
[ ] timer
[ ] weather fetcher
[ ] quote generator
[ ] task tracker
[ ] Spotify API fetch

Milestone:

"I can explain JS appearing inside Orbit."

---

# PHASE 2
# Weeks 3-4
Goal:
Understand React.

Topics:

[ ] components
[ ] props
[ ] state
[ ] useState
[ ] rerenders
[ ] useEffect
[ ] event handlers
[ ] conditional rendering
[ ] lists
[ ] lifting state

Mini builds:

[ ] static weather card
[ ] reminder card
[ ] quote widget
[ ] mini calendar
[ ] task list

Milestone:

"I know WHY widgets update."

---

# PHASE 3
# Weeks 5-6
Goal:
Understand TypeScript instead of surviving TypeScript.

Topics:

[ ] types
[ ] interfaces
[ ] unions
[ ] optional props
[ ] arrays of objects
[ ] generics
[ ] useState<Type>()

Examples to decode:

Weather | null

Reminder[]

useState<Reminder>()

Milestone:

"I understand TS annotations in Orbit."

---

# PHASE 4
# Weeks 6-7
Goal:
Understand desktop behavior.

Experiments:

[ ] transparent window
[ ] dragging
[ ] notifications
[ ] tray icon
[ ] save local file
[ ] autostart
[ ] always-on-top

Milestone:

"I know how Tauri interacts with OS."

---

# PHASE 5
# Weeks 7-8
Goal:
Learn architecture.

For EACH Orbit feature:

Fill:

Feature:

Problem:
What inconvenience exists?

Input:
What data enters?

Output:
What user sees?

State:
What changes?

Services:
External APIs?

Storage:
Saved where?

Failure:
What breaks?

Milestone:

"I can explain Orbit design."

---

# PHASE 6
# Week 8+

Refactor Orbit.

Workflow:

1. Pick feature

2. Map files

3. Learn concepts

4. Rebuild tiny version

5. Compare

6. Refactor real Orbit

Repeat forever.

---

# FIRST 14 DAYS

Day 1:
Map Orbit features

Day 2:
Variables + arrays

Day 3:
Objects + functions

Day 4:
Arrow functions

Day 5:
Async/await

Day 6:
Fetch API

Day 7:
Weather fetch mini app

Day 8:
Components

Day 9:
Props

Day 10:
State

Day 11:
useEffect

Day 12:
Reminder card

Day 13:
Mini widget

Day 14:
Trace Orbit weather feature

---

# LEARNING LOG TEMPLATE

Date:

Concept learned:

Tiny build:

Orbit connection:

What confused me:

Can I explain it without notes?
[ ] yes
[ ] no

---

Reminder:

You are NOT learning JavaScript.

You are learning enough JavaScript, React, TypeScript, and architecture to own Orbit instead of orbiting around your own code.