from add_entry import add_entry
from view_entries import view_entries
from delete_entries import delete_entry
from stats import view_stats
from recommendations import generate_recommendations
from streaks_counter import view_streaks

def main():
    while True:
        print("\nTerminal Tracker")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Delete Entry")
        print("4. View Stats")
        print("5. Generate Recommendations")
        print("6. View Streaks")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            delete_entry()
        elif choice == '4':
            view_stats()
        elif choice == '5':
            generate_recommendations()
        elif choice == '6':
            view_streaks()
        elif choice == '7':
            print("Exiting Terminal Tracker. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")
