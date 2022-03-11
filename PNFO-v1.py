#!/usr/bin/env python3
'''
Program Name: Prime Number Figure-Outer
Author:       Richard Herndon
Date:         11/05/2020
Version:      1
Description:  This program will figure out if a number is prime.
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
    num = get_input()
    result = calculate( num )
    answer( num, result )
    sleep( 5 )

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
    print( '\nThe number', num, 'is', result, '\n' )

########################
# BEGINNING OF PROGRAM #
########################
main()
