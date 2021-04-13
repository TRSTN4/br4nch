# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian


# Adds a new header for the branch.
def add_header(branch, header):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    header_package = librarian("header_package")

    # Adds header > name inside the branch dictionary.
    branches[branch].update({header: {}})

    # Checks if the current branch value is inside the dictionary.
    if not header_package.get(branch):
        # Adds the current branch value as key and a new dictionary as value to the package dictionary.
        header_package.update({branch: {}})
