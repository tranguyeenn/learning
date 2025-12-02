f1_driver = {
    "Max Verstappen": 575,
    "Sergio Perez": 285,
    "Lando Norris": 205,
    "Oscar Piastri": 195,
    "Lewis Hamilton": 180,
    "George Russell": 160,
    "Charles Leclerc": 170,
    "Carlos Sainz": 165,
    "Fernando Alonso": 120,
    "Lance Stroll": 70,
    "Yuki Tsunoda": 50,
    "Daniel Ricciardo": 45,
    "Valtteri Bottas": 15,
    "Zhou Guanyu": 10,
    "Pierre Gasly": 62,
    "Esteban Ocon": 57,
    "Alex Albon": 27,
    "Logan Sargeant": 1,
    "Kevin Magnussen": 3,
    "Nico Hulkenberg": 9
}


f1_driver["Lee Chaeson"] = 50 ##appending the dictionary
lee_point = f1_driver["Lee Chaeson"] ##accessing the value through its key
f1_driver["Logan Sargeant"] = 0 ##updating value in the dictionary
logan_pts = f1_driver["Logan Sargeant"]

print(f"Lee Chaeson points: {lee_point}")
print(f"Logan Sargeant point: {logan_pts}")

del f1_driver["Lee Chaeson"] ##delete dict entry

try:
    print(f1_driver["Lee Chaeson"])
except:
    print("No driver of that name exist in the entry")