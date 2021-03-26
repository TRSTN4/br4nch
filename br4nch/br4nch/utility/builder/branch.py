# Imports all files.
from br4nch.utility.builder.header import build_header
from br4nch.utility.inspector.paint import inspect_paint_clear
from br4nch.utility.inspector.paint import inspect_paint_base
from br4nch.utility.inspector.paint import inspect_paint_all_base
from br4nch.utility.librarian import librarian


# Algorithm to build all the given branches.
def build_branch(arg_branch):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    branch_package = librarian("branch_package")

    # Checks if content in package and returns the right paint clear value.
    paint_clear = inspect_paint_clear(branch_package)

    # Checks if the branch list has any value.
    if branches:
        # "stop" is equal to false.
        stop = False

        # Loops through all branches in the branch list.
        for branch in branches:
            # Resets the paint after every loop.
            paint_branch = paint_clear

            # Resets the newline after every loop.
            newline = ""

            # Checks if inspect paint base returns a value.
            if inspect_paint_base(branch, branch_package):
                # Paint is equal to the returned inspect paint base value.
                paint_branch = inspect_paint_base(branch, branch_package)

            # Checks if inspect paint base all returns a value.
            if inspect_paint_all_base(branch_package):
                # Paint is equal to the returned inspect paint base all value.
                paint_branch = inspect_paint_all_base(branch_package)

            # Checks if there are multiple branches in the list.
            if len(list(dict.keys(branches))) > 1:
                # Passes through every branch except first branch.
                if not branch == list(dict.keys(branches))[0]:
                    # When printing multiple branches, add a newline between every new branch.
                    newline = "\n"

            # Checks if "stop" is equal to true.
            if stop:
                # Breaks the loop and stops the algorithm.
                break

            # Checks the branch name argument is equal to "all".
            if arg_branch == "all":
                # Passes all the break statements and stops when the loop is complete.
                pass

            # If the branch name argument is not equal to "all".
            else:
                # Changes the current branch value to the value of the given branch name argument.
                branch = arg_branch
                # "stop" is set to true.
                stop = True

            # Runs the next task.
            build_header(branch, paint_branch, newline)
