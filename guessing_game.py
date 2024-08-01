print("Guessing Game")

numbers = [0, 1, 2, 3, 4, 5]
secret_number = 3

while True:
    try:
        guess = int(input("Enter a number from 0 to 5: "))

        if guess == secret_number:
            print("Congratulations!👏 You guessed it!🎉")
            break
        elif guess in numbers:
            if guess in [0, 1, 5]:
                print("Not even close! Keep trying!")
            elif guess in [2, 4]:
                print("⚠ Close! Try again!")
        else:
            print("Number out of allowed range. Try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")