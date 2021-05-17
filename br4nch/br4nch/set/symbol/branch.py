# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian


def symbol_branch(branch, line="┃", split="┣━━", end="┗━━"):
    branch_symbols = librarian("branch_symbols")

    if branch in branch_symbols:
        branch_symbols[branch].update({"line": line})
        branch_symbols[branch].update({"split": split})
        branch_symbols[branch].update({"end": end})
