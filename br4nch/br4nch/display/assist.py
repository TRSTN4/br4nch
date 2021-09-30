# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.generator import get_uid
from br4nch.add.branch import arguments as add_branch
from br4nch.add.header import arguments as add_header
from br4nch.add.layer import arguments as add_layer
from br4nch.display.branch import display_branch as build_branch
from br4nch.utility.handler import NotExistingBranchError


# Gets the parsed arguments.
def arguments(branch=""):
    # Parses the arguments to the first task.
    assist(branch)


# Calculates the level of all the layers.
def elevator(branch, value, pos=0):
    # Gets the layer/key and value of the current value variable.
    for layer, value in value.items():
        # Appends position to the levels list.
        levels.append(pos)
        # Recalls the current function and adds the current value of position by one.
        elevator(branch, value, pos + 1)


def calculate(branch, branch_assist, value="", string=""):
    # Gets the needed lists/dictionaries.
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

        if len(string) < 2:
            add_layer(branch=branch_assist, layer=string + ": " + key[:-15])
        else:
            add_layer(branch=branch_assist, layer=string + ": " + key[:-15], pos=string[:-2])

        if value:
            calculate(branch, branch_assist, value, string)


def assist(branch):
    # All global statements.
    global levels, trace

    # Gets the needed lists/dictionaries.
    branches = librarian("branches")

    # Checks if branch is not a instance of list.
    if not isinstance(branch, list):
        # Branch will be equal to a list that contains the value of branch.
        branch = [branch]

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
                branch_assist = y + get_uid(branch)

                # Sets the lists.
                levels = [0]
                trace = [0]

                add_branch(branch=branch_assist)
                add_header(branch=branch_assist, header="0: " + list(branches[branch])[0])

                # Loops through all positions in the pos list.
                calculate(branch, branch_assist)

                build_branch(branch_assist, True)

        if error == 0:
            raise NotExistingBranchError(branch)
