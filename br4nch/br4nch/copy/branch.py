# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.handler import StringInstanceError, InvalidBranchError, DuplicateBranchError, NotExistingBranchError
from br4nch.utility.librarian import branches, output, uids, sizes, symbols, paint_branch, paint_header, paint_layer


def arguments(branch, name, package=False):
    """
    - Gets the arguments and parses them to the 'copy_branch' function.
    """
    copy_branch(branch, name, package)


def copy_branch(argument_branch, argument_name, argument_package):
    """
    Errors:
      - If the branch value is not an instance of a string, then it raises an 'StringInstanceError' error.
      - If the name value is not an instance of a string, then it raises an 'StringInstanceError' error.
      - If the name value contains a character that is not a letter or number, then it raises an
        'InvalidBranchError' error.

    Branches list loop:
      Errors:
        - If the branch is already in the 'branches' dictionary, then it raises a 'DuplicateBranchError' error.

    Branches list loop:
      Errors:
        - If the branch value is not an instance of a string, then it raises an 'StringInstanceError' error.
        - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

    - If the value of the 'argument_package' variable is true, then update the values of all required dictionaries with
      the values of the given package argument.
    - If the value of the 'argument_package' variable is false, then update the values of all required dictionaries with
      the default values for a new branch.
    """
    if not isinstance(argument_branch, str):
        raise StringInstanceError("branch", argument_branch)

    if not isinstance(argument_name, str):
        raise StringInstanceError("name", argument_name)

    if not argument_name.isalnum():
        raise InvalidBranchError

    for branches_branch in list(branches):
        if argument_name.lower() == branches_branch.lower():
            raise DuplicateBranchError(argument_name)

    error = 0
    for branches_branch in list(branches):
        if argument_branch.lower() == branches_branch.lower():
            error = error + 1

            branches.update({argument_name: branches[argument_branch]})
            output.update({argument_name: []})

            if argument_package:
                uids.update({argument_name: uids[branches_branch]})
                sizes.update({argument_name: sizes[branches_branch]})
                symbols.update({argument_name: symbols[branches_branch]})
                paint_branch.update({argument_name: paint_branch[branches_branch]})
                paint_header.update({argument_name: paint_header[branches_branch]})
                paint_layer.update({argument_name: paint_layer[branches_branch]})
            else:
                uids.update({argument_name: []})
                sizes.update({argument_name: 1})
                symbols.update({argument_name: {"line": "┃", "split": "┣━━", "end": "┗━━"}})
                paint_branch.update({argument_name: {}})
                paint_header.update({argument_name: {}})
                paint_layer.update({argument_name: {}})

    if error == 0:
        raise NotExistingBranchError(argument_branch)
