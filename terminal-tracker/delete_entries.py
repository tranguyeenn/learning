import os
from pathlib import Path

def delete_entry():
    try: #check if file exists before trying to delete
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
    
    for i, file in enumerate(sort, 1):
        print(f"Available entries: {i}. {file}")

    delete_file = input("Which entry would you like to delete? (Enter the number) ")

    try:
        delete_index = int(delete_file) - 1
        if delete_index < 0 or delete_index >= len(sort):
            print("Invalid entry number.")
            return
        os.remove(f"terminal-tracker/log/{sort[delete_index]}")
        print(f"Entry '{sort[delete_index]}' has been deleted.")
    except ValueError:
        print("Please enter a valid number.")
    except FileNotFoundError:
        print("File not found. Please try again.")

delete_entry()