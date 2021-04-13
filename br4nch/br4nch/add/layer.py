# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian

# Saves all the given key arguments in the keys list.
keys = []


# Adds a new layer to the branches dictionary.
def add_layer(branch, layer, append="", row="", value=""):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    layer_package = librarian("layer_package")

    # Gets the header of the given branch.
    header = list(branches[branch])[0]

    # Checks if there is no content in value.
    if not value:
        # Value is equal to the value of branches > branch > header > value.
        value = branches[branch][header]

    # Checks if content in append.
    if append:
        # Saves the key and value of the current value dictionary.
        for key, value in value.items():
            # Checks if the key value is in the keys list.
            if key in keys:
                # Position is the value of position + 1.
                # Parses all the branch, layer, append, row, position and value values in the add_layer function.
                add_layer(branch, layer, append, row, value)
                # Breaks the loop.
                break
            # Loops through all values in append list.
            for element in append:
                # Checks if current key of current value is equal to the value of element.
                if key == element:
                    # Checks if layer value is a instance of a list.
                    if isinstance(layer, list):
                        # Loops through all values in layer list.
                        for content in layer:
                            # Adds value to current value dictionary.
                            value.update({content: {}})
                            # Stores the current key value to the keys list.
                            keys.append(key)
                    # If layer value is not a instance of a list.
                    else:
                        # Adds value to current value dictionary.
                        value.update({layer: {}})
                        # Stores the current key value to the keys list.
                        keys.append(key)

    # If there is no content in append, append element directly in branches > branch > header dictionary.
    else:
        # Checks if layer value is a instance of a list.
        if isinstance(layer, list):
            # Loops through all values in layer list.
            for content in layer:
                # Adds value to branches > branch > header dictionary.
                branches[branch][header].update({content: {}})
        # If layer value is not a instance of a list.
        else:
            # Adds value to branches > branch > header dictionary.
            branches[branch][header].update({layer: {}})

    # Checks if the current branch value is inside the dictionary.
    if not layer_package.get(branch):
        # Adds the current branch value as key and a new dictionary as value to the package dictionary.
        layer_package.update({branch: {}})
