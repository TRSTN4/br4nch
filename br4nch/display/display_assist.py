# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import copy

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import InstanceStringError, InstanceIntegerError, InvalidSizeError, NotExistingTreeError
from ..utility.utility_generator import UtilityGenerator
from ..display.display_tree import DisplayTree


class DisplayAssist:
    def __init__(self, tree, size=0, line="┃", split="┣━", end="┗━"):
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

        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(UtilityLibrarian.existing_trees):
                self.trees.append(existing_tree)

        for index in range(len(self.trees)):
            if not isinstance(self.trees[index], str):
                raise InstanceStringError("tree", self.trees[index])

            if self.trees[index].lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise NotExistingTreeError(self.trees[index])

            for existing_tree in list(UtilityLibrarian.existing_trees):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if self.size:
            if not isinstance(self.size, int):
                raise InstanceIntegerError("size", self.size)

            if int(self.size) < 0 or int(self.size) > 20:
                raise InvalidSizeError

        if self.line:
            if not isinstance(self.line, str):
                raise InstanceStringError("line", self.line)

        if self.split:
            if not isinstance(self.split, str):
                raise InstanceStringError("split", self.split)

        if self.end:
            if not isinstance(self.end, str):
                raise InstanceStringError("end", self.end)

    def display_assist(self):
        for tree in self.trees:
            levels = [0]
            self.elevator(levels, UtilityLibrarian.existing_trees[tree][list(UtilityLibrarian.existing_trees[tree])[0]])
            levels.append(0)

            tree_uid = UtilityGenerator("-").generate_uid()

            UtilityLibrarian.existing_trees.update({tree_uid: copy.deepcopy(UtilityLibrarian.existing_trees[tree])})
            UtilityLibrarian.existing_trees[tree_uid][str("0: " + list(UtilityLibrarian.existing_trees[tree])[0])] = \
                UtilityLibrarian.existing_trees[tree_uid].pop(list(UtilityLibrarian.existing_trees[tree_uid])[0])
            UtilityLibrarian.existing_output.update({tree_uid: []})
            UtilityLibrarian.existing_sizes.update({tree_uid: self.size})
            UtilityLibrarian.existing_symbols.update(
                {tree_uid: {"line": self.line, "split": self.split, "end": self.end}})

            self.set_node_positions(levels, [0],
                                    UtilityLibrarian.existing_trees[tree_uid][list(
                                        UtilityLibrarian.existing_trees[tree_uid])[0]])

            DisplayTree(tree_uid, True)

    def elevator(self, levels, nested_dictionary, height=0):
        for children in nested_dictionary.values():
            levels.append(height)
            self.elevator(levels, children, height + 1)

    def set_node_positions(self, levels, trace, nested_dictionary, position=""):
        count = 0
        for parent, children in nested_dictionary.copy().items():
            count = count + 1
            trace[0] = trace[0] + 1

            if levels[trace[0]] <= levels[trace[0] - 1]:
                position = position[:-2]
            position = position + "." + str(count)

            nested_dictionary[position[1:] + ": " + parent] = nested_dictionary.pop(parent)

            if children:
                self.set_node_positions(levels, trace, children, position)
