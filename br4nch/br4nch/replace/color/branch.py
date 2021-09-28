# Part of the br4nch package.

# Imports all files.
from br4nch.utility.executor import executor


# Gets the parsed arguments.
def arguments(paint, branch=""):
    # Runs the executor and replaces the parsed color branch.
    executor("replace_color_branch", [branch, paint])
