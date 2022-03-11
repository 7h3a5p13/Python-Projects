#!/usr/bin/env python3
'''
Program: Rocket Ship
Version: 1.0
Author:  Richard Herndon
Date:    08/03/2020
Purpose: Print a cool ASCII rocket to the console
'''

#################
### CONSTANTS ###
#################

# Used to adjust the size of the rocket
SIZE = 3


#################
### FUNCTIONS ###
#################

# Control program execution
def main():
    print_rocket()



# Control the printing of the rocket
def print_rocket():
    print_nose_cone()
    print_body()
    print_nozzle()



# Control the printing of the nose cone
def print_nose_cone():

    # Control the number of lines in the nose cone
    for line in range( 1, ( SIZE * 2 ) ):

        # Print spaces
        for i in range( 1, ( -1 * line + ( SIZE * 2 + 1 ) ) ):
            print( " ", end = '' )

        # Print forward slashes
        for j in range( 0, line ):
            print( "/",  end = '' )

        # Print asterisks
        print( "**", end = '' )

        # Print back slashes
        for k in range( 0, line ):
            print( "\\", end = '' )

        # Print new line
        print()



# Control the printing of the rocket body
def print_body():
    print_seal()
    print_diamond_top()
    print_diamond_bottom()
    print_seal()
    print_diamond_bottom()
    print_diamond_top()
    print_seal()



# Control the printing of seals
def print_seal():
    print( "+", end = '' )
    for i in range( 0, ( SIZE * 2 ) ):
        print( "=*", end = '' )
    print( "+" )



# Control the printing of diamond tops
def print_diamond_top():

    # Control the number of lines in the rocket body
    for line in range( 1, ( SIZE + 1 ) ):

        # Print left "pipe" symbol
        print( "|", end = '' )

        # Print left dots
        for i in range( 0, ( -1 * line + SIZE ) ):
            print( ".", end = '' )

        # Print left "points"
        for i in range( 0, line ):
            print( "/\\", end = '' )
            
        # Print middle dots
        for i in range( 0, -2 * line + ( SIZE * 2 ) ):
            print( ".", end = '' )

        # Print right "points"
        for i in range( 0, line ):
            print( "/\\", end = '' )

        # Print right dots
        for i in range( 0, ( -1 * line + SIZE ) ):
            print( ".", end = '' )

        # Print right "pipe" symbol
        print( "|" )



# Control the printing of diamond bottoms
def print_diamond_bottom():

    # Control the number of lines
    for line in range( 1, ( SIZE + 1 ) ):

        # Print left "pipe" symbol
        print( "|", end = '' )

        # Print left dots
        for i in range( 0, ( 1 * line -1 ) ):
            print( ".", end = '' )

        # Print left "points"
        for i in range( 0, ( -1 * line + ( SIZE + 1 ) ) ):
            print( "\\/", end = '' )

        # Print the middle dots
        for i in range( 0, ( 2 * line - 2 ) ):
            print( ".", end = '' )

        # Print right "points"
        for i in range( 0, ( -1 * line + ( SIZE + 1 ) ) ):
            print( "\\/", end = '' )

        # Print right dots
        for i in range( 0, ( 1 * line -1 ) ):
            print( ".", end = '' )

        # Print right "pipe" symbol
        print( "|" )



# Control the printing of the nozzle
def print_nozzle():
    print_nose_cone()



### START PROGRAM ###
main()
