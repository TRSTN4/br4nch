# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.painter import painter


# Adds the chosen paint to the parsed header.
def color_header(branch, options):
    # Gets the needed lists/dictionaries.
    paint_package_header = librarian("paint_package_header")

    # Parses the paint options arguments to the painter and the painter returns the paint.
    paint_header = painter(options, branch)

    # Adds the branch as key and the paint as value to the paint package.
    paint_package_header.update({branch: paint_header})
