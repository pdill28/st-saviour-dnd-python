import random
import time
import sys

from draw import draw_d20, draw_d6, draw_d4

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def check_player_alive(lives: int) -> None:
    if lives <= 0:
        print_dramatic_text('You died!')
        sys.exit()

if __name__ == '__main__':
    # create character by collecting user input (name + class)
    # print character sheet
    # specify roll that must be beat and enemy initiative by collecting user input
    # any buffs / debuffs?
    # any critical success / failure?

    print_dramatic_text('Welcome to my trivia game!')

    #  the player starts with three lives and loses one for each wrong answer
    lives = 3
    answer = input('Who was the first to go  missing? ')
    if answer == 'Will':
        print_dramatic_text('correct')
    else:
        print_dramatic_text('Incorrect')
        lives -= 1
        check_player_alive(lives)
    #  you will lose a life when wrong 
    answer = input('What the game the boys play in stranger things? ')
    if answer == 'Dnd':
        print_dramatic_text('correct')
    else:
        print_dramatic_text('Incorrect')
        lives -= 1
        check_player_alive(lives)
    answer = input('Who dose Mille Bobby Brown play in stranger things? ')
    if answer == 'Eleven' or answer == '11':
        print_dramatic_text('correct')
    else:
        print_dramatic_text('Incorrect')
        lives -= 1
        check_player_alive(lives)

    # here are all the random qustions 
    questions = [
        'who created stanger things',
        'when did max die',
        'dose 11 lose her power'
    ] 
                 
    answers = [
        'the duffer brother',
        'sesason 4',
        'yes'
    ]

    r = random.randint(0, 2)
    answer = input(questions[r] + ' ')
    if answer.lower() == answers[r]:
        print_dramatic_text('correct!')
    else:
        print_dramatic_text('incorrect')
        lives -= 1
        check_player_alive(lives)

    print_dramatic_text('you have won my game congrats')