# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

from br4nch.utility.utility_handler import InstanceBooleanError, InstanceStringError, NotExistingBranchError
from br4nch.utility.utility_librarian import branches
from br4nch.utility.utility_printer import printer


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
          - If the sensitive value is not an instance of a boolean, then it raises an 'InstanceBooleanError' error.
          - If the beautify value is not an instance of a boolean, then it raises an 'InstanceBooleanError' error.

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
            - If the branch is in the 'branches' dictionary, it will loop with all positions in the returned list of the
              'format_position' function. And calls the 'display_layer' function for each loop with the built position
              structure of the 'position' as argument
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

                        self.display_layer(branches_branch, layer, argument_sensitive, argument_beautify, levels, [0],
                                           branches[branches_branch][list(branches[branches_branch])[0]])

            if error == 0:
                if branch:
                    raise NotExistingBranchError(branch)

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
                      position_structure=""):
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

          - If the 'argument_sensitive' is 'True', then is checked if the current value of 'layer' is equal to the value
            of 'loop_layer'. If the 'argument_sensitive' is 'False', then is checked if the current value of 'layer' in
            lower text is equal to the value of 'loop_layer' in lower text.
            - If the values are equal, then the 'printer' function is called and a package is supplied with all the
              values in it that are needed. If the 'argument_beautify' variable is false, the given positions are not
              represented with a branch structure.

          - Checks whether the 'value' variable has a value. If there is a value, then the 'display_layer' function is
            called again with the current values of 'value', 'trace' and 'levels' as arguments.
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
                    printer("display_layer", [branch, layer[:-15], position_structure[1:], argument_beautify])
            else:
                if layer[:-15].lower() == loop_layer.lower():
                    printer("display_layer", [branch, layer[:-15], position_structure[1:], argument_beautify])

            if value:
                self.display_layer(branch, loop_layer, argument_sensitive, argument_beautify, levels, trace, value,
                                   position_structure)
