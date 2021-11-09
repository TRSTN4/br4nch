# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches
from br4nch.utility.builder.branch import build_branch
from br4nch.utility.printer import printer
from br4nch.utility.handler import NotExistingBranchError, StringInstanceError, BooleanInstanceError


def arguments(branch, delete=False):
    """Gets the arguments and parses them to the 'display_branch' function."""
    display_branch(branch, delete)


def display_branch(argument_branch, argument_delete):
    """
    Lists:
      - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.

    Errors:
      - If the delete value is not an instance of a boolean, then it raises an 'BooleanInstanceError' error.

    Operators:
      - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
        list.

    Argument branch list loop:
      Errors:
        - If the branch value is not an instance of a string, then it raises an 'StringInstanceError' error.
        - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

      Branches list loop:
        - Calls the 'build_branch' function with the current value of branch as argument.
        - Calls the 'printer' function with the 'display_branch' action and the current 'branches_branch' and
          'argument_delete' argument.
    """

    if not isinstance(argument_branch, list):
        argument_branch = [argument_branch]

    if not isinstance(argument_delete, bool):
        raise BooleanInstanceError("delete", argument_delete)

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

                build_branch(branches_branch)

                printer("display_branch", [branches_branch], argument_delete)

        if error == 0:
            raise NotExistingBranchError(branch)
