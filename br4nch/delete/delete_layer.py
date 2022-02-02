# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

from br4nch.utility.utility_librarian import branches, uids, paint_layer
from br4nch.utility.utility_handler import InstanceStringError, NotExistingBranchError
from br4nch.utility.utility_positioner import format_position


def arguments(branch, position):
    """
    - Gets the arguments and parses them to the 'DeleteLayer' class.
    """
    DeleteLayer(branch, position)


class DeleteLayer:
    def __init__(self, argument_branch, argument_position):
        """
        - Gets the arguments and parses them to the 'build_structure' function.
        """
        self.build_structure(argument_branch, argument_position)

    def build_structure(self, argument_branch, argument_position):
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
            Argument position list loop:
              - Calls the function 'get_layers' to get the needed values from the 'argument_position' variable.
              - Adds the returned value to the list 'queue_delete'.

          - Loops through the list 'queue_delete' and deletes all given layers from the dictionary 'branches'.
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

                    queue_delete = []

                    for position in format_position(branches_branch, argument_position.copy()):
                        value = self.get_layers(branches_branch, position,
                                                branches[branches_branch][list(branches[branches_branch])[0]])

                        queue_delete.append(value)

                    for delete_value in queue_delete:
                        if delete_value:
                            for layer, value in delete_value.items():
                                uids[branches_branch].remove(str(layer[-10:]))
                                paint_layer[branches_branch].pop(layer)

                                self.delete_layer_additions(branches_branch, value[layer])
                                del value[layer]

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

    def delete_layer_additions(self, branch, value):
        """
        Value dictionary loop:
          - Checks if the UID of the current value of 'layer' exists in the 'uids' list. If the UID is in the 'uids'
            list, then it will be removed from the list.
          - Checks if the 'layer' value exists in the 'paint_layer' branch list. If the layer is in the 'paint_layer'
            branch list, then the value of the current layer key in the 'paint_layer' dictionary will be removed.
          - If there is a value of the 'value' variable, the 'delete_layer_additions' function will be called again with
            the new value of the 'value' variable as argument.
        """
        for layer, value in value.items():
            if layer[-10:] in uids[branch]:
                uids[branch].remove(str(layer[-10:]))

            if layer in paint_layer[branch]:
                paint_layer[branch].pop(layer)

            if value:
                self.delete_layer_additions(branch, value)
