# Part of the br4nch package.

# Imports all files.
from br4nch.utility.inspector.paint import inspect_paint_clear
from br4nch.utility.inspector.paint import inspect_paint_layer
from br4nch.utility.librarian import librarian


queue = []


# Algorithm to build all the given headers.
def build_layer(branch, value="", pos=0, neg=0):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    paper = librarian("paper")
    logs = librarian("logs")
    branch_package = librarian("branch_package")
    layer_package = librarian("layer_package")

    branch_paint = branch_package[branch]

    paint_clear = inspect_paint_clear()

    # Gets the header of the given branch.
    header = list(branches[branch])[0]

    newline = "\n"

    # Checks if there is no content in value.
    if not value:
        # Value is equal to the value of branches > branch > header > value.
        value = branches[branch][header]

    saved_value = value.copy()

    if value == branches[branch][header]:
        extend = ""
    else:
        pos_neg = pos - neg
        extend = "┃\t" * pos_neg + "\t" * neg

    for layer, value in value.items():
        # Checks if inspect paint layer all returns a value.
        if inspect_paint_layer(branch, layer, layer_package):
            # Paint is equal to the returned inspect paint layer all value.
            paint_layer = inspect_paint_layer(branch, layer, layer_package)
        else:
            paint_layer = ""

        if value:
            queue.append(value)

            if value and layer == list(reversed(list(saved_value)))[0]:
                paper.append(branch_paint + extend + "┃" + newline + extend + "┗━━ " + paint_clear + paint_layer + layer
                             + paint_clear)
                neg = 1
            else:
                paper.append(branch_paint + extend + "┃" + newline + extend + "┣━━ " + paint_clear + paint_layer + layer
                             + paint_clear)
                neg = 0

            # Adds the state of the building process to the logs dictionary.
            logs.update({layer: "[+] Layer: '" + layer + "' Successfully Build."})

            build_layer(branch, value, pos + 1, neg)
        else:
            if not value and layer != list(reversed(list(saved_value)))[0]:
                paper.append(branch_paint + extend + "┃" + newline + extend + "┣━━ " + paint_clear + paint_layer + layer
                             + paint_clear)
            else:
                paper.append(branch_paint + extend + "┃" + newline + extend + "┗━━ " + paint_clear + paint_layer + layer
                             + paint_clear)

            # Adds the state of the building process to the logs dictionary.
            logs.update({layer: "[+] Layer: '" + layer + "' Successfully Build."})
