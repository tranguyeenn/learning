from datetime import date
import os
import json

class EnergyLevelError(Exception):
    pass

class HoursWorkedError(Exception):
    pass

class DuplicateEntryError(Exception):
    pass

def add_entry():
    today = date.today() 
    mood = input("How are you feeling today? ")

    try: # Validate that energy level is an integer between 1 and 10
        energy_level = int(input("What's your energy level (1-10)? "))
        if energy_level < 1 or energy_level > 10:
            raise EnergyLevelError()
    except ValueError:
        print("Please enter a valid number for energy level.")
        return add_entry()  # Restart the entry process if invalid input is given
    except EnergyLevelError:
        print("Energy level must be between 1 and 10.")
        return add_entry()  # Restart the entry process if invalid input is given
    
    try: # Validate that hours worked is a number and not negative or more than 24
        hours_work = float(input("How many hours did you work today? "))
        if hours_work < 0 or hours_work > 24:
            raise HoursWorkedError()
    except ValueError:
        print("Please enter a valid number for hours worked.")
        return add_entry()  # Restart the entry process if invalid input is given
    except HoursWorkedError:
        print("Hours worked cannot exceed 24 or be negative.")
        return add_entry()  # Restart the entry process if invalid input is given
    
    task = input("What was the main task you accomplished today? ")
    notes = input("Any additional notes? (optional) ")

    entry = {
        "date": today.isoformat(),
        "mood": mood,
        "energy_level": energy_level,
        "hours_work": hours_work,
        "task": task,
        "notes": notes
    }

    return entry

def save_entry(entry):
    filename = f"{date.today().isoformat()}.json"
    filepath = os.path.join("terminal-tracker", "log", filename)
    
    try:
        # 1. Check if it exists BEFORE saving
        if os.path.exists(filepath):
            raise DuplicateEntryError()

        # 2. Try to save
        with open(filepath, "w") as f:
            json.dump(entry, f, indent=4)
            
    except FileNotFoundError:
        # Create directory and retry
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        save_entry(entry) 
        
    except DuplicateEntryError:
        manual_file = input("Filename exists. Enter a different name: ")
        manual_path = os.path.join("terminal-tracker", "log", f'{manual_file}.json')
        with open(manual_path, "w") as f:
            json.dump(entry, f, indent=4)
            
    print("Entry saved successfully!")

entry = add_entry()
save_entry(entry)