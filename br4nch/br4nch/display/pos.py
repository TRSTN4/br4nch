# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.printer import printer
from br4nch.utility.positioner import build_pos
from br4nch.utility.handler import NotExistingBranchError


# Gets the parsed arguments.
def arguments(branch="", layer="", pos=""):
    # Parses the arguments to the first task.
    get_pos(branch, layer, pos)


# Calculates the level of all the layers.
def elevator(branch, value, pos=0):
    # Gets the layer/key and value of the current value variable.
    for layer, value in value.items():
        # Appends position to the levels list.
        levels.append(pos)
        # Recalls the current function and adds the current value of position by one.
        elevator(branch, value, pos + 1)


def calculate(branch, layer="", pos="", action="", value="", string=""):
    # Gets the needed lists/dictionaries.
    positions = librarian("positions")
    branches = librarian("branches")

    # Checks if there is no content in value.
    if not value:
        # Value is equal to the value of all nested layers.
        value = branches[branch][list(branches[branch])[0]]

    # Checks if the length of levels is equal to one.
    if len(levels) == 1:
        # Calls the elevator function to calculate all the positions of all the layers.
        elevator(branch, value)
        # Appends zero to the end of the levels list to prevent index error.
        levels.append(0)

    count = 0

    # Gets the layer/key and value of the current value variable.
    for key, value in value.items():
        trace[0] = trace[0] + 1

        count = count + 1

        if levels[trace[0]] == levels[trace[0] - 1]:
            string = string[:-2]

        if levels[trace[0]] < levels[trace[0] - 1]:
            string = string[:-2]

        string = string + "." + str(count)

        if string[0] == ".":
            string = string[1:]

        if action == "all":
            positions.update({key: {branch: string}})

        if pos and action == "pos":
            if pos == string:
                positions.update({key: {branch: string}})

        if layer and action == "layer":
            if layer.lower() == key.lower()[:-15]:
                positions.update({key: {branch: string}})

        if value:
            calculate(branch, layer, pos, action, value, string)


def get_pos(branch, layer, position):
    # All global statements.
    global levels, trace

    # Gets the needed lists/dictionaries.
    branches = librarian("branches")

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
        for y in list(branches):
            if branch.lower() == y.lower():
                error = error + 1

                branch = y

                if not position[0] and not layer[0]:
                    # Sets the lists.
                    levels = [0]
                    trace = [0]

                    calculate(branch, layer, position, "all")
                else:
                    # Calls the operator function and gets the returned pos.
                    pos = build_pos(branch, position.copy())

                    for pos in pos:
                        # Sets the lists.
                        levels = [0]
                        trace = [0]

                        match = ""

                        # Loops through all values of pos list.
                        for value in pos:
                            # Creates the match variable.
                            for x in value:
                                # Match is equal to current value of match plus the value.
                                match = match + "." + x
                                if match[0] == ".":
                                    match = match[1:]

                        # Loops through all positions in the pos list.
                        calculate(branch, layer, match, "pos")

                    for lay in layer:
                        # Sets the lists.
                        levels = [0]
                        trace = [0]

                        # Loops through all positions in the pos list.
                        calculate(branch, lay, position, "layer")

                    # Prints the founded position(s)/layer(s).
                    printer("display_found", [branch])

        if error == 0:
            raise NotExistingBranchError(branch)
