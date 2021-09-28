# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.painter import painter
from br4nch.utility.positioner import build_pos


# Gets the parsed arguments.
def arguments(paint, branch="", pos=""):
    # Parses the arguments to the first task.
    color_layer(branch, paint, pos)


def calculate(branches, branch, paint, pos, match, value=""):
    # Gets the needed lists/dictionaries.
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
                calculate(branches, branch, paint, pos, match, value)
                # Returns nothing and stops the loop.
                return


# Adds the chosen paint to the parsed position.
def color_layer(branch, paint, position):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")

    # Checks if branch is not a instance of list.
    if not isinstance(branch, list):
        # Branch will be equal to a list that contains the value of branch.
        branch = [branch]

    # Checks if pos is not a instance of list.
    if not isinstance(position, list):
        # Pos will be equal to a list that contains the value of pos.
        position = [position]

    # Gets num value based on the length of entries in pos list.
    for num in range(len(position)):
        # Separates the numbers from the dots in current pos value.
        position[num] = position[num].split(".")

    if not branch[0]:
        for value in list(branches):
            branch.append(value)
        branch.pop(0)

    # Loops through all branches in the branch list.
    for branch in branch:
        for y in list(branches):
            if branch.lower() == y.lower():
                branch = y

                # Calls the operator function and gets the returned pos.
                pos = build_pos(branch, position.copy())

                for pos in pos:
                    match = ""
                    # Loops through all values of pos list.
                    for value in pos:
                        # Creates the match variable.
                        for x in value:
                            # Match is equal to current value of match plus the value.
                            match = match + x

                    # Calls the calculate function.
                    calculate(branches, branch, paint, pos, match)
