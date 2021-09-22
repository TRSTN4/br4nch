# Part of the br4nch package.

# Imports all files.
from br4nch.utility.unpacker import unpack_paint_builder
from br4nch.utility.unpacker import unpack_paint_clear
from br4nch.utility.librarian import librarian


# Configures the lists and resets them everytime the configure function is called.
def configure(branch, paint_branch):
    # All global statements.
    global levels, trace, chain, queue, last

    # Sets the lists.
    levels = [0]
    trace = [0]
    chain = []
    queue = []
    last = [0]

    # Runs next task.
    build_layer(branch, paint_branch)


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


# Calculates the level of all the layers.
def elevator(branch, value, pos=0):
    # Gets the layer/key and value of the current value variable.
    for layer, value in value.items():
        # Appends position to the levels list.
        levels.append(pos)
        # Recalls the current function and adds the current value of position by one.
        elevator(branch, value, pos + 1)


# Algorithm to build the layer.
def build_layer(branch, paint_branch, value="", pos=""):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    paper = librarian("paper")
    symbols = librarian("symbols")
    paint_package_layer = librarian("paint_package_layer")
    size = librarian("size")

    # Branch symbols variables.
    line = symbols[branch].get("line")
    split = symbols[branch].get("split")
    end = symbols[branch].get("end")

    # Returns the calculated paint clear value.
    paint_clear = unpack_paint_clear(branch)

    # Checks if there is no content in value.
    if not value:
        # Value is equal to the value of all nested layers.
        value = branches[branch][list(branches[branch])[0]]

    # Checks if the length of levels is equal to one.
    if len(levels) == 1:
        # Calls the elevator function to calculate all the positions of all the layers.
        elevator(branch, value)
        # Appends zero to the end of the levels list to prevent index error.
        levels.append(0)

    # Stores the previous value.
    prev_value = value.copy()

    # Creates the num variable.
    num = 0

    # Gets the layer/key and value of the current value variable.
    for layer, value in value.items():
        # Num is equal to the value of num plus one.
        num = num + 1

        # Checks if num is equal to one.
        if num == 1:
            # Adds the current num to pos string.
            pos = pos.replace(pos, pos + str(num))
        # If num is not equal to one.
        else:
            # Removes the last num in pos string.
            pos = pos.replace(pos, pos[:-1] + str(num))

        # Checks if the unpacker returns a value.
        if unpack_paint_builder(branch, paint_package_layer, pos):
            # Paint is equal to the returned unpacked value.
            paint_layer = unpack_paint_builder(branch, paint_package_layer, pos)
        # If the unpacker does not returns a value.
        else:
            # Paint is equal to empty string.
            paint_layer = ""

        # Updates the latest trace and adds the current value of trace by one.
        trace[0] = trace[0] + 1
        # Extend is equal to the value returned by the extenders function.
        extend = extenders(branches, branch, line, split, end, value, layer, prev_value)

        spaces = ""
        for _ in range(size[branch]):
             spaces = spaces + extend + line + "\n"

        # Checks if the layer value is equal to the last layer inside the previous value.
        if layer == list(prev_value)[-1]:
            # Appends the current layer branch line to the branch paper list.
            paper[branch].append(paint_branch + spaces + extend + end + " " + paint_clear + paint_layer
                                 + layer[:-15].replace("\n", paint_clear + "\n" + paint_branch + extend + paint_clear
                                                       + " " * int(len(end) + 1) + paint_layer) + paint_clear)
        # If the layer is not equal to the last layer inside the previous value.
        else:
            # Appends the current layer branch line to the branch paper list.
            paper[branch].append(paint_branch + spaces + extend + split + " " + paint_clear + paint_layer
                                 + layer[:-15].replace("\n", paint_clear + "\n" + paint_branch + extend + line
                                                       + paint_clear + " " * int(len(split)) + paint_layer)
                                 + paint_clear)

        # Checks if content in value
        if value:
            # Recalls the current function with the current value of value variable.
            build_layer(branch, paint_branch, value, pos)
