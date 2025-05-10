import random
x = random.randrange(1, 21)
guess = input("Guess the randomly chosen number between 1 and 20: ")
if int(guess)==x:
  print("Your guess is correct")
else:
  if int(guess)>x:
    print("Your number is bigger than the chosen number")
  else:
    print("Your number is smaller than the chosen number")
