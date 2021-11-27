# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

import copy as copy_lib

from br4nch.utility.handler import BooleanInstanceError, StringInstanceError, NotExistingBranchError, \
    PositionNotAllowedError
from br4nch.utility.librarian import branches, uids, paint_layer
from br4nch.utility.positioner import format_position
from br4nch.utility.generator import generate_uid


def arguments(branch, copy, pos, paint=False, delete=False):
    """
    - Gets the arguments and parses them to the 'CopyLayer' class.
    """
    CopyLayer(branch, copy, pos, paint, delete)


class CopyLayer:
    def __init__(self, argument_branch, argument_copy, argument_pos, argument_paint, argument_delete):
        """
        - Gets the arguments and parses them to the 'copy_layer' function.
        """
        self.copy_layer(argument_branch, argument_copy, argument_pos, argument_paint, argument_delete)

    def copy_layer(self, argument_branch, argument_copy, argument_pos, argument_paint, argument_delete):
        """
        Lists:
          - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.
          - If the given copy argument is not an instance of a list, then the copy argument will be set as a list.
          - If the given pos argument is not an instance of a list, then the pos argument will be set as a list.

        Errors:
          - If the paint value is not an instance of a boolean, then it raises an 'BooleanInstanceError' error.
          - If the delete value is not an instance of a boolean, then it raises an 'BooleanInstanceError' error.

        Operators:
          - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
            list.

        Argument branch list loop:
          Errors:
            - If the branch value is not an instance of a string, then it raises an 'StringInstanceError' error.
            - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

          Branches list loop:
            Argument copy list loop:
              Argument pos list loop:
                - Calls the function 'task_manager' to perform the necessary tasks for the variable 'argument_copy'.
                - Adds the second value in the returned package to the list 'queue_delete'.
                - Adds the first value in the returned package and calls the function 'task_manager' to perform the
                  necessary tasks for the variable 'argument_pos' and adds the returned dictionary in a list to the list
                  'queue_add'.

            - Loops through the list 'queue_delete' and deletes all given layers from the dictionary 'branches'.
            - Loops through the list 'queue_add' and adds all given layers from the dictionary 'branches'.
        """
        if not isinstance(argument_branch, list):
            argument_branch = [argument_branch]

        if not isinstance(argument_copy, list):
            argument_copy = [argument_copy]

        if not isinstance(argument_pos, list):
            argument_pos = [argument_pos]

        if not isinstance(argument_delete, bool):
            raise BooleanInstanceError("paint", argument_paint)

        if not isinstance(argument_delete, bool):
            raise BooleanInstanceError("delete", argument_delete)

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

                    for loop_copy in format_position(branches_branch, argument_copy.copy()):
                        for loop_pos in format_position(branches_branch, argument_pos.copy()):
                            package = self.task_manager(branches_branch, loop_copy, [], argument_paint,
                                                        branches[branches_branch][list(branches[branches_branch])[0]])

                            if package:
                                queue_delete.append(package[1])

                                queue_add.append([package[0], self.task_manager(branches_branch, [], loop_pos,
                                                                                argument_paint,
                                                                                branches[branches_branch]
                                                                                [list(branches[branches_branch])[0]])])

                    if argument_delete:
                        for delete_value in queue_delete:
                            if delete_value:
                                for layer, value in delete_value.items():
                                    uids[branches_branch].remove(str(layer[-10:]))
                                    paint_layer[branches_branch].pop(layer)

                                    self.delete_layer_additions(branches_branch, value[layer])

                                    del value[layer]

                    for add_value in queue_add:
                        if add_value:
                            self.change_layer_uid(branches_branch, argument_paint, add_value[0])
                            add_value[1].update(add_value[0])

            if error == 0:
                raise NotExistingBranchError(branch)

    def task_manager(self, branch, copy, position, argument_paint, value):
        """
        Errors:
          - If the value of copy is equal to '0', then it raises a 'PositionNotAllowedError' error.

        Value dictionary loop:
          - For each value of the 'value' variable the 'count' variable is added with plus '1'.

          Count variable equal to the first value of 'copy':
            If the length of the 'copy' list is equal to '1':
              - Adds the current layer and aa deepcopy of the 'value' variable to a dictionary and adds the current
                layer and previous value to a dictionary and returns these two values as a package.

            - If the length of the 'copy' list is not equal to '1' and there is a value of the 'value'
              variable, then the first value from the 'argument_move' list will be removed and the 'task_manager'
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

        if copy and copy[0] == "0":
            raise PositionNotAllowedError("copy")

        for layer, value in value.items():
            count = count + 1

            if copy and count == int(copy[0]):
                if len(copy) == 1:
                    return [{layer: copy_lib.deepcopy(value)}, {layer: previous_value}]
                else:
                    if value:
                        copy.pop(0)
                        return self.task_manager(branch, copy, position, argument_paint, value)

            if position and position[0] == "0":
                return branches[branch][list(branches[branch])[0]]

            if position and count == int(position[0]):
                if len(position) == 1:
                    return value
                else:
                    if value:
                        position.pop(0)
                        return self.task_manager(branch, copy, position, argument_paint, value)

    def delete_layer_additions(self, branch, value):
        """
        Value dictionary loop:
          - Checks if the UID of the current value of 'layer' exists in the 'uids' list. If the UID is in the 'uids'
            list, then it will be removed from the list.
          - Checks if the 'layer' value exists in the 'paint_layer' branch list. If the layer is in the 'paint_layer'
            branch list, then the value of the current layer key in the 'paint_layer' dictionary will be removed.
          - If there is a value of the 'value' variable, the 'delete_layer_additions' function will be called again with
            the new value of the 'value' variable as argument.
        """
        for layer, value in value.items():
            if layer[-10:] in uids[branch]:
                uids[branch].remove(str(layer[-10:]))

            if layer in paint_layer[branch]:
                paint_layer[branch].pop(layer)

            if value:
                self.delete_layer_additions(branch, value)

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
            layer with UID is added to the list with the value of an empty list.

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
