Dict={}
with open("numbers.txt", "r") as file:
    for line in file:
        line = line.rstrip ("\n")
        for digit in line:
            if digit==" ":
                continue
            elif digit not in Dict:
                Dict[digit] = 1
            elif digit in Dict:
                Dict[digit] = Dict[digit]+1

with open('report.txt', 'w') as count:
    for x in "0123456789":
        if x in Dict:
            count.write("{:<2}{}\n".format(x, Dict[x]))
        else:
            count.write("{:<2}{}\n".format(x, "0"))
