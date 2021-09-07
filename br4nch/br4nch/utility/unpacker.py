# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.painter import painter


def unpack_paint_builder(branch, paint_package, layer=""):
    # Checks if content in paint.
    if paint_package[branch]:
        if layer:
            # Loops through all given packages inside the layer paint dictionary.
            for key, value in paint_package[branch].items():
                # Checks if the key is equal to the value of layer.
                if key == layer:
                    # Paint is equal to the value of key.
                    return value
        else:
            # Loops through all given packages inside the layer paint dictionary.
            for key, value in paint_package.items():
                if key == branch:
                    # Paint is equal to the value of key.
                    return value


def unpack_paint_clear(branch):
    # Gets the needed lists/dictionaries.
    paint_package_branch = librarian("paint_package_branch")
    paint_package_header = librarian("paint_package_header")
    paint_package_layer = librarian("paint_package_layer")

    # Stores all packages in a list.
    paint = [paint_package_branch, paint_package_header, paint_package_layer]

    # Loops through all paint.
    for paint in paint:
        # Checks if content in paint.
        if paint:
            # Resets the paint.
            paint_clear = painter("clear", branch)
        # If content not in paint.
        else:
            # Sets the paint to nothing.
            paint_clear = ""

        # Returns the value.
        return paint_clear
