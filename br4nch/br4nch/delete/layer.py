# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches, uids, paint_layer
from br4nch.utility.positioner import format_position
from br4nch.utility.handler import NotExistingBranchError


def arguments(branch, pos):
    """Gets the arguments and parses them to the 'DeleteLayer' class."""
    DeleteLayer(branch, pos)


class DeleteLayer:
    def __init__(self, argument_branch, argument_pos):
        """Gets the arguments and parses them to the 'build_position' function."""
        self.build_position(argument_branch, argument_pos)

    def build_position(self, argument_branch, argument_pos):
        """
        If the given branch argument is not an instance of a list, then the branch argument will be set as a list.
        If the given pos argument is not an instance of a list, then the pos argument will be set as a list.

        If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
        list.

        Loops through the given 'argument_branch' list and checks if the value is already in the 'branches' dictionary.
        If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

        If the branch is in the 'branches' dictionary, then it runs a loop with all positions in the returned list from
        the 'format_position' function. And calls the 'delete_layer' function for every looped position.
        """

        if not isinstance(argument_branch, list):
            argument_branch = [argument_branch]

        if not isinstance(argument_pos, list):
            argument_pos = [argument_pos]

        if "*" in argument_branch:
            argument_branch.clear()
            for branches_branch in list(branches):
                argument_branch.append(branches_branch)

        for branch in argument_branch:
            branch = str(branch)
            error = 0
            for branches_branch in list(branches):
                if branch.lower() == branches_branch.lower():
                    branch = branches_branch
                    error = error + 1

                    count = 0
                    for position in format_position(branch, argument_pos.copy()):
                        print(position)
                        position[-1] = str(int(position[-1]) - count)
                        package = self.delete_layer(branch, position)
                        self.delete_sublayer(branch, package[0], position, package[1])
                        count = count + 1

            if error == 0:
                raise NotExistingBranchError(branch)

    def delete_layer(self, branch, position, position_structure="", value=""):
        """
        If there is no value in the 'value' variable, then the 'value' variable is equal to the value of the branch
        header key in the 'branches' directory.

        If the first value in the 'position' is equal to a '0' then the 'argument_layer' variable is looped and each
        layer of the loop is appended to the value of the header key in the branch of the 'branches' directory. todo

        If the first value in the 'position' is not equal to a '0' then a loop is made and for each value of the 'value'
        variable the 'count' variable is added with '1'.

        If the value of the 'count' variable is equal to the first value of the 'position' variable and the length of
        the 'position' list is equal to '1' then the 'delete_sublayer' function is used which removes all sub-layers.

        If the value of the 'count' variable is equal to the first value of the 'position' variable and the length of
        the 'position' list is not equal to '1' and there is a value of the 'value' variable, then removes the first
        value from the 'position' list and calls the 'delete_layer' again with the new values of the 'value' variable as
        argument.
        """

        if not value:
            value = branches[branch][list(branches[branch])[0]]

        if position[0] == "0":
            for layer in branches[branch][list(branches[branch])[0]].copy():
                uids[branch].remove(layer[-10:])
                del branches[branch][list(branches[branch])[0]][layer]
            return
        else:
            count = 0
            previous_value = value

            for value in value.values():
                count = count + 1

                if count == int(position[0]):
                    position_structure = position_structure + "." + str(count)
                    if position_structure[0] == ".":
                        position_structure = position_structure[1:]

                    if len(position) == 1:
                        return [previous_value, position_structure]
                    else:
                        if value:
                            position.pop(0)
                            position_structure = self.delete_layer(branch, position, position_structure, value)
                            return position_structure

    def delete_sublayer(self, branch, value, pos, position_structure):
        """
        Loops through the given value and deletes all uids from the layers and deletes the values from the 'branches'
        directory. todo
        """

        count = 0
        previous_value = value

        for layer, value in value.copy().items():
            count = count + 1
            if pos[0]:
                if count == int(pos[0]):
                    if len(pos) == 1:
                        for x in range(len(previous_value)):
                            if int(x + 1) >= int(position_structure[-1]) and int(x + 1) != len(previous_value):
                                paint_layer[branch].update({position_structure[:-1] + str(x + 1): paint_layer[branch][position_structure[:-1] + str(x + 2)]})

                            if int(x + 1) == len(previous_value):
                                del paint_layer[branch][position_structure[:-1] + str(x + 1)]

                        uids[branch].remove(layer[-10:])
                        del previous_value[layer]
                    else:
                        if value:
                            self.delete_sublayer(branch, value, pos, position_structure)
