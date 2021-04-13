# Part of the br4nch package.

# Imports all files.
from br4nch.utility.builder.branch import build_branch
from br4nch.utility.printer import printer


# Prints the chosen branches.
def display(branch):
    # Builds the chosen branches.
    build_branch(branch)
    # Prints the chosen branches.
    printer()
