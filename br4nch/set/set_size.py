# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler


class SetSize:
    def __init__(self, tree, size):
        """
        Required argument(s):
        - tree
        - size

        :param tree: The tree(s) where the symbols are added.
        :param size: The size of the space in the tree structure.
        """
        self.trees = tree
        self.size = size

        self.validate_arguments()
        self.set_size()

    def validate_arguments(self):
        """
        Validates the arguments.
        """
        # If the value is not an instance of a list, set the value in the list.
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        # If there is a '*' in the tree value, add all existing trees to the list.
        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(UtilityLibrarian.existing_trees):
                self.trees.append(existing_tree)

        for index in range(len(self.trees)):
            # Raises an error when the tree value is not a string.
            if not isinstance(self.trees[index], str):
                raise UtilityHandler.InstanceStringError("tree", self.trees[index])

            # Raises an error when the given tree does not exist.
            if self.trees[index].lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise UtilityHandler.NotExistingTreeError(self.trees[index])

            # Sets the tree to the exact tree name.
            for existing_tree in list(UtilityLibrarian.existing_trees):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        # Raises an error when the size value is not an int.
        if not isinstance(self.size, int):
            raise UtilityHandler.InstanceIntegerError("size", self.size)

        for tree in self.trees:
            # Raises an error if the symbols are changes and are not the default symbols.
            if UtilityLibrarian.existing_symbols[tree]["line"] != "┃":
                raise UtilityHandler.NotSizeableError
            if UtilityLibrarian.existing_symbols[tree]["split"] != "┣━":
                raise UtilityHandler.NotSizeableError
            if UtilityLibrarian.existing_symbols[tree]["end"] != "┗━":
                raise UtilityHandler.NotSizeableError

        # Raises an error if the given size is lower than '0' and bigger than '20'.
        if self.size < 0 or self.size > 20:
            raise UtilityHandler.InvalidSizeError

    def set_size(self):
        """
        Sets the size.
        """
        for tree in self.trees:
            # Changes each the size of the 'split' and 'end' symbols.
            UtilityLibrarian.existing_symbols[tree]["split"] = "┣━" + "━" * self.size
            UtilityLibrarian.existing_symbols[tree]["end"] = "┗━" + "━" * self.size

            # Sets the size.
            UtilityLibrarian.existing_sizes.update({tree: self.size})
