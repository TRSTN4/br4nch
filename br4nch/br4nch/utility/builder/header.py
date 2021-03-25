# Imports all files.
from br4nch.utility.builder.module import build_module
from br4nch.utility.librarian import librarian
from br4nch.utility.branching import branching


# Algorithm to build all the given headers.
def build_header(branch, paint_branch, newline):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    header_package = librarian("header_package")
    paper = librarian("paper")

    # Checks if content in package.
    if header_package:
        # Resets the paint.
        paint_clear = "\u001b[0m"
    # If content not in package.
    else:
        # Sets the paint to nothing.
        paint_clear = ""

    # Checks if branch key in branch list has any value.
    if branches[branch]:
        # Loops through all headers in the header list.
        for header in branches[branch]:
            # Resets the paint after every loop.
            paint_header = paint_clear

            # Loops through all given packages inside the header package dictionary.
            for key in header_package:
                # Checks if the key is equal to the value of branch.
                if key == branch:
                    # Header paint is equal to the value of the branch inside the header package.
                    paint_header = header_package.get(branch)

            # Loops through all keys in the package directory.
            for key in header_package:
                # Checks if the key is equal to "all" string.
                if key == "all":
                    # Header paint is equal to the "all" value inside the header package.
                    paint_header = header_package.get("all")

            # Uses prefix with the end line symbol and appends the output to the paper list.
            paper.append(paint_clear + paint_header + newline + header + paint_clear + paint_branch +
                         branching("header_end", "") + paint_clear)

            # Runs the next task.
            build_module(branch, header, paint_branch)
