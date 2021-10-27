# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches, paint_layer
from br4nch.utility.handler import NotExistingBranchError
from br4nch.utility.positioner import format_position


def arguments(branch="", move="", pos=""):
    move_layer(branch, move, pos)


def move_layer(argument_branch, argument_move, argument_pos):
    global test, abc, xpo, deel
    test = []
    abc = []
    xpo = []
    deel = []

    if not isinstance(argument_branch, list):
        argument_branch = [argument_branch]

    if not isinstance(argument_move, list):
        argument_move = [argument_move]

    for length in range(len(argument_move)):
        argument_move[length] = argument_move[length].split(".")

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

                for move in argument_pos:
                    calculate(branches_branch, move.copy(), "")

                for pos in format_position(branches_branch, argument_move.copy()):
                    calculate(branches_branch, "", pos.copy())

                for k, v in deel[0].items():
                    print(deel)
                    del v[k]

        if error == 0:
            raise NotExistingBranchError(branch)


def calculate(branch, move, pos, value="", string=""):
    if not value:
        value = branches[branch][list(branches[branch])[0]]

    num = 0

    if move:
        xyz = move
    if pos:
        xyz = pos

    prev_value = value

    for layer, value in value.copy().items():
        num = num + 1

        if layer != list(prev_value)[0]:
            string = string[:-1]

        string = string + "." + str(num)
        string = string.replace("..", ".")

        if string[0] == ".":
            string = string[1:]

        if num == int(xyz[0]):
            if len(xyz) < 2:
                if move:
                    for x in range(len(test)):
                        value.update({list(test[x])[0]: list(test[x].items())[0][1]})
                    xpo.append(string)
                    calculate2(branch, "two", str(string))

                    calculate2(branch, "three", str(string))
                    test.clear()
                    abc.clear()
                    xpo.clear()
                if pos:
                    string = string[:-1]
                    deel.append({layer: prev_value})
                    test.append({list(prev_value)[num - 1]: value})
                    abc.append(string)
                    calculate2(branch, "one", str(string))

            else:
                if value:
                    xyz.pop(0)
                    calculate(branch, move, pos, value, string)
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
                    paint_layer[branch][xpo[x]] = paint_layer[branch].pop(abc[x])
            return

        if value:
            calculate2(branch, action, string, value)


