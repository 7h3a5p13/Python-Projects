#!/usr/bin/env python3
'''
Program Name: Connect Four
Author:       Richard Herndon
Version:      1.0
Start Date:   09/02/2020
End Date:     09/12/2020
Description:  Home-made version of the popular game "Connect 4"

TO-DO: 1) Add input validation for code requiring integers
       2) Make board resizable by changing 1 variable
       3) Once done, remove hard-coded variables at the bottom
'''
###########
# IMPORTS #
###########
from time import sleep
from random import randint
import turtle

#############
# CONSTANTS #
#############
USAIN_BOLT = 0
SCREEN_SIZE_X = 950
SCREEN_SIZE_Y = 750
SCREEN_POSITION_X = 0
SCREEN_POSITION_Y = 0
BOARD_SIZE_X = 740
BOARD_SIZE_Y = 640
RADIUS = 50
DISTANCE_BETWEEN_CIRCLES = 105
CIRCLE_START_POINT_X = -315
CIRCLE_START_POINT_Y = -210
COL_LABEL_START_X = -355
COL_LABEL_START_Y = 330
NUM_COLS = 7
NUM_ROWS = 6


#############
# FUNCTIONS #
#############
def intro():
    print( '\n############################' )
    print( '# Welcome to Connect Four! #' )
    print( '############################\n' )

def decide_first_player():
    # Play the "Guess the Number" game until someone wins
    print( 'Pick a number between 1 and 10 to see who goes first' )
    keep_going = True
    while ( keep_going == True ):
        num = randint( 1, 10 )
        guesses = [ 0 ] * 2

        # Get the number and check its validity for both players
        # TO DO: Validate input is of type "int"!
        for i in range( 1, 3 ):
            print( 'Person #', i, ': ', sep = '', end = '' )
            guesses[ i - 1 ] = int( input() )
            while ( guesses[ i - 1 ] < 1 or guesses[ i - 1 ] > 10 ):
                print( '[ INVALID GUESS - Must be a number between 1 and 10 ]' )
                sleep( 1 )
                print( 'Person #', i, ': ', sep = '', end = '' )
                guesses[ i - 1 ] = int( input() )

        # Calculate whether or not there is a winner
        print( '\nThe number is', num, '\n' )
        if ( abs( guesses[ 0 ] - num ) < abs( guesses[ 1 ] - num ) ):
            print( '---Person #1 was closest!---' )
            keep_going = False
        elif ( abs( guesses[ 0 ] - num ) > abs( guesses[ 1 ] - num ) ):
            print( '---Person #2 was closest!---' )
            keep_going = False
        else:
            print( '---It\'s a tie! Try again---' )
        sleep(2)
        
def get_player_info():
    # Get's the player names and colors
    p1 = get_name( 'first' )
    c1, c2 = get_color()
    p2 = get_name( 'second' )
    print( '\nYour color is', c2 )
    return p1, c1, p2, c2
    
def get_name( player_order ):
    # Get player name
    print( '\nWho\'s going ', player_order, '?', sep = '' )
    return input( 'Enter name: ' )
    
def get_color():
    # Get player color
    print( '\nWhat color do you want?' )
    print( '1) Black' )
    print( '2) Red' )
    color = int( input( 'Enter choice: ' ) )

    # Check input validity
    # TO DO: Validate input is of type "int"!
    while ( color < 1 or color > 2 ):
        print('[ INVALID INPUT - Must be either "1" or "2" ]' )
        sleep( 1 )
        color = input( 'Enter choice: ' )
    if ( color == 1 ):
        print( '\nYou chose Black' )
        return 'BLACK', 'RED'
    else:
        print( '\nYou chose RED' )
        return 'RED', 'BLACK'

