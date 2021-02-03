# Write your code here
import random

while True:
    player = input()

    choices = ['scissors', 'rock', 'paper']

    computer = random.choice(choices)

    conditions = {'scissors': 'rock', 'paper': 'scissors', 'rock': 'paper'}

    if player == '!exit':
        print('Bye!')
        break

    elif player not in choices:
        print('Invalid input')
        continue

    else:
        if conditions[player] == computer:
            print(f'Sorry, but the computer chose {computer}')

        elif player == computer:
            print(f'There is a draw {(player)}')
        else:
            print(f'Well done. The computer chose {computer} and failed')

