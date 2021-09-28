# Part of the br4nch package.

# Imports all files.
from br4nch.utility.executor import executor


# Gets the parsed arguments.
def arguments(paint, branch="", pos=""):
    # Runs the executor and replaces the parsed color layer.
    executor("replace_color_layer", [branch, pos, paint])
