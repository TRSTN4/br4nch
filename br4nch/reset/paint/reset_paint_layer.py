# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

from br4nch.utility.utility_librarian import branches, paint_layer
from br4nch.utility.utility_handler import InstanceStringError, NotExistingBranchError
from br4nch.utility.utility_positioner import format_position


def arguments(branch, position):
    """
    - Gets the arguments and parses them to the 'ResetPaintLayer' class.
    """
    ResetPaintLayer(branch, position)


class ResetPaintLayer:
    def __init__(self, argument_branch, argument_position):
        """
        - Gets the arguments and parses them to the 'build_position_structure' function.
        """
        self.build_position_structure(argument_branch, argument_position)

    def build_position_structure(self, argument_branch, argument_position):
        """
        Lists:
          - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.
          - If the given position argument is not an instance of a list, then the position argument will be set as a
            list.

        Operators:
          - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
            list.

        Argument branch list loop:
          Errors:
            - If the branch value is not an instance of a string, then it raises an 'InstanceStringError' error.
            - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

          Branches list loop:
            - If the branch is in the 'branches' dictionary, then it runs a loop with all positions in the returned list
              from the 'format_position' function. And calls the 'reset_paint_layer' function with the whole branch
              dictionary as value for every looped position.
        """
        if not isinstance(argument_branch, list):
            argument_branch = [argument_branch]

        if not isinstance(argument_position, list):
            argument_position = [argument_position]

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

                    for position in format_position(branches_branch, argument_position):
                        self.reset_paint_layer(branches_branch, position,
                                               branches[branches_branch][list(branches[branches_branch])[0]])

            if error == 0:
                if branch:
                    raise NotExistingBranchError(branch)

    def reset_paint_layer(self, branch, position, value):
        """
        Value dictionary loop:
          - For each value of the 'value' variable the 'count' variable is added with plus '1'.

          Count variable equal to the first value of 'position':
            - If the length of the 'position' list is equal to '1', then the value of the current layer key in the
              'paint_layer' dictionary is updated to an empty list.
            - If the length of the 'position' list is not equal to '1' and there is a value of the 'value' variable,
              then the first value from the 'position' list will be removed and the 'reset_paint_layer' function will
              be called again with the new value of the 'value' variable as argument.
        """
        count = 0

        for layer, value in value.items():
            count = count + 1

            if count == int(position[0]):
                if len(position) == 1:
                    paint_layer[branch].update({layer: []})
                else:
                    position.pop(0)
                    self.reset_paint_layer(branch, position, value)
