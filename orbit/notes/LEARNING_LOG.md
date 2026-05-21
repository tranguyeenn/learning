# Learning Log
Date: 2026-05-20

## Feature Studied
Calendar.tsx
Weather.tsx
Lyric.tsx

---

## What I Learned

These files are entry points for each widget.

Flow:

HTML page
↓
TSX entry file
↓
Find `#root`
↓
React mounts using `createRoot().render()`
↓
Widget component renders
↓
Widget window appears

Each widget has separate HTML pages because separate entry points allow independent widgets instead of one shared application root.

Examples:

calendar.html
↓
calendar.tsx
↓
CalendarWidget

weather.html
↓
weather.tsx
↓
WeatherWidget

lyric.html
↓
lyric.tsx
↓
LyricWidget

---

## Concepts I Understand Better

[x] Entry files (`calendar.tsx`, `weather.tsx`, `lyric.tsx`)

[x] Separate HTML files create separate widget entry points

[x] Vite can build multiple independent widget pages

[x] React components attach to HTML through `#root`

---

## Unknown Concepts

[ ] Why does React need `#root`?

[ ] What does `createRoot().render()` actually do?

[ ] What is mounting?

[ ] What does rendering mean?

[ ] Why use separate HTML pages instead of one App.tsx + routing?

---

## Questions

If widgets share one HTML page, what would break?

Why does React need an existing HTML element before rendering?

---

## Evidence

Files examined:

- Calendar.tsx
- Weather.tsx
- Lyric.tsx

Time spent:
~40 min