# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian


# Changes the symbols of the branch to the given input.
def symbol_branch(branch, line="┃", split="┣━━", end="┗━━"):
    # Gets the needed lists/dictionaries.
    branch_symbols = librarian("branch_symbols")

    # Checks if branch is in the branch_symbols dict.
    if branch in branch_symbols:
        # Updates the branch line symbol to the given input.
        branch_symbols[branch].update({"line": line})
        # Updates the branch split symbol to the given input.
        branch_symbols[branch].update({"split": split})
        # Updates the branch end symbol to the given input.
        branch_symbols[branch].update({"end": end})
