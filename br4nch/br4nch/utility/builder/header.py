# Part of the br4nch package.

# Imports all files.
from br4nch.utility.builder.layer import configure
from br4nch.utility.inspector.paint import inspect_paint_clear
from br4nch.utility.inspector.paint import inspect_paint_base
from br4nch.utility.librarian import librarian


# Algorithm to build all the given headers.
def build_header(branch, paint_branch, newline):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    header_package = librarian("header_package")
    paper = librarian("paper")

    # Checks if content in package and returns the right paint clear value.
    paint_clear = inspect_paint_clear()

    # Checks if branch key in branch list has any value.
    if branches[branch]:
        # Loops through all headers in the header list.
        for header in branches[branch]:
            # Resets the paint after every loop.
            paint_header = paint_clear

            # Checks if inspect paint base returns a value.
            if inspect_paint_base(branch, header_package):
                # Paint is equal to the returned inspect paint base value.
                paint_header = inspect_paint_base(branch, header_package)

            # Uses prefix with the end line symbol and appends the output to the paper list.
            paper[branch].append(paint_clear + paint_header + newline + header + paint_clear + paint_branch + paint_clear)

            # Runs the next task.
            configure(branch)
