# CaineCode
# Sept 2020

''' 
Tic-Tac_toe Game. 
Play against the computer or 2 player. 
Play as many games as you like. 
'''

from time import sleep
from sys import stdout, exit
import random


# Global variables
game_over = "X0X0X0X Game over! X0X0X0X0X\n"

def main():

    board_plays = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    winner = False
    whose_turn = 'X' # X goes first
    turn_num = 1
    player_win = ""
    continue_playing = False
    score = [0,0] # player 1,player 2
    game_num = 1


    players = startup()
    (p1, p2, AI_bool) = players

    # Moves
    while winner == False and turn_num <= 9:
        if whose_turn == 'X':
            go = p1
        else:
            go = p2

        if score[0] + score[0] != 0:
            print(f"Current score:\n{p1} {score[0]} - {score[1]} {p2}\n")

        empty = [k for k, v in board_plays.items() if v == " "]
        print(f"\nX0X0X0X0   GAME {game_num}   X0X0X0X0")
        print(f"X0X0X0X0   Move {turn_num}   X0X0X0X0\n")
        if AI_bool == True:
            if whose_turn == 'X':
                ptr = input(f"{go}, pick a square from \n{str(empty)}\nChoice: ")
                ptr = int(ptr)
                # Validate move
                if ptr not in board_plays.keys():
                    ptr = input(f"Invalid square! Pick another: ")
                    ptr = int(ptr)
                for k in board_plays.keys():
                    if k == ptr:
                        if board_plays[k] != ' ':
                            ptr = input(f"That one is taken! Pick another: ")
                            ptr = int(ptr)
                        else:
                            board_plays[k] = whose_turn
            if whose_turn == '0':
                fred = "Freddie is thinking...\n"
                sleep(1)
                loading(fred)
                AI(empty, AI_bool, whose_turn, board_plays)
        if AI_bool == False:
            ptr = input(f"{go}, pick a square # from \n{str(empty)}\nChoice: ")
            ptr = int(ptr)
            # Validate move
            if ptr not in board_plays.keys():
                ptr = input(f"Invalid square! Pick another: ")
                ptr = int(ptr)
            for k in board_plays.keys():
                if k == ptr:
                    if board_plays[k] != ' ':
                        ptr = input(f"That one is taken! Pick another: ")
                        ptr = int(ptr)
                    else:
                        board_plays[k] = whose_turn

        turn_num += 1
        if whose_turn == 'X':
            whose_turn = '0'
        else:
            whose_turn = 'X'

        #Print UI board_plays
        print()
        print(f"   {board_plays[1]}   {board_plays[2]}   {board_plays[3]}")
        print()
        print(f"   {board_plays[4]}   {board_plays[5]}   {board_plays[6]}")
        print()
        print(f"   {board_plays[7]}   {board_plays[8]}   {board_plays[9]}")
        print()
        result = check(board_plays, winner, player_win, p1, p2, score)
        (winner, player_win, score) = result
        # Print winner if True
        if winner == True:
            loading(game_over)
            print(f"{player_win} is the winner!")
            print(f"\nCurrent score:\n{p1} {score[0]} - {score[1]} {p2}")
            continue_playing_tuple = continue_playing_function(continue_playing, score, p1, p2, whose_turn, turn_num, board_plays, game_num)
            (score, continue_playing, whose_turn, turn_num, board_plays, game_num) = continue_playing_tuple
            winner = False

    loading(game_over)
    print("Game over! It was a draw.")
    continue_playing_tuple = continue_playing_function(continue_playing, score, p1, p2, whose_turn, turn_num, board_plays, game_num)
    (score, continue_playing, whose_turn, turn_num, board_plays, game_num) = continue_playing_tuple
    winner = False


# Functions:

l = "X0X0X0X0X0X0X0X0X0X0X0X0X0X0\n"

def loading(string=l, sleep_time=0.1):
    '''Loading graphics'''
    for i in string:
        stdout.write(i)
        stdout.flush()
        sleep(sleep_time)

def one_or_two():
    '''Give player option to play against AI or with another player'''
    AI_bool = None
    while AI_bool == None:
        play_AI = input("Play against the computer?\n(y/n): ")
        if play_AI == 'y':
            AI_bool = True
        elif play_AI == 'n':
            AI_bool = False
        else:
            print("I don't understand")
    return AI_bool

