# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

from br4nch.utility.utility_librarian import branches, paint_layer
from br4nch.utility.utility_handler import InstanceStringError, NotExistingBranchError, NotExistingPaintError
from br4nch.utility.utility_positioner import format_position


def arguments(branch, position, paint):
    """
    - Gets the arguments and parses them to the 'SetPaintLayer' class.
    """
    SetPaintLayer(branch, position, paint)


class SetPaintLayer:
    def __init__(self, argument_branch, argument_position, argument_paint):
        """
        - Gets the arguments and parses them to the 'build_position_structure' function.
        """
        self.build_position_structure(argument_branch, argument_position, argument_paint)

    def build_position_structure(self, argument_branch, argument_position, argument_paint):
        """
        Lists:
          - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.
          - If the given position argument is not an instance of a list, then the position argument will be set as a
            list.
          - If the given paint argument is not an instance of a list, then the paint argument will be set as a list.

        Operators:
          - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
            list.

        Argument branch list loop:
          Errors:
            - If the branch value is not an instance of a string, then it raises an 'InstanceStringError' error.
            - If the branch value is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

          Branches list loop:
            - Loops through the obtained values of the current value of the 'position' variable and adds all values of
              the variable to the 'position_structure' variable.
            - Calls the 'set_paint_layer' function with the current value of the whole branch dictionary, the 'position'
              and 'argument_paint' variables as arguments.
        """
        if not isinstance(argument_branch, list):
            argument_branch = [argument_branch]

        if not isinstance(argument_position, list):
            argument_position = [argument_position]

        if not isinstance(argument_paint, list):
            argument_paint = [argument_paint]

        for length in range(len(argument_position)):
            argument_position[length] = argument_position[length].split(".")

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

                    for position in format_position(branches_branch, argument_position.copy()):
                        self.set_paint_layer(branches_branch, argument_paint, position,
                                             branches[branches_branch][list(branches[branches_branch])[0]])

            if error == 0:
                if branch:
                    raise NotExistingBranchError(branch)

    def set_paint_layer(self, branch, paint_package, position, value):
        """
        Value dictionary loop:
          - For each value of the 'value' variable the 'count' variable is added with plus '1'.

          Count variable equal to the first value of 'position':
            Errors:
              - If the paint element argument is not an instance of a string, then it raises an 'InstanceStringError'
                error.

            - If the length of the 'position' list is equal to '1' then it check if the 'paint' exists in the given
              list. If it does not exists, it raises a 'NotExistingPaintError' error. If it does exists in the list, it
              will add the 'paint_package' list to the 'paint_layer' list.
            - If the length of the 'position' list is not equal to '1' and there is a value of the 'value' variable,
              then the first value from the 'position' list will be removed and the 'set_paint_layer' function will be
              called again with the new values of the 'value' variable as argument.
        """
        count = 0

        for layer, value in value.items():
            count = count + 1

            if count == int(position[0]):
                if len(position) == 1:
                    for paint in paint_package:
                        if not isinstance(paint, str):
                            raise InstanceStringError("paint", paint)

                        if paint.lower() not in ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
                                                 "bold", "underline"]:
                            raise NotExistingPaintError(paint)

                    paint_layer[branch].update({layer: paint_package})
                else:
                    if value:
                        position.pop(0)
                        return self.set_paint_layer(branch, paint_package, position, value)
