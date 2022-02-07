# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

from br4nch.utility.utility_handler import InstanceStringError, InstanceBooleanError, InvalidPositionError, \
    NotExistingBranchError
from br4nch.utility.utility_librarian import branches, paint_layer
from br4nch.utility.utility_positioner import format_position
from br4nch.utility.utility_generator import generate_uid


def arguments(branch, move, position, put="", paint=False):
    """
    - Gets the arguments and parses them to the 'MoveLayer' class.
    """
    MoveLayer(branch, move, position, put, paint)


class MoveLayer:
    def __init__(self, argument_branch, argument_move, argument_position, argument_put, argument_paint):
        """
        - Gets the arguments and parses them to the 'move_layer' function.
        """
        self.move_layer(argument_branch, argument_move, argument_position, argument_put, argument_paint)

    def move_layer(self, argument_branch, argument_move, argument_position, argument_put, argument_paint):
        """
        Lists:
          - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.
          - If the given move argument is not an instance of a list, then the move argument will be set as a list.

        Errors:
          - If the position argument is not an instance of a string, then it raises an 'InstanceStringError' error.
          - If the put argument is not an instance of a boolean, then it raises an 'InstanceBooleanError' error.
          - If the paint argument is not an instance of a boolean, then it raises an 'InstanceBooleanError' error.
          - If the position argument is not equal to a number and/or operator, then it raises an 'InvalidPositionError'
            error.

        Operators:
          - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
            list.

        Argument branch list loop:
          Errors:
            - If the branch value is not an instance of a string, then it raises an 'InstanceStringError' error.
            - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

          Branches list loop:
            Argument copy list loop:
              - Calls the function 'task_manager' to perform the necessary tasks for the variable 'argument_move'.

                If package:
                  - Adds the second value in the returned package to the list 'queue_delete'.
                  - The branches_branch value will be used as branch to move the chosen position(s) to.

                  If argument_put:
                    Branches list loop:
                      Errors:
                        - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError'
                          error.

                      - The argument_put value will be used as branch to move the chosen position(s) to.

              - Adds the first value in the returned package and calls the function 'task_manager' to perform the
                necessary tasks for the variable 'argument_position' and adds the returned dictionary in a list to the
                list 'queue_add'.

          - Loops through the list 'queue_delete' and deletes all given layers from the dictionary 'branches'.
          - Loops through the list 'queue_add' and adds all given layers from the dictionary 'branches'.
        """
        if not isinstance(argument_branch, list):
            argument_branch = [argument_branch]

        if not isinstance(argument_move, list):
            argument_move = [argument_move]

        if not isinstance(argument_position, str):
            raise InstanceStringError("position", argument_position)

        if not isinstance(argument_put, str):
            raise InstanceStringError("put", argument_put)

        if not isinstance(argument_paint, bool):
            raise InstanceBooleanError("paint", argument_paint)

        for position in argument_position.split("."):
            if not position.isnumeric():
                raise InvalidPositionError("position", argument_position)

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
                    queue_add = []

                    for position in format_position(branches_branch, argument_move.copy()):
                        package = self.task_manager(branches_branch, position, [], {},
                                                    branches[branches_branch][list(branches[branches_branch])[0]])

                        if package:
                            queue_delete.append(package[1])

                            move_branch = branches_branch

                            if argument_put:
                                put_error = 0

                                for branches_branch_two in list(branches):
                                    if argument_put.lower() == branches_branch_two.lower():
                                        put_error = put_error + 1

                                        move_branch = argument_put

                                if put_error == 0:
                                    if argument_put:
                                        raise NotExistingBranchError(argument_put)

                            queue_add.append([package[0], self.task_manager(move_branch, [],
                                                                            argument_position.split("."), package[0],
                                                                            branches[move_branch]
                                                                            [list(branches[move_branch])[0]])])

                    for delete_value in queue_delete:
                        if delete_value:
                            for layer, value in delete_value.items():
                                del value[layer]

                    for add_value in queue_add:
                        if add_value and add_value[0] and add_value[1]:
                            self.change_layer_uid(list(add_value[1])[0], argument_paint, add_value[0])
                            add_value[1][list(add_value[1])[0]].update(add_value[0])

            if error == 0:
                if branch:
                    raise NotExistingBranchError(branch)

    def task_manager(self, branch, move, position, copied_layer, value):
        """
        - If the first 'position' element variable is equal to '0', then it returns the whole branch from the 'branches'
          dictionary.

        Value dictionary loop:
          - For each value of the 'value' variable the 'count' variable is added with plus '1'.

          Count variable equal to the first value of 'move':
            If the length of the 'move' list is equal to '1':
              - Adds the current layer and value to a dictionary and adds the current layer and previous value to a
                dictionary and returns these two values as a package.

            - If the length of the 'move' list is not equal to '1' and there is a value of the 'value'
              variable, then the first value from the 'move' list will be removed and the 'task_manager'
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

            if move and count == int(move[0]):
                if len(move) == 1:
                    return [{layer: value}, {layer: previous_value}]
                else:
                    if value:
                        move.pop(0)
                        return self.task_manager(branch, move, position, copied_layer, value)

            if position and count == int(position[0]):
                if len(position) == 1:
                    return {branch: value}
                else:
                    if value:
                        position.pop(0)
                        return self.task_manager(branch, move, position, copied_layer, value)

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
            layer with UID is added to the list with the value of an empty string.

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
