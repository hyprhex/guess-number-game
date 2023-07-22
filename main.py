# Import random libraries
import random

print("4 chance to get the number right")

# Generate Random number between 1 and 100.
generatedNumber = random.randint(1, 100)

i = 0
while i < 4 :

    # User enter guess number
    userGuessNumber = int(input("Enter your guess number: "))
    # Check if the user guess number is right or low or high
    if generatedNumber == userGuessNumber:
        print('You win!!')
        stopPlaying = input("want to stop (y/n): ")
        if stopPlaying == 'y':
            break
        else:
            continue
    elif generatedNumber > userGuessNumber:
        print('Your guess is too low')
    elif generatedNumber < userGuessNumber:
        print('Your guess is too high')
    
    i += 1
    

