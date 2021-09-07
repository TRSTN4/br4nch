# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian


# The printer prints all the requested actions.
def printer():
    # Gets the needed lists/dictionaries.
    paper = librarian("paper")
    error = librarian("error")

    # Loops through all branches in the paper dict.
    for key, value in paper.copy().items():
        # Loops through all the content of the current branch value.
        for ink in value:
            # Prints the ink from the branch paper content.
            print(ink)
        del paper[key]

    for key, value in error.copy().items():
        for ink in value:
            print(ink)
        del error[key]

    # Clears the paper list.
    paper.clear()
