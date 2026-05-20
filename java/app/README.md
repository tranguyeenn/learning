# java learning log
> same energy as the python repo — build, break, fix, document.

tracking java progress separately so i don’t mix up what i’ve actually practiced in each language.

---

## repo

| project | run |
|---|---|
| calculator | `javac app/Calculator.java && java app.Calculator` |

run from the `learning` root, or from `app/` with `javac Calculator.java && java app.Calculator`.

---

# goals

- learn java syntax and conventions without fighting the compiler
- understand packages, classes, and how the jvm actually runs code
- get comfortable with static typing and compile-time errors
- build small terminal programs before jumping into frameworks
- connect java concepts back to what i already know from python

---

# current focus

## first steps

currently practicing:
- `main` and program entrypoints
- primitive types and `double`
- `if` / `else if` chains
- `Scanner` for terminal input
- packages and folder layout
- compiling with `javac` and running with `java`

current status:
- first java file compiles and runs
- still learning naming rules — class names vs file names vs package names
- debugging jdk errors that sound scarier than they are

---

# projects

## calculator
started: may 2026 · status: complete

a terminal calculator that takes two numbers and an operator, then prints the result. handles divide-by-zero and invalid operators.

**file:** `Calculator.java` · **package:** `app`

concepts practiced:
- `public static void main`
- `Scanner` and `java.util` imports
- `double` and `char`
- conditionals
- string concatenation in output
- closing resources with `close()`

what i learned:
- java files live in a folder that matches the package name
- class name and file name must match — `Calculator.java` holds `class Calculator`
- you cannot use `package java` — that namespace is reserved for the jdk
- compile first, then run the class with the full name: `app.Calculator`
- division by zero needs an explicit check before dividing

---

# things i struggled with

- `SecurityException: Prohibited package name: java` when the folder was named `java` and the package matched
- understanding why vs code tried to run `java.calculator` instead of `app.Calculator`
- remembering to compile before run when coming from python’s interpret-on-save habit
- `Scanner` reading the operator as a string and pulling the first character with `charAt`
- nested `if` blocks for divide-by-zero without making the whole method unreadable

---

# mini wins

- fixed the prohibited package error and got a clean compile
- first program that runs from the terminal with real user input
- handled bad operator and division by zero without crashing
- set up a proper `app` package instead of fighting reserved names

---

# next topics

- methods extracted out of `main` so logic isn’t one long block
- loops and menus — keep calculating until the user quits
- arrays and `ArrayList`
- classes with fields — a calculator object instead of locals in `main`
- exceptions with `try` / `catch` instead of only `if` checks
- maven or gradle once multi-file projects feel necessary
- unit tests with junit

---

# future project ideas

- calculator with history — store past operations in a list
- number guessing game in java
- gradebook or student roster cli
- simple bank account class with deposit and withdraw
- rock paper scissors port from python
- file-backed todo list before touching spring or android

---

# reminder to self

the jdk error messages are verbose on purpose. read the first line that mentions *your* code or package name before googling the rest.

good java habits early:
- match package, folder, and class name
- never name a package `java`, `javax`, or `sun`
- compile, then run with the dotted class name

keep building anyway.