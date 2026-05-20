import time

def countdown(minutes, session_type):
    seconds = minutes * 60

    print(f"\nStarting {session_type} for {minutes} minutes.\n")

    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60

        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")

        time.sleep(1)
        seconds -= 1

    print(f"\n{session_type} finished!\n")


def start_pomodoro():
    try:
        work_minutes = int(input("Enter work session length (minutes): "))

        if work_minutes <= 0:
            print("Please enter a positive number.")
            return

        countdown(work_minutes, "Pomodoro Session")

        break_choice = input("Would you like to start a 5-minute break? (y/n): ").lower()

        if break_choice == "y":
            countdown(5, "Break")

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":

    while True:
        print("=== Pomodoro Timer ===")
        print("1. Start Pomodoro")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            start_pomodoro()

        elif choice == "2":
            print("Goodbye.")
            break

        else:
            print("Invalid option.\n")