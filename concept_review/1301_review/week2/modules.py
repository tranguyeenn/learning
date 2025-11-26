#importing test_modules script
import test_modules

#executing the test_modules script using the dot notation to call the function of the script
print("You have sucessfully enroll in", test_modules.courseCode)
print(f"{test_modules.courseCode} is {test_modules.courseName}")
print(f"The professor for {test_modules.courseCode} is {test_modules.professorName}")
print(f"The time section for {test_modules.courseCode} is {test_modules.courseTime}")
print(f"The location for {test_modules.courseCode} is at {test_modules.location}")

#----------------------------------------------------------------------------------------
#importing the built in python math function
import math

x = 2.103

print(f"Rounding up value: {math.ceil(x)}") #rounding up
print(f"Factorial: {math.factorial(x)}") #factorial

#continue tomorrow