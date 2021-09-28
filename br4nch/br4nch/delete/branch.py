# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian


# Gets the parsed arguments.
def arguments(branch=""):
    # Parses the arguments to the first task.
    delete_branch(branch)


def delete_branch(branch):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    paint_package_branch = librarian("paint_package_branch")
    paint_package_header = librarian("paint_package_header")
    paint_package_layer = librarian("paint_package_layer")
    symbols = librarian("symbols")
    output = librarian("output")
    error = librarian("error")
    size = librarian("size")
    uids = librarian("uids")

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

                del branches[branch]
                del paint_package_branch[branch]
                del paint_package_header[branch]
                del paint_package_layer[branch]
                del symbols[branch]
                del output[branch]
                del error[branch]
                del size[branch]
                del uids[branch]