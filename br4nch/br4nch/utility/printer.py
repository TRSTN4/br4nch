# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian


# The printer prints all the results.
def printer():
    # Gets the needed lists/dictionaries.
    paper = librarian("paper")

    # Loops through all elements in the paper list.
    for ink in paper:
        # Prints the ink from the paper list.
        print(ink)

    # Clears the paper list.
    paper.clear()
