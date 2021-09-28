# Part of the br4nch package.

# Imports all files.
from br4nch.utility.executor import executor


# Gets the parsed arguments.
def arguments(paint, branch=""):
    # Runs the executor and sets the parsed color header.
    executor("set_color_header", [branch, paint])
