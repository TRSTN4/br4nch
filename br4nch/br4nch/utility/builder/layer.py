# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.unpacker import unpack_paint_clear
from br4nch.utility.librarian import branches, output, sizes, symbols, paint_layer
from br4nch.utility.painter import painter


def configure(branch, branch_paint, colors):
    global levels, trace, chain, queue, last

    levels = [0]
    trace = [0]
    chain = []
    queue = []
    last = [0]

    build_layer(branch, branch_paint, colors)


# Creates the extenders/branch line for the layers.
def extenders(branches, branch, line, split, end, value, layer, prev_value):
    # Checks if the position of the current layer is not equal to zero.
    if levels[trace[0]] != 0:
        # Checks if the position of the current layer is not equal to the position of the previous layer.
        if levels[trace[0]] != levels[trace[0] - 1]:
            # Checks if content in queue or last is equal to the length of the zero positions layers (the first layers).
            if queue or last[0] == len(list(branches[branch][list(branches[branch])[0]])):
                # Appends the spaces based on the length of the given "end" symbol to the chain.
                chain.append(" " * int(len(end) + 1))
                # Clears the queue.
                queue.clear()

                # Checks if last is equal to the length of the zero positions layers (the first layers).
                if last[0] == len(list(branches[branch][list(branches[branch])[0]])):
                    # Resets the last value to the default value of last list.
                    last[0] = 0
            # If no content in queue or last is not equal to the length of the zero positions layers (the first layers).
            else:
                # Appends the line and spaces based on the length of the given "split" symbol to the chain.
                chain.append(str(line + " " * int(len(split))))

            # Checks if the position of the current layer is smaller then the position of the previous layer.
            if levels[trace[0]] < levels[trace[0] - 1]:
                # Loops the total length of the value of the previous layer position minus the current layer position.
                for _ in range(-1, int(levels[trace[0] - 1] - levels[trace[0]])):
                    # Removes the latest value of the chain list.
                    chain.pop()

        # Checks if the layer is equal to the last layer inside the previous value dict.
        if layer == list(reversed(list(prev_value)))[0]:
            # Checks if the position of the current layer is smaller then the position of the next layer.
            if levels[trace[0]] < levels[trace[0] + 1]:
                # Appends the current position to the queue.
                queue.append(levels[trace[0]])
    # If the position of the current layer is equal to zero.
    else:
        # Clears the chain list.
        chain.clear()
        # Last value is equal to the current value of last plus one.
        last[0] = last[0] + 1

    # If current value is not equal to the value of the header key (all the layer values).
    if value != branches[branch][list(branches[branch])[0]]:
        # Extend is equal to empty string.
        extend = ""
        # Loops through the chain.
        for line in chain:
            # Builds the extend by loop.
            extend = extend + line
        # Returns the extend value.
        return extend


def elevator(branch, value, pos=0):
    """
    """

    for layer, value in value.items():
        levels.append(pos)

        elevator(branch, value, pos + 1)


def build_layer(branch, branch_paint, colors, value="", pos=""):
    line = symbols[branch].get("line")
    split = symbols[branch].get("split")
    end = symbols[branch].get("end")

    if colors:
        paint_clear = unpack_paint_clear(branch)
    else:
        paint_clear = ""

    if not value:
        value = branches[branch][list(branches[branch])[0]]

    if len(levels) == 1:
        elevator(branch, value)
        levels.append(0)

    previous_value = value

    num = 0

    for layer, value in value.items():
        trace[0] = trace[0] + 1
        num = num + 1

        if num == 1:
            pos = pos.replace(pos, pos + "." + str(num))
        else:
            pos = pos.replace(pos, pos[:-1] + "." + str(num))

        if pos[0] == ".":
            pos = pos[1:]

        pos = pos.replace("..", ".")

        if layer in paint_layer[branch] and colors:
            layer_paint = painter(paint_layer[branch][layer], branch)
        else:
            layer_paint = ""

        extend = extenders(branches, branch, line, split, end, value, layer, previous_value)

        size = ""
        for _ in range(sizes[branch]):
            size = size + extend + line + "\n"

        if layer == list(previous_value)[-1]:
            output[branch].append(branch_paint + size + extend + end + " " + paint_clear + layer_paint + layer[:-15].replace("\n", paint_clear + "\n" + branch_paint + extend + paint_clear + " " * int(len(end) + 1) + layer_paint) + paint_clear)
        else:
            output[branch].append(branch_paint + size + extend + split + " " + paint_clear + layer_paint + layer[:-15].replace("\n", paint_clear + "\n" + branch_paint + extend + line + paint_clear + " " * int(len(split)) + layer_paint) + paint_clear)

        if value:
            build_layer(branch, branch_paint, colors, value, pos)
