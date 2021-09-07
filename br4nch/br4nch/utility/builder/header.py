# Part of the br4nch package.

# Imports all files.
from br4nch.utility.builder.layer import configure
from br4nch.utility.unpacker import unpack_paint_builder
from br4nch.utility.unpacker import unpack_paint_clear
from br4nch.utility.librarian import librarian


# Algorithm to build all the given headers.
def build_header(branch, paint_branch):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    paint_package_header = librarian("paint_package_header")
    paper = librarian("paper")

    # Checks if content in package and returns the right paint clear value.
    paint_clear = unpack_paint_clear(branch)

    # Checks if branch key in branch list has any value.
    if branches[branch]:
        # Loops through all headers in the header list.
        for header in branches[branch]:
            # Resets the paint after every loop.
            paint_header = paint_clear

            # Checks if inspect paint base returns a value.
            if unpack_paint_builder(branch, paint_package_header):
                # Paint is equal to the returned inspect paint base value.
                paint_header = unpack_paint_builder(branch, paint_package_header)

            # Uses prefix with the end line symbol and appends the output to the paper list.
            paper[branch].append(paint_clear + paint_header + header + paint_clear + paint_branch + paint_clear)

            # Runs the next tasks.
            configure(branch)
