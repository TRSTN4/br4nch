# Imports all files.
from br4nch.utility.librarian import librarian


# Manager runs all the needed tasks on start.
def manager():
    # Executes the "construction" action.
    librarian("construction")
