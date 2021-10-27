# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

# Imports all files.
from br4nch.utility.librarian import branches, paint_layer
from br4nch.utility.handler import NotExistingBranchError
from br4nch.utility.positioner import format_position


def arguments(branch, copy, pos, delete=False):
    copy_layer(branch, copy, pos, delete)


def copy_layer(argument_branch, argument_copy, argument_pos, argument_delete):
    global test, abc, xpo
    test = []
    abc = []
    xpo = []

    if not isinstance(argument_branch, list):
        argument_branch = [argument_branch]

    if not isinstance(argument_copy, list):
        argument_copy = [argument_copy]

    for length in range(len(argument_copy)):
        argument_copy[length] = argument_copy[length].split(".")

    if not isinstance(argument_pos, list):
        argument_pos = [argument_pos]

    for num in range(len(argument_pos)):
        argument_pos[num] = argument_pos[num].split(".")

    if not argument_branch[0]:
        for value in list(branches):
            argument_branch.append(value)
        argument_branch.pop(0)

    for branch in argument_branch:
        error = 0

        for branches_branch in list(branches):
            if branch.lower() == branches_branch.lower():
                error = error + 1

                for copy in format_position(branches_branch, argument_copy.copy()):
                    calculate(branches_branch, copy.copy(), "", argument_delete)

                for position in argument_pos:
                    calculate(branches_branch, "", position.copy(), argument_delete)

        if error == 0:
            raise NotExistingBranchError(branch)


def calculate(branch, copy, pos, delete, value="", string=""):

    if copy:
        xyz = copy
    if pos:
        xyz = pos

    if not value:
        value = branches[branch][list(branches[branch])[0]]

    count = 0
    prev_value = value

    for layer, value in value.copy().items():
        count = count + 1

        if layer != list(prev_value)[0]:
            string = string[:-1]

        string = string + "." + str(count)
        string = string.replace("..", ".")

        if count == int(xyz[0]):
            if len(xyz) < 2:
                if copy:
                    string = string[:-1]
                    test.append({list(prev_value)[count - 1]: value})
                    calculate2(branch, "one", string[0:])
                    if delete:
                        del prev_value[layer]

                if pos:
                    for x in range(len(test)):
                        value.update({list(test[x])[0]: list(test[x].items())[0][1]})

                    calculate2(branch, "two", string[0:])
                    calculate2(branch, "three", string[0:])

                    test.clear()
                    abc.clear()
                    xpo.clear()
            else:
                if value:
                    xyz.pop(0)
                    calculate(branch, copy, pos, delete, value, string)
                    return


def calculate2(branch, action, string="", value=""):
    if not value:
        value = test[0]

    count = 0

    prev_value = value
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
                if abc[x] in paint_layer[branch]:
                    paint_layer[branch].update({xpo[x]: paint_layer[branch][abc[x]]})
            return

        if value:
            calculate2(branch, action, string, value)
