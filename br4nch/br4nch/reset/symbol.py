# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches, symbols
from br4nch.utility.handler import BooleanInstanceError, StringInstanceError, NotExistingBranchError


def arguments(branch, line=True, split=True, end=True):
    """
    - Gets the arguments and parses them to the 'reset_symbol' function.
    """
    reset_symbol(branch, line, split, end)


def reset_symbol(argument_branch, argument_line, argument_split, argument_end):
    """
    Lists:
      - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.

    Operators:
      - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
        list.

    Argument branch list loop:
      Errors:
        - If the branch value is not an instance of a string, then it raises an 'StringInstanceError' error.
        - If the branch value is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

      Branches list loop:
        - If the branch is in the 'branches' dictionary, and one of the values of 'line', 'split' and/or 'end' is equal
          to 'True', then the default value(s) are used for the symbols. If the branch is in the dictionary 'branches',
          and one of the values of 'line', 'split' and/or 'end' is equals 'False', then the current value(s) are used
          for the symbols.
        - If the branch is in the 'branches' dictionary, then it will update the current branch key in the 'symbols'
          dictionary with the values for 'line', 'split', 'end'.
    """
    if not isinstance(argument_branch, list):
        argument_branch = [argument_branch]

    if not isinstance(argument_line, bool):
        raise BooleanInstanceError("line", argument_line)

    if not isinstance(argument_split, bool):
        raise BooleanInstanceError("split", argument_split)

    if not isinstance(argument_end, bool):
        raise BooleanInstanceError("end", argument_end)

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

                if argument_line:
                    argument_line = "┃"
                else:
                    argument_line = symbols[branches_branch]["line"]
                if argument_split:
                    argument_split = "┣━━"
                else:
                    argument_split = symbols[branches_branch]["split"]
                if argument_end:
                    argument_end = "┗━━"
                else:
                    argument_end = symbols[branches_branch]["end"]

                symbols.update({branches_branch: {"line": argument_line, "split": argument_split, "end": argument_end}})

        if error == 0:
            raise NotExistingBranchError(branch)
