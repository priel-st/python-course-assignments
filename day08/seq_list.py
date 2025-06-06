def user_seq():
    seq = input("Please type in a sequence: ")
    return seq

def letter_cleaning(seq):
    seq_2 = ""
    for ch in seq:
        if ch in ["A", "C", "T", "G"]:
            seq_2 = seq_2 + ch
        else:
            seq_2 = seq_2 + "X"
    return seq_2

def clean_seq_list(seq_2):
    seq_3 = seq_2.split("X")
    while "" in seq_3:
        seq_3.remove("")
    return seq_3

def sorted_clean_seq(seq_3):
    seq_3.sort(key = len, reverse = True)
    return(seq_3)
