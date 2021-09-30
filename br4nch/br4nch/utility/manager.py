# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian


# Manager runs all the needed tasks on start.
def manager():
    # Executes the "construction" action for the librarian that creates the needed lists and dictionaries.
    librarian("construction")
