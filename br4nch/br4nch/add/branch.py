# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.handler import MissingBranchError, DuplicateBranchError


# Gets the parsed arguments.
def arguments(branch=""):
    if not branch:
        raise MissingBranchError

    # Parses the arguments to the first task.
    add_branch(branch)


# Adds a new name for the branch.
def add_branch(branch):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    output = librarian("output")
    paint_package_branch = librarian("paint_package_branch")
    paint_package_header = librarian("paint_package_header")
    paint_package_layer = librarian("paint_package_layer")
    symbols = librarian("symbols")
    size = librarian("size")
    uids = librarian("uids")

    # Checks if branch is not a instance of list.
    if not isinstance(branch, list):
        # Branch will be equal to a list that contains the value of branch.
        branch = [branch]

    # Loops through all branches in the branch list.
    for branch in branch:
        branch = str(branch)
        for y in list(branches):
            if branch.lower() == y.lower():
                raise DuplicateBranchError(branch)

        # Adds the branch values inside the dictionaries.
        branches.update({branch: {}})

        # Log lists to save output with branch as key and list as value.
        output.update({branch: []})

        size.update({branch: 1})

        uids.update({branch: []})

        # Sets the symbols to default symbols.
        symbols.update({branch: {"line": "┃", "split": "┣━━", "end": "┗━━"}})

        paint_package_branch.update({branch: {}})
        paint_package_header.update({branch: {}})
        paint_package_layer.update({branch: {}})
