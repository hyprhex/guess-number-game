# Import random libraries
import random


# Generate Random number between 1 and 100.
generatedNumber = random.randint(1, 100)

while True:

    # User enter guess number
    userGuessNumber = int(input("Enter your guess number: "))
    # Check if the user guess number is right or low or high
    if generatedNumber == userGuessNumber:
        print('You win!!')
        stopPlaying = input("want to stop (y/n): ")
        if stopPlaying == 'y':
            break
        else:
            generatedNumber = random.randint(1, 100)
            continue
    elif generatedNumber > userGuessNumber:
        print('Your guess is too low')
    elif generatedNumber < userGuessNumber:
        print('Your guess is too high')
    

