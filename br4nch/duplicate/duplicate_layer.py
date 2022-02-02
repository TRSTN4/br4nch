# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

import copy

from br4nch.utility.utility_handler import InstanceBooleanError, InstanceStringError, NotExistingBranchError
from br4nch.utility.utility_librarian import branches, uids, paint_layer
from br4nch.utility.utility_positioner import format_position
from br4nch.utility.utility_generator import generate_uid


def arguments(branch, duplicate, position, put="", paint=False, delete=False):
    """
    - Gets the arguments and parses them to the 'DuplicateLayer' class.
    """
    DuplicateLayer(branch, duplicate, position, put, paint, delete)


class DuplicateLayer:
    def __init__(self, argument_branch, argument_duplicate, argument_position, argument_put, argument_paint,
                 argument_delete):
        """
        - Gets the arguments and parses them to the 'duplicate_layer' function.
        """
        self.duplicate_layer(argument_branch, argument_duplicate, argument_position, argument_put, argument_paint,
                             argument_delete)

    def duplicate_layer(self, argument_branch, argument_duplicate, argument_position, argument_put, argument_paint,
                        argument_delete):
        """
        Lists:
          - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.
          - If the given duplicate argument is not an instance of a list, then the duplicate argument will be set as a
            list.
          - If the given position argument is not an instance of a list, then the position argument will be set as a
            list.
          - If the given put argument is not an instance of a list, then the put argument will be set as a list.

        Errors:
          - If the paint value is not an instance of a boolean, then it raises an 'InstanceBooleanError' error.
          - If the delete value is not an instance of a boolean, then it raises an 'InstanceBooleanError' error.

        Operators:
          - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
            list.
          - If there a '*' in the 'argument_put' list, Then it appends all existing branches to the 'argument_put' list.

        Argument branch list loop:
          Errors:
            - If the branch value is not an instance of a string, then it raises an 'InstanceStringError' error.
            - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

          Branches list loop:
            Argument duplicate list loop:
              Argument position list loop:
                - Calls the function 'task_manager' to perform the necessary tasks for the variable 'argument_copy'.

                If package:
                  - Adds the second value in the returned package to the list 'queue_delete'.

                  - If the 'put' argument is not used. The 'argument_put' list will be changed to the current branch
                    value in a list.

                  Argument put list loop:
                    Errors:
                      - If the branch value is not an instance of a string, then it raises an 'InstanceStringError'
                        error.
                      - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError'
                        error.

                    Branches list loop:
                      - Adds the first value in the returned package and calls the function 'task_manager' to perform
                        the necessary tasks for the variable 'argument_position' and adds the returned dictionary in a
                        list to the list 'queue_add'.

            - Loops through the list 'queue_delete' and deletes all given layers from the dictionary 'branches'.
            - Loops through the list 'queue_add' and adds all given layers from the dictionary 'branches'.
        """
        if not isinstance(argument_branch, list):
            argument_branch = [argument_branch]

        if not isinstance(argument_duplicate, list):
            argument_duplicate = [argument_duplicate]

        if not isinstance(argument_position, list):
            argument_position = [argument_position]

        if not isinstance(argument_put, list):
            argument_put = [argument_put]

        if not isinstance(argument_delete, bool):
            raise InstanceBooleanError("paint", argument_paint)

        if not isinstance(argument_delete, bool):
            raise InstanceBooleanError("delete", argument_delete)

        if "*" in argument_branch:
            argument_branch.clear()
            for branches_branch in list(branches):
                argument_branch.append(branches_branch)

        if "*" in argument_put:
            argument_put.clear()
            for branches_branch in list(branches):
                argument_put.append(branches_branch)

        for branch in argument_branch:
            error = 0

            if not isinstance(branch, str):
                raise InstanceStringError("branch", branch)

            for branches_branch in list(branches):
                if branch.lower() == branches_branch.lower():
                    error = error + 1

                    queue_delete = []
                    queue_add = []

                    for loop_copy in format_position(branches_branch, argument_duplicate.copy()):
                        for loop_position in format_position(branches_branch, argument_position.copy()):
                            package = self.task_manager(branches_branch, loop_copy, [], argument_paint,
                                                        branches[branches_branch][list(branches[branches_branch])[0]])

                            if package:
                                queue_delete.append(package[1])

                                if len(argument_put) == 1 and not argument_put[0]:
                                    argument_put = [branches_branch]

                                for put_branch in argument_put:
                                    put_error = 0

                                    if not isinstance(put_branch, str):
                                        raise InstanceStringError("put", put_branch)

                                    for branches_branch_two in list(branches):
                                        if put_branch.lower() == branches_branch_two.lower():
                                            put_error = put_error + 1

                                            queue_add.append([package[0], self.task_manager(branches_branch_two, [],
                                                                                            loop_position,
                                                                                            argument_paint,
                                                                                            branches
                                                                                            [branches_branch_two]
                                                                                            [list(branches
                                                                                                  [branches_branch_two])
                                                                                            [0]])])

                                    if put_error == 0:
                                        if put_branch:
                                            raise NotExistingBranchError(put_branch)

                    if argument_delete:
                        for delete_value in queue_delete:
                            if delete_value:
                                for layer, value in delete_value.items():
                                    uids[branches_branch].remove(str(layer[-10:]))
                                    paint_layer[branches_branch].pop(layer)

                                    self.delete_layer_additions(branches_branch, value[layer])

                                    del value[layer]

                    for add_value in queue_add:
                        if add_value and add_value[0] and add_value[1]:
                            self.change_layer_uid(list(add_value[1])[0], argument_paint, add_value[0])
                            add_value[1][list(add_value[1])[0]].update(add_value[0])

            if error == 0:
                if branch:
                    raise NotExistingBranchError(branch)

    def task_manager(self, branch, duplicate, position, argument_paint, value):
        """
        - If the first 'position' element variable is equal to '0', then it returns the whole branch from the 'branches'
          dictionary.

        Value dictionary loop:
          - For each value of the 'value' variable the 'count' variable is added with plus '1'.

          Count variable equal to the first value of 'duplicate':
            If the length of the 'duplicate' list is equal to '1':
              - Adds the current layer and aa deepcopy of the 'value' variable to a dictionary and adds the current
                layer and previous value to a dictionary and returns these two values as a package.

            - If the length of the 'duplicate' list is not equal to '1' and there is a value of the 'value'
              variable, then the first value from the 'argument_move' list will be removed and the 'task_manager'
              function will be called again with the new value of the 'value' variable as argument.

          Count variable equal to the first value of 'position':
            If the length of the 'position' list is equal to '1':
              - Returns the current value of the 'value' variable.

            - If the length of the 'position' list is not equal to '1' and there is a value of the 'value' variable,
              then the first value from the 'position' list will be removed and the 'task_manager' function will be
              called again with the new value of the 'value' variable as argument.
        """
        count = 0
        previous_value = value

        if position and position[0] == "0":
            return {branch: branches[branch][list(branches[branch])[0]]}

        for layer, value in value.items():
            count = count + 1

            if duplicate and count == int(duplicate[0]):
                if len(duplicate) == 1:
                    return [{layer: copy.deepcopy(value)}, {layer: previous_value}]
                else:
                    if value:
                        duplicate.pop(0)
                        return self.task_manager(branch, duplicate, position, argument_paint, value)

            if position and count == int(position[0]):
                if len(position) == 1:
                    return {branch: value}
                else:
                    if value:
                        position.pop(0)
                        return self.task_manager(branch, duplicate, position, argument_paint, value)

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

    def change_layer_uid(self, branch, argument_paint, value):
        """
        Value dictionary loop:
          - Generates a new UID for the copied 'layer' variable. Then the old layer is deleted and replaced with the new
            generated layer with the new UID.

          - Checks if the current value of 'layer' exists in the branch's 'paint_layer' list. Then it is checked whether
            the variable 'argument_paint' is true. If the value exists in the list and the 'argument_paint' is true,
            then the newly generated layer with UID is added to the list with the value of the value of the variable
            'layer'.
          - If the current value of 'layer' does not exist in the branch's 'paint_layer' list. Then the newly generated
            layer with UID is added to the list with the value of an empty list.

          - If there is a value of the 'value' variable, the 'change_layer_uid' function will be called again with the
            new value of the 'value' variable as argument.
        """
        previous_value = value

        for layer, value in value.copy().items():
            new_layer = layer[:-15] + generate_uid(branch)

            previous_value[new_layer] = previous_value.pop(layer)

            if layer in paint_layer[branch]:
                if argument_paint:
                    paint_layer[branch].update({new_layer: paint_layer[branch][layer]})
            else:
                paint_layer[branch].update({new_layer: []})

            if value:
                self.change_layer_uid(branch, argument_paint, value)
