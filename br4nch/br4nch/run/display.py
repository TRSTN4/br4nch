# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.builder.branch import build_branch
from br4nch.utility.printer import printer
from br4nch.utility.handler import display_error


# Gets the parsed arguments.
def arguments(branch=""):
    # Parses the arguments to the first task.
    display(branch)


# Prints and builds the chosen branches.
def display(branch):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")

    # Checks if the branch value is a list.
    if isinstance(branch, list):
        # Loops through all branches in the parsed branch value.
        for branch in branch:
            # Checks if the branch exists in the branches dictionary.
            if branch in branches:
                # Builds the chosen branches.
                build_branch(branch)
            # If the branch does not exists in the branches dictionary.
            else:
                # Runs a custom error.
                display_error(branch)

        # Prints the chosen branches.
        printer()
    # If the branch value is not a list.
    else:
        # Checks if the branch exists in the branches dictionary or if the parsed branch value has no content.
        if branch in branches or not branch:
            # Checks if the branch value has no content.
            if not branch:
                # Loops through all branches in the parsed branch value.
                for branch in branches:
                    # Builds the chosen branches.
                    build_branch(branch)
            # If the branch value has content.
            else:
                # Builds the chosen branches.
                build_branch(branch)

            # Prints the chosen branches.
            printer()
        # If the branch does not exists in the branches dictionary or if the parsed branch value has content.
        else:
            # Runs a custom error.
            display_error(branch)
