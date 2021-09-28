# Part of the br4nch package.

# Imports all files.
from br4nch.utility.executor import executor


# Gets the parsed arguments.
def arguments(branch=""):
    # Runs the executor and deletes the parsed color branch.
    executor("delete_color_branch", [branch])
