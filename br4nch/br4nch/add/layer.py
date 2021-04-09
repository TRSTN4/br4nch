# Imports all files.
from br4nch.utility.librarian import librarian

# Saves all the given key arguments in the keys list.
keys = []


# Adds a new layer to the branches dictionary.
def add_layer(branch, layer, append="", row="", value="", position=0):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    positions = librarian("positions")

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
            # Adds the current layer with the position to the positions dictionary.
            positions[branch].update({key: position})
            # Checks if the key value is in the keys list.
            if key in keys:
                # Position is the value of position + 1.
                position = position + 1
                # Parses all the branch, layer, append, row, position and value values in the add_layer function.
                add_layer(branch, layer, append, row, value, position)
                # Breaks the loop.
                break
            # Loops through all values in append list.
            for element in append:
                # Checks if current key of current value is equal to the value of element.
                if key == element:
                    # Checks if content in row.
                    if row:
                        # Loops through all values in layer.
                        for entry in layer:
                            # Adds value to current value dictionary.
                            value.update({entry: {}})
                            # Stores the current key value to the keys list.
                            keys.append(key)
                    # If no content in row.
                    else:
                        # Loops through all values in layer.
                        for entry in layer:
                            # Adds value to current value dictionary.
                            value.update({entry: {}})
                            # Stores the current key value to the keys list.
                            keys.append(key)

    # If there is no content in append, append element directly in branches > branch > header dictionary.
    else:
        # Loops through all values in layer list.
        for element in layer:
            # Adds value to branches > branch > header dictionary.
            branches[branch][header].update({element: {}})
