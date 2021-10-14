# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

import os
import ast

from br4nch.utility.librarian import branches, output, uids, sizes, symbols, paint_branch, paint_header, paint_layer
from br4nch.utility.handler import DictionaryInstanceError, DuplicateBranchError, InvalidBranchFileError,\
    InvalidPackageFileError


def arguments(branch, package=""):
    """Gets the arguments and parses them to the 'load_branch' function."""
    load_branch(branch, package)


def load_branch(argument_branch, argument_package):
    """
    Errors:
      - Raises an 'InvalidBranchFileError' error if the instance of the 'argument_branch' variable is a string and the
        given directory does not exists.
      - Raises an 'InvalidPackageFileError' error if there is value in the the 'argument_package' variable and is
        instance of string and the given directory does not exists.
      - If the branch value is not an instance of a boolean, then it raises an 'BooleanInstanceError' error.
      - If the package value is not an instance of a boolean, then it raises an 'BooleanInstanceError' error.

    - If the 'argument_branch' is instance of a string and the given directory exists, the content of the branch file
      will be assigned to the 'argument_branch' variable.
    - If there is a value in the 'argument_package' variable and instance of a string and the given directory exists,
      the content of the file package file will be assigned to the 'argument_package' variable.

    Branches list loop:
        Errors:
          - If the branch is already in the 'branches' dictionary, then it raises a 'DuplicateBranchError' error.

    - If the value of the 'argument_package' variable is true, then update the values of all required dictionaries with
      the values of the given package argument.
    - If the value of the 'argument_package' variable is false, then update the values of all required dictionaries with
      the default values for a new branch.
    """

    if isinstance(argument_branch, str) and not os.path.isfile(argument_branch):
        raise InvalidBranchFileError(argument_branch)
    elif isinstance(argument_branch, str) and os.path.isfile(argument_branch):
        with open(argument_branch, 'r') as file:
            argument_branch = ast.literal_eval(file.read())
    else:
        if not isinstance(argument_branch, dict):
            raise DictionaryInstanceError("branch", argument_branch)

    if argument_package and isinstance(argument_branch, str) and not os.path.isfile(argument_package):
        raise InvalidPackageFileError(argument_package)
    elif argument_package and isinstance(argument_package, str) and os.path.isfile(argument_package):
        with open(argument_package, 'r', encoding="utf8") as file:
            argument_package = ast.literal_eval(file.read())
    else:
        if argument_package and not isinstance(argument_package, dict):
            raise DictionaryInstanceError("package", argument_package)

    for branches_branch in list(branches):
        if list(argument_branch)[0].lower() == branches_branch.lower():
            raise DuplicateBranchError(list(argument_branch)[0])

    branches.update({list(argument_branch)[0]: list(argument_branch.values())[0]})
    output.update({list(argument_branch)[0]: []})

    if argument_package:
        uids.update({list(argument_branch)[0]: list(argument_package.values())[0][0]})
        sizes.update({list(argument_branch)[0]: list(argument_package.values())[0][1]})
        symbols.update({list(argument_branch)[0]: list(argument_package.values())[0][2]})
        paint_branch.update({list(argument_branch)[0]: list(argument_package.values())[0][3]})
        paint_header.update({list(argument_branch)[0]: list(argument_package.values())[0][4]})
        paint_layer.update({list(argument_branch)[0]: list(argument_package.values())[0][5]})
    else:
        uids.update({list(argument_branch)[0]: []})
        sizes.update({list(argument_branch)[0]: 1})
        symbols.update({list(argument_branch)[0]: {"line": "┃", "split": "┣━━", "end": "┗━━"}})
        paint_branch.update({list(argument_branch)[0]: {}})
        paint_header.update({list(argument_branch)[0]: {}})
        paint_layer.update({list(argument_branch)[0]: {}})
