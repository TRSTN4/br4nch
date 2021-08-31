# Part of the br4nch package.

# Returns paint with the given paint and specials.
def painter(options):
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

    # Saves all the special action ids in a list.
    specials_id = ["bold", "underline", "reversing"]

    # Saves all the special actions in a list.
    specials_action = [bold, underline, reversing]

    # Creates the variables.
    color = ""
    special1 = ""
    special2 = ""
    special3 = ""

    # Checks if options value is equal to one of the colors ids.
    if options in colors_id:
        # Color is equal to the value of options.
        color = options
    # Checks if options value is equal to one of the specials ids.
    if options in specials_id:
        # special1 is equal to the value of options.
        special1 = options

    # The first entry option is color.
    if len(options) > 0 and isinstance(options, list) and options[0].lower() in colors_id:
        # Color is the first entry of the options list.
        color = options[0].lower()
    # If the first entry in the options list is used. If so, the second entry option is special1.
    if len(options) > 1 and isinstance(options, list) and options[1].lower() in specials_id:
        # Special 1 is the second entry of the options list.
        special1 = options[1].lower()
    # If the first and second entry in the options list is used. If so, the third entry option is special2.
    if len(options) > 2 and isinstance(options, list) and options[2].lower() in specials_id:
        # Special 2 is the second entry of the options list.
        special2 = options[2].lower()
    # If the first, second and third entry in the options list is used. If so, the fourth entry option is special3.
    if len(options) > 3 and isinstance(options, list) and options[3].lower() in specials_id:
        # Special 3 is the second entry of the options list.
        special3 = options[3].lower()

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
