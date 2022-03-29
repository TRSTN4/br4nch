# br4nch - Data Structure Tree Builder
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from br4nch.utility.utility_handler import InstanceBooleanError, InstanceStringError, NotExistingBranchError
from br4nch.utility.utility_librarian import branches, output, uids, sizes, symbols, paint_branch, paint_header, \
    paint_layer
from br4nch.utility.utility_generator import generate_uid
from br4nch.display.display_branch import display_branch


def arguments(branch, layer, sensitive=False, beautify=True):
    """
    - Gets the arguments and parses them to the 'DisplayLayer' class.
    """
    DisplayLayer(branch, layer, sensitive, beautify)


class DisplayLayer:
    def __init__(self, argument_branch, argument_layer, argument_sensitive, argument_beautify):
        """
        - Gets the arguments and parses them to the 'build_position_structure' function.
        """
        self.build_position_structure(argument_branch, argument_layer, argument_sensitive, argument_beautify)

    def build_position_structure(self, argument_branch, argument_layer, argument_sensitive, argument_beautify):
        """
        Lists:
          - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.
          - If the given pos argument is not an instance of a list, then the branch argument will be set as a list.

        Errors:
          - If the 'sensitive' value is not an instance of a boolean, then it raises an 'InstanceBooleanError' error.
          - If the 'beautify' value is not an instance of a boolean, then it raises an 'InstanceBooleanError' error.

        Operators:
          - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
            list.

        Argument branch list loop:
          Errors:
            - If the branch value is not an instance of a string, then it raises an 'InstanceStringError' error.
            - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

          Branches list loop:
            Errors:
              - If the 'loop_layer' value is not an instance of a string, then it raises an 'InstanceStringError' error.

            - Calls the 'elevator' function to calculate each level/height of each layer and stores the result in the
              levels list. Then a '0' is added to the 'levels' list so that the 'IndexError' error can be avoided.
            - Calls the 'display_layer' function for each loop in the 'argument_layer' variable with the given layer as
              value and the given arguments.

        If the 'beautify_structure' and 'argument_beautify' has a value of 'True':
          - a new branch is created with all associated dictionaries.

          Value 'beautify_structure' loop:
            - If the 'branch/findings[0]' is not in the new 'branch' dictionary, it will be added to the dictionary.
            - If the 'position/findings[1]' is not in the new 'branch[branch/findings[1]]' dictionary, it will be added
              to the dictionary.
            - If the 'layer/findings[2]' is not in the new 'branch[branch][position]' dictionary, it will be added to
              the dictionary.

          - Then the branch name without uid and the newly created branch dictionary is passed to the 'update_branch'
            function.
          - Calls the 'display_branch' function to print the new branch and then delete it.
        """
        if not isinstance(argument_branch, list):
            argument_branch = [argument_branch]

        if not isinstance(argument_layer, list):
            argument_layer = [argument_layer]

        if not isinstance(argument_sensitive, bool):
            raise InstanceBooleanError("sensitive", argument_sensitive)

        if not isinstance(argument_beautify, bool):
            raise InstanceBooleanError("beautify", argument_beautify)

        if "*" in argument_branch:
            argument_branch.clear()
            for branches_branch in list(branches):
                argument_branch.append(branches_branch)

        beautify_structure = []

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

                    for layer in argument_layer:
                        if not isinstance(layer, str):
                            raise InstanceStringError("layer", layer)

                        beautify_structure = self.display_layer(branches_branch, layer, argument_sensitive,
                                                                argument_beautify, levels, [0],
                                                                branches[branches_branch]
                                                                [list(branches[branches_branch])[0]],
                                                                beautify_structure, "")

            if error == 0:
                if branch:
                    raise NotExistingBranchError(branch)

        if beautify_structure and argument_beautify:
            branch_uid = generate_uid("-")

            branches.update({branch_uid: {"Get Layer Result:": {}}})
            output.update({branch_uid: []})
            uids.update({branch_uid: []})
            sizes.update({branch_uid: 0})
            symbols.update({branch_uid: {"line": "┃", "split": "┣━", "end": "┗━"}})
            paint_branch.update({branch_uid: []})
            paint_header.update({branch_uid: []})
            paint_layer.update({branch_uid: {}})

            for findings in beautify_structure:
                if findings[0] not in branches[branch_uid][list(branches[branch_uid])[0]]:
                    branches[branch_uid][list(branches[branch_uid])[0]].update({findings[0]: {}})

                if findings[1] not in branches[branch_uid][list(branches[branch_uid])[0]][findings[0]]:
                    branches[branch_uid][list(branches[branch_uid])[0]][findings[0]].update({findings[1]: {}})

                if findings[2] not in branches[branch_uid][list(branches[branch_uid])[0]][findings[0]][findings[1]]:
                    branches[branch_uid][list(branches[branch_uid])[0]][findings[0]][findings[1]].update({findings[2]: {}})

            self.update_branch(branch_uid, branches[branch_uid])

            display_branch(branch_uid, True)

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

    def display_layer(self, branch, loop_layer, argument_sensitive, argument_beautify, levels, trace, value,
                      beautify_structure, position_structure):
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

          If the 'argument_sensitive' is 'True':
            - Then is checked if the current value of 'layer' is equal to the value of 'loop_layer'.
            - The 'branch', 'string_position' and the 'layer' without uid will be added to the 'beautify_structure'
              list.
            - If the 'argument_beautify' value is equal to 'False', the 'position_structure' value will be printed.

          If the 'argument_sensitive' is 'False':
            - Then is checked if the current value of 'layer' in lower text is equal to the value of 'loop_layer' in
              lower text.
            - The 'branch', 'string_position' and the 'layer' without uid will be added to the 'beautify_structure'
              list.
            - If the 'argument_beautify' value is equal to 'False', the 'position_structure' value will be printed.

          - If the 'argument_beautify' value is 'False', only the 'position_structure' value will be printed.

          - Checks whether the 'value' variable has a value. If there is a value, then the 'display_layer' function is
            called again with the current values of 'value', 'trace' and 'levels' as arguments.

        - Returns the 'beautify_structure' list.
        """
        count = 0

        for layer, value in value.items():
            count = count + 1

            trace[0] = trace[0] + 1

            if levels[trace[0]] <= levels[trace[0] - 1]:
                position_structure = position_structure[:-2]

            position_structure = position_structure + "." + str(count)

            if argument_sensitive:
                if layer[:-15] == loop_layer:
                    beautify_structure.append([branch, layer[:-15], position_structure[1:]])
                    if not argument_beautify:
                        print(position_structure[1:])
            else:
                if layer[:-15].lower() == loop_layer.lower():
                    beautify_structure.append([branch, layer[:-15], position_structure[1:]])
                    if not argument_beautify:
                        print(position_structure[1:])

            if value:
                self.display_layer(branch, loop_layer, argument_sensitive, argument_beautify, levels, trace, value,
                                   beautify_structure, position_structure)

        return beautify_structure

    def update_branch(self, branch, value, height=0):
        """
        Value dictionary loop:
          - If the 'height' value is equal to '1', the current layer in the value will get updated with 'Branch' and
            gets a unique uid.
          - If the 'height' value is equal to '2', the current layer in the value will get updated with 'Layer' and gets
            a unique uid.
          - If the 'height' value is equal to '3', the current layer in the value will get updated with 'Position' and
            gets a unique uid.

          - If there is a value in 'value', the 'update_branch' function will be called again with the current 'value'
            value and 'height + 1'.
        """
        previous_value = value

        for layer, value in value.copy().items():
            if height == 1:
                previous_value["Branch: " + layer + generate_uid(branch)] = previous_value.pop(layer)

            if height == 2:
                previous_value["Layer: " + layer + generate_uid(branch)] = previous_value.pop(layer)

            if height == 3:
                previous_value["Position: " + layer + generate_uid(branch)] = previous_value.pop(layer)

            if value:
                self.update_branch(branch, value, height + 1)
