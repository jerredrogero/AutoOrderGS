# Guess the Number Game
import random

print('Hello! What is your name?')
name = input()

print('Well,' + name + ' I am thinking of a number between 1 and 20')
secretNumber = random.randint (1,20)

# print ('Debug: Secret number is ' + str(secretNumber))

for guessesTaken in range (1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Nice try, but thats too low.')
    elif guess > secretNumber:
        print('Nice try, but thats too high.')
    else:
        break # This condition is for the correct guess

if guess == secretNumber:
    print('You Win, ' + name + '! it only took you ' + str(guessesTaken) + ' guesses...')
else:
    print('Oof the number was ' + str(secretNumber))
