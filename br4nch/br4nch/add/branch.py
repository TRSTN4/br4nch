# Part of the br4nch package.

# Imports all files.
from br4nch.utility.executor import executor


# Gets the parsed arguments.
def arguments(branch):
    # Runs the executor and adds the parsed header.
    executor("add_branch", [branch])
