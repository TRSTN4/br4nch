# Part of the br4nch package.

# Imports all files.
from br4nch.utility.builder.header import build_header
from br4nch.utility.unpacker import unpack_paint_builder
from br4nch.utility.unpacker import unpack_paint_clear
from br4nch.utility.librarian import paint_branch
from br4nch.utility.painter import painter


# Algorithm to build the branch.
def build_branch(branch, colors=True):
    if colors:
        # Returns the calculated paint clear value.
        paint_clear = unpack_paint_clear(branch)
        # Paint is equal to the returned clear paint value.
        branch_paint = paint_clear
    else:
        paint_clear = ""
        branch_paint = ""

    if paint_branch[branch] and colors:
        branch_paint = painter(paint_branch[branch], branch)
    else:
        branch_paint = ""

    # Runs the next task.
    build_header(branch, branch_paint, colors)
