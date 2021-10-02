# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.handler import NotExistingBranchError
from br4nch.utility.positioner import build_pos


# Gets the parsed arguments.
def arguments(branch="", pos="", move="", delete=False):
    # Parses the arguments to the first task.
    copy_layer(branch, pos, move, delete)


def calculate(branches, branch, pos, move, delete, value="", string=""):
    # Checks if there is no content in value.
    if not value:
        # Value is equal to the value of all nested layers.
        value = branches[branch][list(branches[branch])[0]]

    # Creates the num variable.
    num = 0

    if pos:
        xyz = pos
    if move:
        xyz = move

    prev_value = value

    # Gets the layer/key and value of the current value variable.
    for layer, value in value.copy().items():
        # Num is equal to current value of num plus one.
        num = num + 1

        if layer != list(prev_value)[0]:
            string = string[:-1]

        string = string + "." + str(num)
        string = string.replace("..", ".")

        if string[0] == ".":
            string = string[1:]

        # Checks if the current value of num is equal to the integer of the first entry in the pos list.
        if num == int(xyz[0]):
            # Checks if length of entries in pos is smaller then 2.
            if len(xyz) < 2:
                if pos:
                    string = string[:-1]
                    test.append({list(prev_value)[num - 1]: value})
                    calculate2(branch, "one", str(string))
                    if delete:
                        del prev_value[layer]

                if move:
                    for x in range(len(test)):
                        value.update({list(test[x])[0]: list(test[x].items())[0][1]})
                    calculate2(branch, "two", str(string))

                    calculate2(branch, "three", str(string))
                    test.clear()
                    abc.clear()
                    xpo.clear()
            # If length of entries in pos is not smaller then 2.
            else:
                if value:
                    # Removes the last entry of pos list.
                    xyz.pop(0)
                    # Calls the calculate function.
                    calculate(branches, branch, pos, move, delete, value, string)
                    # Returns nothing and stops the loop.
                    return


def calculate2(branch, action, string="", value=""):
    # Gets the needed lists/dictionaries.
    paint_package_layer = librarian("paint_package_layer")

    # Checks if there is no content in value.
    if not value:
        # Value is equal to the value of all nested layers.
        value = test[0]

    count = 0

    prev_value = value

    # Gets the layer/key and value of the current value variable.
    for key, value in value.items():
        count = count + 1

        if key != list(prev_value)[0]:
            string = string[:-1]

        string = string + "." + str(count)

        if string[0] == ".":
            string = string[1:]

        string = string.replace("..", ".")

        if action == "one":
            abc.append(string)

        if action == "two":
            xpo.append(string)

        if action == "three":
            for x in range(len(abc)):
                if abc[x] in paint_package_layer[branch]:
                    paint_package_layer[branch].update({xpo[x]: paint_package_layer[branch][abc[x]]})
            return

        if value:
            calculate2(branch, action, string, value)


def copy_layer(branch, position, moved, delete):
    # All global statements.
    global test, abc, xpo
    test = []
    abc = []
    xpo = []

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

    if not isinstance(moved, list):
        moved = [moved]

    # Gets num value based on the length of entries in pos list.
    for num in range(len(moved)):
        # Separates the numbers from the dots in current pos value.
        moved[num] = moved[num].split(".")

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
                position = build_pos(branch, position.copy())

                for pos in position:
                    # Calls the calculate function.
                    calculate(branches, branch, pos.copy(), "", delete)

                for move in moved:
                    # Calls the calculate function.
                    calculate(branches, branch, "", move.copy(), delete)

        if error == 0:
            raise NotExistingBranchError(branch)
