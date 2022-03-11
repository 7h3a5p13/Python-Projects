'''
Program Name: Connect Four
Author:       Richard Herndon
Date:         05/10/2021
Version:      2.0
Description:  Popular table-top game which I've written in Python.
Changes:      In version 1.0, I wrote the game to be displayed using the "Turtle"
              library. It was super clunky, but I didn't know how to do it any
              other way. Version 2 has been remade using the "pygame" library.
'''
### IMPORT STATEMENTS ###
import pygame, sys
from pygame.locals import *


### GLOBAL CONSTANTS ###
CONNECT_FOUR        = 'Connect Four' # String to pass when a connect four is found
SCALER              = 1              # (DOESN'T CURRENTLY WORK) Used to scale the board up and down
FPS                 = 30

# Pixel Constants
WINDOW_WIDTH        = 560 * SCALER  # Window width in pixels
WINDOW_HEIGHT       = 500 * SCALER  # Window height in pixels
BOARD_WIDTH         = 460 * SCALER  # Board width in pixels
BOARD_HEIGHT        = 400 * SCALER  # Board height in pixels
HOLE_SIZE           =  50 * SCALER  # Size of viewing holes in pixels
HOLE_RADIUS         = HOLE_SIZE * SCALER // 2 # Radius of viewing holes in pixels
INSIDE_GAP_SIZE     =  10 * SCALER  # Size of gap between viewing holes in pixels
OUTSIDE_GAP_SIZE    =  25 * SCALER  # Size of gap between outer viewing holes and the board edge in pixels

# Board Constants
NUM_ROW_HOLES        = 6 # Number of holes in each row
NUM_COL_HOLES        = 7 # Number of holes in each column
NUM_DIAGONAL_PASSES  = 6 # Number of diagonals to check for Connect Four
HIGHLIGHT_LINE_WIDTH = 2 # Thickness of the lines used to highlight columns
HIGHLIGHT_OFFSET     = 5 # Offset for proper positioning of highlight
X_MARGIN = (WINDOW_WIDTH - BOARD_WIDTH) // 2   # The distance from the edge of the window to the edge of the board in the X axis
Y_MARGIN = (WINDOW_HEIGHT - BOARD_HEIGHT) // 2 # The distance from the edge of the window to the edge of the board in the Y axis

# Color Constants
# Color             R    G    B
BLACK           = (  0,   0,   0)
RED             = (255,   0,   0)
BLUE            = (  0,   0, 255)
LIGHT_GRAY      = (192, 192, 192)
WHITE           = (255, 255, 255)
BOARD_COLOR       = BLUE
BG_COLOR          = LIGHT_GRAY
HIGHLIGHT_COLOR   = WHITE
TEXT_BG_COLOR     = WHITE
P1_COLOR          = BLACK # If changed, be sure to change the constants below
P2_COLOR          = RED   # If changed, be sure to change the constants below

# Player Constants
P1_COLOR_STR      = 'black' # if changed, be sure to change the constants above
P2_COLOR_STR      = 'red'   # if changed, be sure to change the constants above


### CUSTOM EXCEPTIONS ###
# Used in declaring a "Connect Four" has been achieved
class ConnectFour(Exception):
    pass


### INITIALIZE PYGAME AND CREATE WINDOW ###
pygame.init()
# Create window
DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Connect Four')
# Create a clock to keep track of FPS
FPS_CLOCK = pygame.time.Clock()
# Set the font used when printing who won
WINNER_FONT = pygame.font.Font('freesansbold.ttf',48)


