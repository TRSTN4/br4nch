# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.painter import painter


# Adds the chosen paint to the chosen module to a list.
def color_module(branch="", module="", color="", special1="", special2="", special3=""):
    # Gets the needed lists/dictionaries.
    module_package = librarian("module_package")

    # Parses the name, color and specials to the painter. Then the painter returns the paint.
    paint_module = painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

    # Checks if the current branch value is inside the dictionary.
    if not module_package.get(branch):
        # Adds the current branch value as key and a new dictionary as value to the package dictionary.
        module_package.update({branch: {}})

    # Adds the module as key and the paint as value inside the branch > package dictionary.
    module_package[branch].update({module: paint_module})
