# Imports all files.
from br4nch.utility.librarian import librarian


# Adds a new module for the branch.
def add_layer(branch="", layer="", append="", row="", value=""):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")

    # todo
    header = list(branches[branch])[0]

    # Checks if there is no content in value.
    if not value:
        # Value is equal to the value of branches > branch > header > value.
        value = branches[branch][header]

    # Checks if content in append.
    if append:
        # Saves the key and value of the current value dictionary.
        for key, value in value.items():
            # Loops through all values in append list.
            for element in append:
                # Checks if current key of current value is equal to the value of element.
                if key == element:
                    # Checks if content in row.
                    if row:
                        # Loops through all values in layer.
                        for entry in layer:
                            # If the value of entry is not equal to the value of element.
                            if not entry == element:
                                # Adds value to current value dictionary.
                                value.update({entry: {}})
                    # If no content in row.
                    else:
                        # Loops through all values in layer.
                        for entry in layer:
                            # If the value of entry is not equal to the value of element.
                            if not entry == element:
                                # Adds value to current value dictionary.
                                value.update({entry: {}})
    # If there is no content in append, append element directly in branches > branch > header dictionary.
    else:
        # Loops through all values in layer list.
        for element in layer:
            # Adds value to branches > branch > header dictionary.
            branches[branch][header].update({element: {}})

    print(branches)
