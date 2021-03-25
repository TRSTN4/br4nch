# Adds the chosen paint to the chosen branch to a list.
def branch(x="", color="", special1="", special2="", special3=""):
    # Parses the name, color and specials to the painter. Then the painter returns the paint.
    paint_branch = utility.painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

    # Adds the branch as key and the paint as value to the package dictionary.
    branch_package.update({x: paint_branch})
