# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import copy

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler


class DuplicateTree:
    def __init__(self, new_tree, target_tree, attributes=False):
        """
        Required argument(s):
        - new_tree
        - target_tree

        Optional argument(s):
        - attributes

        :param new_tree: The name for the new tree.
        :param target_tree: The target tree that will be copied.
        :param attributes: If this argument is True, then the size and symbols are copied and linked to the new tree.
        """
        self.new_tree = new_tree
        self.target_tree = target_tree
        self.attributes = attributes

        self.validate_arguments()
        self.duplicate_tree()

    def validate_arguments(self):
        """
        Validates the arguments.
        """
        # Raises an error when the tree value is not a string.
        if not isinstance(self.new_tree, str):
            raise UtilityHandler.InstanceStringError("new_tree", self.new_tree)

        # Raises an error when the tree only uses numbers as name.
        if not self.new_tree.isalnum():
            raise UtilityHandler.InvalidTreeNameError(self.new_tree)

        # Raises an error when the tree already exists.
        if self.new_tree.lower() in list(map(str.lower, UtilityLibrarian.existing_trees)):
            raise UtilityHandler.DuplicateTreeError(self.new_tree)

        # Raises an error when the tree value is not a string.
        if not isinstance(self.target_tree, str):
            raise UtilityHandler.InstanceStringError("tree", self.target_tree)

        # Raises an error when the given tree does not exist.
        if self.target_tree.lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
            raise UtilityHandler.NotExistingTreeError(self.target_tree)

        # Sets the tree to the exact tree name.
        for existing_tree in list(UtilityLibrarian.existing_trees):
            if self.target_tree.lower() == existing_tree.lower():
                self.target_tree = existing_tree

        if self.attributes:
            # Raises an error when the attributes value is not a bool.
            if not isinstance(self.attributes, bool):
                raise UtilityHandler.InstanceBooleanError("attributes", self.attributes)

    def duplicate_tree(self):
        """
        Duplicates the old tree values and copies it into the new tree.
        """
        # Copies the old tree values and pastes it with the new tree value.
        UtilityLibrarian.existing_trees.update(
            {self.new_tree: copy.deepcopy(UtilityLibrarian.existing_trees[self.target_tree])})

        if self.attributes:
            # Sets all attributes to the old values.
            UtilityLibrarian.existing_sizes.update({self.new_tree: UtilityLibrarian.existing_sizes[self.target_tree]})
            UtilityLibrarian.existing_symbols.update(
                {self.new_tree: UtilityLibrarian.existing_symbols[self.target_tree]})
        else:
            # Sets all attributes to the default values.
            UtilityLibrarian.existing_sizes.update({self.new_tree: 0})
            UtilityLibrarian.existing_symbols.update({self.new_tree: {"line": "┃", "split": "┣━", "end": "┗━"}})
