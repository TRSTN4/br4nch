# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.painter import painter


# Adds the chosen paint to the chosen header to a list.
def color_layer(branch, options, layer, position= ""):
    # Gets the needed lists/dictionaries.
    layer_package = librarian("layer_package")

    color = ""
    special1 = ""
    special2 = ""
    special3 = ""

    if len(options) > 0 and isinstance(options, list):
        color = options[0].lower()
    elif options in ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white", "clear"]:
        color = options
    elif options in ["bold", "underline", "reversing"]:
        special1 = options
    if len(options) > 1 and isinstance(options, list):
        special1 = options[1].lower()
    if len(options) > 2 and isinstance(options, list):
        special2 = options[2].lower()
    if len(options) > 3 and isinstance(options, list):
        special3 = options[3].lower()

    # Parses the name, color and specials to the painter. Then the painter returns the paint.
    paint_layer = painter(color, special1, special2, special3)

    # Checks if layer value is a instance of a list.
    if not isinstance(layer, list):
        # Layer value is now equal to layer value inside a list.
        layer = [layer]

    # Loops through all content of layer.
    for content in layer:
        # Adds the branch as key and the paint as value to the package dictionary.
        layer_package[branch].update({content: paint_layer})