def AI(empty, AI_bool, whose_turn, board_plays):
    '''AI moves'''
    if AI_bool == True:
        AI_choice = random.choice(empty)
        board_plays[AI_choice] = whose_turn
        print(f"Freddie's choice: {AI_choice}")
        empty.remove(AI_choice)
    return empty

def startup():
    """Startup function"""
    F = "          Freddie's       \n"
    w = "         Tic-tac-toe       \n"
    pm2 = "        1 or 2 player    \n"

    print()
    loading()
    loading(F)
    loading(w)
    loading()
    loading(pm2)
    print()
    sleep(2)

    AI_bool = one_or_two()

    # Ask for names of player 1 and player 2
    if AI_bool == False:
        p1 = input("Player X name: ")
        p2 = input("Playing 0 name: ")
        sleep(1)
        print(f"\nHi, {p1} and {p2}.")
        loading()

    else:
        p2 = "Freddie"
        p1 = input("What's your name? ")
        print(f"\nHi {p1}, you are playing against AI {p2}.")

    sleep(1)

    r = "\nX0X0X0X0    RULES   X0X0X0X0\n"
    loading(r)

    # Rules of the game_num
    #ru = "\n1. The board has 3x3 squares.\n\n2. Taking turns, the winner is \nthe first to get 3 in a horizontal, \nvertical or diagonal row.\n\n3. When prompted, input the \nsquare # you want to play.\n"
    #loading(ru)
    print("1. The board has 3x3 squares.\n")
    sleep(2)
    print("2. Taking turns, the winner is \nthe first to get 3 in a horizontal, \nvertical or diagonal row.\n")
    sleep(2)
    print("3. When prompted, input the \nsquare # you want to play:")
    sleep(2)
    example_board = ((' 1 ', ' 2 ', ' 3 '), (' 4 ', ' 5 ', ' 6 '), (' 7 ', ' 8 ', ' 9 '))
    for row in example_board:
        print(f"\n  {row[0]}  {row[1]}  {row[2]}")

    print()

    #loading(u)
    sleep(2)
    print(f"4. {p1} is playing as X\n5. {p2} is playing as 0\n\n6. {p1} has the first move\n")
    sleep(3)
    g = "X0XO  Lets get started! XOX0"
    loading(g, 0.2)
    print()
    sleep(2)

    players = (p1, p2, AI_bool)
    return players

def check(board_plays, winner, player_win, p1, p2, score):
    '''Checks if a player has got 3 in a row'''
    row_num = ((1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (7,5,3))
    for row in row_num:
        sq1 = board_plays[row[0]]
        sq2 = board_plays[row[1]]
        sq3 = board_plays[row[2]]
        row = (sq1, sq2, sq3)
        if row == ('X','X','X') or row == ('0', '0', '0'):
            winner = True
            if row == ('X','X','X'):
                player_win = p1
                score[0] += 1
            else:
                player_win = p2
                score[1] += 1
    result = (winner, player_win, score)
    return result

def continue_playing_function(continue_playing, score, p1, p2, whose_turn, turn_num, board_plays, game_num):
    '''Checks if players want to continue playing, if so keep score'''
    while continue_playing == False:
        keep_going = input("\nKeep playing? enter: y/n\nAnswer: ")
        keep_going = keep_going.lower()
        if keep_going == 'n':
            loading()
            print(f"\nFinal score:\n{p1} {score[0]} - {score[1]} {p2}")
            if score[0] > score[1]:
                print(f"{p1} is the winner!")
                loading(game_over)
            elif score[0] < score[1]:
                print(f"{p2} is the winner!")
                loading(game_over)
            else:
                print("Game over! It was a draw.")
                loading(game_over)
            print("\nThanks for playing Freddie's Tic-tac-toe.\nGoodbye.\n")
            exit()
        elif keep_going == 'y':
            game_num += 1
            continue_playing = True
            print()
        else:
            print("Sorry I don't understand.")
    continue_playing = False

    whose_turn = 'X' # X goes first
    turn_num = 1
    board_plays = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    continue_playing_tuple = (score, continue_playing, whose_turn, turn_num, board_plays, game_num)
    return continue_playing_tuple

main()


