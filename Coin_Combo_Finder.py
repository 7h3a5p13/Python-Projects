'''
Program Name: Coin Combo Finder
Author:       Richard Herndon
Version:      1
Date:         04/08/2021
Description:  Find all possible coin combinations for a given amount of cents.
'''

### CONSTANTS ###
# Constants for coin values in cents.
QUARTER = 25
DIME = 10
NICKEL = 5

### FUNCTIONS ###
# Main program function.
def main():
    # Get the amount of money (in cents) that you want to calculate all the possibilities for.
    cents = get_input()
    # Determine all the combinations of pennies, nickels, dimes, and quarters.
    combos = find_combos(cents)
    # Display all the combinations to the screen.
    display_combos(cents,combos)

# This function gets user input.
def get_input():
    # Input validation loop.
    while True:
        try:
            cents = int(input('Enter cents: '))
            return cents
        except Exception as err:
            print('\n' + str(err) + '\n')

# This function determines the different combinations that can make the given amount of money.
def find_combos(cents):
    # Initialize a list for holding the lists of combinations.
    combos = []
    ''' 
    The following is an odometer-like block of code for figuring out the possibilities. IT starts off with all
    pennies and then decrements pennies while simultaneously incrementing all the other coin values in sequence.
    The best way that I can explain this is by showing you an example.

    EXAMPLE (assumes 27 cents):
    Iterations | Results
    1:           Q = 0 D = 0 N = 0 P = 27
    2:           Q = 0 D = 0 N = 1 P = 22
    3:           Q = 0 D = 0 N = 2 P = 17
    4:           Q = 0 D = 0 N = 3 P = 12
    5:           Q = 0 D = 0 N = 4 P = 7
    6:           Q = 0 D = 0 N = 5 P = 2
    7:           Q = 0 D = 1 N = 0 P = 17
    8:           Q = 0 D = 1 N = 1 P = 12
    9:           Q = 0 D = 1 N = 2 P = 7
    10:          Q = 0 D = 1 N = 3 P = 2
    11:          Q = 0 D = 2 N = 0 P = 7
    12:          Q = 0 D = 2 N = 1 P = 2
    13:          Q = 1 D = 0 N = 0 P = 2
    '''
    # Beginning of the odometer-like block of code.
    # The max amount of quarters doesn't depend on anything except the given amount of cents.
    max_quarters = cents // QUARTER + 1 # The "+ 1" is necessary to make the following "for" loop work properly.
    for quarters in range(max_quarters):
        # The max amount of dimes depends on the given amount of cents minus the total value of all quarters currently being considered.
        max_dimes = (cents - quarters * QUARTER) // DIME + 1  # The "+ 1" is necessary to make the following "for" loop work properly.
        for dimes in range(max_dimes):
            # The max amount of nickels depends on the given amount of cents minus the total value of all quarters and dimes currently being considered.
            max_nickels = (cents - quarters * QUARTER - dimes * DIME) // NICKEL + 1 # The "+ 1" is necessary to make the following "for" loop work properly.
            for nickels in range(max_nickels):
                # The amount of pennies depends on the given amount of cents minus the total value of all quarters, dimes, and nickels currently being considered.
                pennies = cents - quarters * QUARTER - dimes * DIME - nickels * NICKEL
                # Append a list containing a possible outcome to the list of combinations.
                combos.append([quarters,dimes,nickels,pennies])
    # End of odometer-like block of code.
    
    # Return the results.
    return combos

# This function displays the results in a pretty way.
def display_combos(cents,combos):
    print_header_box(cents)
    print('\tQ\tD\tN\tP\n')
    for i in combos:
        for j in i:
            print('\t' + str(j),end = '')
        print()
    print('\n\tNumber of Combos:', len(combos), '\n')
    input('Hit Enter to close program')

# This actually prints the header.
def print_header_box(cents):
    line_width = (len(str(cents) + ' cents'))
    print_edge(line_width)
    print('\t\t|' +str(cents),'cents|')
    print_edge(line_width)

# This prints the edge of the header.
def print_edge(line_width):
    print('\t\t+',end = '')
    for i in range(line_width):
        print('-',end = '')
    print('+')

### BEGIN PROGRAM ###
main()
