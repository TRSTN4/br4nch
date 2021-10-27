# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches, sizes, symbols
from br4nch.utility.handler import NotExistingBranchError, StringInstanceError, IntegerInstanceError


def arguments(branch, size=1):
    """Gets the arguments and parses them to the 'set_size' function."""
    set_size(branch, size)


def set_size(argument_branch, argument_size):
    """
    Lists:
      - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.

    Errors:
      - If the size value is not an instance of a integer, then it raises an 'IntegerInstanceError' error.

    Operators:
      - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
        list.

    Argument branch list loop:
      Errors:
        - If the branch value is not an instance of a string, then it raises an 'StringInstanceError' error.
        - If the branch value is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

      Branches list loop:
        - If the branch is in the 'branches' dictionary, it checks if the rule variables are default and if so, the
          horizontal line is added times the value of the variable 'argument_size'.
    """

    if not isinstance(argument_branch, list):
        argument_branch = [argument_branch]

    if not isinstance(argument_size, int):
        raise IntegerInstanceError("size", argument_size)

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

                if symbols[branches_branch]["split"] == "┣━━":
                    symbols[branches_branch]["split"] = "┣━" + "━" * argument_size
                if symbols[branches_branch]["end"] == "┗━━":
                    symbols[branches_branch]["end"] = "┗━" + "━" * argument_size

                sizes.update({branches_branch: argument_size})

        if error == 0:
            raise NotExistingBranchError(branch)
