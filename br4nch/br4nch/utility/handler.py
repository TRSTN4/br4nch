# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.painter import painter


# Imports the paint for the custom errors.
def import_paint():
    # All global statements.
    global black, red, green, yellow, blue, magenta, cyan, white, bold, underline, reversing, clear, error

    # Gets the needed lists/dictionaries.
    error = librarian("error")

    # Imports and stores all the colors and specials.
    black = painter("black")
    red = painter("red")
    green = painter("green")
    yellow = painter("yellow")
    blue = painter("blue")
    magenta = painter("magenta")
    cyan = painter("cyan")
    white = painter("white")
    bold = painter("bold")
    underline = painter("underline")
    reversing = painter("reversing")
    clear = painter("clear")


# Drops the error if the parsed branch does not exists.
def display_error(branch):
    # Checks if pares branch exists in the error dictionary.
    if branch not in error:
        # Adds the pared branch to the error dictionary.
        error.update({branch: []})

    # Adds the errors to the error list inside the dictionary.
    error[branch].append(red + "[-] " + bold + "Display Error" + clear + red + ":\n" + " " * 4
                         + "└─ The " + yellow + bold + branch + clear + red
                         + " branch does not exist and therefore cannot be displayed." + clear)


# Drops the error if the parsed branch does not exists.
def add_header_error(branch, header):
    # Checks if pares branch exists in the error dictionary.
    if branch not in error:
        # Adds the pared branch to the error dictionary.
        error.update({branch: []})

    # Adds the errors to the error list inside the dictionary.
    error[branch].append(red + "[-] " + bold + "Add Header Error" + clear + red + ":\n" + " " * 4 + "└─ The " + yellow
                         + bold + branch + clear + red + " branch does not exist and thus the " + yellow + bold
                         + header + clear + red + " header cannot be added." + clear)


def add_layer_error(branch, layer):
    # Checks if pares branch exists in the error dictionary.
    if branch not in error:
        # Adds the pared branch to the error dictionary.
        error.update({branch: []})

    # Creates the required variable.
    multiple = ""

    # Checks if layer value is instance of a list.
    if isinstance(layer, list):
        # Creates the required variables.
        result = ""
        separator = ""

        # Layers is equal to the parsed layer value.
        layers = layer

        # Loops through all layers of the list.
        for layer in layers:
            # Adds all layers in the loop to the result.
            result = result + clear + red + separator + yellow + bold + layer + clear
            # Updates the separator.
            separator = ", "

        # Sets the layer value to the value of result.
        layer = result
        # Multiple adds a "s" if there are multiple layers in the previous loop.
        multiple = "s"

    # Adds the errors to the error list inside the dictionary.
    error[branch].append(red + "[-] " + bold + "Add Layer Error" + clear + red + ":\n" + " " * 4
                         + "└─ The " + yellow + bold + branch + clear + red + " branch does not exist and thus the "
                         + yellow + bold + layer.replace("\n", " ") + clear + red
                         + " layer{multiple} cannot be added.".format(multiple=multiple) + clear)


# Drops the error if the parsed colors and/or specials does not exists.
def paint_error(branch, layer, options):
    # Creates the separator.
    separator = clear + red + ", "

    # Adds the errors to the error list inside the dictionary.
    error[branch].append(red + "[-] " + bold + "Paint Error" + clear + red + ":\n" + " " * 4
                         + "├─ Could not add the paint option: " + yellow + bold + options.lower() + clear + red
                         + " to the " + yellow + bold + layer.replace("\n", " ") + clear + red + " layer in the "
                         + yellow + bold + branch.replace("\n", " ") + clear + red + " branch.\n" + " " * 4
                         + "└─ Please select one of these below:\n" + " " * 7 + "├─ Colors\n" + " " * 7 + "│"
                         + " " * 2 + "└─ " + black + bold + "Black" + separator + bold + "Red" + separator + green
                         + bold + "Green" + separator + yellow + bold + "Yellow" + separator + blue + bold + "Blue"
                         + separator + magenta + bold + "Magenta" + separator + cyan + bold + "Cyan" + separator
                         + white + bold + "White\n" + clear + red + " " * 7 + "└─ Specials\n" + " " * 10 + "└─ "
                         + white + bold + "Bold" + separator + white + bold + "Underline" + separator + white + bold
                         + "Reversing" + clear)
