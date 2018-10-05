from random import randint
# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

#list that pairs names with numbers. 
#used to convert between names and numbers
options = ["Rock","Spock","Paper","Lizard","Scissors"]

#dictionaries to determine wins/losses
#example: dictionary of values paired next to key "2" in dict "win" indicates who 2 wins against
wins = {0:[3,4],1:[4,0],2:[0,1],3:[1,3],4:[2,3]}


#converts number to name
def name_to_number(name):
    return options.index(name.capitalize())

#converts name to number
def number_to_name(number):
    return options[number]

#main program
def rpsls(player_choice):
    
    #gets cpu and player numerical choices
    player_choice = name_to_number(player_choice)
    cpu_choice = randint(0,4)
    
    #prints choices
    print("\nPlayer chooses " + number_to_name(player_choice))
    print("Computer chooses " + number_to_name(cpu_choice))
    
    #game logic
    #1. check if tie, 2. check if cpu choice in wins
    #if both fail, loss
    if player_choice == cpu_choice:
        print("Player and Computer Tie!")
    elif cpu_choice in wins[player_choice]:
        print("Player Wins!")
    else:
        print("Computer Wins!")

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric



