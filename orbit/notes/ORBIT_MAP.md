# Orbit-Map

## Why is there multiple HTML pages?
Each widget (weather, lyrics, calendar) has its own HTML entry file so they can run as independent windows instead of being rendered under one shared application entry point.

Without separate HTML pages:
- Widgets would share the same root entry
- Components would load into one application context
- Opening one widget could mean rendering everything together
- Metadata, styling, and initialization would be harder to isolate

Separate HTML files allow each widget to have:
- Its own root element (`#root`)
- Independent entry scripts
- Separate metadata and body classes
- Isolated rendering behavior
- Individual Tauri windows

This also enables Vite’s multi-page configuration, where each HTML file acts as a separate build entry.

*** Flow ***
Weather.html --> Weather.tsx --> React renders widget --> Tauri runs the application
Lyrics.html --> Lyrics.tsx --> React renders widget --> Tauri runs the application
Calendar.html --> Calendar.tsx --> React renders widget --> Tauri runs the application
Welcome.html --> Welcome.tsx --> React renders screen --> Tauri runs the application 

## Calendar.tsx
Entry point for the calendar widget, it holds everything that the calendar widget needs.
Vite loads calendar.tsx as an ES module and the script finds #root and mount React there.
Contains 4 Import
- StrictMode 
- createRoot
- Widget-Shell.css
- CalendarWidget components

Get roots from calendar.html and throw an error if it cannot find root.

Attach React to #root and create this tree: strict dev checks → widget shell div → calendar component using createRoot(el).render

## Weather.tsx
Entry point for the weather widget, it holds everything that the weather widget needs.
Vite loads weather.tsx as an ES module and the script finds #root and mount React there.
Contains 4 Import
- StrictMode 
- createRoot
- Widget-Shell.css
- WeatherWidget components

Get roots from weather.html and throw an error if it cannot find root.

Attach React to #root and create this tree: strict dev checks → widget shell div → weather component using createRoot(el).render

## Lyric.tsx
Entry point for the lyric widget, it holds everything that the weather widget needs.
Vite loads lyric.tsx as an ES module and the script finds #root and mount React there.
Contains 4 Import
- StrictMode 
- createRoot
- Widget-Shell.css
- LyricWidget components

Get roots from lyric.html and throw an error if it cannot find root.

Attach React to #root and create this tree: strict dev checks → widget shell div → lyric component using createRoot(el).render

## Welcome.tsx
Unlike the rest of the entry point, this one determine the size of the widget (full screen size), whether to show it, and set a timer when the app is first boot up for the day in order to pop up the widget.

Import
- StrictMode
- useCallBack
- useEffect
- useRef
- useState
- createRoot
- welcome-shell.css
- listen from api/event in the tauri folder
- currentMonitor, getCurrentWindow from api/windows
- DailyWelcomeOverlay from components
- clearWelcomeShownToday, markWelcomeShownToday, shouldShowWelcome from library

It waits for the widget to load up for 1.5 seconds before the welcome message is display
