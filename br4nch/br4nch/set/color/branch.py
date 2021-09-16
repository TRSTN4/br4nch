# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.painter import painter


# Gets the parsed arguments.
def arguments(branch, paint):
    # Parses the arguments to the first task.
    color_branch(branch, paint)


# Adds the chosen paint to the parsed branch.
def color_branch(branch, paint):
    # Gets the needed lists/dictionaries.
    paint_package_branch = librarian("paint_package_branch")

    # Checks if branch is not a instance of list.
    if not isinstance(branch, list):
        # Branch will be equal to a list that contains the value of branch.
        branch = [branch]

    # Loops through all branches in the branch list.
    for branch in branch:
        # Adds the branch as key and the paint as value to the paint package.
        paint_package_branch.update({branch: painter(paint, branch)})
