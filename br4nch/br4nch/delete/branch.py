# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches, output, uids, sizes, symbols, paint_branch, paint_header, paint_layer
from br4nch.utility.handler import NotExistingBranchError


def arguments(branch):
    """Gets the arguments and parses them to the 'delete_branch' function."""
    delete_branch(branch)


def delete_branch(argument_branch):
    """
    If the given branch argument is not an instance of a list, then the branch argument will be set as a list.

    If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch' list.

    Loops through the given 'argument_branch' list and checks if the value is already in the 'branches' dictionary. If
    the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

    If the branch is in the 'branches' dictionary, then it will delete the current branch key in all the mandatory
    dictionaries.
    """

    if not isinstance(argument_branch, list):
        argument_branch = [argument_branch]

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

                del branches[branch]
                del output[branch]
                del uids[branch]
                del sizes[branch]
                del symbols[branch]
                del paint_branch[branch]
                del paint_header[branch]
                del paint_layer[branch]

        if error == 0:
            raise NotExistingBranchError(branch)
