# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.handler import StringInstanceError, InvalidPositionError, NotExistingBranchError, \
    PositionNotAllowedError
from br4nch.utility.librarian import branches, paint_layer
from br4nch.utility.positioner import format_position
from br4nch.utility.generator import generate_uid


def arguments(branch, move, pos, paint=False):
    """
    - Gets the arguments and parses them to the 'MoveLayer' class.
    """
    MoveLayer(branch, move, pos, paint)


class MoveLayer:
    def __init__(self, argument_branch, argument_move, argument_pos, argument_paint):
        """
        - Gets the arguments and parses them to the 'move_layer' function.
        """
        self.move_layer(argument_branch, argument_move, argument_pos, argument_paint)

    def move_layer(self, argument_branch, argument_move, argument_pos, argument_paint):
        """
        Lists:
          - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.
          - If the given move argument is not an instance of a list, then the move argument will be set as a list.

        Errors:
          - If the pos argument is not an instance of a string, then it raises an 'StringInstanceError' error.
          - If the pos argument is not equal to a number and/or operator, then it raises an 'InvalidPositionError'
            error.

        Operators:
          - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
            list.

        Argument branch list loop:
          Errors:
            - If the branch value is not an instance of a string, then it raises an 'StringInstanceError' error.
            - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

          Branches list loop:
            Argument copy list loop:
              - Calls the function 'task_manager' to perform the necessary tasks for the variable 'argument_move'.
              - Adds the second value in the returned package to the list 'queue_delete'.
              - Adds the first value in the returned package and calls the function 'task_manager' to perform the
                necessary tasks for the variable 'argument_pos' and adds the returned dictionary in a list to the list
                'queue_add'.

          - Loops through the list 'queue_delete' and deletes all given layers from the dictionary 'branches'.
          - Loops through the list 'queue_add' and adds all given layers from the dictionary 'branches'.
        """
        if not isinstance(argument_branch, list):
            argument_branch = [argument_branch]

        if not isinstance(argument_move, list):
            argument_move = [argument_move]

        if not isinstance(argument_pos, str):
            raise StringInstanceError("pos", argument_pos)

        for pos in argument_pos.split("."):
            if not pos.isnumeric():
                raise InvalidPositionError(argument_pos, "pos")

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

                    queue_delete = []
                    queue_add = []

                    for position in format_position(branches_branch, argument_move.copy()):
                        package = self.task_manager(branches_branch, position, [], {},
                                                    branches[branches_branch][list(branches[branches_branch])[0]])

                        if package:
                            queue_delete.append(package[1])

                            queue_add.append([package[0], self.task_manager(branches_branch, [], argument_pos.split("."),
                                                                            package[0], branches[branches_branch]
                                                                            [list(branches[branches_branch])[0]])])

                    for delete_value in queue_delete:
                        if delete_value:
                            for layer, value in delete_value.items():
                                del value[layer]

                    for add_value in queue_add:
                        if add_value:
                            self.change_layer_uid(branches_branch, argument_paint, add_value[0])
                            add_value[1].update(add_value[0])

            if error == 0:
                raise NotExistingBranchError(branch)

    def task_manager(self, branch, move, position, copied_layer, value):
        """
        Errors:
          - If the value of position is equal to '0', then it raises a 'PositionNotAllowedError' error.

        Value dictionary loop:
          - For each value of the 'value' variable the 'count' variable is added with plus '1'.

          Count variable equal to the first value of 'move':
            If the length of the 'move' list is equal to '1':
              - Adds the current layer and value to a dictionary and adds the current layer and previous value to a
                dictionary and returns these two values as a package.

            - If the length of the 'move' list is not equal to '1' and there is a value of the 'value'
              variable, then the first value from the 'move' list will be removed and the 'task_manager'
              function will be called again with the new value of the 'value' variable as argument.

          - If the first 'position' element variable is equal to '0', then it returns the whole branch from the
            'branches' dictionary.

          Count variable equal to the first value of 'position':
            If the length of the 'position' list is equal to '1':
              - Returns the current value of the 'value' variable.

            - If the length of the 'position' list is not equal to '1' and there is a value of the 'value' variable,
              then the first value from the 'position' list will be removed and the 'task_manager' function will be
              called again with the new value of the 'value' variable as argument.
        """
        count = 0
        previous_value = value

        if move and move[0] == "0":
            raise PositionNotAllowedError("move")

        for layer, value in value.items():
            count = count + 1

            if move and count == int(move[0]):
                if len(move) == 1:
                    return [{layer: value}, {layer: previous_value}]
                else:
                    if value:
                        move.pop(0)
                        return self.task_manager(branch, move, position, copied_layer, value)

            if position and position[0] == "0":
                return branches[branch][list(branches[branch])[0]]

            if position and count == int(position[0]):
                if len(position) == 1:
                    return value
                else:
                    if value:
                        position.pop(0)
                        return self.task_manager(branch, move, position, copied_layer, value)

    def change_layer_uid(self, branch, argument_paint, value):
        """
        Value dictionary loop:
          - Generates a new UID for the copied 'layer' variable. Then the old layer is deleted and replaced with the new
            generated layer with the new UID.

          - Checks if the current value of 'layer' exists in the branch's 'paint_layer' list. Then it is checked whether
            the variable 'argument_paint' is true. If the value exists in the list and the 'argument_paint' is true,
            then the newly generated layer with UID is added to the list with the value of the value of the variable
            'layer'.
          - If the current value of 'layer' does not exist in the branch's 'paint_layer' list. Then the newly generated
            layer with UID is added to the list with the value of an empty string.

          - If there is a value of the 'value' variable, the 'change_layer_uid' function will be called again with the
            new value of the 'value' variable as argument.
        """
        previous_value = value

        for layer, value in value.copy().items():
            new_layer = layer[:-15] + generate_uid(branch)

            previous_value[new_layer] = previous_value.pop(layer)

            if layer in paint_layer[branch]:
                if argument_paint:
                    paint_layer[branch].update({new_layer: paint_layer[branch][layer]})
            else:
                paint_layer[branch].update({new_layer: []})

            if value:
                self.change_layer_uid(branch, argument_paint, value)
