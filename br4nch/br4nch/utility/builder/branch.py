# Imports all files.
from br4nch.utility.builder.header import build_header
from br4nch.utility.librarian import librarian


# Algorithm to build all the given branches.
def build_branch(branch_name):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    branch_package = librarian("branch_package")

    # Resets the paint.
    paint_clear = "\u001b[0m"

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
            if branch_name == "all":
                # Passes all the break statements and stops when the loop is complete.
                pass

            # If the branch name argument is not equal to "all".
            else:
                # Changes the current branch value to the value of the given branch name argument.
                branch = branch_name
                # "stop" is set to true.
                stop = True

            # Loops through all keys in the package directory.
            for key in branch_package:
                # Checks if the key is equal to the value of branch.
                if key == branch:
                    # Branch paint is equal to the value of the key inside the branch package.
                    paint_branch = branch_package.get(branch)

            # Loops through all given packages inside the branch package dictionary.
            for key in branch_package:
                # Checks if the key is equal to "all" string.
                if key == "all":
                    # Branch paint is equal to the value of "all" inside the branch package.
                    paint_branch = branch_package.get("all")

            # Runs the next task.
            build_header(paint_branch, branch, newline)
