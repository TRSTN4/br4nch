# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.handler import NotExistingBranchError, MissingBranchError, MissingNameError


# Gets the parsed arguments.
def arguments(branch="", name=""):
    if not branch:
        raise MissingBranchError

    if not name:
        raise MissingNameError

    # Parses the arguments to the first task.
    replace_branch(branch, name)


# Adds a new name for the branch.
def replace_branch(branch, name):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    output = librarian("output")
    paint_package_branch = librarian("paint_package_branch")
    paint_package_header = librarian("paint_package_header")
    paint_package_layer = librarian("paint_package_layer")
    symbols = librarian("symbols")
    size = librarian("size")
    uids = librarian("uids")

    branch = str(branch)
    error = 0
    for y in list(branches):
        if branch.lower() == y.lower():
            error = error + 1

            branch = y

            branches[name] = branches.pop(branch)
            output[name] = output.pop(branch)
            size[name] = size.pop(branch)
            symbols[name] = symbols.pop(branch)
            paint_package_branch[name] = paint_package_branch.pop(branch)
            paint_package_header[name] = paint_package_header.pop(branch)
            paint_package_layer[name] = paint_package_layer.pop(branch)
            uids[name] = uids.pop(branch)

            for x in list(branches)[:-1]:
                branches[x] = branches.pop(x)
                output[x] = output.pop(x)
                size[x] = size.pop(x)
                symbols[x] = symbols.pop(x)
                paint_package_branch[x] = paint_package_branch.pop(x)
                paint_package_header[x] = paint_package_header.pop(x)
                paint_package_layer[x] = paint_package_layer.pop(x)
                uids[x] = uids.pop(x)

    if error == 0:
        raise NotExistingBranchError(branch)
