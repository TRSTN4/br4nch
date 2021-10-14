# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import branches, paint_header
from br4nch.utility.painter import painter
from br4nch.utility.handler import NotExistingBranchError, MissingPaintError


# Gets the parsed arguments.
def arguments(branch="", paint=""):
    if not paint:
        raise MissingPaintError

    # Parses the arguments to the first task.
    color_header(branch, paint)


# Adds the chosen paint to the parsed header.
def color_header(branch, paint):
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

                # Adds the branch as key and the paint as value to the paint package.
                paint_header.update({branch: paint})

        if error == 0:
            raise NotExistingBranchError(branch)
