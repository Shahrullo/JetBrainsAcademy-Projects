import random

print('H A N G M A N')

list_words = ['python', 'java', 'kotlin', 'javascript']
choice = random.choice(list_words)
attempt = 8
start = ['-'] * len(choice)
guessed_letter = []

while True:

    menu = ''
    while menu not in ['play', 'exit']:
        menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == 'exit':
        break

    while attempt > 0:
        print()

        print(''.join(start))

        x = input('Input a letter: ')

        if len(x) != 1:
            print('You should input a single letter')
            continue

        if not (x.islower()):
            print('Please enter a lowercase English letter')
            continue

        if x in guessed_letter or x in start:
            print('You\'ve already guessed this letter')
            continue

        guessed_letter.append(x)

        if x in choice:
            for i in range(len(choice)):
                if choice[i] == x:
                    start[i] = x
            if ''.join(start) == choice:
                print('You guessed the word!\nYou survived!')
                break
        else:
            print('That letter doesn\'t appear in the word')
            attempt -= 1

    if attempt == 0:
        print('You lost!')

