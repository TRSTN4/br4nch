# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.handler import NotExistingBranchError
from br4nch.utility.printer import printer


# Gets the parsed arguments.
def arguments(branch="", file="", package=""):
    # Parses the arguments to the first task.
    export(branch, file, package)


def export(branch, file, package):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    paint_package_branch = librarian("paint_package_branch")
    paint_package_header = librarian("paint_package_branch")
    paint_package_layer = librarian("paint_package_branch")
    symbols = librarian("symbols")
    size = librarian("size")
    uids = librarian("uids")

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

                export_branch = {branch: branches[branch]}

                if package:
                    export_package = {branch: [paint_package_branch[branch], paint_package_header[branch],
                                               paint_package_layer[branch], symbols[branch], size[branch],
                                               uids[branch]]}
                else:
                    export_package = {}

                if file:
                    export_file = open(file, "w", encoding='utf-8')
                    export_file.write(str(export_branch) + "\n")
                    export_file.close()
                if package:
                    export_file = open(package, "w", encoding='utf-8')
                    export_file.write(str(export_package) + "\n")
                    export_file.close()

                if not file and not package:
                    printer("display_export_branch", [branch, export_branch, export_package])

        if error == 0:
            raise NotExistingBranchError(branch)
