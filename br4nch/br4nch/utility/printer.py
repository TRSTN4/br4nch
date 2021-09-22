# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.handler import get_pos_result


# The printer prints the output after the branch has been build.
def printer(action):
    # Gets the needed lists/dictionaries.
    found_positions = librarian("found_positions")
    paper = librarian("paper")
    error = librarian("error")

    if action == "display_found":
        for layer, value in found_positions.copy().items():
            for branch, pos in value.items():
                print(get_pos_result(branch, layer[:-15], pos))
            del found_positions[layer]

    if action == "display_branch":
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
