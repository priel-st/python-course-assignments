colors = []
with open("colors.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        colors.append(line)
for col in colors:
    ind = colors.index(col)+1
    print(f"{ind}. {col}")
numberpick = input("Please pick a color from the above menu by typing in its number: ")
if not numberpick.isdigit() or int(numberpick) > len(colors):
    print("Please pick a valid number from the above menu")
else:
    print("You picked:", colors[int(numberpick)-1])
