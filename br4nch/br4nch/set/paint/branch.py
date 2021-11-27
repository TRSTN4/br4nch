# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches, paint_branch
from br4nch.utility.handler import StringInstanceError, NotExistingPaintError, NotExistingBranchError


def arguments(branch, paint):
    """
    - Gets the arguments and parses them to the 'set_paint_branch' function.
    """
    set_paint_branch(branch, paint)


def set_paint_branch(argument_branch, argument_paint):
    """
    Lists:
      - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.
      - If the given paint argument is not an instance of a list, then the paint argument will be set as a list.

    Errors:
      - If the paint value is not an instance of a string, then it raises an 'StringInstanceError' error.

    Operators:
      - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
        list.

    Argument branch list loop:
      Errors:
        - If the branch value is not an instance of a string, then it raises an 'StringInstanceError' error.
        - If the branch value is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

      Branches list loop:
        Errors:
          - If the paint element argument is not an instance of a string, then it raises an 'StringInstanceError' error.

        - If the branch is in the 'branches' dictionary, then it check if the 'paint' exists in the given list. If it
          does not exists, it raises a 'NotExistingPaintError' error. If it does exists in the list, it will add the
          'argument_paint' list to the 'paint_branch' list.
    """
    if not isinstance(argument_branch, list):
        argument_branch = [argument_branch]

    if not isinstance(argument_paint, list):
        argument_paint = [argument_paint]

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

                for paint in argument_paint:
                    if not isinstance(paint, str):
                        raise StringInstanceError("paint", paint)

                    if paint.lower() not in ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
                                             "bold", "underline", "reversing"]:
                        raise NotExistingPaintError(paint)

                paint_branch.update({branches_branch: argument_paint})

        if error == 0:
            raise NotExistingBranchError(branch)
