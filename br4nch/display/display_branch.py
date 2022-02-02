# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

from br4nch.utility.utility_handler import InstanceBooleanError, InstanceStringError, NotExistingBranchError
from br4nch.utility.utility_librarian import branches, paint_branch, paint_header, paint_layer
from br4nch.utility.utility_builder import Builder
from br4nch.utility.utility_printer import printer


def arguments(branch, delete=False):
    """
    - Gets the arguments and parses them to the 'display_branch' function.
    """
    display_branch(branch, delete)


def display_branch(argument_branch, argument_delete):
    """
    Lists:
      - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.

    Errors:
      - If the delete value is not an instance of a boolean, then it raises an 'InstanceBooleanError' error.

    Operators:
      - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
        list.

    Argument branch list loop:
      Errors:
        - If the branch value is not an instance of a string, then it raises an 'InstanceStringError' error.
        - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

      Branches list loop:
        Paint validator:
          - If there is a value in the value of the key branch of the 'paint_branch' dictionary, then the first element
            in the list 'total' is updated with the value + 1.
          - If there is a value in the value of the key branch of the 'paint_header' dictionary, then the first element
            in the list 'total' is updated with the value + 1.
          - Then the 'paint_layer' is looped through with the value of the key branch. For each 'layer' value, it is
            checked whether that layer/value has a value in the 'paint_layer' dictionary with the key branch. If there
            is no value in the 'layer' key, then the 'no_paint' variable is added with the value + 1. If the value of
            the 'no_paint' variable is equal to the value of the length of the 'paint_layer' dictionary with the key
            branch, then the first element in the list 'total' is updated with the value + 1.
          - If the first element in the 'total' list is equal to '3', the 'colored' variable becomes 'false'. Otherwise
            the 'colored' variable becomes 'true'.

        - Calls the 'Builder' class with the current value of branch as argument.
        - Calls the 'printer' function with the 'display_branch' action and the current 'branches_branch' and
          'argument_delete' argument.
    """
    if not isinstance(argument_branch, list):
        argument_branch = [argument_branch]

    if not isinstance(argument_delete, bool):
        raise InstanceBooleanError("delete", argument_delete)

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

                total = [0]
                if not paint_branch[branches_branch]:
                    total[0] = total[0] + 1

                if not paint_header[branches_branch]:
                    total[0] = total[0] + 1

                no_paint = 0
                for layer in paint_layer[branches_branch]:
                    if not paint_layer[branches_branch][layer]:
                        no_paint = no_paint + 1

                if no_paint == len(paint_layer[branches_branch]):
                    total[0] = total[0] + 1

                if total[0] == 3:
                    colored = False
                else:
                    colored = True

                Builder(branches_branch, colored)
                printer("display_branch", [branches_branch], argument_delete)

        if error == 0:
            if branch:
                raise NotExistingBranchError(branch)
