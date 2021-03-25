# Imports all files.
from br4nch.utility.librarian import librarian


# Adds a new module for the branch.
def add_module(branch, header, module):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")

    # Adds the module > header > name inside the branch dictionary.
    branches[branch][header].update({module: {}})
