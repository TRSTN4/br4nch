# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian


# Gets the parsed arguments.
def arguments(name, branch=""):
    # Parses the arguments to the first task.
    replace_header(name, branch)


# Adds a new name for the branch.
def replace_header(name, branch):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
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

                branches[branch][name] = branches[branch].pop(list(branches[branch])[0])
                error[branch].clear()
                output[branch].clear()
