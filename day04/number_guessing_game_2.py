import random
x = random.randrange(1, 21)
guess = input("Guess the randomly chosen number between 1 and 20: ")
while (guess)!= "x":
    if int(guess)>x:
        guess = input("Your number is bigger than the chosen number, try again: ")
    elif int(guess)<x:
        guess = input("Your number is smaller than the chosen number, try again: ")
    elif int(guess) == x:
        print("Your guess is correct")
        break
