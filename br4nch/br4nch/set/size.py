# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.handler import NotExistingBranchError, InvalidSizeError


# Gets the parsed arguments.
def arguments(branch="", size=1):
    # Parses the arguments to the first task.
    set_size(branch, size)


def set_size(branch, number):
    # Gets the needed lists/dictionaries.
    size = librarian("size")
    branches = librarian("branches")
    symbols = librarian("symbols")

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
        number = str(number)
        error = 0
        for y in list(branches):
            if branch.lower() == y.lower():
                error = error + 1

                branch = y

                if number.isdecimal():
                    number = int(number)
                else:
                    raise InvalidSizeError(number)

                if symbols[branch]["split"] == "┣━━":
                    symbols[branch]["split"] = "┣━" + "━" * number
                if symbols[branch]["end"] == "┗━━":
                    symbols[branch]["end"] = "┗━" + "━" * number

                size.update({branch: number})

        if error == 0:
            raise NotExistingBranchError(branch)
