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
    print('you are in the {}'.format(currentRoom))


# Player action function. Note: verb is present for future iteration of game
def player_action(presentRoom, verb, noun):
    global currentRoom
    # verifies action is either go or get. for this version only 'go' is valid.
    if verb == 'go':
        # verifies movement action is valid
        if noun in rooms[presentRoom]:
            currentRoom = rooms[presentRoom][noun]
        else:
            print('not valid breh')
    else:
        print('invalid action breh')


# Begin Game

# Set Player in Start Room
currentRoom = 'Great Hall'

# show game instructions
print('This is the simplified dragon game')
print('type the directions: north, east, south, west to move, or exit to quit')

# begin game loop
while True:
    # Game Logic that runs prior to each player movement
    player_status(currentRoom)
    userInput = input('Enter a move: ')
    inputMove = userInput.lower().split()

    # validate input action and leaves on exit
    if 'exit' not in inputMove:
        directive = inputMove[0]
        actionSubject = inputMove[1]
        player_action(currentRoom, directive, actionSubject)
    else:
        print('Thanks for Playing!')
        break
