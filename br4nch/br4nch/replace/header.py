# Part of the br4nch package.

# Imports all files.
from br4nch.utility.executor import executor


# Gets the parsed arguments.
def arguments(name, branch=""):
    # Runs the executor and replaces the parsed header.
    executor("replace_header", [branch, name])
