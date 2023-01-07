import random
def guessing_game():
    random_integer = random.randint(0, 100)
    while guess := int(input("Please enter a number between 0 and 100: ")):
        if guess == random_integer:
            print(f"You guessed it right {random_integer}")
            break
        if guess < random_integer:
            print(f"{guess} is low")
        else:
            print(f"{guess} is high")

guessing_game()