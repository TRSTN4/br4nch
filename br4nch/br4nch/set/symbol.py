# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.handler import StringInstanceError, RequiredChangeError, NotExistingBranchError
from br4nch.utility.librarian import branches, symbols


def arguments(branch, line="", split="", end=""):
    """
    - Gets the arguments and parses them to the 'set_symbol' function.
    """
    set_symbol(branch, line, split, end)


def set_symbol(argument_branch, argument_line, argument_split, argument_end):
    """
    Lists:
      - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.

    Errors:
      - If the line value is not an instance of a string, then it raises an 'StringInstanceError' error.
      - If the split value is not an instance of a string, then it raises an 'StringInstanceError' error.
      - If the end value is not an instance of a string, then it raises an 'StringInstanceError' error.
      - If there is no value in the 'line', 'split' and 'end' arguments, then it raises an 'RequiredChangeError' error.

    Operators:
      - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
        list.

    Argument branch list loop:
      Errors:
        - If the branch value is not an instance of a string, then it raises an 'StringInstanceError' error.
        - If the branch value is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

      Branches list loop:
        - If there is no value in any of the 'line', 'split' or 'end' arguments, the value that is currently active of
          the missing arguments is used.
        - If the branch is in the 'branches' dictionary, then all values of the symbol arguments are added to the
          required directories.
    """
    if not isinstance(argument_branch, list):
        argument_branch = [argument_branch]

    if not isinstance(argument_line, str):
        raise StringInstanceError("line", argument_line)

    if not isinstance(argument_split, str):
        raise StringInstanceError("split", argument_split)

    if not isinstance(argument_end, str):
        raise StringInstanceError("end", argument_end)

    if not argument_line and not argument_split and not argument_end:
        raise RequiredChangeError

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

                if not argument_line:
                    argument_line = symbols[branches_branch]["line"]
                if not argument_split:
                    argument_split = symbols[branches_branch]["split"]
                if not argument_end:
                    argument_end = symbols[branches_branch]["end"]

                symbols[branches_branch].update({"line": argument_line, "split": argument_split, "end": argument_end})

        if error == 0:
            raise NotExistingBranchError(branch)
