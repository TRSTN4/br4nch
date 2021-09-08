# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.painter import painter


# Unpacks the paint packages for the branch.
def unpack_paint_builder(branch, paint_package, layer=""):
    # Action is equal to branch.
    action = branch

    # Checks if layer has content.
    if layer:
        # Action is equal to layer.
        action = layer
        # The paint package is equal to the paint package with the given branch as key.
        paint_package = paint_package[branch]

    # Checks if content in paint package.
    if paint_package:
        # Loops through all paint inside the paint package.
        for key, paint in paint_package.items():
            # Checks if the key is equal to the value of action.
            if key == action:
                # Returns the paint.
                return paint


# Unpacks and calculates the paint clear value.
def unpack_paint_clear(branch):
    # Gets the needed lists/dictionaries.
    paint_package_branch = librarian("paint_package_branch")
    paint_package_header = librarian("paint_package_header")
    paint_package_layer = librarian("paint_package_layer")

    # Stores all the paint packages in a list.
    paint_packages = [paint_package_branch, paint_package_header, paint_package_layer]

    # Loops through all paint packages from the list.
    for paint_package in paint_packages:
        # Checks if content in paint package.
        if paint_package:
            # Get the clear paint value.
            paint_clear = painter("clear", branch)
        # If content not in paint package.
        else:
            # Paint is equal to empty string.
            paint_clear = ""

        # Returns the paint.
        return paint_clear
