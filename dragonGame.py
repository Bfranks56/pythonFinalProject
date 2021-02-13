# Bryant Franks

# room dictionary
rooms = {
        'Lower Decks': {'north': 'Air Lock', 'east': 'Mess Hall'},
        'Air Lock': {'south': 'Lower Decks', 'east': 'Meditation Garden'},
        'Meditation Garden': {'north': 'Space Bridge', 'south': 'Mess Hall', 'west': 'Air Lock'},
        'Space Bridge': {'south': 'Meditation Garden'},
        'Mess Hall': {'north': 'Meditation Garden', 'south': 'Kitchen', 'east': 'Showers', 'west': 'Lower Decks'},
        'Kitchen': {'north': 'Mess Hall', 'east': 'Sleep Quarters'},
        'Showers': {'south': 'Sleep Quarters', 'west': 'Mess Hall'},
        'Sleep Quarters': {'north': 'Showers', 'west': 'Kitchen'}
}
# move commands
moveCommands = {'north', 'east', 'south', 'west', 'exit'}


# Current Player Status function
def player_status(currentRoom):
    print('_______________________________________')
    print('you are in the {}. Could be spooky, could be calming. I don\'t know what you get into...'.format(currentRoom))


# Player action function. Note: verb is present for future iteration of game
def player_action(presentRoom, verb, noun):
    global currentRoom
    # verifies action is either go or get. for this version only 'go' is valid.
    if verb == 'go':
        # verifies movement action is valid
        if noun in rooms[presentRoom]:
            currentRoom = rooms[presentRoom][noun]
            print('Ninja VANISH!!! You silently Naruto Run {}.'.format(noun))
        else:
            print('Did you not pay attention in Space Ninja Awareness class? {} isn\'t an option!'.format(noun))
    else:
        print('Can\'t do that breh. try again.')


# Begin Game

# Set Player in Start Room
currentRoom = 'Lower Decks'

# show game instructions
print('This is a goddamn ninja game')
print('type the directions: north, east, south, west to move, or exit to quit')

# begin game loop
while True:
    # Game Logic that runs prior to each player movement
    player_status(currentRoom)
    userInput = input('What are you gonna do wannabe Space Ninja?: ')
    inputMove = userInput.lower().split()

    # validate input action and leaves on exit
    if 'exit' not in inputMove:
        directive = inputMove[0]
        actionSubject = inputMove[1]
        player_action(currentRoom, directive, actionSubject)
    else:
        print('Thanks for Playing!')
        break
