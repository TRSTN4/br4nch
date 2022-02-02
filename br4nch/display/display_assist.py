# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

import copy

from br4nch.utility.utility_librarian import branches, output, uids, sizes, symbols, paint_branch, paint_header, \
    paint_layer
from br4nch.utility.utility_handler import InstanceStringError, InstanceIntegerError, InvalidSizeError, \
    NotExistingBranchError
from br4nch.utility.utility_generator import generate_uid
from br4nch.display.display_branch import display_branch


def arguments(branch, size=0, line="", split="", end=""):
    """
    - Gets the arguments and parses them to the 'DisplayAssist' class.
    """
    DisplayAssist(branch, size, line, split, end)


class DisplayAssist:
    def __init__(self, argument_branch, argument_size, argument_line, argument_split, argument_end):
        """
        - Gets the arguments and parses them to the 'display_assist' function.
        """
        self.display_assist(argument_branch, argument_size, argument_line, argument_split, argument_end)

    def display_assist(self, argument_branch, argument_size, argument_line, argument_split, argument_end):
        """
        Lists:
          - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.

        Errors:
          - If the size value is not an instance of a integer, then it raises an 'InstanceIntegerError' error.
          - If the line value is not an instance of a string, then it raises an 'InstanceStringError' error.
          - If the split value is not an instance of a string, then it raises an 'InstanceStringError' error.
          - If the end value is not an instance of a string, then it raises an 'InstanceStringError' error.

        Operators:
          - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
            list.

        Argument branch list loop:
          Errors:
            - If the branch value is not an instance of a string, then it raises an 'InstanceStringError' error.
            - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

          Branches list loop:
            - Calls the 'elevator' function to calculate each level/height of each layer and stores the result in the
              levels list. Then a '0' is added to the 'levels' list so that the 'IndexError' error can be avoided and
              after that the new value from the 'levels' list is returned.
            - If the branch is in the 'branches' dictionary, then a new name is generated for the value of the
              'branches_branch' variable. If the name already exists in the 'branches' dictionary, the loop starts again
              until a unique branch name is generated that does not yet exist in the 'branches' dictionary.
            - It then creates a deep copy of the current value of the 'branches_branch' value of the 'branches'
              directory and it is added as value to the 'branches' dictionary with the unique branch name as the key.
            - If there is no value in any of the 'line', 'split' or 'end' arguments, the value that is currently active
              of the missing arguments is used.
            - Then the unique branch name is added to the corresponding dictionaries with the default values as the
              value. The 'argument_size' variable will be updated to the 'sizes' dictionary.
            - Calls the function 'set_layer_pos_name' to add all positions to the corresponding layers.
            - Calls the 'display_branch' function to build and print the current branch.
        """
        if not isinstance(argument_branch, list):
            argument_branch = [argument_branch]

        if not isinstance(argument_size, int):
            raise InstanceIntegerError("size", argument_size)

        if not isinstance(argument_line, str):
            raise InstanceStringError("line", argument_line)

        if not isinstance(argument_split, str):
            raise InstanceStringError("split", argument_split)

        if not isinstance(argument_end, str):
            raise InstanceStringError("end", argument_end)

        if int(argument_size) < 0 or int(argument_size) > 20:
            raise InvalidSizeError

        if "*" in argument_branch:
            argument_branch.clear()
            for branches_branch in list(branches):
                argument_branch.append(branches_branch)

        for branch in argument_branch:
            error = 0

            if not isinstance(branch, str):
                raise InstanceStringError("branch", branch)

            for branches_branch in list(branches):
                if branch.lower() == branches_branch.lower():
                    error = error + 1

                    levels = [0]
                    self.elevator(levels, branches[branches_branch][list(branches[branches_branch])[0]])
                    levels.append(0)

                    while True:
                        branch_uid = branches_branch + generate_uid(branches_branch)

                        if branch_uid in list(branches):
                            continue
                        else:
                            uids[branches_branch].remove(branch_uid[-10:])
                            break

                    if not argument_line:
                        argument_line = symbols[branches_branch]["line"]
                    if not argument_split:
                        argument_split = symbols[branches_branch]["split"]
                    if not argument_end:
                        argument_end = symbols[branches_branch]["end"]

                    branches.update({branch_uid: copy.deepcopy(branches[branches_branch])})
                    branches[branch_uid][str("0: " + list(branches[branches_branch])[0])] = \
                        branches[branch_uid].pop(list(branches[branch_uid])[0])
                    output.update({branch_uid: []})
                    uids.update({branch_uid: []})
                    sizes.update({branch_uid: argument_size})
                    symbols.update({branch_uid: {"line": argument_line, "split": argument_split, "end": argument_end}})
                    paint_branch.update({branch_uid: ""})
                    paint_header.update({branch_uid: ""})
                    paint_layer.update({branch_uid: {}})

                    self.set_layer_pos_name(branch_uid, levels, [0],
                                            branches[branch_uid][list(branches[branch_uid])[0]])

                    display_branch(branch_uid, True)

            if error == 0:
                if branch:
                    raise NotExistingBranchError(branch)

    def set_layer_pos_name(self, branch, levels, trace, value, position_structure=""):
        """
        Value dictionary loop:
          - For each value of the 'value' variable the 'count' variable and the first element of the 'trace' list is
            added with plus '1'.

          Position structure:
            - Then it is checked whether the "level"/"height" of the current value of the loop is equal to or smaller
              than the previous "level"/"height" value of the loop. If the instantaneous value is equal or less, the
              last position and dot in the 'position_structure' variable is removed.
            - Then the current value of the 'position_structure' variable is added with the value of 'count' separated
              by a dot to the 'position_structure' variable.

          - Adds the position to the layer in the current value of 'previous_value'.
          - Checks whether the 'value' variable has a value. If there is a value, then the 'set_layer_pos_name' function
            is called again with the current values of 'value', 'trace' and 'levels' as arguments.
        """
        count = 0
        previous_value = value

        for layer, value in value.copy().items():
            count = count + 1

            trace[0] = trace[0] + 1

            if levels[trace[0]] <= levels[trace[0] - 1]:
                position_structure = position_structure[:-2]
            position_structure = position_structure + "." + str(count)

            previous_value[position_structure[1:] + ": " + layer] = previous_value.pop(layer)

            if value:
                self.set_layer_pos_name(branch, levels, trace, value, position_structure)

    def elevator(self, levels, value, pos=0):
        """
        Value dictionary loop:
          - Loops through each "height" of the value dictionary and adds the value of the 'pos' variable to the 'levels'
            list.
          - Then the 'elevator' function is called again with the current value of the 'value' dictionary.
        """
        for value in value.values():
            levels.append(pos)

            self.elevator(levels, value, pos + 1)
