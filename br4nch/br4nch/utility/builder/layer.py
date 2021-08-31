# Part of the br4nch package.

# Imports all files.
from br4nch.utility.inspector.paint import inspect_paint_clear
from br4nch.utility.inspector.paint import inspect_paint_layer
from br4nch.utility.librarian import librarian


# Configures the lists.
def configure(branch):
    # All global statements.
    global levels, trace, chain, queue, name

    # Required lists.
    levels = [0]
    trace = [0]
    chain = []
    queue = []
    name = []

    # Calls the build_layer function.
    build_layer(branch)


# Creates the extenders/branch for the layers.
def extenders(branches, branch, line, value, layer, prev_value):
    # Checks if the position of the current layer is not equal to zero.
    if levels[trace[0]] != 0:
        # Checks if the position of the current layer is not equal to the position of the previous layer.
        if levels[trace[0]] != levels[trace[0] - 1]:
            # Checks if the latest layer is equal to the last layer inside the previous value dict.
            if layer == list(reversed(list(prev_value)))[0]:
                # Checks if the position of the current layer is smaller then the position of the next layer.
                if levels[trace[0]] < levels[trace[0] + 1]:
                    # Appends the current level-trace to the queue.
                    queue.append(levels[trace[0]])
                    # Appends the layer name to the name list.
                    name.append(layer)

            # Checks if content in queue and layer name is not equal to layer name in name list.
            if queue and layer != name[0]:
                # Appends the spaces/tab to the chain
                chain.append("\t")
                # Clears the queue and name lists.
                queue.clear()
                name.clear()
            # If not content in queue and layer name is equal to layer name in name list.
            else:
                # Appends a line and spaces/tab to the chain.
                chain.append(str(line + "\t"))

            # Checks if the position of the current layer is smaller then the position of the previous layer.
            if levels[trace[0]] < levels[trace[0] - 1]:
                # Loops the total length of the value of the current layer position minus the previous layer position.
                for _ in range(-1, levels[trace[0] - 1] - int(levels[trace[0]])):
                    # Removes the latest value of the chain list.
                    chain.pop()

    # If the position of the current layer is equal to zero.
    else:
        # Clears the chain list.
        chain.clear()

    # If current value is not equal to this branch value.
    if value != branches[branch][list(branches[branch])[0]]:
        # Extend is equal to empty string.
        extend = ""
        # Loops through the chain.
        for x in chain:
            # Builds the extend by loop.
            extend = extend + x
        # Returns the extend value.
        return extend


# Calculates the level of all the layers.
def elevator(branch, value, pos=0):
    # Gets the layer/key and value of the current value variable.
    for layer, value in value.items():
        # Appends pos to the levels list.
        levels.append(pos)
        # Recalls the current function and adds the current value of pos by one.
        elevator(branch, value, pos + 1)


# Algorithm to build all the given headers.
def build_layer(branch, value=""):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    paper = librarian("paper")
    branch_package = librarian("branch_package")
    layer_package = librarian("layer_package")
    branch_symbols = librarian("branch_symbols")

    # Branch symbols variables.
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

    # Checks if the length of levels is equal to one.
    if len(levels) == 1:
        # Calls the elevator function with the branch and value variables.
        elevator(branch, value)

    # Stores the previous value.
    prev_value = value.copy()

    # Gets the layer/key and value of the current value variable.
    for layer, value in value.items():
        # Updates the latest trace and adds the current value of trace by one.
        trace[0] = trace[0] + 1
        # Extend is equal to the value returned by the extenders function.
        extend = extenders(branches, branch, line, value, layer, prev_value)

        # Checks if inspect paint layer all returns a value.
        if inspect_paint_layer(branch, layer, layer_package):
            # Paint is equal to the returned inspect paint layer all value.
            paint_layer = inspect_paint_layer(branch, layer, layer_package)
        # If inspect paint layer all does not returns a value.
        else:
            # Paint layer is equal to empty string.
            paint_layer = ""

        # Checks if the latest layer is equal to the last layer inside the previous value dict.
        if layer == list(reversed(list(prev_value)))[0]:
            # Appends the current layer branch line to the branch paper list.
            paper[branch].append(branch_paint + extend + line + "\n" + extend + end + " " + paint_clear + paint_layer
                                 + layer.replace("\n", paint_clear + "\n" + branch_paint + extend + paint_clear + " "
                                                 * int(len(end) + 1) + paint_layer) + paint_clear)
        # If the latest layer is not equal to the last layer inside the previous value dict.
        else:
            # Appends the current layer branch line to the branch paper list.
            paper[branch].append(branch_paint + extend + line + "\n" + extend + split + " " + paint_clear + paint_layer
                                 + layer.replace("\n", paint_clear + "\n" + branch_paint + extend + line + paint_clear
                                                 + " " * int(len(split)) + paint_layer) + paint_clear)

        # Checks if content in value
        if value:
            # Recalls the current function with the current value of value variable.
            build_layer(branch, value)
0