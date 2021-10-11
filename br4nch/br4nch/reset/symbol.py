# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches, symbols
from br4nch.utility.handler import NotExistingBranchError


def arguments(branch):
    """Gets the arguments and parses them to the 'reset_symbol' function."""
    reset_symbol(branch)


def reset_symbol(argument_branch):
    """
    If the given branch argument is not an instance of a list, then the branch argument will be set as a list.

    If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch' list.

    Loops through the given 'argument_branch' list and checks if the value is already in the 'branches' dictionary. If
    the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

    If the branch is in the 'branches' dictionary, then it will update the current branch key in the 'symbols'
    dictionary with the standard values for 'line', 'split', 'end'.
    """

    if not isinstance(argument_branch, list):
        argument_branch = [argument_branch]

    if "*" in argument_branch:
        argument_branch.clear()
        for branches_branch in list(branches):
            argument_branch.append(branches_branch)

    for branch in argument_branch:
        error = 0
        for branches_branch in list(branches):
            if str(branch).lower() == branches_branch.lower():
                error = error + 1

                symbols.update({str(branches_branch): {"line": "┃", "split": "┣━━", "end": "┗━━"}})

        if error == 0:
            raise NotExistingBranchError(str(branch))
