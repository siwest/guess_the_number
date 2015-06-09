#!/usr/bin/env python3
# Guess the number game - player vs. cpu
import random


def get_user_choice(string):
    """Ask user for input, and validate values are legit
    mesg - Sentence to display to user
    validation_funct - function to use to validate input is good
    return - validate input
    """

    user_input = raw_input(string)

    valid = is_valid_choice(user_input)
    if (valid):
        user_input = int(user_input)
        return user_input
    else:
        get_user_choice(string)
        pass

def is_valid_choice(user_data):
    """Check to see if given data is valid
    user_data - data is check against
    return - True if valid False if not valid

    >>> is_valid_number('525600')
    True
    >>> is_valid_number('dog')
    False
    """
    contains_digits = False
    for char in list(user_data):
    	if char.isdigit():
    		contains_digits = True
    		break
    if (contains_digits == True):
    	return True
    else:
    	return False

def calculate_winner(input1, input2):
    """Compare input from 2 sources and return True if equal False if not

    >>> calculate_winner(1,1)
    True
    >>> calculate_winner(1,2)
    False
    """
    if input1 == input2:
        return True
    else:
        return False

if __name__ == "__main__":
    #   My code goes here
    player_string = 'Pick a number between 1-10: '
    player_choice = get_user_choice(player_string)
    cpu_choice = random.randint(1,10)
    print("Cpu choice is " + str(cpu_choice))
    winner = calculate_winner(player_choice, cpu_choice)

    if winner:
        print('You win!');
    else:
        print('You lose :-( ');
