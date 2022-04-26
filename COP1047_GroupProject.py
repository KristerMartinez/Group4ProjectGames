# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 21:23:04 2022

@author: iambi
"""

def menu():
    print("[1] Paper Rock Scissors")
    print("[2] Tic Tac Toe")
    print("[0] Exit the program.")
    
#Or if you don't put the game code below, put it here with def option():   
    
menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        #do option 1 stuff
        print("Paper Rock Scissors Game")
        # imports
        import random
        import math

        def game_on():
            player = input("Please enter your move: 'r' for rock, 'p' for paper, 's' for scissors\n")
            player = player.lower()
            
            comp = random.choice(['r', 'p', 's'])
            
            if player == comp:
                return (0, player, comp)
            
            if winner(player, comp):
                return (1, player, comp)
            
            return (-1, player, comp)

        def winner(human_player, comp_player):
            if (human_player == 'r' and comp_player == 's') or (human_player == 's' and comp_player ==  'p') or (human_player == 'p' and comp_player == 'r'):
                return True
            return False


        def most_wins_of(w):
            human_player_wins = 0
            comp_player_wins = 0
            wins_needed = math.ceil(w/2)
            while human_player_wins < wins_needed and comp_player_wins <wins_needed:
                score, player, comp = game_on()
                
                if score == 0:
                    print("You and the computer have tied the game.  We both choose {}. \n".format(player))
                    
                elif score == 1:
                    human_player_wins += 1
                    print("You beat me! you picked {} and the computer picked {}\n".format(player, comp))
                    
                else:
                    comp_player_wins += 1
                    print("You lost, HA! You picked {} and the computer picked {}\n".format(player, comp))
                    
            if human_player_wins > comp_player_wins:
                print("You have won {} games! Give me another chance to beat you!".format(w))
                
            else:
                print("I finally Conquered you! You have lost {} games,  Sorry but not sorry".format(w))
                
                
        if __name__=='__main__':
            most_wins_of(3)
        # This is where I will have to put the code for game 1.
    elif option == 2:
        #do option 2 stuff
        print("Tic Tac Toe Game")
        board = [

            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]

            ]

        # true x otherwise o
        player = True 
        turns = 0

        def show_board(board):
            for row in board:
                for slot in row:
                    print(f"{slot} ", end="")
                print()

        show_board(board)

        def end_game(player_input):
            if player_input == "q":
                print("I hope you had a blast playing Tic-Tac-Toe.  See you soon.")
                return True
            else:
                return False  

        def check_player_input(player_input):
            if not isitanumber(player_input):
                return False
            player_input = int(player_input)
            if not bounds(player_input):
                return False
            return True    

        def isitanumber(player_input):
            if not player_input.isnumeric():
                print("This is not a numeric number")
                return False
            else: return True

        def bounds(player_input):
            if player_input >9 or player_input < 1:
                print("This number is out of bounds")
                return False
            else:
                return True

        def istaken(coords, board):
            row = coords[0]
            col = coords[1]
            if board[row] [col] != "-":
                print("This position is already taken")
                return True
            else:
                return False

        def coordinates(player_input):
            row = int(player_input / 3)
            col = player_input
            if col > 2: col = int(col % 3)
            return (row, col)    

        def add_to_board(coords, board, active_player):
            row = coords[0]
            col = coords[1]
            board[row][col] = active_player

        def current_player(player):
            if player: 
                return "x"
            else:
                return "o"

        def iswin(player, board):
            if check_row(player, board):
                return True
            if check_col(player, board):
                return True 
            if check_diag(player, board):
                return True
            return False

        def check_row(player, board):
            for row in board:
                complete_row = True
                for slot in row:
                    if slot != player:
                        complete_row = False
                        break
                if complete_row:
                    return True
            return False

        def check_col(player, board):
            for col in range(3):
                complete_col = True
                for row in range(3):
                    if board[row][col] != player:
                        complete_col = False
                        break
                if complete_col:
                    return True
            return False

        def check_diag(player, board):
            if board[0][0] == player and board[1][1] == player and board[2][2] == player:
                return True
            elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
                return True
            else:
                return False

        while turns < 9:
            active_player = current_player(player)
            show_board(board)
            player_input = input("Plese enter a position 1 through 9 or enter \"q\" to quit: ")
            if end_game(player_input):
                break
            if not check_player_input(player_input):
                print("Please try once more")
                continue
            player_input = int(player_input) - 1
            coords = coordinates(player_input)
            if istaken(coords, board):
                print("Please try again.")
                continue
            add_to_board(coords, board, active_player)
            if iswin(active_player, board):
                print(f"{active_player.upper()} won!!")
                break

            turns += 1
            if turns == 9:
                print("Tie !!")
            player = not player    

    else:
        print("Invalid option.")     
    print()
    menu()
    option = int(input("Enter your option: "))

print("Thanks for using this program. Good Bye.")