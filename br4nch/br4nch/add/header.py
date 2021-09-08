# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.handler import add_header_error


# Adds a new header for the branch.
def add_header(branch, header):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    paint_package_header = librarian("paint_package_header")

    # Checks if the branch exists in the branches dictionary.
    if branch in branches:
        # Adds header inside the selected branch dictionary.
        branches[branch].update({header: {}})

        # Checks if the current branch value is inside the paint package.
        if not paint_package_header.get(branch):
            # Adds the current branch value as key and a new dictionary as value to the paint package.
            paint_package_header.update({branch: {}})
    # If the branch does not exists in the branches dictionary.
    else:
        # Runs a custom error.
        add_header_error(branch, header)
