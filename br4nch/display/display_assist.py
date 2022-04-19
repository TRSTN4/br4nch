# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import copy

from br4nch.utility.utility_librarian import existing_trees, existing_output, existing_uids, existing_sizes, \
    existing_symbols
from br4nch.utility.utility_handler import InstanceStringError, InstanceIntegerError, InvalidSizeError, \
    NotExistingTreeError
from br4nch.utility.utility_generator import UtilityGenerator
from br4nch.display.display_tree import DisplayTree


class DisplayAssist:
    def __init__(self, tree, size=0, line="", split="", end=""):
        self.trees = tree
        self.size = size
        self.line = line
        self.split = split
        self.end = end

        self.validate_arguments()
        self.display_assist()

    def validate_arguments(self):
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        for index in range(len(self.trees)):
            if not isinstance(self.trees[index], str):
                raise InstanceStringError("tree", self.trees[index])

            if self.trees[index].lower() not in list(map(str.lower, existing_trees)):
                raise NotExistingTreeError(self.trees[index])

            for existing_tree in list(existing_trees):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(existing_trees):
                self.trees.append(existing_tree)

        if not isinstance(self.size, int):
            raise InstanceIntegerError("size", self.size)

        if int(self.size) < 0 or int(self.size) > 20:
            raise InvalidSizeError

        if not isinstance(self.line, str):
            raise InstanceStringError("line", self.line)

        if not isinstance(self.split, str):
            raise InstanceStringError("split", self.split)

        if not isinstance(self.end, str):
            raise InstanceStringError("end", self.end)

    def display_assist(self):
        for tree in self.trees:
            levels = [0]
            self.elevator(levels, existing_trees[tree][list(existing_trees[tree])[0]])
            levels.append(0)

            while True:
                tree_uid = tree + UtilityGenerator(tree).generate_uid()

                if tree_uid in list(existing_trees):
                    continue
                else:
                    existing_uids[tree].remove(tree_uid[-10:])
                    break

            if not self.line:
                self.line = existing_symbols[tree]["line"]
            if not self.split:
                self.split = existing_symbols[tree]["split"]
            if not self.end:
                self.end = existing_symbols[tree]["end"]

            existing_trees.update({tree_uid: copy.deepcopy(existing_trees[tree])})
            existing_trees[tree_uid][str("0: " + list(existing_trees[tree])[0])] = \
                existing_trees[tree_uid].pop(list(existing_trees[tree_uid])[0])
            existing_output.update({tree_uid: []})
            existing_uids.update({tree_uid: []})
            existing_sizes.update({tree_uid: self.size})
            existing_symbols.update({tree_uid: {"line": self.line, "split": self.split, "end": self.end}})

            self.set_node_positions(levels, [0], existing_trees[tree_uid][list(existing_trees[tree_uid])[0]])

            DisplayTree(tree_uid, True)

    def elevator(self, levels, child, height=0):
        for child_nodes in child.values():
            levels.append(height)
            self.elevator(levels, child_nodes, height + 1)

    def set_node_positions(self, levels, trace, child, node_position=""):
        count = 0
        for parent_node, child_nodes in child.copy().items():
            count = count + 1
            trace[0] = trace[0] + 1

            if levels[trace[0]] <= levels[trace[0] - 1]:
                node_position = node_position[:-2]
            node_position = node_position + "." + str(count)

            child[node_position[1:] + ": " + parent_node] = child.pop(parent_node)

            if child_nodes:
                self.set_node_positions(levels, trace, child_nodes, node_position)
