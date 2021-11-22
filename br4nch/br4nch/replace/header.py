# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches
from br4nch.utility.handler import NotExistingBranchError, StringInstanceError


def arguments(branch, name):
    """
    - Gets the arguments and parses them to the 'replace_header' function.
    """
    replace_header(branch, name)


def replace_header(argument_branch, argument_name):
    """
    Lists:
      - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.

    Errors:
      - If the name argument is not an instance of a string, then it raises an 'StringInstanceError' error.

    Operators:
      - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
        list.

    Branches list loop:
      Errors:
        - If the branch value is not an instance of a string, then it raises an 'StringInstanceError' error.
        - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

      - Deletes the given header and creates a new one with the given name and the copied values from the given header.
    """
    if not isinstance(argument_branch, list):
        argument_branch = [argument_branch]

    if not isinstance(argument_name, str):
        raise StringInstanceError("name", argument_name)

    if "*" in argument_branch:
        argument_branch.clear()
        for branches_branch in list(branches):
            argument_branch.append(branches_branch)

    for branch in argument_branch:
        error = 0

        if not isinstance(branch, str):
            raise StringInstanceError("branch", branch)

        for branches_branch in list(branches):
            if branch.lower() == branches_branch.lower():
                error = error + 1

                branches[branches_branch][argument_name] = \
                    branches[branches_branch].pop(list(branches[branches_branch])[0])

        if error == 0:
            raise NotExistingBranchError(branch)
