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
print(f"{first_name} is {age}")
print(f"{initial} is {gender}")
print(f"Major: {major}")
print(f"{initial} is from {country}")