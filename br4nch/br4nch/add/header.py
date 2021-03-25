# Imports all files.
from br4nch.utility.librarian import librarian


# Adds a new header for the branch.
def add_header(branch, header):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")

    # Adds header > name inside the branch dictionary.
    branches[branch].update({header: {}})
