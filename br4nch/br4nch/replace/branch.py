# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian


# Gets the parsed arguments.
def arguments(branch, name):
    # Parses the arguments to the first task.
    replace_branch(branch, name)


# Adds a new name for the branch.
def replace_branch(branch, name):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    output = librarian("output")
    error = librarian("error")
    paint_package_branch = librarian("paint_package_branch")
    paint_package_header = librarian("paint_package_header")
    paint_package_layer = librarian("paint_package_layer")
    symbols = librarian("symbols")
    size = librarian("size")
    uids = librarian("uids")

    for y in list(branches):
        if branch.lower() == y.lower():
            branches[name] = branches.pop(y)
            output[name] = output.pop(y)
            error[name] = error.pop(y)
            size[name] = size.pop(y)
            symbols[name] = symbols.pop(y)
            paint_package_branch[name] = paint_package_branch.pop(y)
            paint_package_header[name] = paint_package_header.pop(y)
            paint_package_layer[name] = paint_package_layer.pop(y)
            uids[name] = uids.pop(y)

            for x in list(branches)[:-1]:
                branches[x] = branches.pop(x)
                output[x] = output.pop(x)
                error[x] = error.pop(x)
                size[x] = size.pop(x)
                symbols[x] = symbols.pop(x)
                paint_package_branch[x] = paint_package_branch.pop(x)
                paint_package_header[x] = paint_package_header.pop(x)
                paint_package_layer[x] = paint_package_layer.pop(x)
                uids[x] = uids.pop(x)

            error[branch].clear()
            output[branch].clear()
