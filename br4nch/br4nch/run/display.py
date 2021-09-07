# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.builder.branch import build_branch
from br4nch.utility.printer import printer
from br4nch.utility.handler import display_error


# Prints and builds the chosen branches.
def display(branch=""):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")

    if isinstance(branch, list):
        for branch in branch:
            if branch in branches:
                # Builds the chosen branches.
                build_branch(branch)
            else:
                display_error(branch)

        # Prints the chosen branches.
        printer()
    else:
        if branch in branches or not branch:
            if not branch:
                for branch in branches:
                    # Builds the chosen branches.
                    build_branch(branch)
            else:
                build_branch(branch)

            # Prints the chosen branches.
            printer()
        else:
            display_error(branch)
