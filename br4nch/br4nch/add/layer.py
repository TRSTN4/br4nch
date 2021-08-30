# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian

# Saves all the given key arguments in the keys list.
keys = []


# Adds a new layer to the branches dictionary.
def add_layer(branch, layer, append="", position="", value=""):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    layer_package = librarian("layer_package")

    # Checks if layer value is a instance of a list.
    if not isinstance(layer, list):
        layer = [layer]

    # Checks if append value is a instance of a list.
    if not isinstance(append, list) and append:
        append = [append]

    # Checks if position value is a instance of a list.
    if not isinstance(position, list) and position:
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

                            for x, y in value.items():
                                if x == append[0] and len(keys) == len(position):
                                    y.update({layer[0]: {}})
                                    keys.clear()

                # Checks if current key of current value is equal to the value of element.
                if key == element:
                    # Checks if content in positions.
                    if position:
                        # Checks if the length of position list is equal to the length of the keys list.
                        if len(position) == len(keys):
                            # Loops through all entries of the layer list.
                            for content in layer:
                                # todo
                                value.update({content: {}})

                            if key == list(value)[-1]:
                                # Clears all content in the keys list.
                                keys.clear()
                                # todo
                                return
                    # Checks if content not in positions.
                    else:
                        # Loops through all entries inside the layer list.
                        for content in layer:
                            # todo
                            value.update({content: {}})
                # Checks if current key of current value is not equal to the value of element.
                else:
                    # Checks if content in value.
                    if value:
                        # todo
                        add_layer(branch, layer, append, position, value)

    # If there is no content in append, append element directly in branches > branch > header dictionary.
    else:
        # Loops through all values in layer list.
        for content in layer:
            # Adds value to branches > branch > header dictionary.
            branches[branch][list(branches[branch])[0]].update({content: {}})

    # Checks if the current branch value is inside the dictionary.
    if not layer_package.get(branch):
        # Adds the current branch value as key and a new dictionary as value to the package dictionary.
        layer_package.update({branch: {}})
