# Part of the br4nch package.

# Imports all files.
from br4nch.utility.executor import executor


# Gets the parsed arguments.
def arguments(name, pos="", branch=""):
    # Runs the executor and replaces the parsed layer.
    executor("replace_layer", [branch, pos, name])
