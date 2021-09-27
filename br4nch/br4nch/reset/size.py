# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian


# Gets the parsed arguments.
def arguments(branch=""):
    # Parses the arguments to the first task.
    reset_size(branch)


def reset_size(branch):
    # Gets the needed lists/dictionaries.
    size = librarian("size")
    branches = librarian("branches")
    error = librarian("error")
    output = librarian("output")

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

                size.update({branch: 1})
                error[branch].clear()
                output[branch].clear()
