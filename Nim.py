"""
TODO: Write a description here
"""

import random
def main():
    STONES = 20
    TURN = True
    while STONES > 0:
        print(f'There are {STONES} stones left')
        if TURN == True:
            answer = int(input("Player 1 would you like to remove 1 or 2 stones? "))
            while answer != 1 and answer != 2:
                answer=int(input("Please enter 1 or 2: "))
            STONES -= answer
            TURN = False
        else:
            answer = int(input("Player 2 would you like to remove 1 or 2 stones? "))
            while answer != 1 and answer != 2:
                answer=int(input("Please enter 1 or 2: "))
            TURN = True
            STONES -= answer
        print(f'')
    if TURN:
        print(f'Player 1 wins!')
    else:
        print(f'Player 2 wins!')

if __name__ == '__main__':
    main()