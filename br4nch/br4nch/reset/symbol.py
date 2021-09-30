# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.handler import NotExistingBranchError


# Gets the parsed arguments.
def arguments(branch=""):
    # Parses the arguments to the first task.
    symbol_branch(branch)


# Changes the symbols of the branch to the given input.
def symbol_branch(branch):
    # Gets the needed lists/dictionaries.
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
        error = 0
        for y in list(branches):
            if branch.lower() == y.lower():
                error = error + 1

                branch = y

                symbols.update({branch: {"line": "┃", "split": "┣━━", "end": "┗━━"}})

        if error == 0:
            raise NotExistingBranchError(branch)
