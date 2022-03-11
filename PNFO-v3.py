#!/usr/bin/env python3
'''
Program Name: Prime Number Figure-Outer
Author:       Richard Herndon
Date:         11/17/2020
Version:      3
Description:  This program will figure out if a number is prime, display
              its factors, and ask if the user wants to do another.
'''
###########
# IMPORTS #
###########
from time import sleep

#############
# FUNCTIONS #
#############
def main():
    intro()
    again = True
    while ( again == True ):
        num = get_input()
        result, factors = calculate( num )
        answer( num, result, factors )
        again = ask_for_another()
    outro()
    sleep( 3 )

# Introduce the program to the user.
def intro():
    print( '\nPRIME NUMBER FIGURE-OUTER' )
    print( '-------------------------' )
    print( '\nThis program will determine' )
    print( 'whether or not a number is' )
    print( 'a prime number.' )

# Get a number from the user.
def get_input():
    return int( input( '\nEnter number you want to check: ' ) )

# Figure out if the number is prime and what it's factors are.
def calculate( num ):
    # Assumes that num is prime until it figures out it isn't.
    prime = True
    # List for keeping track of factors (beside 1 and num).
    factors = []
    # Try every number between 2 and num to check if num is prime or not.
    for i in range( 2, num ):
        # If i is a factor, add it to the list and set prime to False.
        if ( num % i == 0 ):
            prime = False
            factors.append( i )
    # If num is prime...
    if prime:
        return 'PRIME', factors
    # Else...
    return 'NOT PRIME', factors

# Print result.
def answer( num, result, factors ):
    print( 'The number', num, 'is', result )
    print( 'The factors are: 1, ', end = '' )
    # If num isn't prime, print the factors from the list.
    if ( result == 'NOT PRIME' ):    
        for n in factors:
            print( n, ', ', sep = '', end = '' )
    print( num, '\n' )

# Ask the user if they want to try another number.
def ask_for_another():
    ask = True
    while ( ask == True ):
        response = input( 'Do you want to try another number? (y/n): ' )
        if ( response.lower() != 'y' and response.lower() != 'n' ):
            print( 'INVALID ENTRY' )
        else:
            ask = False
    # Returns a boolean value depending on the result of this expression
    # (If response is NOT 'y', it will return False).
    return ( response.lower() == 'y' )

# Print outro.
def outro():
    print( '\n\nTHANK YOU FOR USING PRIME NUMBER FIGURE-OUTER!' )
    

########################
# BEGINNING OF PROGRAM #
########################
main()
