import random
x = random.randrange(1, 21)
debug_mode = False
move_mode = False
while True:
    if move_mode:
        x = x + random.randrange(-2, 3)
    if debug_mode:
        print(f"The correct guess is {x}")
    guess = input("Guess the randomly chosen number between 1 and 20: ")
    if guess == "s":
        print(f"The chosen number is {x}")
        break
    elif guess == "d":
        debug_mode = not debug_mode
        continue
    if guess == "x":
        break
    if guess == "m":
        move_mode = not move_mode
    else:
        if int(guess)>x:
            print("Your number is too big, try again.")
            continue
        elif int(guess)<x:
            print("Your number is too small, try again.")
            continue
        elif int(guess) == x:
            print("Your guess is correct")
            break
