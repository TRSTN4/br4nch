# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.painter import painter


# Adds the chosen paint to the chosen header to a list.
def color_header(branch, options):
    # Gets the needed lists/dictionaries.
    header_package = librarian("header_package")

    # Parses the paint options arguments to the painter. Then the painter returns the paint.
    paint_header = painter(options)

    # Adds the branch as key and the paint as value to the package dictionary.
    header_package.update({branch: paint_header})
