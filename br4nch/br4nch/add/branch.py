# Imports all files.
from br4nch.utility.librarian import librarian


# Adds a new name for the branch.
def add_branch(branch):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    positions = librarian("positions")

    # Adds the branch inside the branches dictionary.
    branches.update({branch: {}})

    # Adds the branch inside the positions dictionary.
    positions.update({branch: {}})
