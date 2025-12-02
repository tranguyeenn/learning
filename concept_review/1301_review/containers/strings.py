courses = "Principles of Computer Science I"
city = "Ho Chi Minh City, Vietnam"
demo = "18, F"

##user input is default as a string
first_name = input("Enter your first name: ") 
last_name = input("Enter your last name: ")

##length of string
length_of_first = len(first_name)
length_of_last = len(last_name)

##string indexing - start at 0
initial = first_name[0] + last_name[0]

##reverse indexing - start at -1
gender = demo[-1]

##slicing
age = demo[:2] ##return everything up to the 1st index 
major = courses[14:30] ##return from index 14 to 29
country = city[18:] ##return from index 18 to the last index

##printing
print()
print(f"{first_name} is {age}")
print(f"{initial} is {gender}")
print(f"Major: {major}")
print(f"{initial} is from {country}")

#-------------------STRING FORMATTING--------------------------#
num = 76089
float_num = 194.24514925
hex_val = 31

print()
print(f"Decimal with commas: {num:,d}")
print(f"Leading zeros: {num:07d}")
print(f"Hex (lower): {hex_val:x}")
print(f"Hex (upper): {hex_val:X}")
print(f"Binary of 4: {4:b}")
print(f"Exponent: {44:e}")
print(f"Fixed-point default: {float_num:f}")
print(f"Fixed-point (2 decimals): {float_num:.2f}")
print(f"Commas + precision: {float_num:,.2f}")