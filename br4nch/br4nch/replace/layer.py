# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import branches, uids
from br4nch.utility.positioner import format_position
from br4nch.utility.generator import generate_uid
from br4nch.utility.handler import NotExistingBranchError


# Gets the parsed arguments.
def arguments(branch="", name="", pos=""):
    # Parses the arguments to the first task.
    add_layer(branch, name, pos)


# Calculates where to add the parsed layer in the given position.
def replace_position(branch, pos, value=""):
    # Checks if there is no content in value.
    if not value:
        # Value is equal to the value of all nested layers.
        value = branches[branch][list(branches[branch])[0]]

    # Checks if the first entry in the pos list is equal to zero or the first entry in the pos list doesnt have a value.
    if pos[0] == "0" or not pos[0]:
        # Loops through all layers in layer list.
        for lay in branches[branch][list(branches[branch])[0]].copy():
            test.update({lay: value})
        return
    else:
        # Creates the count variable.
        count = 0

        prev_value = value

        # Gets the value of the current value variable.
        for value in value.values():
            # Count is equal to current value of count plus one.
            count = count + 1

            # Checks if the current value of count is equal to the int of the first entry in the pos list.
            if count == int(pos[0]):
                # Checks if length of entries in pos is smaller then 2.
                if len(pos) < 2:
                    num = 0
                    # Loops through all layers in layer list.
                    for lay in list(prev_value):
                        num = num + 1
                        if num == int(pos[0]):
                            test.update({lay: prev_value})
                            return

                # If length of entries in pos is not smaller then 2.
                else:
                    # Removes the last entry of pos list.
                    pos.pop(0)
                    # Calls the calculate function.
                    replace_position(branch, pos, value)
                    # Returns nothing and stops the loop.
                    return


def add_layer(branch, name, position):
    global test
    test = {}

    # Checks if branch is not a instance of list.
    if not isinstance(branch, list):
        # Branch will be equal to a list that contains the value of branch.
        branch = [branch]

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
        for y in list(branches):
            if branch.lower() == y.lower():
                error = error + 1

                branch = y

                # Calls the operator function and gets the returned pos.
                position = format_position(branch, position)
                # Loops through all positions in the pos list.
                for pos in position:
                    # Calls the calculate_position function.
                    replace_position(branch, pos.copy())

                for key, value in test.items():
                    uids[branch].remove(key[-10:])
                    index = list(value).index(key)
                    value[name + generate_uid(branch)] = value.pop(key)

                    for x in list(value)[index:-1]:
                        value[x] = value.pop(x)

                test.clear()

        if error == 0:
            raise NotExistingBranchError(branch)