def play( player_1, color_1, player_2, color_2 ):
    # Set up the screen and board
    turtle.setup( SCREEN_SIZE_X, SCREEN_SIZE_Y,
                  SCREEN_POSITION_X, SCREEN_POSITION_Y )

    # Initializes control and counting variables
    play_again = 'yes'

    # Loop to control 
    while ( play_again.lower() == 'yes' or play_again.lower() == 'y' ):
        winner = False
        turn = 0
        draw_board()

        # Creates a two-dimensional list to keep track of colors and placement
        circle_grid = []
        for i in range( NUM_COLS ):
            col = []
            for j in range( NUM_ROWS ):
                col.append( 'EMPTY' )
            circle_grid.append( col )

        '''
            The above loop creates a 2D list that represents the following
            grid. Imagine it sort of like a mathmatical graph and that x
            and y are positive values:
                              
                                 Columns
                  |           
                (0,5) (1,5) (2,5) (3,5) (4,5) (5,5) (6,5)
                  |   
                (0,4) (1,4) (2,4) (3,4) (4,4) (5,4) (6,4)
                  |  
                (0,3) (1,3) (2,3) (3,3) (4,3) (5,3) (6,3)
           Rows   |   
                (0,2) (1,2) (2,2) (3,2) (4,2) (5,2) (6,2)
                  |   
                (0,1) (1,1) (2,1) (3,1) (4,1) (5,1) (6,1)
                  |   
                (0,0)-(1,0)-(2,0)-(3,0)-(4,0)-(5,0)-(6,0)-
        '''

        # Asks players for moves until someone wins or no more possible moves
        while ( winner == False ):
            if ( turn != 42 ):
                x_adj, y_adj, circle_grid = player_move( player_1, color_1,
                                                            circle_grid )
                fill_circle( x_adj, y_adj, color_1 )
                turn += 1
                winner, winning_color = check_winner_status( turn, circle_grid )
                if ( winner == False ):
                    x_adj, y_adj, circle_grid = player_move( player_2, color_2,
                                                            circle_grid )
                    fill_circle( x_adj, y_adj, color_2 )
                    turn += 1
                    winner, winning_color = check_winner_status( turn, circle_grid )
            else: # (if tied)
                winner = True
                winning_color = 'BROWN'

        # Prints who won
        if ( winning_color == color_1 ):
            print( '\nWE HAVE A WINNER!' )
            sleep( 1 )
            print( player_1, 'is the winner!\n' )
        elif ( winning_color == color_2 ):
            print( '\nWE HAVE A WINNER!' )
            sleep( 1 )
            print( player_2, 'is the winner!\n' )
        else:
            print( '\nWE HAVE A TIE!' )
            sleep( 1 )
            print( 'You are both winners!' )

        # Asks if you want to play again
        print( 'Do you want to play again?' )
        play_again = input( '(yes/no) ' )

        # Switches who goes first after a game if players want to play again
        if ( play_again.lower() == 'yes' or play_again.lower() == 'y' ):
            temp = player_1
            player_1 = player_2
            player_2 = temp
            temp = color_1
            color_1 = color_2
            color_2 = temp

def draw_board():
    # Draw the board
    turtle.clearscreen()
    turtle.speed( USAIN_BOLT )
    turtle.hideturtle()
    turtle.penup()
    turtle.goto( BOARD_SIZE_X / 2, - ( BOARD_SIZE_Y / 2 ) )
    turtle.setheading( 180 )
    turtle.pendown()
    turtle.fillcolor( 'BLUE' )
    turtle.begin_fill()
    for i in range( 0, 2 ):
        turtle.forward( BOARD_SIZE_X )
        turtle.right( 90 )
        turtle.forward( BOARD_SIZE_Y )
        turtle.right( 90 )
    turtle.end_fill()
    turtle.penup()

    # Draw holes in the board
    for i in range( 0, 7 ):
        for j in range( 0, 6 ):
            turtle.goto( CIRCLE_START_POINT_X + DISTANCE_BETWEEN_CIRCLES * i,
                         CIRCLE_START_POINT_Y + DISTANCE_BETWEEN_CIRCLES * j )
            turtle.pendown()
            turtle.fillcolor( 'WHITE' )
            turtle.begin_fill()
            turtle.circle( RADIUS )
            turtle.end_fill()
            turtle.penup()

    # Draw column labels
    for i in range( 0, 7 ):
        turtle.goto( COL_LABEL_START_X + DISTANCE_BETWEEN_CIRCLES * i,
                     COL_LABEL_START_Y )
        turtle.write( 'Column ' + str( i + 1 ), font=( "Arial", 14, "normal") )

def player_move( player, color, circle_grid ):
    # Get the player's move
    print( 'It\'s ', player, '\'s turn', sep = '' )
    good_input = False
    num_empty = 0
    while ( good_input == False ):
        col = int( input( 'Select column (1-7): ' ) )
        # Check to see if input is within the valid range
        if ( col > 0 and col < 8 ):
            # Check to see if that column is already filled
            for i in range( 0, 6 ):
                if ( circle_grid[ col - 1 ][ i ] == 'EMPTY' ):
                    num_empty += 1
            # If the row is filled, print invalid and repeat the while loop
            if ( num_empty == 0 ):
                print( '[ INVALID INPUT - No more space left in column ]' )
                sleep( 1 )
            # If the row has open slots, do this
            else:
                x_adj = col - 1
                y_adj = 6 - num_empty
                circle_grid[ x_adj ][ y_adj ] = color
                good_input = True
        else:
            print( '[ INVALID INPUT - Must be between 1 and 7 ]' )
            sleep( 1 )
    return x_adj, y_adj, circle_grid