### FUNCTIONS ###
def main():
    # This loop initializes the game (see comment on next while loop)
    while True:
        mouse_x = 0 # stores x coordinate of mouse events
        mouse_y = 0 # stores y coordinate of mouse events
        board_data = generate_board_data('empty')
        move_number = 1
        whose_turn = P1_COLOR_STR

        # This loop contains the game. When a winner is found, it breaks out to the above loop and reinitializes the game.
        while True:
            mouse_clicked = False
            DISPLAY_SURFACE.fill(BG_COLOR)
            draw_board(board_data)

            # Get relevant events
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION:
                    mouse_x, mouse_y = event.pos
                elif event.type == MOUSEBUTTONUP:
                    mouse_x, mouse_y = event.pos
                    mouse_clicked = True

            # Get the location of the mouse on the board (if it is on the board at all)
            column = get_column_at_pixel(mouse_x, mouse_y)

            # Checks if the mouse is currently over a column on the board
            if column != None:
                # If the mouse is over a column that has open slots, highlight the column
                if 'empty' in board_data[column]:
                    highlight_column(column)
                # Checks if the mouse is currently over a column and the mouse has been clicked
                if 'empty' in board_data[column] and mouse_clicked:
                    # "7" here is a fake index value and is for finding if there are any pieces in that column or not.
                    p1_index = 7  
                    p2_index = 7
                    # Find the index of the next available hole by determining the index of the top-most populated hole
                    if P1_COLOR_STR in board_data[column]:
                        p1_index = board_data[column].index(P1_COLOR_STR)
                    if P2_COLOR_STR in board_data[column]:
                        p2_index = board_data[column].index(P2_COLOR_STR)
                    # Populate the next available slot with the current player's color
                    if p1_index == p2_index:
                        board_data[column][NUM_ROW_HOLES - 1] = whose_turn
                    else:
                        board_data[column][min(p1_index, p2_index) - 1] = whose_turn
                    
                    # Check if there is a winner
                    if move_number >= 7: # At least 7 moves must pass before someone can win
                        result = check_connect_four(board_data)
                        if result == CONNECT_FOUR:
                            draw_board(board_data)
                            pygame.display.update()
                            winner(whose_turn)
                            break

                    # Change whose move it is
                    move_number += 1
                    if whose_turn == P1_COLOR_STR:
                        whose_turn = P2_COLOR_STR
                    else:
                        whose_turn = P1_COLOR_STR

            # Update the display
            pygame.display.update()
            FPS_CLOCK.tick(FPS)
        
            
# Generate empty board for keeping track of pieces
def generate_board_data(val):
    board = []
    for col in range(NUM_COL_HOLES):
        column = []
        for row in range(NUM_ROW_HOLES):
            column.append(val)
        board.append(column)
    return board


# Figure out where the mouse is in relation to a column
def get_column_at_pixel(mouse_x, mouse_y): 
    for column_x in range(NUM_COL_HOLES):
        # "None" here indicates that I only want the top left coords of the highlight area for a column
        x, y = get_coords(column_x, None)
        column_rect = pygame.Rect(x, y, HOLE_SIZE + INSIDE_GAP_SIZE, BOARD_HEIGHT)
        # If the mouse IS over a column, return that column number, otherwise return a "None" object
        if column_rect.collidepoint(mouse_x, mouse_y): 
            return column_x
    return None


# Gets the coordinates of either a column or a specific hole in a column
def get_coords(column_x, column_y):
    # If the Y coords ARE given (for getting coords of holes)
    if column_y != None: 
        return (X_MARGIN + OUTSIDE_GAP_SIZE + (INSIDE_GAP_SIZE + HOLE_SIZE) * column_x + HOLE_RADIUS), \
               (Y_MARGIN + OUTSIDE_GAP_SIZE + (INSIDE_GAP_SIZE + HOLE_SIZE) * column_y + HOLE_RADIUS)
    # If the Y coords ARE NOT given (for getting coords of columns only)
    else:
        return (X_MARGIN + OUTSIDE_GAP_SIZE + (INSIDE_GAP_SIZE + HOLE_SIZE) * column_x - HIGHLIGHT_OFFSET), (Y_MARGIN + OUTSIDE_GAP_SIZE - HIGHLIGHT_OFFSET)


# Used for highlighting a column
def highlight_column(column):
    x, y = get_coords(column, None)
    x_length = HOLE_SIZE + INSIDE_GAP_SIZE
    y_length = (HOLE_SIZE + INSIDE_GAP_SIZE) * NUM_ROW_HOLES + HIGHLIGHT_OFFSET
    pygame.draw.rect(DISPLAY_SURFACE, HIGHLIGHT_COLOR, (x, y, x_length, y_length), HIGHLIGHT_LINE_WIDTH)


