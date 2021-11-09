# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches, paint_layer
from br4nch.utility.handler import NotExistingBranchError
from br4nch.utility.positioner import format_position


def arguments(branch, copy, pos):
    build_position_structure(branch, copy, pos)


def build_position_structure(argument_branch, argument_copy, argument_pos):
    if not isinstance(argument_branch, list):
        argument_branch = [argument_branch]

    if not isinstance(argument_copy, list):
        argument_copy = [argument_copy]

    if not isinstance(argument_pos, list):
        argument_pos = [argument_pos]

    for length in range(len(argument_copy)):
        argument_copy[length] = argument_copy[length].split(".")

    for length in range(len(argument_pos)):
        argument_pos[length] = argument_pos[length].split(".")

    if "*" in argument_branch:
        argument_branch.clear()
        for branches_branch in list(branches):
            argument_branch.append(branches_branch)

    for branch in argument_branch:
        error = 0

        for branches_branch in list(branches):
            if branch.lower() == branches_branch.lower():
                error = error + 1

                for copy_loop in format_position(branches_branch, argument_copy.copy()):
                    package = copy_layer(branches_branch, copy_loop.copy(), [], [], [],
                                         branches[branch][list(branches[branch])[0]])

                for position_loop in argument_pos:
                    copy_layer(branches_branch, [], position_loop.copy(), package[0], package[1],
                               branches[branch][list(branches[branch])[0]])

        if error == 0:
            raise NotExistingBranchError(branch)


def copy_layer(branch, copy, position, copied_layers, copied_positions, value, string=""):
    count = 0
    prev_value = value

    for layer, value in value.copy().items():
        count = count + 1

        if layer != list(prev_value)[0]:
            string = string[:-1]

        string = string + "." + str(count)
        string = string.replace("..", ".")

        if copy and count == int(copy[0]) or position and count == int(position[0]):
            if copy and len(copy) < 2 or position and len(position) < 2:
                if copy:
                    copied_layers.append({list(prev_value)[count - 1]: value})
                    package = set_layer_paint(branch, "one", [], string[1:], copied_layers[0], [], copy)
                    return [copied_layers, package[0]]

                if position:
                    for length in range(len(copied_layers)):
                        value.update({list(copied_layers[length])[0]: list(copied_layers[length].items())[0][1]})

                    package = set_layer_paint(branch, "two", [], string[0:], copied_layers[0], [], [])
                    set_layer_paint(branch, "three", package[1], string[0:], copied_layers[0], copied_positions, [])

                    copied_layers.clear()
            else:
                if value:
                    if copy:
                        copy.pop(0)
                    if position:
                        position.pop(0)

                    package = copy_layer(branch, copy, position, copied_layers, copied_positions, value, string)
                    return package


def set_layer_paint(branch, action, positions, string, value, copied_positions, copy):
    count = 0
    prev_value = value

    for key, value in value.items():
        count = count + 1

        if key != list(prev_value)[0]:
            string = string[:-1]

        string = string + "." + str(count)
        string = string.replace("..", ".")

        if action == "one":
            copied_positions.append(string)

        if action == "two":
            print(copy)
            if len(copy) < 2:
                positions.append(string[1:])

            if value:
                copy.pop(0)
                set_layer_paint(branch, action, positions, string, value, copied_positions, copy)
                return [copied_positions, positions]

        if action == "three":
            print(copied_positions, positions)
            for x in copied_positions:
                paint_layer[branch].update({positions[0]: paint_layer[branch][x]})
                positions.pop(0)
            return

        if value:
            set_layer_paint(branch, action, positions, string, value, copied_positions, [])
            return [copied_positions, positions]
