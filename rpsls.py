''' Determine rock, paper, scissors, lizard, Spock winner between player and computer'''

import random

def name_to_number(name):
    ''' convert name to integer'''
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Name not valid"
        
       
def number_to_name(number):
    '''convert integer to name'''
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"               
    elif number == 3:
        return "lizard"   
    elif number == 4:
        return "scissors"
    else:
        return "Number not valid"
    

def rpsls(players_choice):
    '''determine winner of rpsls game'''
    player_number = name_to_number(players_choice)
    comp_number =random.randint(0,4)
    comp_choice = number_to_name(comp_number)
    
    print("Player chooses",players_choice)
    print("Compluter chooses", comp_choice)
    
    if (player_number-comp_number)%5 == 1 or (player_number-comp_number)%5 == 2:
        print("Player wins!")
    elif (player_number-comp_number)%5 == 3 or (player_number-comp_number)%5 == 4:
        print("Computer wins!")
    else:
        print("Player and computer tie!")
    print()
    
# Calling rpsls with Player's Choice:    
rpsls("Spock")
rpsls("rock")
rpsls("lizard")
rpsls("paper")
rpsls("scissors")
