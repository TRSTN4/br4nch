# Part of the br4nch package.

# Imports all files.
from br4nch.utility.executor import executor


# Gets the parsed arguments.
def arguments(branch, name):
    # Runs the executor and replaces the parsed branch.
    executor("replace_branch", [branch, name])
