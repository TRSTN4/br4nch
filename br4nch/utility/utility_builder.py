# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import copy

from br4nch.utility.utility_librarian import existing_trees, existing_output, existing_sizes, \
    existing_symbols, existing_paint_trees, existing_paint_headers, existing_paint_nodes
from br4nch.utility.utility_painter import UtilityPainter


class UtilityBuilder:
    def __init__(self, tree, paint):
        self.tree = tree
        self.paint = paint

        self.tree_paint = None
        self.header_paint = None
        self.clear_paint = None

        self.validate_arguments()
        self.manager()

    def validate_arguments(self):
        if self.paint:
            self.tree_paint = UtilityPainter(copy.deepcopy(existing_paint_trees[self.tree]))
            self.header_paint = UtilityPainter(copy.deepcopy(existing_paint_headers[self.tree]))
            self.clear_paint = UtilityPainter(["clear"])
        else:
            self.tree_paint = ""
            self.header_paint = ""
            self.clear_paint = ""

    def manager(self):
        existing_output[self.tree].append(self.clear_paint + self.header_paint + list(existing_trees[self.tree])[0] +
                                          self.clear_paint + existing_paint_trees + self.clear_paint)

        levels = [0]
        self.elevator(levels, existing_trees[self.tree][list(existing_trees[self.tree])[0]])
        levels.append(0)

        self.build_nodes([existing_paint_trees, self.clear_paint], [levels, [0], [], [], [0]],
                         existing_trees[self.tree][list(existing_trees[self.tree])[0]])

    def elevator(self, levels, value, pos=0):
        for value in value.values():
            levels.append(pos)
            self.elevator(levels, value, pos + 1)

    def build_nodes(self, colored, package, child):
        count = 0
        for parent_node, child_nodes in child.items():
            count = count + 1

            package[1][0] = package[1][0] + 1

            if colored and parent_node in existing_paint_nodes[self.tree]:
                node_paint = UtilityPainter(copy.deepcopy(existing_paint_nodes[self.tree])[parent_node])
            else:
                node_paint = ""

            extend = self.build_extender(parent_node, child, package[0], package[1], package[2], package[3], package[4])

            size = ""
            for _ in range(existing_sizes[self.tree]):
                size = size + extend + existing_symbols[self.tree].get("line") + "\n"

            if parent_node != list(child)[-1]:
                existing_output[self.tree].append(colored[0] + size + extend + existing_symbols[self.tree].get("split")
                                                  + " " + colored[1] + node_paint
                                                  + parent_node[:-15].replace("\n", colored[1] + "\n"
                                                                              + colored[0] + extend
                                                                              + existing_symbols[self.tree].get("line")
                                                                              + colored[1] + " "
                                                                              * int(len(existing_symbols[self.tree]
                                                                                        .get("split")))
                                                                              + node_paint) + colored[1])
            else:
                existing_output[self.tree].append(colored[0] + size + extend + existing_symbols[self.tree].get("end")
                                                  + " " + colored[1] + node_paint
                                                  + parent_node[:-15].replace("\n", colored[1] + "\n" + colored[0]
                                                                              + extend + colored[1] + " "
                                                                              * int(len(existing_symbols[self.tree]
                                                                                        .get("end")) + 1)
                                                                              + node_paint) + colored[1])

            if child_nodes:
                self.build_nodes(colored, package, child_nodes)

    def build_extender(self, node, child, levels, trace, chain, queue, last):
        if levels[trace[0]] != 0:
            if levels[trace[0]] != levels[trace[0] - 1]:
                if queue or last[0] == len(list(existing_trees[self.tree][list(existing_trees[self.tree])[0]])):
                    chain.append(" " * int(len(existing_symbols[self.tree].get("end")) + 1))
                    queue.clear()

                    if last[0] == len(list(existing_trees[self.tree][list(existing_trees[self.tree])[0]])):
                        last[0] = 0
                else:
                    chain.append(str(existing_symbols[self.tree].get("line") + " "
                                     * int(len(existing_symbols[self.tree].get("split")))))

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
