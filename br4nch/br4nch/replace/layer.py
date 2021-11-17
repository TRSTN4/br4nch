# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches, uids, paint_layer
from br4nch.utility.positioner import format_position
from br4nch.utility.generator import generate_uid
from br4nch.utility.handler import NotExistingBranchError, StringInstanceError


def arguments(branch, pos, name):
    """Gets the arguments and parses them to the 'ReplaceLayer' class."""
    ReplaceLayer(branch, pos, name)


class ReplaceLayer:
    def __init__(self, argument_branch, argument_pos, argument_name):
        """Gets the arguments and parses them to the 'replace_layer' function."""
        self.replace_layer(argument_branch, argument_pos, argument_name)

    def replace_layer(self, argument_branch, argument_pos, argument_name):
        """
        Lists:
          - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.
          - If the given pos argument is not an instance of a list, then the pos argument will be set as a list.

        Errors:
          - If the name argument is not an instance of a string, then it raises an 'StringInstanceError' error.

        Operators:
          - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
            list.

        Branches list loop:
          Errors:
            - If the branch value is not an instance of a string, then it raises an 'StringInstanceError' error.
            - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

          Argument copy list loop:
            - Calls the function 'task_manager' to perform the necessary tasks for the variable 'argument_copy' and
              stores the returned output in the 'queue_replace' list.

            - Loops through the list 'queue_replace' and replaces all given layers from the mandatory dictionaries.
        """
        if not isinstance(argument_branch, list):
            argument_branch = [argument_branch]

        if not isinstance(argument_pos, list):
            argument_pos = [argument_pos]

        if not isinstance(argument_name, str):
            raise StringInstanceError("name", argument_name)

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

                    queue_replace = []

                    for position in format_position(branches_branch, argument_pos.copy()):
                        queue_replace.append(self.get_layers(branches_branch, position,
                                                             branches[branches_branch][list(branches[branches_branch])[0]]))

                    for replace_value in queue_replace:
                        for layer, value in replace_value.items():
                            new_layer = argument_name + generate_uid(branches_branch)

                            uids[branches_branch].remove(layer[-10:])
                            paint_layer[branches_branch][new_layer] = paint_layer[branches_branch].pop(layer)

                            index = list(value).index(layer)
                            value[new_layer] = value.pop(layer)

                            for position in list(value)[index:-1]:
                                value[position] = value.pop(position)
                                paint_layer[branches_branch][position] = paint_layer[branches_branch].pop(position)

            if error == 0:
                raise NotExistingBranchError(branch)

    def get_layers(self, branch, position, value):
        """
        Value dictionary loop:
          - For each value of the 'value' variable the 'count' variable is added with plus '1'.

          Count variable equal to the first value of 'position':
            If the length of the 'position' list is equal to '1':
              - Returns the current layer and previous value in an dictionary.

            - If the length of the 'position' list is not equal to '1' and there is a value of the 'value' variable,
              then the first value from the 'argument_move' list will be removed and the 'task_manager' function will be
              called again with the new value of the 'value' variable as argument.
        """
        count = 0
        previous_value = value

        for layer, value in value.items():
            count = count + 1

            if count == int(position[0]):
                if len(position) < 2:
                    return {layer: previous_value}
                else:
                    if value:
                        position.pop(0)
                        return self.get_layers(branch, position, value)
