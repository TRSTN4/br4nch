# Adds the chosen paint to the chosen header to a list.
def header(branch="", color="", special1="", special2="", special3=""):
    # Parses the name, color and specials to the painter. Then the painter returns the paint.
    paint_header = utility.painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

    # Adds the branch as key and the paint as value to the package dictionary.
    header_package.update({branch: paint_header})
