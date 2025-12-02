from collections import namedtuple

##Tuple creation
school = (32.1574, 82.9071) 
university = (33, "Gilmer St", "SE", "Atlanta", "GA", "30303")

##Accessing tuple
print(f"My house coordinate is {school[0]} north, {school[-1]} west")

##Length of tuple
print(f"Length of my school address: {len(university)}")

##Tuple cannot be changed
try:
    school[1] = -84
except:
    print("Tuples are immutable")


f1 = namedtuple("Team", ["team", "driver1", "driver2", "engine", "points"])

mcLaren = f1(team = "McLaren", driver1 = "Lando Norris", driver2 = "Oscar Piastri", engine = "Mercedes", points = 433)
red_bull = f1(team = "Red Bull Racing", driver1 = "Max Verstappen", driver2 = "Sergio Perez", engine = "Honda", points = 860)

print(f"The best driver is {mcLaren.driver1}") ##accessing an attribute in the namedTuple
print(f"The highest point earning team is {red_bull.team}")

print(mcLaren) ##printing the entire namedTuple
print(red_bull)