# Bryant Franks


# Current Player Status function
def player_status(currentRoom):
    print('_______________________________________')
    print(
        'you are in the {}. Could be spooky, could be calming. I don\'t know what you get into...\n'.format(
            currentRoom))


# Begin Game
def main():
    # Variables
    rooms = {
        'Lower Decks': {'north': 'Air Lock', 'east': 'Mess Hall', 'item': ''},
        'Air Lock': {'south': 'Lower Decks', 'east': 'Meditation Garden', 'item': ''},
        'Meditation Garden': {'north': 'Space Bridge', 'south': 'Mess Hall', 'west': 'Air Lock',
                              'item': 'night vision goggles'},
        'Space Bridge': {'south': 'Meditation Garden', 'item': 'chest guard'},
        'Mess Hall': {'north': 'Meditation Garden', 'south': 'Kitchen', 'east': 'Showers', 'west': 'Lower Decks',
                      'item': 'pair of gauntlets'},
        'Kitchen': {'north': 'Mess Hall', 'east': 'Sleep Quarters', 'item': 'laser sword'},
        'Showers': {'south': 'Sleep Quarters', 'west': 'Mess Hall', 'item': 'shuriken'},
        'Sleep Quarters': {'north': 'Showers', 'west': 'Kitchen', 'item': 'slightly rusted pair of sais'}
    }
    playerInventory = []

    # Set Player in Start Room
    currentRoom = 'Lower Decks'

    # show game instructions
    print('This is a goddamn ninja game')
    print('type the directions: north, east, south, west to move, or exit to quit')

    # begin game loop
    while True:
        # Game Logic that runs prior to each player movement
        player_status(currentRoom)

        # Checks if an item is available in the current room and prints appropriate output
        if rooms[currentRoom]['item'] == '':
            # Conditional for alternate flavor text in final boss room
            if currentRoom == 'Air Lock':
                print('Something feels ominous, and you can\'t put that in a bag.')
            else:
                print('you look around, but you don\'t see anything.  whack.')
        else:
            print('as you look around, you see a {}'.format(rooms[currentRoom]['item']))
        print('one look in your satchel and you see: {}'.format(playerInventory))

        # sets win/lose criteria for final boss
        if currentRoom == 'Air Lock':
            print('\nOH NOEZ! MASTER HUMLAE AWAITS YOU!\n')
            if len(playerInventory) + 1 < 6:
                print('Told you sleeping in class would come back to bite you. Master Humlae '
                      'bopped your unprepared butt! YOU LOSE')
            else:
                print('You were ready for this fight!  Master Humlae lies defeated! YOU WIN!!!')
            break

        # action input
        userInput = input('\nWhat are you gonna do wannabe Space Ninja?:')
        inputMove = userInput.lower().split()

        # validate input action and leaves on exit
        if 'exit' not in inputMove:
            # validates a non-exit entry has a valid length
            if len(inputMove) < 2:
                print('\nSomething went wrong with your input, try again.')
            else:
                directive = inputMove[0]
                # items may be more than one word, re-maps the input move into two values
                actionSubject = inputMove[1:]
                action = ' '.join(map(str, actionSubject))
        else:
            print('Thanks for Playing!')
            break

        # verifies action is either go or get.
        if directive == 'go':
            # verifies movement action is valid
            if action in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][action]
                print('\nNinja VANISH!!! You silently Naruto Run {}.'.format(action))
            else:
                print('\nDid you not pay attention in Space Ninja Awareness class? {} isn\'t an option!'.format(action))

        # verifies action is either go or get.
        elif directive == 'get':
            # verifies if item is available to get, validates on partial match because fat fingers may be annoying, but shouldn't be punished.
            if action in rooms[currentRoom]['item']:
                if action in playerInventory:
                    print('\nLook at you greedypants. you\'ve already got a {} in your satchel...'.format(action))
                else:
                    print('\nOh Sweet! this could help! better put this {} in your satchel'.format(rooms[currentRoom]['item']))
                    playerInventory.append(rooms[currentRoom]['item'])
                    rooms[currentRoom]['item'] = ''
            else:
                print('\nyou can\'t do that... are you feeling okay? what is a {} even?'.format(action))
        else:
            print('\nCan\'t do that breh. try again.')

main()
