# Part of the br4nch package.

# Imports all files.
from br4nch.utility.inspector.paint import inspect_paint_clear
from br4nch.utility.inspector.paint import inspect_paint_layer
from br4nch.utility.librarian import librarian


# Algorithm to build all the given headers.
def build_layer(branch, value="", pos=0, neg=0):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    paper = librarian("paper")
    logs = librarian("logs")
    branch_package = librarian("branch_package")
    layer_package = librarian("layer_package")
    branch_symbols = librarian("branch_symbols")

    line = branch_symbols[branch].get("line")
    split = branch_symbols[branch].get("split")
    end = branch_symbols[branch].get("end")

    # Paint is equal to the returned inspect paint base value.
    branch_paint = branch_package[branch]

    # Checks if content in package and returns the right paint clear value.
    paint_clear = inspect_paint_clear()

    # Checks if there is no content in value.
    if not value:
        # Value is equal to the value of branches > branch > header > value.
        value = branches[branch][list(branches[branch])[0]]

    saved_value = value.copy()

    if value == branches[branch][list(branches[branch])[0]]:
        extend = ""
    else:
        extend = str(line + "\t") * int(pos - neg) + "\t" * neg

    for layer, value in value.items():
        # Checks if inspect paint layer all returns a value.
        if inspect_paint_layer(branch, layer, layer_package):
            # Paint is equal to the returned inspect paint layer all value.
            paint_layer = inspect_paint_layer(branch, layer, layer_package)
        else:
            paint_layer = ""

        if layer == list(reversed(list(saved_value)))[0]:
            paper.append(branch_paint + extend + line + "\n" + extend + end + " " + paint_clear + paint_layer
                         + layer.replace("\n", "\n" + branch_paint + extend + paint_clear + " " * int(len(end) + 1)
                                         + paint_layer) + paint_clear)
        else:
            paper.append(branch_paint + extend + line + "\n" + extend + split + " " + paint_clear + paint_layer
                         + layer.replace("\n", "\n" + branch_paint + extend + line + paint_clear + " " * len(split)
                                         + paint_layer) + paint_clear)

        if value:
            if layer == list(reversed(list(saved_value)))[0]:
                neg = 1
            else:
                neg = 0

            build_layer(branch, value, pos + 1, neg)

        # Adds the state of the building process to the logs dictionary.
        logs.update({layer: "[+] Layer: '" + layer + "' Successfully Build."})
