# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.handler import add_layer_error


def calculate(branch, layer, pos, value, branches):
    if pos[0] == "0" or not pos[0]:
        for content in layer:
            branches[branch][list(branches[branch])[0]].update({content: {}})
    else:
        num_one = 0
        # Saves the key and value of the current value.
        for key, value in value.items():
            num_one = num_one + 1

            if num_one == int(pos[0]):
                if len(pos) < 2:
                    for content in layer:
                        value.update({content: {}})
                else:
                    pos.pop(0)
                    calculate(branch, layer, pos, value, branches)
                    return


# Adds a new layer to the branches dictionary.
def add_layer(branch, layer, pos="", value="", new=False):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    paint_package_layer = librarian("paint_package_layer")

    # Checks if the branch exists in the branches dictionary.
    if branch in branches:
        # Checks if layer value is a instance of a list.
        if not isinstance(layer, list):
            # Changes the current value to list value.
            layer = [layer]

        if not isinstance(pos, list):
            pos = [pos]

        # Checks if there is no content in value.
        if not value:
            # Value is equal to the value of all nested layers.
            value = branches[branch][list(branches[branch])[0]]

        if not new and isinstance(pos, list) and len(pos) > 1:
            for num in range(len(pos)):
                pos[num] = pos[num].split(".")
        else:
            pos[0] = pos[0].split(".")

        for pos in pos:
            calculate(branch, layer, pos, value, branches)

        # Checks if the current branch value is inside the paint package.
        if not paint_package_layer.get(branch):
            # Adds the current branch value as key and a new dictionary as value to the paint package.
            paint_package_layer.update({branch: {}})

    # If the branch does not exists in the branches dictionary.
    else:
        # Runs a custom error.
        add_layer_error(branch, layer)
