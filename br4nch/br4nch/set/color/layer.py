# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.painter import painter


# Gets the parsed arguments.
def arguments(branch, paint, pos=""):
    # Parses the arguments to the first task.
    color_layer(branch, paint, pos)


def calculate(branch, paint, pos, match, value=""):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    paint_package_layer = librarian("paint_package_layer")

    # Checks if there is no content in value.
    if not value:
        # Value is equal to the value of all nested layers.
        value = branches[branch][list(branches[branch])[0]]

    # Creates the num variable.
    num = 0

    # Gets the layer/key and value of the current value variable.
    for layer, value in value.items():
        # Num is equal to current value of num plus one.
        num = num + 1

        # Checks if the current value of num is equal to the integer of the first entry in the pos list.
        if num == int(pos[0]):
            # Checks if length of entries in pos is smaller then 2.
            if len(pos) < 2:
                # Adds the current value of pos and the requested paint to the current branch paint package.
                paint_package_layer[branch].update({match: painter(paint, branch, layer)})
            # If length of entries in pos is not smaller then 2.
            else:
                # Removes the first entry of pos list.
                pos.pop(0)
                # Calls the calculate function.
                calculate(branch, paint, pos, match, value)
                # Returns nothing and stops the loop.
                return


# Adds the chosen paint to the parsed position.
def color_layer(branch, paint, pos):
    # Checks if branch is not a instance of list.
    if not isinstance(branch, list):
        # Branch will be equal to a list that contains the value of branch.
        branch = [branch]

    # Checks if pos is not a instance of list.
    if not isinstance(pos, list):
        # Pos will be equal to a list that contains the value of pos.
        pos = [pos]

    # Gets num value based on the length of entries in pos list.
    for num in range(len(pos)):
        # Separates the numbers from the dots in current pos value.
        pos[num] = pos[num].split(".")

    # Saves the current pos value.
    saved_pos = pos.copy()

    # Loops through all branches in the branch list.
    for branch in branch:
        # Reverts to original saved pos value for each loop.
        pos = saved_pos
        # Loops through all positions in the pos list.
        for pos in pos:
            # Creates the match variable.
            match = ""
            # Loops through all values of pos list.
            for value in pos:
                # Match is equal to current value of match plus the value.
                match = match + value
            # Calls the calculate function.
            calculate(branch, paint, pos, match)
