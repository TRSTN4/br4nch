# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

import os

from br4nch.utility.librarian import branches, uids, sizes, symbols, paint_branch, paint_header, paint_layer
from br4nch.utility.printer import printer
from br4nch.utility.handler import StringInstanceError, BooleanInstanceError, InvalidDirectoryError,\
    NotExistingBranchError


def arguments(branch, package=False, beautify=True, directory=""):
    """
    - Gets the arguments and parses them to the 'export_branch' function.
    """
    export_branch(branch, package, beautify, directory)


def export_branch(argument_branch, argument_package, argument_beautify, argument_directory):
    """
    Lists:
      - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.

    Errors:
      - If the package value is not an instance of a boolean, then it raises an 'BooleanInstanceError' error.
      - If the beautify value is not an instance of a boolean, then it raises an 'BooleanInstanceError' error.
      - If the directory value is not an instance of a string, then it raises an 'StringInstanceError' error.

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
        - Then it is checked whether the variable 'argument_directory' is equal to false, the 'printer' function is
          called with the 'export_branch' action that prints the given 'branches_branch' dictionary and the
          'branches_branch' package dictionary. If the 'argument_beautify' variable is false, the given dictionary(s)
          are not represented with a branch structure.

        If argument directory is equal to true:
          If the given directory exists:
            - Creates the custom br4nch directory if it does not exist in the given directory argument.
            - Appends the value of the branch in the 'branches' directory to a custom file in the custom br4nch folder.
            - If there is a value in the 'argument_package' argument, then adds the values of all required directories
              to a custom file in the custom br4nch folder.

          - If the given directory argument does not exist, it will throw a 'InvalidDirectoryError' error.
    """
    if not isinstance(argument_branch, list):
        argument_branch = [argument_branch]

    if not isinstance(argument_package, bool):
        raise BooleanInstanceError("package", argument_package)

    if not isinstance(argument_beautify, bool):
        raise BooleanInstanceError("beautify", argument_beautify)

    if not isinstance(argument_directory, str):
        raise StringInstanceError("directory", argument_directory)

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

                if not argument_directory:
                    printer("export_branch", [branches_branch, {branches_branch: branches[branches_branch]},
                                              export_package, argument_beautify])
                else:
                    if os.path.isdir(argument_directory):
                        if not os.path.isdir(argument_directory + "/br4nch-" + branches_branch):
                            os.mkdir(argument_directory + "/br4nch-" + branches_branch)

                        with open(argument_directory + "/br4nch-" + branches_branch + "/branch-" + branches_branch,
                                  'w') as file:
                            file.write(str({branches_branch: branches[branches_branch]}))

                        if argument_package:
                            with open(argument_directory + "/br4nch-" + branches_branch + "/package-" + branches_branch, 'w',
                                      encoding='utf-8') as file:
                                file.write(str(export_package))
                    else:
                        raise InvalidDirectoryError(argument_directory)

        if error == 0:
            raise NotExistingBranchError(branch)
