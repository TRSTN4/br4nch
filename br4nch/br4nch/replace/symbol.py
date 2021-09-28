# Part of the br4nch package.

# Imports all files.
from br4nch.utility.executor import executor


# Gets the parsed arguments.
def arguments(branch="", line="", split="", end=""):
    # Runs the executor and replaces the parsed symbol.
    executor("replace_symbol", [branch, line, split, end])
