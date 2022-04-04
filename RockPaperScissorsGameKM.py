# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 17:46:24 2022

@author: Krister Martinez

"""

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
    
    
    
    
    
    
    