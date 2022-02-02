# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

from br4nch.utility.utility_librarian import branches, paint_layer
from br4nch.utility.utility_handler import InstanceStringError, NotExistingBranchError
from br4nch.utility.utility_positioner import format_position
from br4nch.utility.utility_generator import generate_uid


def arguments(branch, layer, position):
    """
    - Gets the arguments and parses them to the 'CreateLayer' class.
    """
    CreateLayer(branch, layer, position)


class CreateLayer:
    def __init__(self, argument_branch, argument_layer, argument_position):
        """
        - Gets the arguments and parses them to the 'build_position_structure' function.
        """
        self.build_position_structure(argument_branch, argument_layer, argument_position)

    def build_position_structure(self, argument_branch, argument_layer, argument_position):
        """
        Lists:
          - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.
          - If the given layer argument is not an instance of a list, then the layer argument will be set as a list.
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
            Errors:
              - If the branch value is not an instance of a string, then it raises an 'InstanceStringError' error.
              - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

            - If the branch is in the 'branches' dictionary, then it runs a loop with all positions in the returned list
              from the 'format_position' function. And calls the 'add_layer' function with the whole branch dictionary
              as value for every looped position.
        """
        if not isinstance(argument_branch, list):
            argument_branch = [argument_branch]

        if not isinstance(argument_layer, list):
            argument_layer = [argument_layer]

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
                        self.create_layer(branches_branch, argument_layer, position,
                                          branches[branches_branch][list(branches[branches_branch])[0]])

            if error == 0:
                if branch:
                    raise NotExistingBranchError(branch)

    def create_layer(self, branch, argument_layer, position, value):
        """
        Position variable equal to zero:
          Errors:
            - If the 'loop_layer' value is not an instance of a string, then it raises an 'InstanceStringError' error.

          - If the last character in 'loop_layer' is equal to a newline/'\n', then it removes it from 'loop_layer'.

          - If the first value in the 'position' is equal to a '0' then the 'argument_layer' variable is looped and in
            each loop it will create the current layer with a generated UID to the value to the 'paint_layer' list and
            to the 'value' dictionary from the 'branches' dictionary.

        Value dictionary loop:
          - For each value of the 'value' variable the 'count' variable is added with plus '1'.

          Count variable equal to the first value of 'position':
            If the length of the 'position' list is equal to '1':
              Errors:
                - If the layer value is not an instance of a string, then it raises an 'InstanceStringError' error.

              - If the last character in 'loop_layer' is equal to a newline/'\n', then it removes it from 'loop_layer'.

              - Then it will create the current layer with a generated UID to the value to the 'paint_layer' list and to
                the 'value' dictionary from the 'branches' dictionary.

            - If the length of the 'position' list is not equal to '1' and there is a value of the 'value' variable,
              then the first value from the 'position' list will be removed and the 'add_layer' function will be called
              again with the new value of the 'value' variable as argument.
        """
        if position[0] == "0":
            for loop_layer in argument_layer:
                if not isinstance(loop_layer, str):
                    raise InstanceStringError("layer", loop_layer)

                while True:
                    if loop_layer and loop_layer[-1] == "\n":
                        loop_layer = loop_layer[:-1]
                    else:
                        break

                uid_layer = loop_layer + generate_uid(branch)

                paint_layer[branch].update({uid_layer: []})
                branches[branch][list(branches[branch])[0]].update({uid_layer: {}})
            return

        count = 0

        for value in value.values():
            count = count + 1

            if count == int(position[0]):
                if len(position) == 1:
                    for loop_layer in argument_layer:
                        if not isinstance(loop_layer, str):
                            raise InstanceStringError("layer", loop_layer)

                        while True:
                            if loop_layer and loop_layer[-1] == "\n":
                                loop_layer = loop_layer[:-1]
                            else:
                                break

                        uid_layer = loop_layer + generate_uid(branch)

                        paint_layer[branch].update({uid_layer: []})
                        value.update({uid_layer: {}})
                    return
                else:
                    if value:
                        position.pop(0)
                        return self.create_layer(branch, argument_layer, position, value)
