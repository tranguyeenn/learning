#importing test_modules script
import test_modules

#executing the test_modules script using the dot notation to call the function of the script
print("You have sucessfully enroll in", test_modules.courseCode)
print(f"{test_modules.courseCode} is {test_modules.courseName}")
print(f"The professor for {test_modules.courseCode} is {test_modules.professorName}")
print(f"The time section for {test_modules.courseCode} is {test_modules.courseTime}")
print(f"The location for {test_modules.courseCode} is at {test_modules.location}")
print()
#----------------------------------------------------------------------------------------
#importing the built in python math function
import math

x = 2.103
z = 9
y = 2
n = -21
myList = [1, 2, 3, 4, 5, 6]

print(f"Rounding up value: {math.ceil(x)}") 
print(f"Factorial: {math.factorial(y)}") 
print(f"Remainder of division: {math.fmod(z, y)}")
print(f"Absolute value: {math.fabs(n)}")
print(f"Rounding down value: {math.floor(x)}")
print(f"Floating point sum of a range: {math.fsum(myList)}")
print(f"Exponential function: {math.exp(y)}")
print(f"Power function: {math.pow(y, z)}")
print(f"Natural Log: {math.log(y)}; Log Function: {math.log(y, z)}")
print(f"Square root: {math.sqrt(z)}")
print(f"Arc cosin: {math.acos(1)}")
print(f"Arc tangent: {math.atan(1)}")
print(f"Arc sine: {math.asin(1)}")
print(f"Arc tangent with two parameters: {math.atan2(1, 0)}")
print(f"Cosine: {math.cos(math.pi)}")
print(f"Sine: {math.sin(math.pi)}")
print(f"Length of vector from origin: {math.hypot(9, 2)}")
print(f"Convert rad to degree: {math.degrees(math.pi/3)}")
print(f"Convert degress to radians: {math.radians(90)}")
print(f"Tangent: {math.tan(math.pi)}")
print(f"Hyperbolic cosine: {math.cosh(1)}")
print(f"Hyperbolic sine: {math.sinh(1)}")
print(f"Gamma function: {math.gamma(1)}")
print(f"Error Function: {math.erf(z)}")
print(f"Pi constant: {math.pi}")
print(f"e constant: {math.e}")