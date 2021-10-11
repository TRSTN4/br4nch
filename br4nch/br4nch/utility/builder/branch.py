# Part of the br4nch package.

# Imports all files.
from br4nch.utility.builder.header import build_header
from br4nch.utility.unpacker import unpack_paint_builder
from br4nch.utility.unpacker import unpack_paint_clear
from br4nch.utility.librarian import paint_branch


# Algorithm to build the branch.
def build_branch(branch):
    # Returns the calculated paint clear value.
    paint_clear = unpack_paint_clear(branch)
    # Paint is equal to the returned clear paint value.
    branch_paint = paint_clear

    # Checks if the unpacker returns a value.
    if unpack_paint_builder(branch, paint_branch):
        # Paint is equal to the returned unpacked value.
        branch_paint = unpack_paint_builder(branch, paint_branch)

    # Runs the next task.
    build_header(branch, branch_paint)
