# Bryant Franks

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.

rooms = {
    'Great Hall': {'south': 'Bedroom'},
    'Bedroom': {'north': 'Great Hall', 'east': 'Cellar'},
    'Cellar': {'west': 'Bedroom'}
}
moveCommands = {'north', 'east', 'south', 'west', 'exit'}


# functions
def player_status(currentRoom):
    print('_______________________________________')
    print('you are in the {}'.format(currentRoom))


def player_action(presentRoom, verb, noun):
    global currentRoom

    if presentRoom in rooms:
        if noun in rooms[presentRoom]:
            currentRoom = rooms[presentRoom][noun]
        else:
            print('not valid breh')
        # Get Values from nested Dictionary
        # north = rooms[presentRoom]['north']
        # south = rooms[presentRoom]['south']
        # east = rooms[presentRoom]['east']
        # west = rooms[presentRoom]['west']

    # for room in rooms:
    #     if presentRoom not in room:
    #         continue
    #     else:
    #         for option in rooms[room]:
    #             print(rooms[room][option], 'is the target room')
    #             print(room, 'is the room currently be iterated')
    #             # print(rooms[currentRoom])
    #             # print(rooms[currentRoom][noun])
    #             # print(rooms[currentRoom][option])
    #             print(option, 'is the available option')
    #             if noun not in option:
    #                 print('{} is the option being iterated and does not math the inputed noun which is {}'.format(option, noun))
    #             else:
    #                 print(option, 'is the successful option chosen')
    #                 currentRoom = rooms[presentRoom][noun]
    #                 break


# Begin Game

# Set Player in Start Room
currentRoom = 'Great Hall'

# show game instructions
print('This is the simplified dragon game')
print('type the directions: north, east, south, west to move, or exit to quit')

# begin game loop
while True:
    player_status(currentRoom)
    userInput = input('Enter a move: ')
    inputMove = userInput.lower().split()

    if 'exit' not in inputMove:
        directive = inputMove[0]
        actionSubject = inputMove[1]
        player_action(currentRoom, directive, actionSubject)
    else:
        print('exit check worked')
        break

# # input direction
# print('you are in {}'.format(currentRoom))
# moveInput = input('Enter a command')
# moveInput = moveInput.lower().split()
# directive = moveInput[0]
# actionSubject = moveInput[1]
#
#
# # GAME LOOP
# while directive != 'exit' and actionSubject != 'exit':
#     moveInput = input('Enter a direction you want to go: North, East, South, or West')
#     moveInput = moveInput.lower()
#     print(actionSubject)
# print('loop broken')
