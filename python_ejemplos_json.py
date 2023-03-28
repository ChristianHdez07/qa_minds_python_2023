import json

with open("ejemplo.json") as file:
    data = json.load(file)
    print(data["contacts"][0]["nombre"])