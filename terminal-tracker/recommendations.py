import os
from pathlib import Path
import json
from datetime import datetime, timedelta

def load_files():
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

    return sort

def sort_dates():
    sort = load_files()

    if sort == []:
        print("No entries found.")
        return

    dates = []
    for file in sort:
        with open(f"terminal-tracker/log/{file}", "r") as f:
            entry = json.load(f)
            dates.append(entry["date"])

    #bubble sort
    n = len(dates)

    for i in range(n):
        for j in range(0, n - i - 1):
            if dates[j] > dates[j + 1]:
                dates[j], dates[j + 1] = dates[j + 1], dates[j]
    
    return dates

def valid_entries():
    dates = sort_dates()

    if dates == []:
        print("No entries found.")
        return
    
    valid_dates = []
    
    for date in dates:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        if date_obj >= datetime.now() - timedelta(days=30):
            valid_dates.append(date)
        if date_obj > datetime.now():
            valid_dates.remove(date)

    return valid_dates

def avg_energy():
    valid_dates = valid_entries()

    if valid_dates == []:
        print("No valid entries found.")
        return
    
    total_energy = 0
    count = 0

    for date in valid_dates:
        with open(f"terminal-tracker/log/{date}.json", "r") as f:
            entry = json.load(f)
            total_energy += entry["energy_level"]
            count += 1

    avg_energies = total_energy / count

    return avg_energies

def productivity_hours():
    valid_dates = valid_entries()

    if valid_dates == []:
        print("No valid entries found.")
        return
    
    productivity_hours = 0

    for date in valid_dates:
        with open(f"terminal-tracker/log/{date}.json", "r") as f:
            entry = json.load(f)
            productivity_hours += entry["hours_work"]

    return productivity_hours

def common_mood():
    valid_dates = valid_entries()

    if valid_dates == []:
        print("No valid entries found.")
        return
    
    moods = []

    for date in valid_dates:
        with open(f"terminal-tracker/log/{date}.json", "r") as f:
            entry = json.load(f)
            moods.append(entry["mood"])

    mood_counts = {}
    for mood in moods:
        if mood in mood_counts:
            mood_counts[mood] += 1
        else:
            mood_counts[mood] = 1

    most_common_mood = max(mood_counts, key=mood_counts.get)

    return most_common_mood

def generate_recommendations():
    avg_energy_level = avg_energy()
    total_productivity_hours = productivity_hours()
    common_mood_value = common_mood()

    #energy level recommendations
    if avg_energy_level is not None and avg_energy_level < 4:
        print("Energy has been low recently. Consider rest.")
    elif avg_energy_level >= 4 and avg_energy_level < 7:
        print("Energy levels are moderate. Keep monitoring.")
    else:
        print("Energy levels are good. Keep up the good work!")

    #productivity hours recommendations
    if total_productivity_hours is not None and total_productivity_hours > 40:
        print("Possible burnout detected. Consider taking breaks.")
    elif total_productivity_hours >= 20 and total_productivity_hours <= 40:
        print("Productivity hours are within a healthy range. Keep it up!")
    else:
        print("Productivity hours are low. Consider setting achievable goals.")

    #mood recommendations
    if common_mood_value is not None:
        if common_mood_value.lower() in ["motivated", "excited", "happy", "good"]:
            print("Productivity trend improving. Keep up the positive mindset!")
        elif common_mood_value.lower() in ["stressed", "anxious", "overwhelmed", "sad", "tired"]:
            print("Consider stress management techniques to improve mood.")
        else:
            print(f"Your most common mood is {common_mood_value}. Consider activities that boost your mood.")
