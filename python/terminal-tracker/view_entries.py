from pathlib import Path
import os
import json

def view_entries():
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
        
    for i, file in enumerate(sort, 1):
        print(f"Available entries: {i}. {file}")
    
    view_file = input("Which entry would you like to view? (Enter the number): ")

    try:
        view_index = int(view_file) - 1
        if view_index < 0 or view_index >= len(sort):
            print("Invalid entry number.")
            return
        with open(f"terminal-tracker/log/{sort[view_index]}", "r") as f:
            entry = json.load(f)
            print(json.dumps(entry, indent=4))
    except ValueError:
        print("Please enter a valid number.")
    except FileNotFoundError:
        print("File not found. Please try again.")

view_entries()