# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

from br4nch.utility.utility_librarian import branches, output, uids, sizes, symbols, paint_branch, paint_header, \
    paint_layer
from br4nch.utility.utility_handler import InstanceStringError, NotExistingBranchError


def arguments(branch):
    """
    - Gets the arguments and parses them to the 'delete_branch' function.
    """
    delete_branch(branch)


def delete_branch(argument_branch):
    """
    Lists:
      - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.

    Operators:
      - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
        list.

    Branches list loop:
      Errors:
        - If the branch value is not an instance of a string, then it raises an 'InstanceStringError' error.
        - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

      - If the branch is in the 'branches' dictionary, then it will delete the current branch key in all the mandatory
        dictionaries.
    """
    if not isinstance(argument_branch, list):
        argument_branch = [argument_branch]

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

                del branches[branches_branch]
                del output[branches_branch]
                del uids[branches_branch]
                del sizes[branches_branch]
                del symbols[branches_branch]
                del paint_branch[branches_branch]
                del paint_header[branches_branch]
                del paint_layer[branches_branch]

        if error == 0:
            if branch:
                raise NotExistingBranchError(branch)
