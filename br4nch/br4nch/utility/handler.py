# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian


def import_paint():
    # All global statements.
    global black, red, green, yellow, blue, magenta, cyan, white, bold, underline, reversing, clear, error

    # Gets the needed lists/dictionaries.
    error = librarian("error")

    # Stores all the colors and specials.
    black = ""
    red = "\u001b[31m"  # Red
    green = "\u001b[32m"  # Green
    yellow = "\u001b[33m"  # Yellow
    blue = "\u001b[34m"  # Blue
    magenta = "\u001b[35m"  # Magenta
    cyan = "\u001b[36m"  # Cyan
    white = "\u001b[37m"  # White
    bold = "\u001b[1m"  # Bold
    underline = "\u001b[4m"  # Underline
    reversing = "\u001b[4m"  # Reversing
    clear = "\u001b[0m"  # Clear


def paint_error(branch, layer, options):
    # Separator variable.
    sep = clear + red + ", "

    #
    error[branch].append(red + "[-] " + bold + "Paint Error" + clear + red + ":\n" + " " * 4
                         + "├─ Could not add the paint option: " + yellow + bold + options.lower() + clear + red
                         + " to the " + yellow + bold + layer.replace("\n", " ") + clear + red + " layer in the "
                         + yellow + bold + branch.replace("\n", " ") + clear + red + " branch.\n" + " " * 4
                         + "└─ Please select one of these below:\n" + " " * 7 + "├─ Colors\n" + " " * 7 + "│"
                         + " " * 2 + "└─ " + black + bold + "Black" + sep + bold + "Red" + sep + green + bold
                         + "Green" + sep + yellow + bold + "Yellow" + sep + blue + bold + "Blue" + sep + magenta
                         + bold + "Magenta" + sep + cyan + bold + "Cyan" + sep + white + bold + "White\n" + clear
                         + red + " " * 7 + "└─ Specials\n" + " " * 10 + "└─ " + white + bold + "Bold" + sep + white
                         + bold + "Underline" + sep + white + bold + "Reversing" + clear)


def add_header_error(branch, header):
    if branch not in error:
        error.update({branch: []})

    error[branch].append(red + "[-] " + bold + "Add Header Error" + clear + red + ":\n" + " " * 4 + "└─ The " + yellow
                         + bold + branch + clear + red + " branch does not exist and thus the " + yellow + bold
                         + header + clear + red + " header cannot be added." + clear)


def add_layer_error(branch, layer):
    if branch not in error:
        error.update({branch: []})

    multiple = ""

    if isinstance(layer, list):
        layers = layer
        result = ""
        sep = ""
        for layer in layers:
            result = result + clear + red + sep + yellow + bold + layer + clear
            sep = ", "
        layer = result
        multiple = "s"

    error[branch].append(red + "[-] " + bold + "Add Layer Error" + clear + red + ":\n" + " " * 4
                         + "└─ The " + yellow + bold + branch + clear + red + " branch does not exist and thus the "
                         + yellow + bold + layer.replace("\n", " ") + clear + red
                         + " layer{multiple} cannot be added.".format(multiple=multiple) + clear)


def display_error(branch):
    if branch not in error:
        error.update({branch: []})

    error[branch].append(red + "[-] " + bold + "Display Error" + clear + red + ":\n" + " " * 4
                         + "└─ The " + yellow + bold + branch + clear + red
                         + " branch does not exist and therefore cannot be displayed." + clear)
