# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches
from br4nch.utility.printer import printer
from br4nch.utility.handler import NotExistingBranchError, StringInstanceError, BooleanInstanceError


def arguments(branch, layer, beautify=True):
    """Gets the arguments and parses them to the 'DisplayPos' class."""
    DisplayPos(branch, layer, beautify)


class DisplayPos:
    def __init__(self, argument_branch, argument_layer, argument_beautify):
        """Gets the arguments and parses them to the 'display_pos' function."""
        self.display_pos(argument_branch, argument_layer, argument_beautify)

    def display_pos(self, argument_branch, argument_layer, argument_beautify):
        """
        Lists:
          - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.
          - If the given pos argument is not an instance of a list, then the branch argument will be set as a list.

        Errors:
          - If the branch value is not an instance of a boolean, then it raises an 'BooleanInstanceError' error.

        Operators:
          - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
            list.

        Argument branch list loop:
          Errors:
            - If the branch value is not an instance of a string, then it raises an 'StringInstanceError' error.
            - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

          Branches list loop:
            - If the branch is in the 'branches' dictionary, it will loop with all positions in the returned list of the
              'format_position' function. And calls the 'add_layer' function for each loop with the built position
              structure of the 'position' as argument
        """
        if not isinstance(argument_branch, list):
            argument_branch = [argument_branch]

        if not isinstance(argument_layer, list):
            argument_layer = [argument_layer]

        if not isinstance(argument_beautify, bool):
            raise BooleanInstanceError("beautify", argument_beautify)

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

                    for layer in argument_layer:
                        self.calculate(branches_branch, layer, argument_beautify, [0], [0],
                                       branches[branch][list(branches[branch])[0]])

            if error == 0:
                raise NotExistingBranchError(branch)

    def calculate(self, branch, loop_layer, argument_beautify, levels, trace, value, position_structure=""):
        """
        - First, it is checked whether the 'levels' list is "empty". If the list is "empty", the 'elevator' function is
          called with the 'levels' and 'trace' list as arguments.

        Value dictionary loop:
          - For each value of the 'value' variable the 'count' variable and the first element of the 'trace' list is
            added with plus '1'.

          Position structure:
            - Then it is checked whether the "level"/"height" of the current value of the loop is equal to or smaller
              than the previous "level"/"height" value of the loop. If the instantaneous value is equal or less, the
              last position and dot in the 'position_structure' variable is removed.
            - Then the current value of the 'position_structure' variable is added with the value of 'count' separated
              by a dot to the 'position_structure' variable.
            - Then it is checked whether the current value of 'position' is equal to the value of 'position_structure'.
              If the values are equal, then the 'printer' function is called and a package is supplied with all the
              values in it that are needed. If the 'argument_beautify' variable is false, the given positions are not
              represented with a branch structure.

          - Checks whether the 'value' variable has a value. If there is a value, then the 'update_layer' function is
            called again with the current values of 'value', 'trace' and 'levels' as arguments.
        """
        if len(levels) == 1:
            levels = self.elevator(branch, levels, trace, value)

        count = 0

        for layer, value in value.items():
            count = count + 1

            trace[0] = trace[0] + 1

            if levels[trace[0]] <= levels[trace[0] - 1]:
                position_structure = position_structure[:-2]

            position_structure = position_structure + "." + str(count)

            if layer[:-15] == loop_layer:
                printer("display_layer", [branch, layer[:-15], position_structure[1:], argument_beautify])
                return

            if value:
                self.calculate(branch, loop_layer, argument_beautify, levels, trace, value, position_structure)

    def elevator(self, branch, levels, trace, value, pos=0):
        """
        Value dictionary loop:
          - Loops through each "height" of the value dictionary and adds the value of the 'pos' variable to the 'levels'
            list.
          - Then the 'elevator' function is called again with the current value of the 'value' dictionary.

        - Then a '0' is added to the 'levels' list so that the 'IndexError' error can be avoided and after that the new
          value from the 'levels' list is returned.
        """
        for layer, value in value.items():
            levels.append(pos)

            self.elevator(branch, levels, trace, value, pos + 1)

        levels.append(0)

        return levels
