# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

from br4nch.utility.utility_handler import InstanceStringError, NotExistingBranchError
from br4nch.utility.utility_librarian import branches, uids, paint_layer
from br4nch.utility.utility_positioner import format_position
from br4nch.utility.utility_generator import generate_uid


def arguments(branch, replace, position):
    """
    - Gets the arguments and parses them to the 'ReplaceLayer' class.
    """
    ReplaceLayer(branch, replace, position)


class ReplaceLayer:
    def __init__(self, argument_branch, argument_replace, argument_position):
        """
        - Gets the arguments and parses them to the 'replace_layer' function.
        """
        self.replace_layer(argument_branch, argument_replace, argument_position)

    def replace_layer(self, argument_branch, argument_replace, argument_position):
        """
        Lists:
          - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.
          - If the given position argument is not an instance of a list, then the position argument will be set as a
            list.

        Errors:
          - If the replace argument is not an instance of a string, then it raises an 'InstanceStringError' error.

        Operators:
          - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
            list.

        Branches list loop:
          Errors:
            - If the branch value is not an instance of a string, then it raises an 'InstanceStringError' error.
            - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

          Argument copy list loop:
            - Calls the function 'task_manager' to perform the necessary tasks for the variable 'argument_copy'
            - If the last character in 'argument_replace' is equal to a newline/'\n', then it removes it from
              'argument_replace'.
            - Loops through the items from the returned dictionary and replaces all given layers from the mandatory
              dictionaries.
            - To keep the order the same, a loop will be made that loops through the 'value' dictionary and
              'paint_layer' list with the given slice values, removing all values and adding them again.
        """
        if not isinstance(argument_branch, list):
            argument_branch = [argument_branch]

        if not isinstance(argument_position, list):
            argument_position = [argument_position]

        if not isinstance(argument_replace, str):
            raise InstanceStringError("replace", argument_replace)

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
                        returned_value = self.get_layers(branches_branch, position,
                                                         branches[branches_branch][list(branches[branches_branch])[0]])
                        if returned_value:
                            for layer, value in returned_value.items():
                                while True:
                                    if argument_replace and argument_replace[-1] == "\n":
                                        argument_replace = argument_replace[:-1]
                                    else:
                                        break

                                new_layer = argument_replace + generate_uid(branches_branch)
                                uids[branches_branch].remove(layer[-10:])
                                paint_layer[branches_branch][new_layer] = paint_layer[branches_branch].pop(layer)

                                index = list(value).index(layer)
                                value[new_layer] = value.pop(layer)

                                for number in list(value)[index:-1]:
                                    value[number] = value.pop(number)
                                    paint_layer[branches_branch][number] = paint_layer[branches_branch].pop(number)

            if error == 0:
                if branch:
                    raise NotExistingBranchError(branch)

    def get_layers(self, branch, position, value):
        """
        Value dictionary loop:
          - For each value of the 'value' variable the 'count' variable is added with plus '1'.

          Count variable equal to the first value of 'position':
            If the length of the 'position' list is equal to '1':
              - Returns the current layer and previous value in an dictionary.

            - If the length of the 'position' list is not equal to '1' and there is a value of the 'value' variable,
              then the first value from the 'argument_move' list will be removed and the 'get_layers' function will be
              called again with the new value of the 'value' variable as argument.
        """
        count = 0
        previous_value = value

        for layer, value in value.items():
            count = count + 1

            if count == int(position[0]):
                if len(position) == 1:
                    return {layer: previous_value}
                else:
                    if value:
                        position.pop(0)
                        return self.get_layers(branch, position, value)
