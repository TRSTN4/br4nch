# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches, paint_layer
from br4nch.utility.positioner import format_position
from br4nch.utility.handler import NotExistingBranchError, StringInstanceError


def arguments(branch, move, pos):
    """Gets the arguments and parses them to the 'MoveLayer' class."""
    MoveLayer(branch, move, pos)


class MoveLayer:
    def __init__(self, argument_branch, argument_move, argument_pos):
        """Gets the arguments and parses them to the 'build_structure' function."""
        self.build_structure(argument_branch, argument_move, argument_pos)

    def build_structure(self, argument_branch, argument_move, argument_pos):
        if not isinstance(argument_branch, list):
            argument_branch = [argument_branch]

        if not isinstance(argument_move, list):
            argument_move = [argument_move]

        if not isinstance(argument_pos, str):
            raise StringInstanceError("pos", argument_pos)

        if "*" in argument_branch:
            argument_branch.clear()
            for branches_branch in list(branches):
                argument_branch.append(branches_branch)

        for branch in argument_branch:
            error = 0

            if not isinstance(branch, str):
                raise StringInstanceError("branch", branch)

            for branches_branch in list(branches):
                if branch.lower() == branches_branch.lower():
                    error = error + 1

                    for loop_move in argument_move:
                        if not isinstance(loop_move, str):
                            raise StringInstanceError("move", loop_move)

                        move_extend = ""
                        for pos in loop_move.split("."):
                            move_extend = move_extend + "." + pos

                        package = self.task_manager(branches_branch, loop_move.split("."), move_extend[1:], [], "", {},
                                                    [], branches[branches_branch][list(branches[branches_branch])[0]])

                        self.task_manager(branches_branch, [], "", format_position(branches_branch, [argument_pos])[0],
                                          argument_pos, package[0].copy(), package[1].copy(),
                                          branches[branches_branch][list(branches[branches_branch])[0]])

            if error == 0:
                raise NotExistingBranchError(branch)

    def task_manager(self, branch, argument_move, move_extend, position, position_extend, copied_layer,
                     copied_positions, value, string=""):
        count = 0
        previous_value = value

        for layer, value in value.copy().items():
            count = count + 1

            if layer != list(previous_value)[0]:
                string = string[:-1]

            string = string + "." + str(count)
            string = string.replace("..", ".")

            if argument_move and count == int(argument_move[0]):
                if argument_move and len(argument_move) < 2:
                    if argument_move:
                        previous_value.pop(layer)
                        return [{layer: value}, self.copy_positions(branch, value, move_extend, [move_extend])]
                else:
                    if value:
                        argument_move.pop(0)
                        return self.task_manager(branch, argument_move, move_extend, position, position_extend,
                                                 copied_layer, copied_positions, value, string)

            if position and count == int(position[0]):
                if position and len(position) < 2:
                    if position:
                        value.update(copied_layer)
                        self.set_paint(branch, value, position_extend, copied_positions.copy())
                else:
                    if value:
                        position.pop(0)
                        return self.task_manager(branch, argument_move, move_extend, position, position_extend,
                                                 copied_layer, copied_positions, value, string)

    def copy_positions(self, branch, value, extend, copied_positions, string=""):
        count = 0
        previous_value = value

        for layer, value in value.items():
            count = count + 1

            if layer != list(previous_value)[0]:
                string = string[:-1]

            string = string + "." + str(count)
            string = string.replace("..", ".")

            copied_positions.append(extend + string)

            if value:
                self.copy_positions(branch, value, extend, copied_positions, string)

        return copied_positions

    def set_paint(self, branch, value, extend, copied_positions, string=""):
        count = 0
        previous_value = value

        for layer, value in value.items():
            count = count + 1

            if layer != list(previous_value)[0]:
                string = string[:-1]

            string = string + "." + str(count)
            string = string.replace("..", ".")

            print(extend + string, copied_positions)
            paint_layer[branch].update({extend + string: paint_layer[branch][copied_positions[0]]})
            copied_positions.pop(0)

            if value:
                self.set_paint(branch, value, extend, copied_positions, string)
