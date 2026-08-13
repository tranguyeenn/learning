'''
Author: Trang Nguyen
Description: Allows user to track their habits and view their progress over time.
'''

def add_habits():
    habits = []
    user_habits = input("Enter your habits separated by commas: ")

    user_habits_list = user_habits.split(",")

    for habit in user_habits_list:
        habit = habit.strip()
        if habit not in habits:
            habits.append(habit)
    return habits

def view_habits(habits):
    print("Your habits are: ", end="")
    for i, habit in enumerate(habits):
        if i == len(habits) - 1:
            print(habit)
        else:
            print(habit, end=", ")

def delete_habits(habits):
    habit_to_delete = input("Enter the habit you want to delete: ")
    if habit_to_delete in habits:
        habits.remove(habit_to_delete)
        print(f"{habit_to_delete} has been deleted.")
    else:
        print(f"{habit_to_delete} is not in your habit list.")

if __name__ == "__main__":
    habits = add_habits()
    view = view_habits(habits)
    delete = delete_habits(habits)
    view = view_habits(habits)