# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches
from br4nch.utility.handler import NotExistingBranchError, InvalidPositionError, StringInstanceError


def arguments(branch, move, pos):
    """
    - Gets the arguments and parses them to the 'MoveLayer' class.
    """
    MoveLayer(branch, move, pos)


class MoveLayer:
    def __init__(self, argument_branch, argument_move, argument_pos):
        """
        - Gets the arguments and parses them to the 'move_layer' function.
        """
        self.move_layer(argument_branch, argument_move, argument_pos)

    def move_layer(self, argument_branch, argument_move, argument_pos):
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
            - The function 'task_manager' is called to perform the necessary tasks for the variable 'argument_move'.
            - Then last value in the package variable returned from the 'task_manager' function is added to the
              'queue_delete' list.
            - Calls the function 'task_manager' to perform the necessary tasks for the variable 'argument_pos'.
            - Loops through the list 'queue_delete' and deletes all given layers from the dictionary 'branches'.
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

                    for loop_move in argument_move:
                        package = self.task_manager(branches_branch, loop_move.split("."), [], {},
                                                    branches[branches_branch][list(branches[branches_branch])[0]])

                        queue_delete.append(package[1])

                        self.task_manager(branches_branch, [], argument_pos.split("."), package[0],
                                          branches[branches_branch][list(branches[branches_branch])[0]])

                    for delete_value in queue_delete:
                        for layer, value in delete_value.items():
                            del value[layer]

            if error == 0:
                raise NotExistingBranchError(branch)

    def task_manager(self, branch, argument_move, position, copied_layer, value):
        """
        Value dictionary loop:
          - For each value of the 'value' variable the 'count' variable is added with plus '1'.

          Count variable equal to the first value of 'argument_move':
            If the length of the 'argument_move' list is equal to '1':
              - Adds the current layer and value to a dictionary and adds the current layer and previous value to a
                dictionary and returns these two values as a package.

            - If the length of the 'argument_move' list is not equal to '1' and there is a value of the 'value'
              variable, then the first value from the 'argument_move' list will be removed and the 'task_manager'
              function will be called again with the new value of the 'value' variable as argument.

          Count variable equal to the first value of 'position':
            If the length of the 'position' list is equal to '1':
              - Adds the value of 'copied_layer' to the current value of 'value' in the 'branches' dictionary.

            - If the length of the 'position' list is not equal to '1' and there is a value of the 'value' variable,
              then the first value from the 'position' list will be removed and the 'task_manager' function will be
              called again with the new value of the 'value' variable as argument.
        """
        count = 0
        previous_value = value

        for layer, value in value.items():
            count = count + 1

            if argument_move and count == int(argument_move[0]):
                if len(argument_move) < 2:
                    return [{layer: value}, {layer: previous_value}]
                else:
                    if value:
                        argument_move.pop(0)
                        return self.task_manager(branch, argument_move, position, copied_layer, value)

            if position and count == int(position[0]):
                if len(position) < 2:
                    value.update(copied_layer)
                else:
                    if value:
                        position.pop(0)
                        return self.task_manager(branch, argument_move, position, copied_layer, value)
