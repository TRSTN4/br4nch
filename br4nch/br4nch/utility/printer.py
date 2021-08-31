# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian


# The printer prints all the results.
def printer():
    # Gets the needed lists/dictionaries.
    paper = librarian("paper")

    # Loops through all branches in the paper dict.
    for branch in paper.values():
        # Loops through all the content of the current branch value.
        for ink in branch:
            # Prints the ink from the branch paper content.
            print(ink)

    # Clears the paper list.
    paper.clear()
