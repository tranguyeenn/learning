# Java OOP 

## Purpose

This repository exists to intentionally learn **Object-Oriented Programming (OOP)** using Java as a constraint-heavy language.

The goal is **not** to master Java syntax or frameworks, but to:
- build strong object design instincts
- understand ownership, responsibility, and boundaries
- transfer OOP thinking to TypeScript, Python, and backend systems

Java is used because it forces discipline.

---

## How This Repository Is Structured

This repo is organized by **phases**, where each phase focuses on a single OOP concept.

Each phase:
- lives in its own folder
- is implemented independently
- may intentionally duplicate class names from earlier phases

This allows redesigning the same ideas with better understanding over time.

```text
src/
├── phase0_basics/
├── phase1_objects/
├── phase2_behavior/
├── phase3_composition/
├── phase4_inheritance/
├── phase5_interfaces/
├── phase6_state/
├── phase7_exceptions/
└── capstone/
```

Earlier phases are expected to feel naive or imperfect.

That is intentional.

---

## Learning Rules

These rules are enforced throughout the curriculum:

- VS Code only (no IntelliJ features doing design for me)
- No frameworks (Spring, etc.)
- No Lombok or code generation
- No copying full solutions
- Design before implementation
- Prefer composition over inheritance
- Business rules live inside the objects they affect
- Refactoring is expected and encouraged

---

## Phase Overview

### Phase 0 — Basics & Setup
**Focus:**  
- Running Java from the terminal
- Understanding project structure

**Reflection:**
- What felt different from scripting languages?
- What felt unnecessarily verbose?

---

### Phase 1 — Objects & Encapsulation
**Focus:**  
- Classes and objects
- Constructors
- Access modifiers
- Immutability

**Reflection:**
- What data should never be invalid?
- What rules belong in constructors?
- What should not be publicly accessible?

---

### Phase 2 — Behavior & Invariants
**Focus:**  
- Methods as behavior
- Enforcing business rules
- Mutability vs immutability

**Reflection:**
- Where did logic initially live incorrectly?
- What broke when rules were bypassed?
- How did moving logic into objects help?

---

### Phase 3 — Composition & Ownership
**Focus:**  
- Object relationships
- “Has-a” vs “Is-a”
- Ownership boundaries

**Reflection:**
- Who owns what data?
- Which objects should not know about each other?
- Where was composition clearly better than inheritance?

---

### Phase 4 — Inheritance (and Its Problems)
**Focus:**  
- Inheritance
- Method overriding
- Base vs derived responsibilities

**Reflection:**
- Where inheritance felt tempting
- Where it felt wrong
- What problems inheritance introduced

---

### Phase 5 — Interfaces & Abstraction
**Focus:**  
- Interfaces
- Decoupling
- Programming to contracts

**Reflection:**
- How did interfaces reduce coupling?
- What became easier to change?
- What became harder to understand?

---

### Phase 6 — State & Lifecycle
**Focus:**  
- Object state
- Enums
- Valid vs invalid transitions

**Reflection:**
- What states exist in the domain?
- Which transitions should be forbidden?
- Where should state logic live?

---

### Phase 7 — Exceptions as Design
**Focus:**  
- Domain exceptions
- Fail-fast design
- Error boundaries

**Reflection:**
- What errors are part of the domain?
- Where should exceptions be thrown?
- Where should they NOT be handled?

---

## Capstone Project

The capstone combines all prior concepts into a single, cohesive domain model.

**Goals:**
- Clear ownership
- Minimal public surface area
- No god objects
- Well-defined responsibilities

**Reflection:**
- What design decisions changed from earlier phases?
- Where did Java help clarity?
- Where did Java feel restrictive?

---

## Transfer of Knowledge

This curriculum is language-agnostic in outcome.

**Reflections:**
- How Java interfaces map to TypeScript interfaces
- How encapsulation translates to Python
- How this affects backend and system design thinking

The goal is to leave Java with better instincts, not dependency.

---

## Final Notes

This repository represents **deliberate practice**, not production code.

Messy phases are expected.  
Refactoring is part of learning.  
Understanding > speed.