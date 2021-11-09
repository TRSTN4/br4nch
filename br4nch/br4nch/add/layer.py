# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches, paint_layer
from br4nch.utility.positioner import format_position
from br4nch.utility.generator import generate_uid
from br4nch.utility.handler import NotExistingBranchError, StringInstanceError


def arguments(branch, layer, pos):
    """Gets the arguments and parses them to the 'AddLayer' class."""
    AddLayer(branch, layer, pos)


class AddLayer:
    def __init__(self, argument_branch, argument_layer, argument_pos):
        """Gets the arguments and parses them to the 'build_position_structure' function."""
        self.build_position_structure(argument_branch, argument_layer, argument_pos)

    def build_position_structure(self, argument_branch, argument_layer, argument_pos):
        """
        Lists:
          - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.
          - If the given layer argument is not an instance of a list, then the layer argument will be set as a list.
          - If the given pos argument is not an instance of a list, then the pos argument will be set as a list.

        Operators:
          - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
            list.

        Argument branch list loop:
          Errors:
            - If the branch value is not an instance of a string, then it raises an 'StringInstanceError' error.
            - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

          Branches list loop:
            - If the branch is in the 'branches' dictionary, then it runs a loop with all positions in the returned list
              from the 'format_position' function. And calls the 'add_layer' function with the whole branch dictionary
              as value for every looped position.
        """
        if not isinstance(argument_branch, list):
            argument_branch = [argument_branch]

        if not isinstance(argument_layer, list):
            argument_layer = [argument_layer]

        if not isinstance(argument_pos, list):
            argument_pos = [argument_pos]

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

                    for position in format_position(branches_branch, argument_pos):
                        self.add_layer(branches_branch, argument_layer, position,
                                       branches[branch][list(branches[branch])[0]])

            if error == 0:
                raise NotExistingBranchError(branch)

    def add_layer(self, branch, argument_layer, position, value, position_structure=""):
        """
        Position variable equal to zero:
          Errors:
            - If the layer value is not an instance of a string, then it raises an 'StringInstanceError' error.

          - If the first value in the 'position' is equal to a '0' then the 'argument_layer' variable is looped and each
            layer value of the loop is appended to the value of the header key in the branch of the 'branches'
            directory.

        Value dictionary loop:
          - For each value of the 'value' variable the 'count' variable is added with plus '1'.

          Count variable equal to the first value of position:
            If the length of the 'position' list is equal to '1':
              Errors:
                - If the layer value is not an instance of a string, then it raises an 'StringInstanceError' error.

              - Then it will add the current branch key in the 'branches' dictionary with an empty string as value to
                the 'paint_layer' directory.

            - If the length of the 'position' list is not equal to '1' and there is a value of the 'value' variable,
              then the first value from the 'position' list will be removed and the 'add_layer' function will be called
              again with the new values of the 'value' variable as argument.
        """
        if position[0] == "0":
            for layer in argument_layer:
                if not isinstance(layer, str):
                    raise StringInstanceError("layer", layer)

                branches[branch][list(branches[branch])[0]].update({layer + generate_uid(branch): {}})
            return
        else:
            count = 0

            for value in value.values():
                count = count + 1

                position_structure = position_structure + "." + str(count)
                if position_structure[0] == ".":
                    position_structure = position_structure[1:]

                if count == int(position[0]):
                    if len(position) == 1:
                        for layer in argument_layer:
                            if not isinstance(layer, str):
                                raise StringInstanceError("layer", layer)

                            value.update({layer + generate_uid(branch): {}})
                            paint_layer[branch].update({position_structure: ""})
                        return
                    else:
                        if value:
                            position.pop(0)
                            self.add_layer(branch, argument_layer, position, value, position_structure)
                            return
