import sys

filename = sys.argv[1]

Dict = {}
with open(filename, "r") as file:
    for line in file:
        line = line.rstrip("\n")
        wordsList = line.split()
        for word in wordsList:
            word = word.lower()
            if word not in Dict:
                Dict[word] = 1
            else:
                Dict[word] = Dict[word]+1

Dict_sorted = sorted(Dict)
for x in Dict_sorted:
    print("{:<15}{}\n".format(x, Dict[x]))
