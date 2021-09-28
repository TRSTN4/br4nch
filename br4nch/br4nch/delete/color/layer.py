# Part of the br4nch package.

# Imports all files.
from br4nch.utility.executor import executor


# Gets the parsed arguments.
def arguments(branch="", pos=""):
    # Runs the executor and deletes the parsed color layer.
    executor("delete_color_layer", [branch, pos])
