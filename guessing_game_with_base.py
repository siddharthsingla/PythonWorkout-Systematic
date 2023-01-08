import random
def guessing_game():
    random_integer = random.randint(0, 100)
    required_base = random.choice([2, 8, 10, 16])
    while True:
        try:
            guess = int(input("Please enter a number between 0 and 100: "), required_base)
            if guess == random_integer:
                print(f"You guessed it right {random_integer}")
                break
            if guess < random_integer:
                print(f"{guess} is low")
            else:
                print(f"{guess} is high")
        except ValueError:
            print(f"number not valid for base {required_base}")

guessing_game()