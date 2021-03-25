# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.painter import painter


# Adds the chosen paint to the chosen branch to a list.
def color_branch(branch="", color="", special1="", special2="", special3=""):
    # Gets the needed lists/dictionaries.
    branch_package = librarian("branch_package")

    # Parses the name, color and specials to the painter. Then the painter returns the paint.
    paint_branch = painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

    # Adds the branch as key and the paint as value to the package dictionary.
    branch_package.update({branch: paint_branch})
