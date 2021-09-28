# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian


# Gets the parsed arguments.
def arguments(branch="", line="", split="", end=""):
    # Parses the arguments to the first task.
    symbol_branch(branch, line, split, end)


# Changes the symbols of the branch to the given input.
def symbol_branch(branch, line, split, end):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    symbols = librarian("symbols")
    output = librarian("output")
    error = librarian("error")

    # Checks if branch is not a instance of list.
    if not isinstance(branch, list):
        # Branch will be equal to a list that contains the value of branch.
        branch = [branch]

    if not branch[0]:
        for value in list(branches):
            branch.append(value)
        branch.pop(0)

    # Loops through all branches in the branch list.
    for branch in branch:
        for y in list(branches):
            if branch.lower() == y.lower():
                branch = y

                lineX = line
                splitX = split
                endX = end

                # Checks if not line.
                if not line:
                    # Line symbol is equal to one space.
                    lineX = symbols[branch]["line"]
                # Checks if not split.
                if not split:
                    # Split symbol is equal to one space.
                    splitX = symbols[branch]["split"]
                # Checks if not end.
                if not end:
                    # End symbol is equal to one space.
                    endX = symbols[branch]["end"]

                # Checks if branch is in the symbols dictionary.
                if branch in symbols:
                    # Updates the branch line symbol to the given input.
                    symbols[branch].update({"line": lineX})
                    # Updates the branch split symbol to the given input.
                    symbols[branch].update({"split": splitX})
                    # Updates the branch end symbol to the given input.
                    symbols[branch].update({"end": endX})

                error[branch].clear()
                output[branch].clear()
