# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

from br4nch.utility.utility_handler import InstanceIntegerError, InvalidSizeError, InstanceStringError, \
    NotExistingBranchError
from br4nch.utility.utility_librarian import branches, symbols, sizes


def arguments(branch, size):
    """
    - Gets the arguments and parses them to the 'set_size' function.
    """
    set_size(branch, size)


def set_size(argument_branch, argument_size):
    """
    Lists:
      - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.

    Errors:
      - If the size value is not an instance of a integer, then it raises an 'InstanceIntegerError' error.
      - If the size value is smaller than '0' or bigger than '20', then it raises an 'InvalidSizeError' error.

    Operators:
      - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
        list.

    Argument branch list loop:
      Errors:
        - If the branch value is not an instance of a string, then it raises an 'InstanceStringError' error.
        - If the branch value is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

      Branches list loop:
        - If the branch is in the 'branches' dictionary, it checks if the rule variables are default and if so, the
          horizontal line is added times the value of the variable 'argument_size'.
    """
    if not isinstance(argument_branch, list):
        argument_branch = [argument_branch]

    if not isinstance(argument_size, int):
        raise InstanceIntegerError("size", argument_size)

    if argument_size < 0 or argument_size > 20:
        raise InvalidSizeError

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

                if symbols[branches_branch]["split"] == "┣━":
                    symbols[branches_branch]["split"] = "┣━" + "━" * argument_size
                if symbols[branches_branch]["end"] == "┗━":
                    symbols[branches_branch]["end"] = "┗━" + "━" * argument_size

                sizes.update({branches_branch: argument_size})

        if error == 0:
            if branch:
                raise NotExistingBranchError(branch)
