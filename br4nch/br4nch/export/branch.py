# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches, uids, sizes, symbols, paint_branch, paint_header, paint_layer
from br4nch.utility.printer import printer
from br4nch.utility.handler import StringInstanceError, BooleanInstanceError, NotExistingBranchError


def arguments(branch, package=False, beautify=True):
    """Gets the arguments and parses them to the 'export_branch' function."""
    export_branch(branch, package, beautify)


def export_branch(argument_branch, argument_package, argument_beautify):
    """
    Lists:
      - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.

    Errors:
      - If the package value is not an instance of a boolean, then it raises an 'BooleanInstanceError' error.
      - If the beautify value is not an instance of a boolean, then it raises an 'BooleanInstanceError' error.

    Operators:
      - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
        list.

    Argument branch list loop:
      Errors:
        - If the branch value is not an instance of a string, then it raises an 'StringInstanceError' error.
        - If and the branch value is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

      Branches list loop:
        - If the branch is in the 'branches' dictionary, then it is checked whether the variable 'argument_package' is
          equal to true, if the variable is equal to true, then a dictionary is created with the values of all necessary
          dictionaries.
        - The 'printer' function is called with the 'display_export_branch' action that prints the given
          'branches_branch' dictionary and the 'branches_branch' package dictionary. If the 'argument_beautify' variable
          is false, the given dictionary(s) are not represented with a branch structure.
    """

    if not isinstance(argument_branch, list):
        argument_branch = [argument_branch]

    if not isinstance(argument_package, bool):
        raise BooleanInstanceError("package", argument_package)

    if not isinstance(argument_beautify, bool):
        raise BooleanInstanceError("beautify", argument_beautify)

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

                export_package = {}

                if argument_package:
                    export_package = {branches_branch: [uids[branches_branch], sizes[branches_branch],
                                                        symbols[branches_branch], paint_branch[branches_branch],
                                                        paint_header[branches_branch], paint_layer[branches_branch]]}

                printer("display_export_branch", [branches_branch,
                                                  {branches_branch: branches[branches_branch]},
                                                  export_package, argument_beautify])

        if error == 0:
            raise NotExistingBranchError(branch)
