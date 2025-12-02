info = {0, 2, 3, 5, 1, 2, 8}
data = {20, 32, 45, 28, 84, 92}

length = len(info) ##length of the set
info.update(data) ##concatenating two sets
print(f"Combining two sets is {info}")

info.add(7) ##appending the value to the end of the list
print(f"Updating the set: {info}")

print(f"The length of the set is {length}")

info.remove(8) ##removing a value from the set
print(info)

data.pop() ##popping the last value of the set
print(data)

info.clear() ##clearing the entire set
print(info)

#--------------------------STATISTICS------------------------------#
stats = {200, 492, 3884, 92942, 1982}
census = {492, 3801, 8402, 92942, 1938, 294}

intersection = set.intersection(stats, census)
##Return a new set containing only the elements in common between set
union = set.union(stats, census)
##Returns a new set containing all of the unique elements in all sets
difference = set.difference(stats, census)
##Return a set containing only the elements of set that are not found in any of the provided sets
symmetric_difference = stats.symmetric_difference(census)
##Return a set containing only elements that appear in exactly one of the set

print()
print("Intersection:", intersection)
print("Union:", union)
print("Difference:", difference)
print("Symmetric Difference:", symmetric_difference)