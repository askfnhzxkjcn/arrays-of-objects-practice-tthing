# COLOR DATA PRACTICE

import json

# Load Color Data from JSON file
file = open("color-data.json", "r")
dataStr = file.read()
file.close()

color_data = json.loads(dataStr)


for i in range(len(color_data)):
    print(color_data[i]["name"], color_data[i]["family"])

for i in range(len(color_data)):
    if color_data[i]["brightness"] >= 200:
        print(color_data[i]["name"], color_data[i]["brightness"])

n = 0
for color in color_data:
    if color["family"] == "Red" or color["family"] == "Pink":
        n+=1
print(f"the number of colors in the family: {n}")

selection = input("Choose a color family: ")
families = 0
for i in range(len(color_data)):
    if color_data[i]["family"] == selection:
        families +=1
        print(color_data[i]["name"], color_data[i]["family"])
print(f"the number of colors that belong to this family: {families}")

check = input("type a single letter: ")

counter = 0
for i in range(len(color_data)):

    if color_data[i]["name"][0] == (check):
        counter+=1
        print(color_data[i]["name"])
print(f"the amount of colors that start with letter {check}: {counter}")