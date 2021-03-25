# Adds the chosen paint to the chosen object to a list.
def object(branch="", x="", color="", special1="", special2="", special3=""):
    # Parses the name, color and specials to the painter. Then the painter returns the paint.
    paint_object = utility.painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

    # Checks if the current branch value is inside the dictionary.
    if not object_package.get(branch):
        # Adds the current branch value as key and a new dictionary as value to the package dictionary.
        object_package.update({branch: {}})

    # Adds the object as key and the paint as value inside the branch > package dictionary.
    object_package[branch].update({x: paint_object})
