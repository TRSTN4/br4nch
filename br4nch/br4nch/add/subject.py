# Imports all files.
from br4nch.utility.librarian import librarian


# Adds a new subject for the branch.
def add_subject(branch, header, module, subject):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")

    # Adds the subject > module > header > name inside the branch dictionary.
    branches[branch][header][module].update({subject: {}})
