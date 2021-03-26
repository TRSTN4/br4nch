from br4nch.utility.librarian import librarian


# Inspects if content in package.
def inspect_paint_clear(package):
    # Checks if content in package.
    if package:
        # Resets the paint.
        paint_clear = "\u001b[0m"
    # If content not in package.
    else:
        # Sets the paint to nothing.
        paint_clear = ""

    # Returns the value.
    return paint_clear


# Inspects if "all" in layer package.
def inspect_paint_layer(branch, layer, package):
    # Checks if content in package.
    if package:
        # Loops through all given packages inside the layer package dictionary.
        for content in package:
            # Checks if the package is equal to "all" string.
            if content == "all":
                # Loops through all keys inside the "all" package.
                for key in package["all"]:
                    # Checks if the key is equal to the "all" string.
                    if key == "all":
                        # Paint is equal to the value of "all" inside layer > "all" package.
                        return package["all"].get("all")
                    # If the key is not equal to the "all" string.
                    else:
                        # Checks if the key is equal to the value of layer.
                        if key == layer:
                            # Paint is equal to the value of layer inside layer > "all" package.
                            return package["all"].get(layer)
            # If the package is not equal to "all" string.
            else:
                # Loops through all keys inside the layer > branch package.
                for key in package[branch]:
                    # Checks if the key is equal to the "all" string.
                    if key == "all":
                        # Paint is equal to the value of the key in the layer > branch package.
                        return package[branch].get(key)


# Inspects todo
def inspect_paint_base(branch, package):
    # Checks if content in package.
    if package:
        # Loops through all keys in the package directory.
        for key in package:
            # Checks if the key is equal to the value of branch.
            if key == branch:
                # Paint is equal to the value of the key inside the package.
                return package.get(branch)


# Inspects if "all" in layer package.
def inspect_paint_all_layer(branch, layer, package):
    # Checks if content in package.
    if package:
        # Loops through all given packages inside the layer package dictionary.
        for content in package:
            # Checks if the package is equal to "all" string.
            if content == "all":
                # Loops through all keys inside the "all" package.
                for key in package["all"]:
                    # Checks if the key is equal to the "all" string.
                    if key == "all":
                        # Paint is equal to the value of "all" inside layer > "all" package.
                        return package["all"].get("all")
                    # If the key is not equal to the "all" string.
                    else:
                        # Checks if the key is equal to the value of layer.
                        if key == layer:
                            # Paint is equal to the value of layer inside layer > "all" package.
                            return package["all"].get(layer)
            # If the package is not equal to "all" string.
            else:
                # Loops through all keys inside the layer > branch package.
                for key in package[branch]:
                    # Checks if the key is equal to the "all" string.
                    if key == "all":
                        # Paint is equal to the value of the key in the layer > branch package.
                        return package[branch].get(key)


# Inspects if "all" in layer package.
def inspect_paint_all_base(package):
    # Checks if content in package.
    if package:
        # Loops through all given packages inside the branch package dictionary.
        for key in package:
            # Checks if the key is equal to "all" string.
            if key == "all":
                # Branch paint is equal to the value of "all" inside the branch package.
                return package.get("all")
