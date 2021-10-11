# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import branches, output, uids, sizes, symbols, paint_branch, paint_header, paint_layer
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
    branch = str(branch)
    error = 0
    for y in list(branches):
        if branch.lower() == y.lower():
            error = error + 1

            branch = y

            index = list(branches).index(branch)

            branches[name] = branches.pop(branch)
            output[name] = output.pop(branch)
            sizes[name] = sizes.pop(branch)
            symbols[name] = symbols.pop(branch)
            paint_branch[name] = paint_branch.pop(branch)
            paint_header[name] = paint_header.pop(branch)
            paint_layer[name] = paint_layer.pop(branch)
            uids[name] = uids.pop(branch)

            for x in list(branches)[index:-1]:
                branches[x] = branches.pop(x)
                output[x] = output.pop(x)
                sizes[x] = sizes.pop(x)
                symbols[x] = symbols.pop(x)
                paint_branch[x] = paint_branch.pop(x)
                paint_header[x] = paint_header.pop(x)
                paint_layer[x] = paint_layer.pop(x)
                uids[x] = uids.pop(x)

    if error == 0:
        raise NotExistingBranchError(branch)
