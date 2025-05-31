dict={}
with open("numbers.txt", "r") as file:
    for line in file:
        line = line.rstrip ("\n")
        for digit in line:
            if digit==" ":
                continue
            elif digit not in dict:
                dict[digit] = 1
            elif digit in dict:
                dict[digit] = dict[digit]+1

with open('report.txt', 'w') as count:
    for x in "0123456789":
        if x in dict:
            count.write("{:<2}{}\n".format(x, dict[x]))
        else:
            count.write("{:<2}{}\n".format(x, "0"))
