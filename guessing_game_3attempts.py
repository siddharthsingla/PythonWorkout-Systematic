import random
def guessing_game():
    remaining_guesses = 2
    random_integer = random.randint(0, 100)
    while remaining_guesses >= 0:
        remaining_guesses -= 1
        guess = int(input("Enter an integer between 0 and 100: "))
        if guess == random_integer:
            print(f"You guessed it right {random_integer}")
            break
        if guess < random_integer:
            print(f"{guess} is low")
        else:
            print(f"{guess} is high")
    #else associated with while loop
    else:
        print("your 3 chances are up!")

guessing_game()