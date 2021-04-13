# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.painter import painter


# Inspects if content in package.
def inspect_paint_clear():
    # Gets the needed lists/dictionaries.
    branch_package = librarian("branch_package")
    header_package = librarian("branch_package")
    layer_package = librarian("layer_package")

    # Stores all packages in a list.
    packages = [branch_package, header_package, layer_package]

    # Loops through all packages.
    for package in packages:
        # Checks if content in package.
        if package:
            # Resets the paint.
            paint_clear = painter("clear")
        # If content not in package.
        else:
            # Sets the paint to nothing.
            paint_clear = ""

        # Returns the value.
        return paint_clear


# Inspects all the paint in branch and header package.
def inspect_paint_base(branch, package):
    # Checks if content in package.
    if package:
        # Loops through all given packages inside the branch package dictionary.
        for key, value in package.items():
            # Checks if the key is equal to "all" string.
            if key == "all":
                # Branch paint is equal to the value of "all" inside the branch package.
                return value
            # If the key is not equal to the "all" string.
            else:
                # Checks if the key is equal to the value of branch.
                if key == branch:
                    # Paint is equal to the value of the key inside the package.
                    return package.get(branch)


# Inspects all the paint in layer package.
def inspect_paint_layer(branch, layer, package):
    # Checks if content in package.
    if package[branch]:
        # Loops through all given packages inside the layer package dictionary.
        for key, value in package[branch].items():
            # Checks if the package is equal to "all" string.
            if key == "all":
                # Paint is equal to the value of key.
                return value
            # Checks if the layer value is equal to key value and if the first 4 characters of key is equal to "all-"
            elif layer == key[4:] and key[:4] == "all-":
                # Paint is equal to the value of key.
                return value
            # If the key is not equal to the "all" string.
            else:
                # Checks if the key is equal to the value of layer.
                if key == layer:
                    # Paint is equal to the value of key.
                    return value
