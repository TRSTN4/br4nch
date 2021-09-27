# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian


# Gets the parsed arguments.
def arguments(branch):
    # Parses the arguments to the first task.
    add_branch(branch)


# Adds a new name for the branch.
def add_branch(branch):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    output = librarian("output")
    error = librarian("error")
    paint_package_branch = librarian("paint_package_branch")
    symbols = librarian("symbols")
    size = librarian("size")
    uids = librarian("uids")

    # Checks if branch is not a instance of list.
    if not isinstance(branch, list):
        # Branch will be equal to a list that contains the value of branch.
        branch = [branch]

    # Loops through all branches in the branch list.
    for branch in branch:
        # Adds the branch values inside the dictionaries.
        branches.update({branch: {}})

        # Log lists to save output with branch as key and list as value.
        output.update({branch: []})
        error.update({branch: []})

        size.update({branch: 1})

        uids.update({branch: []})

        # Sets the symbols to default symbols.
        symbols.update({branch: {"line": "┃", "split": "┣━━", "end": "┗━━"}})

        # Checks if the current branch value is inside the paint package.
        if not paint_package_branch.get(branch):
            # Adds the current branch value as key and a new dictionary as value to the paint package.
            paint_package_branch.update({branch: {}})
