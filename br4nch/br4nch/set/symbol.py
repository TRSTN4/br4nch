# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.handler import NotExistingBranchError


# Gets the parsed arguments.
def arguments(branch="", line="┃", split="┣━━", end="┗━━"):
    # Parses the arguments to the first task.
    symbol_branch(branch, line, split, end)


# Changes the symbols of the branch to the given input.
def symbol_branch(branch, line, split, end):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    symbols = librarian("symbols")

    # Checks if not line.
    if not line:
        # Line symbol is equal to one space.
        line = " "
    # Checks if not split.
    if not split:
        # Split symbol is equal to one space.
        split = " "
    # Checks if not end.
    if not end:
        # End symbol is equal to one space.
        end = " "

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

                # Checks if branch is in the symbols dictionary.
                if branch in symbols:
                    # Updates the branch line symbol to the given input.
                    symbols[branch].update({"line": line})
                    # Updates the branch split symbol to the given input.
                    symbols[branch].update({"split": split})
                    # Updates the branch end symbol to the given input.
                    symbols[branch].update({"end": end})

        if error == 0:
            raise NotExistingBranchError(branch)
