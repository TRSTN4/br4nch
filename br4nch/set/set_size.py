# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler


class SetSize:
    def __init__(self, tree, size):
        self.trees = tree
        self.size = size

        self.validate_arguments()
        self.set_size()

    def validate_arguments(self):
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(UtilityLibrarian.existing_trees):
                self.trees.append(existing_tree)

        for index in range(len(self.trees)):
            if not isinstance(self.trees[index], str):
                raise UtilityHandler.InstanceStringError("tree", self.trees[index])

            if self.trees[index].lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise UtilityHandler.NotExistingTreeError(self.trees[index])

            for existing_tree in list(UtilityLibrarian.existing_trees):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if not isinstance(self.size, int):
            raise UtilityHandler.InstanceIntegerError("size", self.size)

        for tree in self.trees:
            if UtilityLibrarian.existing_symbols[tree]["line"] != "┃":
                raise UtilityHandler.NotSizeableError
            if UtilityLibrarian.existing_symbols[tree]["split"] != "┣━":
                raise UtilityHandler.NotSizeableError
            if UtilityLibrarian.existing_symbols[tree]["end"] != "┗━":
                raise UtilityHandler.NotSizeableError

        if self.size < 0 or self.size > 20:
            raise UtilityHandler.InvalidSizeError

    def set_size(self):
        for tree in self.trees:
            if UtilityLibrarian.existing_symbols[tree]["split"] == "┣━":
                UtilityLibrarian.existing_symbols[tree]["split"] = "┣━" + "━" * self.size
            if UtilityLibrarian.existing_symbols[tree]["end"] == "┗━":
                UtilityLibrarian.existing_symbols[tree]["end"] = "┗━" + "━" * self.size

            UtilityLibrarian.existing_sizes.update({tree: self.size})
