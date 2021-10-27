# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches, paint_layer
from br4nch.utility.positioner import format_position
from br4nch.utility.handler import NotExistingBranchError, StringInstanceError


def arguments(branch, pos, paint):
    """Gets the arguments and parses them to the 'SetColorLayer' class."""
    SetColorLayer(branch, pos, paint)


class SetColorLayer:
    def __init__(self, argument_branch, argument_pos, argument_paint):
        """Gets the arguments and parses them to the 'build_position' function."""
        self.build_position(argument_branch, argument_pos, argument_paint)

    def build_position(self, argument_branch, argument_pos, argument_paint):
        """
        Lists:
          - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.
          - If the given pos argument is not an instance of a list, then the pos argument will be set as a list.

        Operators:
          - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
            list.

        Argument branch list loop:
          Errors:
            - If the branch value is not an instance of a string, then it raises an 'StringInstanceError' error.
            - If the branch value is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

          Branches list loop:
            - Loops through the obtained values of the current value of the 'position' variable and adds all values of the
              variable to the 'position_structure' variable.
            - Calls the 'color_layer' function with the current value of 'position' and 'position_structure' as arguments.
        """

        if not isinstance(argument_branch, list):
            argument_branch = [argument_branch]

        if not isinstance(argument_pos, list):
            argument_pos = [argument_pos]

        for length in range(len(argument_pos)):
            argument_pos[length] = argument_pos[length].split(".")

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

                    for position in format_position(branch, argument_pos.copy()):
                        position_structure = ""
                        for value in position:
                            for x in value:
                                position_structure = position_structure + "." + x

                        self.set_color_layer(branch, argument_paint, position, position_structure[1:])

            if error == 0:
                raise NotExistingBranchError(branch)

    def set_color_layer(self, branch, paint, position, position_structure, value=""):
        """
        Values:
          - If there is no value in the 'value' variable, then the 'value' variable is equal to the value of the branch
            header key in the 'branches' directory.

        Value dictionary loop:
          - For each value of the 'value' variable the 'count' variable is added with plus '1'.

          Count variable equal to the first value of position:
            - If the length of the 'position' list is equal to '1' then it will add the current branch key in the
              'values' dictionary with the given paint as value to the 'paint_layer' directory.
            - If the length of the 'position' list is not equal to '1' and there is a value of the 'value' variable,
              then the first value from the 'position' list will be removed and the 'add_layer' function will be called
              again with the new values of the 'value' variable as argument.
        """

        if not value:
            value = branches[branch][list(branches[branch])[0]]

        count = 0

        for layer, value in value.items():
            count = count + 1

            if count == int(position[0]):
                if len(position) < 2:
                    paint_layer[branch].update({position_structure: paint})
                else:
                    if value:
                        position.pop(0)
                        self.set_color_layer(branch, paint, position, position_structure, value)
                        return
