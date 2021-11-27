# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches
from br4nch.utility.printer import printer
from br4nch.utility.positioner import format_position
from br4nch.utility.handler import NotExistingBranchError, StringInstanceError, BooleanInstanceError,\
    PositionNotAllowedError


def arguments(branch, pos, beautify=True):
    """
    - Gets the arguments and parses them to the 'DisplayPos' class.
    """
    DisplayPos(branch, pos, beautify)


class DisplayPos:
    def __init__(self, argument_branch, argument_pos, argument_beautify):
        """
        - Gets the arguments and parses them to the 'build_position_structure' function.
        """
        self.build_position_structure(argument_branch, argument_pos, argument_beautify)

    def build_position_structure(self, argument_branch, argument_pos, argument_beautify):
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
              'format_position' function. And calls the 'display_pos' function for each loop with the built position
              structure and the built 'string_position' variable as arguments.
        """
        if not isinstance(argument_branch, list):
            argument_branch = [argument_branch]

        if not isinstance(argument_pos, list):
            argument_pos = [argument_pos]

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

                    for position in format_position(branches_branch, argument_pos.copy()):
                        string_position = ""

                        for character in position:
                            string_position = string_position + "." + character

                        self.display_pos(branches_branch, position, string_position[1:], argument_beautify,
                                         branches[branches_branch][list(branches[branches_branch])[0]])

            if error == 0:
                raise NotExistingBranchError(branch)

    def display_pos(self, branch, position, string_position, argument_beautify, value):
        """
        Errors:
          - If the value of position is equal to '0', then it raises a 'PositionNotAllowedError' error.

        Value dictionary loop:
          - For each value of the 'value' variable the 'count' variable is added with plus '1'.

          Count variable equal to the first value of 'position':
            If the length of the 'position' list is equal to '1':
              - The 'printer' function is called and a package is supplied with all the values in it that are needed.
                If the 'argument_beautify' variable is false, the given positions are not represented with a branch
                structure.

            - If the length of the 'position' list is not equal to '1' and there is a value of the 'value' variable,
              then the first value from the 'position' list will be removed and the 'display_pos' function will be
              called again with the new value of the 'value' variable as argument.
        """
        count = 0

        if position[0] == "0":
            raise PositionNotAllowedError("pos")

        for layer, value in value.items():
            count = count + 1

            if count == int(position[0]):
                if len(position) == 1:
                    return printer("display_pos", [branch, layer[:-15], string_position, argument_beautify])
                else:
                    if value:
                        position.pop(0)
                        return self.display_pos(branch, position, string_position, argument_beautify, value)
