# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.positioner import build_pos
from br4nch.utility.handler import add_layer_error


# Gets the parsed arguments.
def arguments(branch, layer, pos=""):
    # Parses the arguments to the first task.
    add_layer(branch, layer, pos)


# Generates a unique UID.
def get_uid(length=10):
    # Imports the built-in python uuid package.
    import uuid

    # Gets the needed lists/dictionaries.
    uids = librarian("uids")

    # Creates the UID.
    uid = str(uuid.uuid4()).replace("-", "")[0:length]

    # Loops until a unique UID is created.
    while True:
        # Checks if UID in UIDS list.
        if uid in uids:
            # Recalls the function and creates a new UID.
            get_uid(length)
            # Returns nothing.
            return
        # If UID not in UIDS list.
        else:
            # Appends the UID to the UIDS list.
            uids.append(uid)
            # Breaks the loop.
            break
    # Returns the UID.
    return ":uid=" + uid


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
            branches[branch][list(branches[branch])[0]].update({layer + get_uid(): {}})
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
                        value.update({layer + get_uid(): {}})
                # If length of entries in pos is not smaller then 2.
                else:
                    # Removes the last entry of pos list.
                    pos.pop(0)
                    # Calls the calculate function.
                    add_position(branch, layer, pos, branches, value)
                    # Returns nothing and stops the loop.
                    return


# Adds a new layer to the branches dictionary.
def add_layer(branch, layer, pos=""):
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
    if not isinstance(pos, list):
        # Pos will be equal to a list that contains the value of pos.
        pos = [pos]

    # Loops through all branches in the branch list.
    for branch in branch:
        # Checks if the branch exists in the branches dictionary.
        if branch in branches:
            # Calls the operator function and gets the returned pos.
            pos = build_pos(branch, pos)

            # Loops through all positions in the pos list.
            for pos in pos:
                # Calls the calculate_position function.
                add_position(branch, layer, pos, branches)

            # Checks if the current branch value is inside the paint package.
            if not paint_package_layer.get(branch):
                # Adds the current branch value as key and a new dictionary as value to the paint package.
                paint_package_layer.update({branch: {}})

        # If the branch does not exists in the branches dictionary.
        else:
            # Runs a custom error.
            add_layer_error(branch, layer)
