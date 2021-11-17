# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches, output, uids, sizes, symbols, paint_branch, paint_header, paint_layer
from br4nch.utility.handler import DuplicateBranchError, InvalidBranchError, StringInstanceError


def arguments(branch, name):
    """Gets the arguments and parses them to the 'replace_branch' function."""
    replace_branch(branch, name)


def replace_branch(argument_branch, argument_name):
    """
    Argument branch list loop:
      Errors:
        - If the branch value is not an instance of a string, then it raises an 'StringInstanceError' error.
        - If the name value is not an instance of a string, then it raises an 'StringInstanceError' error.
        - If the branch value contains a character that is not a letter or number, then it raises an
          'InvalidBranchError' error.

      Branches list loop:
        Errors:
          - If the branch is already in the 'branches' dictionary, then it raises a 'DuplicateBranchError' error.

      - The index of the given branch in the 'branches' list is stored in the variable 'index'.
      - Deletes the given branch and creates a new one with the given name and the copied values from the given branch.
      - To keep the order the same, a loop will be made that loops through the branches with the given slice values,
        removing all values and adding them again.
    """
    if not isinstance(argument_branch, str):
        raise StringInstanceError("branch", argument_branch)

    if not isinstance(argument_name, str):
        raise StringInstanceError("name", argument_name)

    if not argument_name.isalnum():
        raise InvalidBranchError

    for branches_branch in list(branches):
        if argument_name.lower() == branches_branch.lower():
            raise DuplicateBranchError(argument_branch)

    index = list(branches).index(argument_branch)

    branches[argument_name] = branches.pop(argument_branch)
    output[argument_name] = output.pop(argument_branch)
    sizes[argument_name] = sizes.pop(argument_branch)
    symbols[argument_name] = symbols.pop(argument_branch)
    paint_branch[argument_name] = paint_branch.pop(argument_branch)
    paint_header[argument_name] = paint_header.pop(argument_branch)
    paint_layer[argument_name] = paint_layer.pop(argument_branch)
    uids[argument_name] = uids.pop(argument_branch)

    for position in list(branches)[index:-1]:
        branches[position] = branches.pop(position)
        output[position] = output.pop(position)
        sizes[position] = sizes.pop(position)
        symbols[position] = symbols.pop(position)
        paint_branch[position] = paint_branch.pop(position)
        paint_header[position] = paint_header.pop(position)
        paint_layer[position] = paint_layer.pop(position)
        uids[position] = uids.pop(position)
