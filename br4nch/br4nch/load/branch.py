# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches, output, uids, sizes, symbols, paint_branch, paint_header, paint_layer
from br4nch.utility.handler import DictionaryInstanceError, DuplicateBranchError


def arguments(branch, package=""):
    """Gets the arguments and parses them to the 'load_branch' function."""
    load_branch(branch, package)


def load_branch(argument_branch, argument_package):
    """
    Errors:
      - If the branch value is not an instance of a boolean, then it raises an 'BooleanInstanceError' error.
      - If the package value is not an instance of a boolean, then it raises an 'BooleanInstanceError' error.

    Branches list loop:
        Errors:
          - If the branch is already in the 'branches' dictionary, then it raises a 'DuplicateBranchError' error.

    - If the value of the 'argument_package' variable is true, then update the values of all required dictionaries with
      the values of the given package argument.
    - If the value of the 'argument_package' variable is false, then update the values of all required dictionaries with
      the default values for a new branch.
    """
    if not isinstance(argument_branch, dict):
        raise DictionaryInstanceError("branch", argument_branch)

    if argument_package and not isinstance(argument_package, dict):
        raise DictionaryInstanceError("package", argument_package)

    for branches_branch in list(branches):
        if list(argument_branch)[0].lower() == branches_branch.lower():
            raise DuplicateBranchError(list(argument_branch)[0])

    branches.update({list(argument_branch)[0]: list(argument_branch.values())[0]})
    output.update({list(argument_branch)[0]: []})

    if argument_package:
        uids.update({list(argument_branch)[0]: list(argument_package.values())[0][5]})
        sizes.update({list(argument_branch)[0]: list(argument_package.values())[0][4]})
        symbols.update({list(argument_branch)[0]: list(argument_package.values())[0][3]})
        paint_branch.update({list(argument_branch)[0]: list(argument_package.values())[0][0]})
        paint_header.update({list(argument_branch)[0]: list(argument_package.values())[0][1]})
        paint_layer.update({list(argument_branch)[0]: list(argument_package.values())[0][2]})
    else:
        uids.update({list(argument_branch[0]): []})
        sizes.update({list(argument_branch)[0]: 1})
        symbols.update({list(argument_branch)[0]: {"line": "┃", "split": "┣━━", "end": "┗━━"}})
        paint_branch.update({list(argument_branch)[0]: {}})
        paint_header.update({list(argument_branch)[0]: {}})
        paint_layer.update({list(argument_branch)[0]: {}})
