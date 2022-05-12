# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian


class UtilityBuilder:
    def __init__(self, tree):
        self.tree = tree

        self.output = []

        self.manager()

    def manager(self):
        """
        Runs all the main tasks.
        """
        # Adds the header to the output.
        self.output.append(list(UtilityLibrarian.existing_trees[self.tree])[0])

        # Gets each height and stores it in the 'levels' list.
        levels = [0]
        self.elevator(levels,
                      UtilityLibrarian.existing_trees[self.tree][list(
                          UtilityLibrarian.existing_trees[self.tree])[0]])
        levels.append(0)

        # Build the nodes and adds them to the output list.
        self.build_nodes([levels, [0], [], [], [0]],
                         UtilityLibrarian.existing_trees[self.tree][list(
                             UtilityLibrarian.existing_trees[self.tree])[0]])

    def elevator(self, levels, nested_dictionary, height=0):
        """
        Appends each height to a list.
        """
        # Loops through nested dictionary.
        for children in nested_dictionary.values():
            # Appends the current 'height' value to the list.
            levels.append(height)
            # Appends the current 'height' value with '+1' and continues nesting the loop.
            self.elevator(levels, children, height + 1)

    def build_nodes(self, package, nested_dictionary):
        """
        Builds and each node and adds it to the output.
        """
        # Loops through nested dictionary.
        for parent, children in nested_dictionary.items():
            package[1][0] = package[1][0] + 1

            # Calls the function and builds the extender for each node.
            extend = self.build_extender(parent, nested_dictionary, package[0], package[1], package[2], package[3],
                                         package[4])

            size = ""
            # Calculates the given size and builds the size.
            for _ in range(UtilityLibrarian.existing_sizes[self.tree]):
                size = size + extend + UtilityLibrarian.existing_symbols[self.tree].get("line") + "\n"

            # Checks if the parent/node value is the last value in the dictionary.
            if parent == list(nested_dictionary)[-1]:
                # Adds the node and end symbol with added extender to the output.
                self.output.append(
                    size + extend + UtilityLibrarian.existing_symbols[self.tree].get("end") + " "
                    + parent[:-15].replace("\n", "\n" + extend + " " * int(
                        len(UtilityLibrarian.existing_symbols[self.tree].get("end")) + 1)))
            else:
                # Adds the node and split symbol with added extender to the output.
                self.output.append(
                    size + extend + UtilityLibrarian.existing_symbols[self.tree].get("split") + " "
                    + parent[:-15].replace("\n", "\n" + extend
                                           + UtilityLibrarian.existing_symbols[self.tree].get("line") + " "
                                           * int(len(UtilityLibrarian.existing_symbols[self.tree].get("split")))))

            if children:
                # Continue the nested loop.
                self.build_nodes(package, children)

    def build_extender(self, node, child, levels, trace, chain, queue, last):
        """
        Builds and calculates the extenders.
        """
        # Node height is not equal to '0'.
        if levels[trace[0]] != 0:
            # Node height is equal to the previous node height.
            if levels[trace[0]] != levels[trace[0] - 1]:
                # Value in 'queue' or first element in 'last' list is equal to the length of all nodes in height '0':
                if queue or last[0] == len(list(UtilityLibrarian.existing_trees[self.tree][list(
                        UtilityLibrarian.existing_trees[self.tree])[0]])):
                    # Adds "x" spaces based on the length of the 'end' symbol and appends it to the 'chain' list.
                    chain.append(" " * int(len(UtilityLibrarian.existing_symbols[self.tree].get("end")) + 1))
                    queue.clear()

                    # First element in the 'last' list is equal to the length of all nodes in height '0'.
                    if last[0] == len(list(UtilityLibrarian.existing_trees[self.tree][list(
                            UtilityLibrarian.existing_trees[self.tree])[0]])):
                        last[0] = 0
                else:
                    # Adds a 'line' symbol and "x" spaces based on the length of the 'split' symbol and appends it to
                    # the 'chain' list.
                    chain.append(str(UtilityLibrarian.existing_symbols[self.tree].get("line") + " "
                                     * int(len(UtilityLibrarian.existing_symbols[self.tree].get("split")))))

                # Node height is smaller than the previous node height.
                if levels[trace[0]] < levels[trace[0] - 1]:
                    # The loop will run based on the sum of the current node height minus the next node height.
                    for _ in range(-1, int(levels[trace[0] - 1] - levels[trace[0]])):
                        # With each loop, the last element of the 'chain' list will be removed.
                        chain.pop()

            # Value of node is equal to the last node in the 'child' list.
            if node == list(child)[-1]:
                # Height of the node is less than the height of the next node
                if levels[trace[0]] < levels[trace[0] + 1]:
                    # The current height of the node is appended to the 'queue' list.
                    queue.append(levels[trace[0]])
        else:
            chain.clear()
            last[0] = last[0] + 1

        extend = ""
        # Loops through the 'chain' list and builds the 'extend' variable.
        for line in chain:
            extend = extend + line
        return extend

    def get_output(self):
        """
        Returns the output list.
        """
        return self.output
