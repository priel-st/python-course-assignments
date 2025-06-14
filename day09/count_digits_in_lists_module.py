import dig_count

def main(numbers):
    joined = join_numbers(numbers)
    L = digit_list(joined)
    count_dig(L, joined)
    return None

nums = [1203, 1256, 312456, 98]
if __name__ == "__main__":
    main(nums)
