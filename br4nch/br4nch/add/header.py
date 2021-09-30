# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.handler import MissingHeaderError, NotExistingBranchError


# Gets the parsed arguments.
def arguments(branch="", header=""):
    if not header:
        raise MissingHeaderError

    # Parses the arguments to the first task.
    add_header(branch, header)


# Adds a new header for the branch.
def add_header(branch, header):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    paint_package_header = librarian("paint_package_header")

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
        branch = str(branch)
        error = 0
        for y in list(branches):
            if branch.lower() == y.lower():
                error = error + 1

                branch = y

                # Adds header inside the selected branch dictionary.
                branches[branch].update({header: {}})

                # Checks if the current branch value is inside the paint package.
                if not paint_package_header.get(branch):
                    # Adds the current branch value as key and a new dictionary as value to the paint package.
                    paint_package_header.update({branch: {}})

        if error == 0:
            raise NotExistingBranchError(branch)
