# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.painter import painter


# Adds the chosen paint to the chosen branch to a list.
def color_branch(branch, options):
    # Gets the needed lists/dictionaries.
    paint_package_branch = librarian("paint_package_branch")

    # Parses the paint options arguments to the painter. Then the painter returns the paint.
    paint_branch = painter(options, branch)

    # Adds the branch as key and the paint as value to the package dictionary.
    paint_package_branch.update({branch: paint_branch})
