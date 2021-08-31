# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.painter import painter


# Adds the chosen paint to the chosen header to a list.
def color_layer(branch, options, layer):
    # Gets the needed lists/dictionaries.
    layer_package = librarian("layer_package")

    # Parses the paint options arguments to the painter. Then the painter returns the paint.
    paint_layer = painter(options)

    # Checks if layer value is a instance of a list.
    if not isinstance(layer, list):
        # Layer value is now equal to layer value inside a list.
        layer = [layer]

    # Loops through all content of layer.
    for content in layer:
        # Adds the branch as key and the paint as value to the package dictionary.
        layer_package[branch].update({content: paint_layer})
