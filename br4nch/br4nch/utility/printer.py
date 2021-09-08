# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian


# The printer prints the output after the branch has been build.
def printer():
    # Gets the needed lists/dictionaries.
    paper = librarian("paper")
    error = librarian("error")

    # Queue for all the dictionaries that have to be printed.
    queue = [paper, error]

    # Loops through all output dictionaries from the queue.
    for output in queue:
        # Loops through all branches in the dictionary.
        for branch, lines in output.copy().items():
            # Loops through all the lines of a branch.
            for line in lines:
                # Prints the current line.
                print(line)
            # Deletes the current branch from the dictionary.
            del output[branch]
