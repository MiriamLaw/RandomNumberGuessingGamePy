import random

def main():
    min_number = 1
    max_number = 100
    random_number = random.randint(min_number, max_number)

    guesses = 0

    while guesses < 5:
        try:
            guess = int(input(f"Pick a number between {min_number} and {max_number}: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess < min_number or guess > max_number:
            print(f"Your guess is not between {min_number} and {max_number}, please try again.")
            continue
        elif guess == random_number:
            print("You win!")
            return
        else:
            if guess < random_number:
                print("Please pick a higher number.")
            else:
                print("Please pick a lower number.")
            guesses += 1

    print(f"You lose. The number to guess was: {random_number}")

if __name__ == "__main__":
    main()
