# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.painter import painter


# Adds the chosen paint to the chosen header to a list.
def color_layer(branch, layer, color, special1="", special2="", special3=""):
    # Gets the needed lists/dictionaries.
    layer_package = librarian("layer_package")

    # Parses the name, color and specials to the painter. Then the painter returns the paint.
    paint_layer = painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

    # Checks if layer value is a instance of a list.
    if isinstance(layer, list):
        for content in layer:
            # Adds the branch as key and the paint as value to the package dictionary.
            layer_package[branch].update({content: paint_layer})
    # If layer value is not a instance of a list.
    else:
        # Adds the branch as key and the paint as value to the package dictionary.
        layer_package[branch].update({layer: paint_layer})
