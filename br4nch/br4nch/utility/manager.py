# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.handler import import_paint


# Manager runs all the needed tasks on start.
def manager():
    # Executes the "construction" action.
    librarian("construction")

    # Imports the paint for the handler script.
    import_paint()
