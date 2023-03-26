import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}:"))
        print(guess)
        if guess < random_number:
            print('sorry, too low, guess again.')
        elif guess > random_number:
            print('sorry, too high, guess again.')
    
    print(f'Congrats! You have guessed the number {random_number} correctly!')
            
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low(L) or correct(C)?').lower()
        if feedback == 'h':
            high = guess -1
        if feedback == 'l':
            low = guess +1
    print(f'Congrats! The computer guessed the number {guess} correctly!')


print('If you want to guess a number against computer press 1, \
\nIf you want to think a number to computer guess press 2.')

start = int(input('Please insert 1 or 2:'))
if start == 1:
    x = int(input('Whats the limit of game (10, 100, 1000...)? '))
    guess(x)

if start == 2:
    x = int(input('Whats the limit of game (10, 100, 1000...)? '))
    computer_guess(x)

