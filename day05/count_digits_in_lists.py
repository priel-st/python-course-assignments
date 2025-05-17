numbers = [1203, 1256, 312456, 98]
joined = "".join(map(str,numbers))
L = []
for digit in joined:
    if digit not in L:
        L.append(digit)
L.sort()
for x in L:
    num = joined.count(x)
    print("{:<2}{}".format(x, num))
