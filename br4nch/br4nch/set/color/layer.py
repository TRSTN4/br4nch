# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.painter import painter


# Adds the chosen paint to the parsed layer.
def color_layer(branch, options, layer):
    # Gets the needed lists/dictionaries.
    paint_package_layer = librarian("paint_package_layer")

    # Parses the paint options arguments to the painter and the painter returns the paint.
    paint_layer = painter(options, branch, layer)

    # Checks if layer value is a instance of a list.
    if not isinstance(layer, list):
        # Layer value is equal to the layer value inside a list.
        layer = [layer]

    # Loops through all content of the parsed layer value.
    for content in layer:
        # Adds the branch as key and the paint as value to the paint package.
        paint_package_layer[branch].update({content: paint_layer})
