def hungry(isHungry):
    if isHungry == True:
        return True
    else:
        return False

print(hungry(True))

def courses(spring26):
    creditHour = 0

    for course, credits in spring26.items():
        creditHour += credits

    return creditHour, list(spring26.keys())

spring26 = {"Human Communication": 2,
            "Jazz Origins, Style, Influence Music Appreciation": 3,
            "Linear Algebra I": 3,
            "Principle of Computer Science II Lab": 1,
            "Principle of Computer Science II": 3,
            "Theoretical Foundation of Computer Science": 3}
print(courses(spring26))
        