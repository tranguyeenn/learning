##list can hold multiple data types, array can't
info = [2025, "December", "Winter", 12.05, 48]
data = [2024, "December", "Winter"]
num = [1, 5, 6, 2, 3, 5, 6]

year = info[0] ##accessing the first element of the list, same as string
info[2] = "Autumn" ##updating an element
info.append("Monday") ##add value to the end of the list
time = info.pop(3) ##removing an element at a certain index and stores it
info.remove(48) ##remove the first element that matches the value
info_data = info + data ##concatenating list
minimum = min(num) ##minimum
maximum = max(num) ##maximum
sum_list = sum(num) ##sum of all the list 

print(f"The year is {year}")
print(f"My favorite season is {info[2]}")
print(f"Today is {info[-1]}")
print(f"The time is {time}")
print(f"The length of the list is {len(info)} elements")
print(info)
print(f"The list info data includes: {info_data}")
print(f"The maximum of nums is {maximum}; the minimum of nums is {minimum}; the sum of nums is {sum_list}")
print(f"Winter index is at {data.index("Winter")}") ##index of a vlaue
print(f"The reoccurence of December in info_data is {info_data.count("December")}") ##count the occurence of the value
