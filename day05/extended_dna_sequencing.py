seq = input("Please type in a sequence: ")
seq_2 = ""
for ch in seq:
    if ch in ["A", "C", "T", "G"]:
        seq_2 = seq_2 + ch
    else:
        seq_2 = seq_2 + "X"
seq_3 = seq_2.split("X")
while "" in seq_3:
    seq_3.remove("")
seq_3.sort(key = len, reverse = True)
print(seq_3)
