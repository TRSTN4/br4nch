# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

# Imports all files.
from br4nch.utility.librarian import branches, paint_header
from br4nch.utility.handler import NotExistingBranchError


# Gets the parsed arguments.
def arguments(branch=""):
    # Parses the arguments to the first task.
    delete_color_header(branch)


def delete_color_header(branch):
    # Checks if branch is not a instance of list.
    if not isinstance(branch, list):
        # Branch will be equal to a list that contains the value of branch.
        branch = [branch]

    if not branch[0]:
        for value in list(branches):
            branch.append(value)
        branch.pop(0)
    # Loops through all branches in the branch list.
    for branch in branch:
        branch = str(branch)
        error = 0
        for y in list(branches):
            if branch.lower() == y.lower():
                error = error + 1

                branch = y

                paint_header.update({branch: {}})

        if error == 0:
            raise NotExistingBranchError(branch)
