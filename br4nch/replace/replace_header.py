# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

from br4nch.utility.utility_handler import InstanceStringError, NotExistingBranchError
from br4nch.utility.utility_librarian import branches


def arguments(branch, replace):
    """
    - Gets the arguments and parses them to the 'replace_header' function.
    """
    replace_header(branch, replace)


def replace_header(argument_branch, argument_replace):
    """
    Lists:
      - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.

    Errors:
      - If the replace argument is not an instance of a string, then it raises an 'InstanceStringError' error.

    Operators:
      - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
        list.

    Branches list loop:
      Errors:
        - If the branch value is not an instance of a string, then it raises an 'InstanceStringError' error.
        - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

      - Deletes the given header and creates a new one with the given replace and the copied values from the given header.
    """
    if not isinstance(argument_branch, list):
        argument_branch = [argument_branch]

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

                branches[branches_branch][argument_replace] = \
                    branches[branches_branch].pop(list(branches[branches_branch])[0])

        if error == 0:
            if branch:
                raise NotExistingBranchError(branch)
