# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from br4nch.utility.utility_librarian import existing_trees, existing_symbols, existing_sizes
from br4nch.utility.utility_handler import InstanceIntegerError, InstanceStringError, InvalidSizeError, \
    NotExistingTreeError


class SetSize:
    def __init__(self, tree, size):
        self.trees = tree
        self.size = size

        self.validate_arguments()
        self.set_size()

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

        if self.size < 0 or self.size > 20:
            raise InvalidSizeError

    def set_size(self):
        for tree in self.trees:
            if existing_symbols[tree]["split"] == "┣━":
                existing_symbols[tree]["split"] = "┣━" + "━" * self.size
            if existing_symbols[tree]["end"] == "┗━":
                existing_symbols[tree]["end"] = "┗━" + "━" * self.size

            existing_sizes.update({tree: self.size})
