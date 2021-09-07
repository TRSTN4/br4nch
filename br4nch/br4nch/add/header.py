# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.handler import add_header_error


# Adds a new header for the branch.
def add_header(branch, header):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    paint_package_header = librarian("paint_package_header")

    if branch in branches:
        # Adds header > name inside the branch dictionary.
        branches[branch].update({header: {}})

        # Checks if the current branch value is inside the dictionary.
        if not paint_package_header.get(branch):
            # Adds the current branch value as key and a new dictionary as value to the paint dictionary.
            paint_package_header.update({branch: {}})
    else:
        add_header_error(branch, header)
