# Part of the br4nch package.

# Imports all files.
from br4nch.utility.executor import executor


# Gets the parsed arguments.
def arguments(layer, branch="", pos=""):
    # Runs the executor and adds the parsed header.
    executor("add_layer", [branch, pos, layer])
