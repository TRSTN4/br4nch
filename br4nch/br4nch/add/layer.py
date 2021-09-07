# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.handler import add_layer_error

# Saves all the given key arguments in the keys list.
keys = []


# Adds a new layer to the branches dictionary.
def add_layer(branch, layer, append="", position="", value=""):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    paint_package_layer = librarian("paint_package_layer")

    if branch in branches and branches[branch]:
        # Checks if layer value is a instance of a list.
        if not isinstance(layer, list):
            # Changes the current value to list value.
            layer = [layer]

        # Checks if append value is a instance of a list.
        if not isinstance(append, list) and append:
            # Changes the current value to list value.
            append = [append]

        # Checks if position value is a instance of a list.
        if not isinstance(position, list) and position:
            # Changes the current value to list value.
            position = [position]

        # Checks if there is no content in value.
        if not value:
            # Value is equal to the value of branches > branch > header > value.
            value = branches[branch][list(branches[branch])[0]]

        # Checks if content in append.
        if append:
            # Saves the key and value of the current value dictionary.
            for key, value in value.items():
                # Loops through all entries inside the append list.
                for element in append:
                    # Checks if content in position.
                    if position:
                        # Loops through all entries of position.
                        for pos in position:
                            # Checks if pos value is equal to the value of key.
                            if pos == key:
                                # Checks if value of key is not inside the keys list.
                                if key not in keys:
                                    # Appends the current value of key inside the keys list.
                                    keys.append(key)

                    # Checks if current key of current value is equal to the value of element.
                    if key == element:
                        # Checks if content in positions.
                        if position:
                            # Checks if the length of position list is equal to the length of the keys list.
                            if len(position) == len(keys):
                                # Loops through all entries of the layer list.
                                for content in layer:
                                    # Updates the current value and adds the content with dict value.
                                    value.update({content: {}})

                                if key == list(value)[-1]:
                                    # Clears all content in the keys list.
                                    keys.clear()
                        # Checks if content not in positions.
                        else:
                            # Loops through all entries inside the layer list.
                            for content in layer:
                                # Updates the current value and adds the content with dict value.
                                value.update({content: {}})
                    # Checks if current key of current value is not equal to the value of element.
                    else:
                        # Checks if content in value.
                        if value:
                            # Recalls the current function with the new values.
                            add_layer(branch, layer, append, position, value)

        # If there is no content in append, append element directly in branches > branch > header dictionary.
        else:
            # Loops through all values in layer list.
            for content in layer:
                # Adds value to branches > branch > header dictionary.
                branches[branch][list(branches[branch])[0]].update({content: {}})

        # Checks if the current branch value is inside the dictionary.
        if not paint_package_layer.get(branch):
            # Adds the current branch value as key and a new dictionary as value to the package dictionary.
            paint_package_layer.update({branch: {}})
    else:
        add_layer_error(branch, layer)
