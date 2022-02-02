# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

import copy

from br4nch.utility.utility_painter import painter
from br4nch.utility.utility_librarian import paint_branch, paint_header, output, branches, paint_layer, sizes, symbols


class Builder:
    def __init__(self, branch, paint):
        """
        - Gets the arguments and parses them to the 'manager' function.
        """
        self.manager(branch, paint)

    def manager(self, branch, paint):
        """
        - If the 'paint' variable is 'True', then the 'branch_paint', 'header_paint' and 'clear_paint' will be equal to
          the returned values of the painter class.
        - If the 'paint' variable is 'False', then the 'branch_paint', 'header_paint' and 'clear_paint' will be equal to
          empty strings.

        - dictionary, then the corresponding line/output is made for the current value of 'layer'.
        - Calls the 'elevator' function to calculate each level/height of each layer and stores the result in the levels
          list. Then a '0' is added to the 'levels' list so that the 'IndexError' error can be avoided.
        - Calls the 'build_layer' function to create the corresponding output for all layers.
        """
        if paint:
            branch_paint = painter(copy.deepcopy(paint_branch[branch]))
            header_paint = painter(copy.deepcopy(paint_header[branch]))
            clear_paint = painter(["clear"])
        else:
            branch_paint = ""
            header_paint = ""
            clear_paint = ""

        output[branch].append(clear_paint + header_paint + list(branches[branch])[0] + clear_paint + branch_paint +
                              clear_paint)

        levels = [0]
        self.elevator(levels, branches[branch][list(branches[branch])[0]])
        levels.append(0)

        self.build_layer(branch, paint, [branch_paint, clear_paint], [levels, [0], [], [], [0]],
                         branches[branch][list(branches[branch])[0]])

    def elevator(self, levels, value, pos=0):
        """
        Value dictionary loop:
          - Loops through each "height" of the value dictionary and adds the value of the 'pos' variable to the 'levels'
            list.
          - Then the 'elevator' function is called again with the current value of the 'value' dictionary.
        """
        for value in value.values():
            levels.append(pos)

            self.elevator(levels, value, pos + 1)

    def build_layer(self, branch, colored, paint, package, value):
        """
        Value dictionary loop:
          - For each value of the 'value' variable the 'count' variable and the first element of the second element in
            the 'package' list is added with plus '1'.

          - If the 'colored' variable is 'True' and the current value of 'layer' is in the list of 'paint_layer' with
            the branch key, then the 'layer_paint' is equal to the returned values of the painter class.
          - If the 'colored' variable is 'False' or the current value of 'layer' is not in the list of 'paint_layer'
            with the branch key, then the 'layer_paint' is equal to a empty string.

          - Calls the 'build_extender' function to build the corresponding extender for the current value of 'layer'.

          Output:
            - If the value of 'layer' is not equal to the last value of the 'previous_value' dictionary, then the
              corresponding 'split' line/output is made for the current value of 'layer'.
            - If the value of 'layer' is equal to the last value of the 'previous_value' dictionary, then the
              corresponding line/output is made for the current value of 'layer'.

          - Checks whether the 'value' variable has a value. If there is a value, then the 'display_pos' function is
            called again with the current values of 'value', 'trace' and 'levels' as arguments.
        """
        count = 0
        previous_value = value

        for layer, value in value.items():
            count = count + 1

            package[1][0] = package[1][0] + 1

            if colored and layer in paint_layer[branch]:
                layer_paint = painter(copy.deepcopy(paint_layer[branch])[layer])
            else:
                layer_paint = ""

            extend = self.build_extender(branch, layer, previous_value, package[0], package[1], package[2], package[3],
                                         package[4])

            size = ""
            for _ in range(sizes[branch]):
                size = size + extend + symbols[branch].get("line") + "\n"

            if layer != list(previous_value)[-1]:
                output[branch].append(paint[0] + size + extend + symbols[branch].get("split") + " " + paint[1] +
                                      layer_paint + layer[:-15].replace("\n", paint[1] + "\n" + paint[0] + extend +
                                                                        symbols[branch].get("line") + paint[1] + " " *
                                                                        int(len(symbols[branch].get("split"))) +
                                                                        layer_paint) + paint[1])
            else:
                output[branch].append(paint[0] + size + extend + symbols[branch].get("end") + " " + paint[1] +
                                      layer_paint + layer[:-15].replace("\n", paint[1] + "\n" + paint[0] + extend +
                                                                        paint[1] + " " *
                                                                        int(len(symbols[branch].get("end")) + 1) +
                                                                        layer_paint) + paint[1])

            if value:
                self.build_layer(branch, colored, paint, package, value)

    @staticmethod
    def build_extender(branch, layer, previous_value, levels, trace, chain, queue, last):
        """
        Layer height is not equal to '0':
          Layer height is equal to the previous layer height equal:
            Value in 'queue' or first element in 'last' list is equal to the length of all layers in height '0':
              - Adds "x" spaces based on the length of the 'end' symbol and appends it to the 'chain' list and then
                clears the 'queue' list.
              - If the first element in the 'last' list is equal to the length of all layers in height '0', then the
                first element in the 'last' list is equal to '0'.

            - If there is no value in 'queue' or first element in 'last' list is not equal to the length of all layers
              in height '0', then adds a 'line' symbol and "x" spaces based on the length of the 'split' symbol and
              appends it to the 'chain' list.
            - If the layer height is smaller than the previous layer height, the loop will run just as long based on the
              sum of the current layer height minus the next layer's height. With each loop, the last element of the
              'chain' list will be removed.

          - If the value of 'layer' is equal to the last layer in the 'previous_value' list and the height/level of the
            layer is less than the height of the next layer, then the current height of the layer is appended to the
            'queue' list.

        - If the height/level of layer is equal to '0', then the 'chain' list is cleared and the first element in the
          'last' list is added with '1'.

        - Loops through the 'chain' list and composes the 'extend' variable. After the loop, the 'extend' variable is
          returned.
        """
        if levels[trace[0]] != 0:
            if levels[trace[0]] != levels[trace[0] - 1]:
                if queue or last[0] == len(list(branches[branch][list(branches[branch])[0]])):
                    chain.append(" " * int(len(symbols[branch].get("end")) + 1))
                    queue.clear()

                    if last[0] == len(list(branches[branch][list(branches[branch])[0]])):
                        last[0] = 0
                else:
                    chain.append(str(symbols[branch].get("line") + " " * int(len(symbols[branch].get("split")))))

                if levels[trace[0]] < levels[trace[0] - 1]:
                    for _ in range(-1, int(levels[trace[0] - 1] - levels[trace[0]])):
                        chain.pop()

            if layer == list(previous_value)[-1]:
                if levels[trace[0]] < levels[trace[0] + 1]:
                    queue.append(levels[trace[0]])
        else:
            chain.clear()
            last[0] = last[0] + 1

        extend = ""
        for line in chain:
            extend = extend + line
        return extend
