# Part of the br4nch package.

# Returns the requested paint.
def painter(options, branch="", layer=""):
    # All global statements.
    global black, red, green, yellow, blue, magenta, cyan, white, bold, underline, reversing, clear

    # Stores all the colors and specials.
    black = "\u001b[30m"
    red = "\u001b[31m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    blue = "\u001b[34m"
    magenta = "\u001b[35m"
    cyan = "\u001b[36m"
    white = "\u001b[37m"
    bold = "\u001b[1m"
    underline = "\u001b[4m"
    reversing = "\u001b[4m"
    clear = "\u001b[0m"

    # Saves all the lists and dictionaries in storage list.
    colors_action = [black, red, green, yellow, blue, magenta, cyan, white, clear]
    specials_action = [bold, underline, reversing]

    # Saves all the lists and dictionaries in identity list.
    colors_id = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white", "clear"]
    specials_id = ["bold", "underline", "reversing"]

    # Creates the required variables.
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
        # Special 2 is the third entry of the options list.
        special2 = options[2].lower()
    # If the first, second and third entry in the options list is used. If so, the fourth entry option is special3.
    if len(options) > 3 and isinstance(options, list) and options[3].lower() in specials_id:
        # Special 3 is the fourth entry of the options list.
        special3 = options[3].lower()

    # Checks if the option value is instance of a list.
    if not isinstance(options, list):
        # Checks if the parsed option is equal to "clear" color action.
        if options != "clear":
            # Checks if option value is not in colors
            if options not in colors_id + specials_id:
                # Imports the handler for the custom error.
                from br4nch.utility.handler import paint_error
                # Runs a custom error.
                paint_error(branch, layer, options)

    # Checks if the color value has content.
    if color:
        # Loops through total length of the colors action list.
        for number in range(len(colors_action)):
            # Checks if the parsed action is equal to the action identity given by the length number.
            if color == colors_id[number]:
                # Colors is equal to the requested color.
                color = colors_action[number]

    # Checks if the special1, special2 or special3 variables has content.
    if special1 or special2 or special3:
        # Loops through total length of the specials action list.
        for number in range(len(specials_action)):
            # Checks if the parsed action is equal to the action identity given by the length number.
            if special1 == specials_id[number]:
                # Sets the requested special1 action to the special1 variable.
                special1 = specials_action[number]
            # Checks if the parsed action is equal to the action identity given by the length number.
            if special2 == specials_id[number]:
                # Sets the requested special2 action to the special2 variable.
                special2 = specials_action[number]
            # Checks if the parsed action is equal to the action identity given by the length number.
            if special3 == specials_id[number]:
                # Sets the requested special3 action to the special3 variable.
                special3 = specials_action[number]

    # Returns the requested paint.
    return color + special1 + special2 + special3
