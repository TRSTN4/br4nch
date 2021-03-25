# Imports all files.
from br4nch.utility.librarian import librarian


# Adds a new object for the branch.
def add_object(branch, header, module, subject, object):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")

    # Adds the object > subject > module > header > name inside the branch dictionary.
    branches[branch][header][module][subject].update({object: {}})
