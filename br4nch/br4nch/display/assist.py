# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

import copy

from br4nch.utility.librarian import branches, output, uids, sizes, symbols, paint_branch, paint_header, paint_layer
from br4nch.utility.generator import generate_uid
from br4nch.display.branch import display_branch as build_branch
from br4nch.utility.handler import NotExistingBranchError, StringInstanceError


def arguments(branch):
    """Gets the arguments and parses them to the 'DisplayAssist' class."""
    DisplayAssist(branch)


class DisplayAssist:
    def __init__(self, argument_branch):
        """Gets the arguments and parses them to the 'display_assist' function."""
        self.display_assist(argument_branch)

    def display_assist(self, argument_branch):
        """
        Lists:
          - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.

        Operators:
          - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
            list.

        Argument branch list loop:
          Errors:
            - If the branch value is not an instance of a string, then it raises an 'StringInstanceError' error.
            - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

          Branches list loop:
            - If the branch is in the 'branches' dictionary, then a new name is generated for the value of the
              'branches_branch' variable. If the name already exists in the 'branches' dictionary, the loop starts again
              until a unique branch name is generated that does not yet exist in the 'branches' dictionary.
            - It then creates a deep copy of the current value of the 'branches_branch' value of the 'branches'
              directory and it is added as value to the 'branches' dictionary with the unique branch name as the key.
            - Then the unique branch name is added to the corresponding dictionaries with the default values as the
              value.
        """
        if not isinstance(argument_branch, list):
            argument_branch = [argument_branch]

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

                    while True:
                        branch_uid = branches_branch + generate_uid(branch)

                        if branch_uid in list(branches):
                            continue
                        else:
                            break

                    branches.update({branch_uid: copy.deepcopy(branches[branches_branch])})

                    header = str("0: " + list(branches[branch_uid])[0])
                    branches[branch_uid][header] = branches[branch_uid].pop(list(branches[branch_uid])[0])
                    output.update({branch_uid: []})
                    uids.update({branch_uid: []})
                    sizes.update({branch_uid: 1})
                    symbols.update({branch_uid: {"line": "┃", "split": "┣━━", "end": "┗━━"}})
                    paint_branch.update({branch_uid: {}})
                    paint_header.update({branch_uid: {}})
                    paint_layer.update({branch_uid: {}})

                    self.update_layer(branch_uid, [0], [0], branches[branch_uid][list(branches[branch_uid])[0]])

                    build_branch(branch_uid, True)

            if error == 0:
                raise NotExistingBranchError(branch)

    def update_layer(self, branch, levels, trace, value, position_structure=""):
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

          - Checks whether the 'value' variable has a value. If there is a value, then the 'update_layer' function is
            called again with the current values of 'value', 'trace' and 'levels' as arguments.
        """
        if len(levels) == 1:
            levels = self.elevator(branch, levels, trace, value)

        count = 0
        previous_value = value

        for key, value in value.copy().items():
            count = count + 1

            trace[0] = trace[0] + 1

            if levels[trace[0]] <= levels[trace[0] - 1]:
                position_structure = position_structure[:-2]

            position_structure = position_structure + "." + str(count)

            previous_value[position_structure[1:] + ": " + key] = previous_value.pop(key)

            if value:
                self.update_layer(branch, levels, trace, value, position_structure)

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
