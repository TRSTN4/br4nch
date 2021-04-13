# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian


# Adds a new name for the branch.
def add_branch(branch):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    branch_package = librarian("branch_package")

    # Adds the branch inside the branches dictionary.
    branches.update({branch: {}})

    # Checks if the current branch value is inside the dictionary.
    if not branch_package.get(branch):
        # Adds the current branch value as key and a new dictionary as value to the package dictionary.
        branch_package.update({branch: {}})
