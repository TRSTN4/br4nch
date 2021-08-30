# Part of the br4nch package.

# Imports all files.
from br4nch.utility.inspector.paint import inspect_paint_clear
from br4nch.utility.inspector.paint import inspect_paint_layer
from br4nch.utility.librarian import librarian

levels = [0]
trace = [0]
chain = []
queue = []
name = []


def extenders(branches, branch, line, value, layer, prev_value):
    if levels[trace[0]] != 0:
        if levels[trace[0] - 1] != levels[trace[0]]:
            if queue and layer != name[0]:
                chain.append("\t")
                queue.clear()
                name.clear()
            else:
                chain.append(str(line + "\t"))

            if levels[trace[0]] < levels[trace[0] - 1]:
                for _ in range(-1, int(levels[trace[0] - 1] - levels[trace[0]])):
                    chain.pop()

        if layer == list(reversed(list(prev_value)))[0]:
            if levels[trace[0]] < levels[trace[0] + 1]:
                queue.append(levels[trace[0]])
                name.append(layer)
    else:
        chain.clear()

    if not value == branches[branch][list(branches[branch])[0]]:
        extend = ""
        for x in chain:
            extend = extend + x
        return extend


def elevator(branch, value, pos=0):
    for layer, value in value.items():
        levels.append(pos)
        elevator(branch, value, pos + 1)


# Algorithm to build all the given headers.
def build_layer(branch, value=""):
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
    print(branches)
    # Paint is equal to the returned inspect paint base value.
    branch_paint = branch_package[branch]

    # Checks if content in package and returns the right paint clear value.
    paint_clear = inspect_paint_clear()

    # Checks if there is no content in value.
    if not value:
        # Value is equal to the value of branches > branch > header > value.
        value = branches[branch][list(branches[branch])[0]]

    if len(levels) == 1:
        elevator(branch, value)

    prev_value = value.copy()

    for layer, value in value.items():
        trace[0] = trace[0] + 1
        extend = extenders(branches, branch, line, value, layer, prev_value)

        # Checks if inspect paint layer all returns a value.
        if inspect_paint_layer(branch, layer, layer_package):
            # Paint is equal to the returned inspect paint layer all value.
            paint_layer = inspect_paint_layer(branch, layer, layer_package)
        else:
            paint_layer = ""

        if layer == list(reversed(list(prev_value)))[0]:
            paper.append(branch_paint + extend + line + "\n" + extend + end + " " + paint_clear + paint_layer
                         + layer.replace("\n", paint_clear + "\n" + branch_paint + extend + paint_clear + " " *
                                         int(len(end) + 1) + paint_layer) + paint_clear)
        else:
            paper.append(branch_paint + extend + line + "\n" + extend + split + " " + paint_clear + paint_layer
                         + layer.replace("\n", paint_clear + "\n" + branch_paint + extend + line + paint_clear + " " *
                                         len(split) + paint_layer) + paint_clear)

        if value:
            build_layer(branch, value)

        # Adds the state of the building process to the logs dictionary.
        logs.update({layer: "[+] Layer: '" + layer + "' Successfully Build."})
