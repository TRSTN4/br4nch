# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian


class UtilityBuilder:
    def __init__(self, tree):
        self.tree = tree

        self.manager()

    def manager(self):
        UtilityLibrarian.existing_output[self.tree].append(list(UtilityLibrarian.existing_trees[self.tree])[0])

        levels = [0]
        self.elevator(
            levels, UtilityLibrarian.existing_trees[self.tree][list(UtilityLibrarian.existing_trees[self.tree])[0]])
        levels.append(0)

        self.build_nodes(
            [levels, [0], [], [], [0]],
            UtilityLibrarian.existing_trees[self.tree][list(UtilityLibrarian.existing_trees[self.tree])[0]])

    def elevator(self, levels, nested_dictionary, height=0):
        for children in nested_dictionary.values():
            levels.append(height)
            self.elevator(levels, children, height + 1)

    def build_nodes(self, package, nested_dictionary):
        for parent, children in nested_dictionary.items():
            package[1][0] = package[1][0] + 1

            extend = self.build_extender(parent, nested_dictionary, package[0], package[1], package[2], package[3],
                                         package[4])

            size = ""
            for _ in range(UtilityLibrarian.existing_sizes[self.tree]):
                size = size + extend + UtilityLibrarian.existing_symbols[self.tree].get("line") + "\n"

            if parent != list(nested_dictionary)[-1]:
                UtilityLibrarian.existing_output[self.tree].append(
                    size + extend + UtilityLibrarian.existing_symbols[self.tree].get("split") + " "
                    + parent[:-15].replace("\n", "\n" + extend
                                           + UtilityLibrarian.existing_symbols[self.tree].get("line") + " "
                                           * int(len(UtilityLibrarian.existing_symbols[self.tree].get("split")))))
            else:
                UtilityLibrarian.existing_output[self.tree].append(
                    size + extend + UtilityLibrarian.existing_symbols[self.tree].get("end") + " "
                    + parent[:-15].replace("\n", "\n" + extend + " " * int(
                        len(UtilityLibrarian.existing_symbols[self.tree].get("end")) + 1)))

            if children:
                self.build_nodes(package, children)

    def build_extender(self, node, child, levels, trace, chain, queue, last):
        if levels[trace[0]] != 0:
            if levels[trace[0]] != levels[trace[0] - 1]:
                if queue or last[0] == len(
                        list(UtilityLibrarian.existing_trees[self.tree][list(
                            UtilityLibrarian.existing_trees[self.tree])[0]])):
                    chain.append(" " * int(len(UtilityLibrarian.existing_symbols[self.tree].get("end")) + 1))
                    queue.clear()

                    if last[0] == len(
                            list(UtilityLibrarian.existing_trees[self.tree][list(
                                UtilityLibrarian.existing_trees[self.tree])[0]])):
                        last[0] = 0
                else:
                    chain.append(str(UtilityLibrarian.existing_symbols[self.tree].get("line") + " "
                                     * int(len(UtilityLibrarian.existing_symbols[self.tree].get("split")))))

                if levels[trace[0]] < levels[trace[0] - 1]:
                    for _ in range(-1, int(levels[trace[0] - 1] - levels[trace[0]])):
                        chain.pop()

            if node == list(child)[-1]:
                if levels[trace[0]] < levels[trace[0] + 1]:
                    queue.append(levels[trace[0]])
        else:
            chain.clear()
            last[0] = last[0] + 1

        extend = ""
        for line in chain:
            extend = extend + line
        return extend
