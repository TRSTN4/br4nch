# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian


# Adds a new name for the branch.
def add_branch(branch):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    paper = librarian("paper")
    error = librarian("error")
    paint_package_branch = librarian("paint_package_branch")
    branch_symbols = librarian("branch_symbols")

    # Adds the branch values inside the dictionaries.
    branches.update({branch: {}})

    # Log lists to save output with branch as key and list as value.
    paper.update({branch: []})
    error.update({branch: []})

    # Sets the symbols to default symbols.
    branch_symbols.update({branch: {"line": "┃", "split": "┣━━", "end": "┗━━"}})

    # Checks if the current branch value is inside the paint package.
    if not paint_package_branch.get(branch):
        # Adds the current branch value as key and a new dictionary as value to the paint package.
        paint_package_branch.update({branch: {}})
