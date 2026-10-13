from secret_number import secretNum

MAX_ATTEMPTS = 5
attempts = 0

while True:
    user_guess = int(input("Enter your guess: "))
    attempts += 1

    if user_guess < secretNum:
        print("Your guess is too low.")
    elif user_guess > secretNum:
        print("Your guess is too high.")
    else:
        print("Congratulations! You guessed the secret number.")
        break

    if attempts >= MAX_ATTEMPTS:
        print("Maximum number of attempts reached.")
        # Part 4: Infinite loop upon exceeding 5 attempts
        while True:
            print("Oh! Noooooo...")
