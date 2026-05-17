import os
from pathlib import Path
import json
from datetime import datetime, timedelta

def current_streak():
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

    date = []

    for file in sort:
        with open(f"terminal-tracker/log/{file}", "r") as f:
            entry = json.load(f)
            date.append(entry["date"])

    current_streak = 0

    for i in range(len(date) - 1):
        current_date = date[i]
        next_date = date[i + 1]
        tomorrow = datetime.strptime(current_date, "%Y-%m-%d") + timedelta(days=1)
        if tomorrow.strftime("%Y-%m-%d") == next_date:
            current_streak += 1
        elif current_date == next_date:
            continue
        else:
            current_streak = 0

    print(f"Current streak: {current_streak}")

def longest_streak():
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

    date = []

    for file in sort:
        with open(f"terminal-tracker/log/{file}", "r") as f:
            entry = json.load(f)
            date.append(entry["date"])

    longest_streak = 0
    current_streak = 0

    for i in range(len(date) - 1):
        current_date = date[i]
        next_date = date[i + 1]
        tomorrow = datetime.strptime(current_date, "%Y-%m-%d") + timedelta(days=1)
        if tomorrow.strftime("%Y-%m-%d") == next_date:
            current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        elif current_date == next_date:
            continue
        else:
            current_streak = 0

    print(f"Longest streak: {longest_streak}")

longest_streak()

def view_streaks():
    print("Current Streaks: ")
    current_streak()
    print("Longest Streaks: ")
    longest_streak()