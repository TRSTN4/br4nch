# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import paint_branch, paint_header, paint_layer
from br4nch.utility.painter import painter


# Unpacks the paint packages for the branch.
def unpack_paint_builder(branch, paint, pos=""):
    # Action is equal to branch.
    action = branch

    # Checks if pos has value.
    if pos:
        # Action is equal to pos.
        action = pos
        # The paint package is equal to the paint package with the given branch as key.
        paint = paint[branch]

    # Checks if content in paint package.
    if paint:
        # Loops through all paint inside the paint package.
        for key, p in paint.items():
            # Checks if the key is equal to the value of action.
            if key == action:
                # Returns the paint.
                return p


# Unpacks and calculates the paint clear value.
def unpack_paint_clear(branch):
    # Stores all the paint packages in a list.
    paint_packages = [paint_branch, paint_header, paint_layer]

    # Loops through all paint packages from the list.
    for p in paint_packages:
        # Checks if content in paint package.
        if p:
            # Get the clear paint value.
            paint_clear = painter("clear", branch)
        # If content not in paint package.
        else:
            # Paint is equal to empty string.
            paint_clear = ""

        # Returns the paint.
        return paint_clear
