# Bryant Franks


# Current Player Status function
def player_status(currentRoom):
    print('_______________________________________')
    print(
        'you are in the {}. Could be spooky, could be calming. I don\'t know what you get into...'.format(
            currentRoom))
    # not the right place for this.  maybe add in the function?
    # print('as you look around, you see a {} sitting on the floor.'.format(rooms[currentRoom]['item']))

    # def player_action(presentRoom, verb, noun):
    #
    #     global currentRoom
    #     # verifies action is either go or get. for this version only 'go' is valid.
    #     if verb == 'go':
    #         # verifies movement action is valid
    #         if noun in rooms[presentRoom]:
    #             currentRoom = rooms[presentRoom][noun]
    #             print('Ninja VANISH!!! You silently Naruto Run {}.'.format(noun))
    #             return
    #         else:
    #             print('Did you not pay attention in Space Ninja Awareness class? {} isn\'t an option!'.format(noun))
    #
    #     elif verb == 'get':
    #         if noun in rooms[presentRoom]['item']:
    #             if noun in playerInventory:
    #                 print('Look at you greedypants. you\'ve already got a {} in your satchel...'.format(noun))
    #             else:
    #                 print('got the {}!'.format(noun))
    #                 playerInventory.append(noun)
    #                 print(playerInventory)
    #                 print(rooms[presentRoom]['item'])
    #         else:
    #             print('not viable')
    #     #     write get item method
    #     # checks to see if item is in inventory
    #     # if so adds item to personal inventory list
    #     # removes item from room dictionary
    #     # if item not in dictionary prints error message
    #     else:
    #         print('Can\'t do that breh. try again.')

# Begin Game


def main():
    rooms = {
        'Lower Decks': {'north': 'Air Lock', 'east': 'Mess Hall', 'item': 'bunch of nothing'},
        'Air Lock': {'south': 'Lower Decks', 'east': 'Meditation Garden'},
        'Meditation Garden': {'north': 'Space Bridge', 'south': 'Mess Hall', 'west': 'Air Lock',
                              'item': 'night vision goggles'},
        'Space Bridge': {'south': 'Meditation Garden', 'item': 'chest guard'},
        'Mess Hall': {'north': 'Meditation Garden', 'south': 'Kitchen', 'east': 'Showers', 'west': 'Lower Decks',
                      'item': 'gauntlets'},
        'Kitchen': {'north': 'Mess Hall', 'east': 'Sleep Quarters', 'item': 'laser sword'},
        'Showers': {'south': 'Sleep Quarters', 'west': 'Mess Hall', 'item': 'shuriken'},
        'Sleep Quarters': {'north': 'Showers', 'west': 'Kitchen', 'item': 'sais'}
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

        # sets lose criteria
        if currentRoom == 'Air Lock':
            print('OH SHIT! MASTER HUMLAE AWAITS YOU!')
            print('trash bitch. you lose')
            break

        userInput = input('What are you gonna do wannabe Space Ninja?: ')
        inputMove = userInput.lower().split()

        # validate input action and leaves on exit
        if 'exit' not in inputMove:
            # validates a non-exit entry has a valid length
            if len(inputMove) < 2:
                print('Something went wrong with your input, try again.')
            else:
                directive = inputMove[0]
                # items may be more than one word, re-maps the input move into two values
                actionSubject = inputMove[1:]
                action = ' '.join(map(str, actionSubject))
                # player_action(currentRoom, directive, action)
        else:
            print('Thanks for Playing!')
            break

        # verifies action is either go or get. for this version only 'go' is valid.
        if directive == 'go':
            # verifies movement action is valid
            if action in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][action]
                print('Ninja VANISH!!! You silently Naruto Run {}.'.format(action))
            else:
                print('Did you not pay attention in Space Ninja Awareness class? {} isn\'t an option!'.format(action))

        elif directive == 'get':
            if action in rooms[currentRoom]['item']:
                if action in playerInventory:
                    print('Look at you greedypants. you\'ve already got a {} in your satchel...'.format(action))
                else:
                    print('got the {}!'.format(action))
                    playerInventory.append(action)
                    print(playerInventory)
                    print(rooms[currentRoom]['item'])
            else:
                print('not viable')
        #     write get item method
        # checks to see if item is in inventory
        # if so adds item to personal inventory list
        # removes item from room dictionary
        # if item not in dictionary prints error message
        else:
            print('Can\'t do that breh. try again.')

main()
