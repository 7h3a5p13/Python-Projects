#!/usr/bin/env python3
'''
Program Name: Prime Number Figure-Outer
Author:       Richard Herndon
Date:         11/07/2020
Version:      2
Description:  This program will figure out if a given number is prime and asks
              if the user wants to do another.
'''
###########
# IMPORTS #
###########
from time import sleep
from math import sqrt , ceil

#############
# FUNCTIONS #
#############
def main():
    intro()
    again = True
    while ( again == True ):
        num = get_input()
        result = calculate( num )
        answer( num, result )
        again = ask_for_another()
    outro()
    sleep( 3 )

def intro():
    print( '\nPRIME NUMBER FIGURE-OUTER' )
    print( '-------------------------' )
    print( '\nThis program will determine' )
    print( 'whether or not a number is' )
    print( 'a prime number.' )

def get_input():
    return int( input( '\nEnter number you want to check: ' ) )

def calculate( num ):
    cap = ceil( sqrt( num ) )
    for i in range( 2, cap ):
        if ( num % i == 0 ):
            return 'NOT PRIME'
    return 'PRIME'

def answer( num, result ):
    print( 'The number', num, 'is', result, '\n' )

def ask_for_another():
    get_input = True
    while ( get_input == True ):
        response = input( 'Do you want to try another number? (y/n): ' )
        if ( response.lower() != 'y' and response.lower() != 'n' ):
            print( 'INVALID ENTRY' )
        else:
            get_input = False
    return ( response.lower() == 'y' )

def outro():
    print( '\n\nTHANK YOU FOR USING PRIME NUMBER FIGURE-OUTER!' )
    

########################
# BEGINNING OF PROGRAM #
########################
main()
