# Part of the br4nch package.

# Imports all files.
from br4nch.utility.executor import executor


# Gets the parsed arguments.
def arguments(branch="", size=0):
    # Runs the executor and sets the parsed size.
    executor("set_size", [branch, size])