# Used for drawing the board based on the state of the data contained in the "board_data" variable
def draw_board(board_data):
    # Draw the board
    pygame.draw.rect(DISPLAY_SURFACE, BOARD_COLOR, (X_MARGIN, Y_MARGIN, BOARD_WIDTH, BOARD_HEIGHT))
    # Draw the holes on the board (with any pieces in the holes)
    for col in range(NUM_COL_HOLES):
        for row in range(NUM_ROW_HOLES):
            x, y = get_coords(col, row)
            if board_data[col][row] == P1_COLOR_STR:
                pygame.draw.circle(DISPLAY_SURFACE, P1_COLOR, (x, y), HOLE_RADIUS, 0)
            elif board_data[col][row] == P2_COLOR_STR:
                pygame.draw.circle(DISPLAY_SURFACE, P2_COLOR, (x, y), HOLE_RADIUS, 0)
            else: # if board_data[col][row] == 'empty'
                pygame.draw.circle(DISPLAY_SURFACE, BG_COLOR, (x, y), HOLE_RADIUS, 0)


def check_connect_four(board_data):    
    # Check columns for Connect Four
    for col in range(NUM_COL_HOLES):
        current_color = 'empty'
        color_streak = 0
        for row in range(NUM_ROW_HOLES):
            color = board_data[col][row]
            
            current_color, color_streak = check_color_streak(color, current_color, color_streak)
            if color_streak == 4:
                return CONNECT_FOUR
            
    # Check rows for Connect Four
    for row in range(NUM_ROW_HOLES):
        current_color = 'empty'
        color_streak = 0
        for col in range(NUM_COL_HOLES):
            color = board_data[col][row]
            current_color, color_streak = check_color_streak(color, current_color, color_streak)
            if color_streak == 4:
                return CONNECT_FOUR

    # Check diagonals (/) for Connect Four
    col = 0
    row = 3
    # Used to limit the number of holes checked on a given diagonal line.
    cap = 4 
    # For each diagonal in this direction
    for i in range(NUM_DIAGONAL_PASSES):
        current_color = 'empty'
        color_streak = 0
        for j in range(cap):
            color = board_data[col][row]
            current_color, color_streak = check_color_streak(color, current_color, color_streak)
            if color_streak == 4:
                return CONNECT_FOUR
            col += 1
            row -= 1
        # These rules would take too long to explain in a comment, so just trust
        # me here. These rules make sure the program has the proper starting
        # indices for each diagonal.
        if i < 2:
            col = 0
            row = i + 4
            cap += 1
        else: # i >= 2
            col = i - 1
            row = 5
            cap = 8 - i
    
    # Check diagonals (\) for Connect Four
    col = 6
    row = 3
    # Used to limit the number of holes checked on a given diagonal line.
    cap = 4
    # For each diagonal in this direction
    for i in range(NUM_DIAGONAL_PASSES):
        current_color = 'empty'
        color_streak = 0
        for j in range(cap):
            color = board_data[col][row]
            current_color, color_streak = check_color_streak(color, current_color, color_streak)
            if color_streak == 4 and current_color != 'empty':
                return CONNECT_FOUR
            col -= 1
            row -= 1
        # These rules would take too long to explain in a comment, so just trust
        # me here. These rules make sure the program has the proper starting
        # indices for each diagonal.
        if i < 2:
            col = 6
            row = i + 4
            cap += 1
        else: # i >= 2
            col = 7 - i
            row = 5
            cap = 8 - i


# Processes each hole in the board and checks to see if there is a sufficient color streak for a winner to be declared
def check_color_streak(color, current_color, color_streak):
    try:
        if color != 'empty':
            if color == current_color:
                color_streak += 1
                if color_streak == 4:
                    raise ConnectFour
            else: # color != current_color
                current_color = color
                color_streak = 1
        else: # color == 'empty'
            color_streak = 0
            current_color = 'empty'
            return current_color, color_streak
            
    except ConnectFour:
        return current_color, color_streak
    return current_color, color_streak


# Used for displaying who won
def winner(player):
    text_surface_obj = WINNER_FONT.render(player.upper() + ' WINS!', True, BLACK, TEXT_BG_COLOR)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    DISPLAY_SURFACE.blit(text_surface_obj,text_rect_obj)
    pygame.display.update()
    pygame.time.wait(5000)
    
main()
