# Part of the br4nch package.

# Imports all files.
from br4nch.utility.builder.layer import configure
from br4nch.utility.unpacker import unpack_paint_builder
from br4nch.utility.unpacker import unpack_paint_clear
from br4nch.utility.librarian import librarian


# Algorithm to build the header.
def build_header(branch, paint_branch):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    paint_package_header = librarian("paint_package_header")
    paper = librarian("paper")

    # Returns the calculated paint clear value.
    paint_clear = unpack_paint_clear(branch)
    # Paint is equal to the returned clear paint value.
    paint_header = paint_clear

    # Checks if branch exists in branches dictionary.
    if branches[branch]:
        # Gets the header of the parsed branch.
        header = list(branches[branch].keys())[0]

        # Checks if the unpacker returns a value.
        if unpack_paint_builder(branch, paint_package_header):
            # Paint is equal to the returned unpacked value.
            paint_header = unpack_paint_builder(branch, paint_package_header)

        # Appends the current header branch line to the branch paper list.
        paper[branch].append(paint_clear + paint_header + header + paint_clear + paint_branch + paint_clear)

        # Runs the next task.
        configure(branch, paint_branch)
