import seq_list

def main():
    sequence = seq_list.user_seq()
    letter_clean = seq_list.letter_cleaning(sequence)
    clean_list = seq_list.clean_seq_list(letter_clean)
    sorted_list = seq_list.sorted_clean_seq(clean_list)
    print(sorted_list)
    
if __name__ == "__main__":
    main()
