#initializing variables using user input
x = int(input("input a number: "))
y = int(input("input a number: "))
assignment = 0

#artihmetic expression
addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y
floor_division = x // y
exponent = x ** y

print(f"addition: {addition}")
print(f"subtraction: {subtraction}")
print(f"multiplication: {multiplication}")
print(f"division: {division}")
print(f"floor division: {floor_division}")
print(f"exponent: {exponent}")

##compound operators
assignment += 2
print(f"addition assignment = {assignment}")
assignment -= 1
print(f"subtraction assignment = {assignment}")
assignment *= 10
print(f"multiplication assignment = {assignment}")
assignment /= 2
print(f"division assignment = {assignment}")
assignment *= 2
print(f"multiplication assignment = {assignment}")
assignment //= 3
print(f"floor division assignment = {assignment}")
assignment %= 2
print(f"modulo assignment = {assignment}")
