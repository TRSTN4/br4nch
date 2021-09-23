# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.builder.branch import build_branch
from br4nch.utility.printer import printer
from br4nch.utility.handler import display_error


# Gets the parsed arguments.
def arguments(branch="", delete=False):
    # Parses the arguments to the first task.
    display_branch(branch, delete)


# Prints and builds the chosen branches.
def display_branch(branch, delete):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    output = librarian("output")

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

                if not output[branch]:
                    # Builds the chosen branches.
                    build_branch(branch)

                # Prints the chosen branches.
                printer("display_branch", branch, delete)
