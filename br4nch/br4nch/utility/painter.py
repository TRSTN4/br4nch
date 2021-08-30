# Part of the br4nch package.

# Returns paint with the given paint and specials.
def painter(color="", special1="", special2="", special3=""):
    # Stores all the colors and specials.
    black = "\u001b[30m"        # Black
    red = "\u001b[31m"          # Red
    green = "\u001b[32m"        # Green
    yellow = "\u001b[33m"       # Yellow
    blue = "\u001b[34m"         # Blue
    magenta = "\u001b[35m"      # Magenta
    cyan = "\u001b[36m"         # Cyan
    white = "\u001b[37m"        # White
    bold = "\u001b[1m"          # Bold
    underline = "\u001b[4m"     # Underline
    reversing = "\u001b[4m"     # Reversing
    clear = "\u001b[0m"         # Clear

    # Saves all the color actions in a list.
    colors_action = [black, red, green, yellow, blue, magenta, cyan, white, clear]

    # Saves all the color action ids in a list.
    colors_id = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white", "clear"]

    # Saves all the special actions in a list.
    specials_action = [bold, underline, reversing]

    # Saves all the special action ids in a list.
    specials_id = ["bold", "underline", "reversing"]

    if color not in colors_id:
        color = ""
    if special1 not in specials_id:
        special1 = ""
    if special2 not in specials_id:
        special2 = ""
    if special3 not in specials_id:
        special3 = ""

    # Checks if the color variable has any value.
    if color:
        # Loops through total length of the colors action list.
        for number in range(len(colors_action)):
            # Checks if the parsed color is equal to a id in the id list.
            if color == colors_id[number]:
                # Sets the requested color action to the color variable.
                color = colors_action[number]

    # Checks if the special1, special2 or special3 variables has any value.
    if special1 or special2 or special3:
        # Loops through total length of the specials action list.
        for number in range(len(specials_action)):
            # Checks if the parsed special1 is equal to a id in the id list.
            if special1 == specials_id[number]:
                # Sets the requested special1 action to the special1 variable.
                special1 = specials_action[number]
            # Checks if the parsed special2 is equal to a id in the id list.
            if special2 == specials_id[number]:
                # Sets the requested special2 action to the special2 variable.
                special2 = specials_action[number]
            # Checks if the parsed special3 is equal to a id in the id list.
            if special3 == specials_id[number]:
                # Sets the requested special3 action to the special3 variable.
                special3 = specials_action[number]

    # Returns the requested action.
    return color + special1 + special2 + special3
