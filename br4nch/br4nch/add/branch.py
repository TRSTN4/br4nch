# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches, output, uids, sizes, symbols, paint_branch, paint_header, paint_layer
from br4nch.utility.handler import StringInstanceError, InvalidBranchError, DuplicateBranchError


def arguments(branch):
    """Gets the arguments and parses them to the 'add_branch' function."""
    add_branch(branch)


def add_branch(argument_branch):
    """
    Lists:
      - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.

    Argument branch list loop:
      Errors:
        - If the branch value is not an instance of a string, then it raises an 'StringInstanceError' error.
        - If the branch value contains a character that is not a letter or number, then it raises an
          'InvalidBranchError' error.

      Branches list loop:
        Errors:
          - If the branch is already in the 'branches' dictionary, then it raises a 'DuplicateBranchError' error.

      - Then it will add the current branch key in all the mandatory dictionaries with a empty dictionary as value.
    """

    if not isinstance(argument_branch, list):
        argument_branch = [argument_branch]

    for branch in argument_branch:
        if not isinstance(branch, str):
            raise StringInstanceError("branch", branch)

        if not branch.isalnum():
            raise InvalidBranchError

        for branches_branch in list(branches):
            if branch.lower() == branches_branch.lower():
                raise DuplicateBranchError(branch)

        branches.update({branch: {}})
        output.update({branch: []})
        uids.update({branch: []})
        sizes.update({branch: 1})
        symbols.update({branch: {"line": "┃", "split": "┣━━", "end": "┗━━"}})
        paint_branch.update({branch: {}})
        paint_header.update({branch: {}})
        paint_layer.update({branch: {}})
