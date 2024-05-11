import random


def number_guessing_game():

    point = 20
    attempt = 4
    guessed_number = None
    random_integer = random.randint(1, 10)
    clue = ["number is odd", "number is even", "number is a multiple of 3",
            "number is between 5 and 10"]

    while True:

        # Generates a random integer between 1 and 10
        random_integer = random.randint(1, 10)

        #  Accepts integer input and stores value in variable
        guessed_number = int(input("Guess a number between 1 & 10: "))

        #   increment point and attempt by 5 and 1 if condition is true
        if guessed_number == random_integer:
            print("Correct guess!")
            point = point + 5
            attempt += 1
            print(f"Attempts left: {attempt}, Current score: {point}")
            print()

        #   decrement point and attempt by 5 and 1 if condition is true
        elif guessed_number != random_integer:
            print("Incorrect guess!")
            point = point - 5
            attempt -= 1
            print(f"Attempts left: {attempt}, Current score: {point}")

            #  Gives clues from a list depending on the random integer
            #  generated
            if random_integer % 2 == 1:
                print(clue[0])
            elif random_integer % 2 == 0:
                print(clue[1])
            elif random_integer // 3 == 3:
                print(clue[2])
            elif random_integer > 4:
                print(clue[3])

            print()

#  Exits and break out of the loop if condition is true

        if attempt == 0:
            print("Game Over")
            break


number_guessing_game()
