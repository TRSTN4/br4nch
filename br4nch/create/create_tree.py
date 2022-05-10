# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler


class CreateTree:
    def __init__(self, tree, header):
        """
        Required argument(s):
        - tree
        - header

        :param tree: The name for the tree.
        :param header: The header for the tree.
        """
        self.trees = tree
        self.header = header

        self.validate_arguments()
        self.create_tree()

    def validate_arguments(self):
        """
        Validates the arguments.
        """
        # If the value is not an instance of a list, set the value in the list.
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        for tree in self.trees:
            # Raises an error when the tree value is not a string.
            if not isinstance(tree, str):
                raise UtilityHandler.InstanceStringError("tree", tree)

            # Raises an error when the tree only uses numbers as name.
            if not tree.isalnum():
                raise UtilityHandler.InvalidTreeNameError(tree)

            # Raises an error when the tree already exists.
            if tree.lower() in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise UtilityHandler.DuplicateTreeError(tree)

        # Raises an error when the header value is not a string.
        if not isinstance(self.header, str):
            raise UtilityHandler.InstanceStringError("header", self.header)

    def create_tree(self):
        """
        Creates each tree.
        """
        # Sets all required values for the dictionaries to create a new tree.
        for tree in self.trees:
            UtilityLibrarian.existing_trees.update({tree: {self.header: {}}})
            UtilityLibrarian.existing_output.update({tree: []})
            UtilityLibrarian.existing_sizes.update({tree: 0})
            UtilityLibrarian.existing_symbols.update({tree: {"line": "┃", "split": "┣━", "end": "┗━"}})
