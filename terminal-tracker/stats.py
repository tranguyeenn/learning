import json
import os
from pathlib import Path

def load_entries():
    try:
        folder = Path("terminal-tracker/log")
        files = []

        for file in folder.iterdir():
            name = file.name
            if name.endswith(".json"):
                files.append(name)

        sort = sorted(files, key=lambda x: x.split(".")[0])

    except FileNotFoundError:
        os.makedirs("terminal-tracker/log", exist_ok=True)
        print("No entries found.")
        return

    if sort == []:
        print("No entries found.")
        return

    entries = []
    for file in sort:
        with open(f"terminal-tracker/log/{file}", "r") as f:
            entry = json.load(f)
            entries.append(entry)

    return entries

def avg_energy():
    entries = load_entries()  # Ensure entries are loaded
    
    total_energy = 0
    count = 0

    for entry in entries:
        total_energy += entry.get("energy_level", 0)
        count += 1

    avg_energy = total_energy / count if count > 0 else 0
    print(f"Average energy: {avg_energy:.2f}")

def avg_hours():
    entries = load_entries()  # Ensure entries are loaded

    total_hours = 0
    count = 0

    for entry in entries:
        total_hours += entry.get("hours_work", 0)
        count += 1

    avg_hours = total_hours / count if count > 0 else 0
    print(f"Average hours worked: {avg_hours:.2f}")

def common_mood():
    entries = load_entries()  # Ensure entries are loaded

    mood_count = {}

    for entry in entries:
        mood = entry.get("mood", "Unknown")
        mood_count[mood] = mood_count.get(mood, 0) + 1

    common_mood = max(mood_count, key=mood_count.get)
    print(f"Most common mood: {common_mood} ({mood_count[common_mood]} entries)")

def common_tasks():
    entries = load_entries() # Ensure entries are loaded
    task_count = {}
    
    for entry in entries:
        tasks = entry.get("tasks", [])
        for task in tasks:
            task_count[task] = task_count.get(task, 0) + 1
            
    if not task_count:
        print("Most common task: None")
        return
        
    common_task = max(task_count, key=task_count.get)
    print(f"Most common task: {common_task} ({task_count[common_task]} entries)")


def total_entries():
    entries = load_entries()  # Ensure entries are loaded
    total = len(entries) if entries else 0
    print(f"Total entries: {total}")

def view_stats():
    print("\n--- Statistics ---")
    avg_energy()
    avg_hours()
    common_mood()
    common_tasks()
    total_entries()