# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.painter import painter


# Gets the parsed arguments.
def arguments(paint, branch=""):
    # Parses the arguments to the first task.
    replace_color_branch(branch, paint)


def replace_color_branch(branch, paint):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    paint_package_branch = librarian("paint_package_branch")
    output = librarian("output")
    error = librarian("error")

    # Checks if branch is not a instance of list.
    if not isinstance(branch, list):
        # Branch will be equal to a list that contains the value of branch.
        branch = [branch]

    if not branch[0]:
        for value in list(branches):
            branch.append(value)
        branch.pop(0)
    # Loops through all branches in the branch list.
    for branch in branch:
        for y in list(branches):
            if branch.lower() == y.lower():
                branch = y
                paint_package_branch.update({branch: painter(paint, branch)})

                error[branch].clear()
                output[branch].clear()
