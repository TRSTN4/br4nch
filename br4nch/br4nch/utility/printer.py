# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian


# The printer prints the output after the branch has been build.
def printer(action, branch="", delete=False):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    positions = librarian("positions")
    output = librarian("output")
    size = librarian("size")
    symbols = librarian("symbols")
    paint_package_branch = librarian("paint_package_branch")
    paint_package_header = librarian("paint_package_header")
    paint_package_layer = librarian("paint_package_layer")
    uids = librarian("uids")

    if action == "display_found":
        for layer, value in positions.copy().items():
            for key, pos in value.items():
                print("Get Position Result" + ":\n" + " " * 4 + "└─ Branch: " + branch + "\n" + " " * 7 + "└─ Layer: "
                      + layer.replace("\n", " ")[:-15] + "\n" + " " * 10 + "└─ Position: " + pos)
            del positions[layer]

    if action == "display_branch":
        for y in list(branches):
            if branch.lower() == y.lower():
                branch = y

                for x in output[branch]:
                    print(x)

                if delete:
                    del output[branch]
                    del branches[branch]
                    del size[branch]
                    del symbols[branch]
                    del paint_package_branch[branch]
                    del paint_package_header[branch]
                    del paint_package_layer[branch]
                    del uids[branch]
