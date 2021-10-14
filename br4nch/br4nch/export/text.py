# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

import os

from br4nch.utility.librarian import branches, output
from br4nch.utility.builder.branch import build_branch
from br4nch.utility.handler import StringInstanceError, InvalidDirectoryError, NotExistingBranchError


def arguments(branch, directory):
    """Gets the arguments and parses them to the 'export_text' function."""
    export_text(branch, directory)


def export_text(argument_branch, argument_directory):
    """
    Lists:
      - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.

    Errors:
      - If the directory value is not an instance of a string, then it raises an 'StringInstanceError' error.

    Operators:
      - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
        list.

    Argument branch list loop:
      Errors:
        - If the branch value is not an instance of a string, then it raises an 'StringInstanceError' error.
        - If and the branch value is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

      Branches list loop:
        Errors:
          - If the given directory argument does not exist, it will throw a 'InvalidDirectoryError' error.

        If the given directory exists:
          - Creates a new file with a custom name of the value of branch
          - Calls the 'build_branch' function to create the branch's 'output' variable.
          - Loops through the output of the branch and appends each element in the last to the file with a new line.
          - Clears the output list from the value of branch.
    """

    if not isinstance(argument_branch, list):
        argument_branch = [argument_branch]

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

                if os.path.isdir(argument_directory):
                    with open(argument_directory + "/branch-" + branch + ".txt", 'w', encoding='utf-8') as file:
                        build_branch(branch, False)
                        for line in output[branch]:
                            file.write(line + "\n")
                        output[branch].clear()
                else:
                    raise InvalidDirectoryError(argument_directory)

        if error == 0:
            raise NotExistingBranchError(branch)
