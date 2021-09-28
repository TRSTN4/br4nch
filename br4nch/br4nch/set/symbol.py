# Part of the br4nch package.

# Imports all files.
from br4nch.utility.executor import executor


# Gets the parsed arguments.
def arguments(branch="", line="┃", split="┣━━", end="┗━━"):
    # Runs the executor and sets the parsed color symbol.
    executor("set_symbol", [branch, line, split, end])
