GLOBAL VARIABLES
SET: Move commands
SET: Dictionary of Room, adjacent rooms, and items
SET: player inventory
END GLOBAL VARIABLES

SET: initial room location

PRINT Game intro and directions

GAME LOOP LOGIC

PRINT: player status ie: current room location, inventory, and available directional movements
CONDITIONAL: exit loop if in victory status (in boss room with full inventory)
    PRINT: victory message
CONDITIONAL: exit loop if in losing status (in boss room without full inventory)
    PRINT losing message
PRINT: Action prompt
INPUT: Move Command
SET: Move command into action array to validate if move action is valid

CONDITIONAL if action array indicates movement
    MOVE LOGIC LOOP
    VALIDATE: if Move command array has a matching parameter in the Room Dictionary
    CONDITIONAL: if move command is invalid:
        PRINT: validation error message
    ELSE:
        SET: New Room location and end Move logic loop
    END MOVE LOGIC LOOP

CONDITIONAL if action array indicates inventory action

INVENTORY LOGIC LOOP
VALIDATE: if Inventory command array has a matching parameter in the Room Dictionary
CONDITIONAL: if Inventory command is invalid:
    PRINT: validation error message
ELSE:
    PRINT: inventory addition message
    SET: Room item into player inventory and end Inventory Logic Loop
END INVENTORY LOGIC LOOP

END GAME LOOP LOGIC







