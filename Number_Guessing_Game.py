import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range<= 0:
        print("Enter a Number Greater Than 0 Next Time.")
        quit()
else:
    print("Enter a Digit Next Time i.e Greater Than Zero")
    quit()

random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make A Guess :")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Enter a Number Next Time")
        continue

    if user_guess == random_number:
        print("You Got It! hurray")
        break
    elif user_guess > random_number:
        print("You Guessed a Higher Number")
    else:
        print("You Guessed a Lower Number")

print("You Got it in",guesses, "guesses")