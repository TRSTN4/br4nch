# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.builder.branch import build_branch
from br4nch.utility.printer import printer
from br4nch.utility.handler import display_error


# Gets the parsed arguments.
def arguments(branch=""):
    # Parses the arguments to the first task.
    display_branch(branch)


# Prints and builds the chosen branches.
def display_branch(branch):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")

    # Checks if branch is not a instance of list.
    if not isinstance(branch, list):
        # Branch will be equal to a list that contains the value of branch.
        branch = [branch]

    if not branch[0]:
        for value in list(branches):
            branch.append(value)
        branch.pop(0)

    # Loops through all branches in the parsed branch value.
    for branch in branch:
        for y in list(branches):
            if branch.lower() == y.lower():
                branch = y

                # Builds the chosen branches.
                build_branch(y)

    # Prints the chosen branches.
    printer("display_branch")
