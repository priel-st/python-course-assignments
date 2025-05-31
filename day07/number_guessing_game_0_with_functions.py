import random

def generate_random_num():
    return random.randrange(1,21)

def user_guess():
    guess = input("Guess the randomly chosen number between 1 and 20: ")
    return int(guess)

def compare_guess_to_random(guess, rand):
    if guess == rand:
        print("Your guess is correct")
    else:
        if guess > rand:
            print("Your number is bigger than the chosen number")
        else:
            print("Your number is smaller than the chosen number")
def main():
    random_num = generate_random_num()
    input_guess = user_guess()
    compare_guess_to_random(input_guess, random_num)
    
if __name__ == "__main__":
    main()
