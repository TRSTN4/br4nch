# Imports all files.
from br4nch.utility.librarian import librarian


# Adds a new module for the branch.
def add_layer(branch="", layer="", append="", row=""):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")

    header = list(branches[branch])[0]

    if not type(layer) is list:
        layer = [layer]

    if append:
        for element in append:

            for layer1 in branches[branch][header]:
                if row:
                    if element == layer1 and layer1 == row:
                        for entry in layer:
                            if not entry == element:
                                branches[branch][header][row].update({entry: {}})
                else:
                    if element == layer1:
                        for entry in layer:
                            if not entry == element:
                                branches[branch][header][layer1].update({entry: {}})

                for layer2 in branches[branch][header][layer1]:
                    if row:
                        if element == layer2 and layer2 in branches[branch][header][row]:
                            for entry in layer:
                                if not entry == element:
                                    branches[branch][header][row][layer2].update({entry: {}})
                    else:
                        if element == layer2:
                            for entry in layer:
                                if not entry == element:
                                    branches[branch][header][layer1][layer2].update({entry: {}})

                    for layer3 in branches[branch][header][layer1][layer2]:
                        if row:
                            if element == layer3 and layer3 in branches[branch][header][row][layer2]:
                                for entry in layer:
                                    if not entry == element:
                                        branches[branch][header][row][layer2][layer3].update({entry: {}})
                        else:
                            if element == layer3:
                                for entry in layer:
                                    if not entry == element:
                                        branches[branch][header][layer1][layer2][layer3].update({entry: {}})
    else:
        for element in layer:
            branches[branch][header].update({element: {}})

    print(branches)
