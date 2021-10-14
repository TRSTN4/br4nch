# Part of the br4nch package.

# Imports all files.
from br4nch.utility.builder.layer import configure
from br4nch.utility.unpacker import unpack_paint_builder
from br4nch.utility.unpacker import unpack_paint_clear
from br4nch.utility.librarian import branches, output, paint_header
from br4nch.utility.painter import painter


# Algorithm to build the header.
def build_header(branch, paint_branch, colors):
    if colors:
        # Returns the calculated paint clear value.
        paint_clear = unpack_paint_clear(branch)
        # Paint is equal to the returned clear paint value.
        header_paint = paint_clear
    else:
        paint_clear = ""
        header_paint = ""

    # Checks if branch exists in branches dictionary.
    if branches[branch]:
        # Gets the header of the parsed branch.
        header = list(branches[branch].keys())[0]

        if paint_header[branch] and colors:
            header_paint = painter(paint_header[branch], branch)
        else:
            header_paint = ""

        # Appends the current header branch line to the branch paper list.
        output[branch].append(paint_clear + header_paint + header + paint_clear + paint_branch + paint_clear)

        # Runs the next task.
        configure(branch, paint_branch, colors)
