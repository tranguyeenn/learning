nested_list = [[10, 12], [20, 20], [30, 50]]

new_list = (row[0] * row[1] for row in nested_list)

print(list(new_list))