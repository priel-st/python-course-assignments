dict={}
with open("/Users/mac/numbers.txt", "r") as file:
    for line in file:
        line = line.rstrip ("\n")
        for digit in line:
            if digit==" ":
                continue
            elif digit not in dict:
                dict[digit] = 1
            elif digit in dict:
                dict[digit] = dict[digit]+1

for x in "0123456789":
    if x in dict:
        print("{:<2}{}".format(x, dict[x]))
    else:
        print("{:<2}{}".format(x, "0"))
