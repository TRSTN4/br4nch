# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.painter import painter


# Adds the chosen paint to the chosen subject to a list.
def color_subject(branch="", subject="", color="", special1="", special2="", special3=""):
    # Gets the needed lists/dictionaries.
    subject_package = librarian("subject_package")

    # Parses the name, color and specials to the painter. Then the painter returns the paint.
    paint_subject = painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

    # Checks if the current branch value is inside the dictionary.
    if not subject_package.get(branch):
        # Adds the current branch value as key and a new dictionary as value to the package dictionary.
        subject_package.update({branch: {}})

    # Adds the subject as key and the paint as value inside the branch > package dictionary.
    subject_package[branch].update({subject: paint_subject})