def fill_circle( x_adj, y_adj, color ):
    # Fill in the circle chosen by the player 
    turtle.speed( USAIN_BOLT )
    turtle.penup()
    turtle.fillcolor( color )
    turtle.goto( CIRCLE_START_POINT_X + DISTANCE_BETWEEN_CIRCLES * x_adj,
                 CIRCLE_START_POINT_Y + DISTANCE_BETWEEN_CIRCLES * y_adj )
    turtle.begin_fill()
    turtle.circle( RADIUS )
    turtle.end_fill()
    turtle.penup()

def check_winner_status( turn, circle_grid ):
    # Checks to see if a Connect Four is even possible
    if ( turn < 7 ):
        return False, 'Too_soon'

    # Check for a Connect Four along each column
    color = 'BLAH'
    for col in range( NUM_COLS ):
        counter = 0
        for row in range( NUM_ROWS ):
            result, color, counter = check_color( col, row, circle_grid,
                                                  color, counter )
            if ( result == 'CONNECT FOUR' ):
                return True, color
    
    # Check for a Connect Four along each row
    color = 'BLAH'
    for row in range( NUM_ROWS ):
        counter = 0
        for col in range( NUM_COLS ):
            result, color, counter = check_color( col, row, circle_grid,
                                                  color, counter )
            if ( result == 'CONNECT FOUR' ):
                return True, color

    # Check for a Connect Four on diagonal lines going from bottom left to
    # top right
    color = 'BLAH'
    limit = 4
    past_halfway = False
    for i in range( 0, 6 ):
        counter = 0
        if ( past_halfway == False ):
            col = 3 - i
            row = 0            
            diag_count = 0
            
            # Evaluates whether or not the "bottom left to top right" check has
            # reached the halfway point (used to account for the coordinate
            # change at the corners)
            if ( col == 1 ):
                past_halfway = True

            # Executes while there is another value in the current diagonal line
            while ( diag_count < limit ):
                result, color, counter = check_color( col, row, circle_grid,
                                                      color, counter )
                if ( result == 'CONNECT FOUR' ):
                    return True, color
                col += 1
                row += 1
                diag_count += 1
            limit += 1
        else:
            limit -= 1
            col = i - 3
            row = i - 3
            diag_count = 0
            while ( diag_count < limit ):
                result, color, counter = check_color( col, row, circle_grid,
                                                      color, counter )
                if ( result == 'CONNECT FOUR' ):
                    return True, color
                col += 1
                row += 1
                diag_count += 1

    # Check for a Connect Four along diagonal lines going from bottom right to
    # top left
    color = 'BLAH'
    limit = 4
    past_halfway = False
    for i in range( 0, 6 ):
        counter = 0
        if ( past_halfway == False ):
            col = 6
            row = 2 - i            
            diag_count = 0
            
            # Evaluates whether or not the "bottom right to top left" check has
            # reached the halfway point (used to account for the coordinate
            # change at the corners)
            if ( row == 0 ):
                past_halfway = True
                
            # Executes while there is another value in the current diagonal line
            while ( diag_count < limit ):
                result, color, counter = check_color( col, row, circle_grid,
                                                      color, counter )
                if ( result == 'CONNECT FOUR' ):
                    return True, color
                col -= 1
                row += 1
                diag_count += 1
            limit += 1
        else:
            limit -= 1
            col = -1 * i + 8
            row = 0
            diag_count = 0
            while ( diag_count < limit ):
                result, color, counter = check_color( col, row, circle_grid,
                                                      color, counter )
                if ( result == 'CONNECT FOUR' ):
                    return True, color
                col -= 1
                row += 1
                diag_count += 1
                
    return False, color

def check_color( col, row, circle_grid, color, counter ):
    if ( ( circle_grid[ col ][ row ] == 'BLACK' or
           circle_grid[ col ][ row ] == 'RED' ) and
         circle_grid[ col ][ row ] == color ):
        counter += 1
        if ( counter == 4 ):
            return 'CONNECT FOUR', color, counter
    else:
        counter = 1
        color = circle_grid[ col ][ row ]
    return 'NO CONNECT FOUR', color, counter
    
########################
# BEGINNING OF PROGRAM #
########################
'''
intro()
decide_first_player()
player_1, color_1, player_2, color_2 = get_player_info()'''
player_1 = 'Player 1'
color_1 = 'BLACK'
player_2 = 'Player 2'
color_2 = 'RED'
play( player_1, color_1, player_2, color_2 )
