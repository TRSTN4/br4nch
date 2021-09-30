# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.positioner import build_pos
from br4nch.utility.generator import get_uid
from br4nch.utility.handler import NotExistingBranchError


# Gets the parsed arguments.
def arguments(layer, branch="", pos=""):
    # Parses the arguments to the first task.
    add_layer(branch, layer, pos)


# Calculates where to add the parsed layer in the given position.
def add_position(branch, layer, pos, branches, value=""):
    # Checks if there is no content in value.
    if not value:
        # Value is equal to the value of all nested layers.
        value = branches[branch][list(branches[branch])[0]]

    # Checks if the first entry in the pos list is equal to zero or the first entry in the pos list doesnt have a value.
    if pos[0] == "0" or not pos[0]:
        # Loops through all layers in layer list.
        for layer in layer:
            # Updates the current value and adds the layer with uid and new dictionary as value.
            branches[branch][list(branches[branch])[0]].update({layer + get_uid(branch): {}})
        return
    # If the first entry in the pos list is not equal to zero or the first entry in the pos list does have a value.
    else:
        # Creates the count variable.
        count = 0

        # Gets the value of the current value variable.
        for value in value.values():
            # Count is equal to current value of count plus one.
            count = count + 1

            # Checks if the current value of count is equal to the int of the first entry in the pos list.
            if count == int(pos[0]):
                # Checks if length of entries in pos is smaller then 2.
                if len(pos) < 2:
                    # Loops through all layers in layer list.
                    for layer in layer:
                        # Updates the current value and adds the layer with uid and new dictionary as value.
                        value.update({layer + get_uid(branch): {}})
                    return
                # If length of entries in pos is not smaller then 2.
                else:
                    if value:
                        # Removes the last entry of pos list.
                        pos.pop(0)
                        # Calls the calculate function.
                        add_position(branch, layer, pos, branches, value)
                        # Returns nothing and stops the loop.
                        return


# Adds a new layer to the branches dictionary.
def add_layer(branch, layer, position):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    paint_package_layer = librarian("paint_package_layer")

    # Checks if branch is not a instance of list.
    if not isinstance(branch, list):
        # Branch will be equal to a list that contains the value of branch.
        branch = [branch]

    # Checks if layer is not a instance of list.
    if not isinstance(layer, list):
        # Layer will be equal to a list that contains the value of layer.
        layer = [layer]

    # Checks if pos is not a instance of list.
    if not isinstance(position, list):
        # Pos will be equal to a list that contains the value of pos.
        position = [position]

    if not branch[0]:
        for value in list(branches):
            branch.append(value)
        branch.pop(0)

    # Loops through all branches in the branch list.
    for branch in branch:
        branch = str(branch)
        error = 0

        # Calls the operator function and gets the returned pos.
        position = build_pos(branch, position)

        for y in list(branches):
            if branch.lower() == y.lower():
                error = error + 1

                branch = y

                # Loops through all positions in the pos list.
                for pos in position:
                    # Calls the calculate_position function.
                    add_position(branch, layer, pos.copy(), branches)

                # Checks if the current branch value is inside the paint package.
                if not paint_package_layer.get(branch):
                    # Adds the current branch value as key and a new dictionary as value to the paint package.
                    paint_package_layer.update({branch: {}})

        if error == 0:
            raise NotExistingBranchError(branch)
