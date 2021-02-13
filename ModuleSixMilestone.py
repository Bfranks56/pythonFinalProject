# Bryant Franks

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.

rooms = {
    'Great Hall': {'south': 'Bedroom'},
    'Bedroom': {'north': 'Great Hall', 'east': 'Cellar'},
    'Cellar': {'west': 'Bedroom'}
}
moveCommands = {'north', 'east', 'south', 'west', 'exit'}


# Current Player Status function
def player_status(currentRoom):
    print('_______________________________________')
    print('You are in the {}.'.format(currentRoom))


# Player action function. TODO: verb is present for future iteration of game
def player_action(presentRoom, verb, noun):
    global currentRoom
    # verifies action is either go or get. TODO: for this version only 'go' is valid.
    if verb == 'go':
        # verifies movement action is valid
        if noun in rooms[presentRoom]:
            currentRoom = rooms[presentRoom][noun]
            print('You decide to follow the path to the {}.'.format(noun))
        else:
            print('There is no path to the {}.'.format(noun))
    else:
        print('This is not permitted.')


# Begin Game

# Set Player in Start Room
currentRoom = 'Great Hall'

# show game instructions
print('This is the simplified dragon game.')
print('Type the instruction: Go North, Go South, Go East, or Go West. Type Exit to quit.')

# begin game loop
while True:
    # Game Logic that runs prior to each player movement
    player_status(currentRoom)
    userInput = input('Enter a move: Go North, Go South, Go East, or Go West. Type Exit to quit.')
    inputMove = userInput.lower().split()

    # validate input action and leaves on exit
    if 'exit' not in inputMove:
        # Validates input move length before continuing.
        if len(inputMove) != 2:
            print('Something went wrong with your input, try again.')
        else:
            directive = inputMove[0]
            actionSubject = inputMove[1]
            player_action(currentRoom, directive, actionSubject)
    else:
        print('Thanks for Playing!')
        break
