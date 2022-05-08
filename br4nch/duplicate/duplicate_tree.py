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
        self.new_tree = new_tree
        self.target_tree = target_tree
        self.attributes = attributes

        self.validate_arguments()
        self.duplicate_tree()

    def validate_arguments(self):
        if not isinstance(self.new_tree, str):
            raise UtilityHandler.InstanceStringError("new_tree", self.new_tree)

        if not self.new_tree.isalnum():
            raise UtilityHandler.InvalidTreeNameError(self.new_tree)

        if self.new_tree.lower() in list(map(str.lower, UtilityLibrarian.existing_trees)):
            raise UtilityHandler.DuplicateTreeError(self.new_tree)

        if not isinstance(self.target_tree, str):
            raise UtilityHandler.InstanceStringError("target_tree", self.target_tree)

        if self.target_tree.lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
            raise UtilityHandler.NotExistingTreeError(self.target_tree)

        for existing_tree in list(UtilityLibrarian.existing_trees):
            if self.target_tree.lower() == existing_tree.lower():
                self.target_tree = existing_tree

        if self.attributes:
            if not isinstance(self.attributes, bool):
                raise UtilityHandler.InstanceBooleanError("attributes", self.attributes)

    def duplicate_tree(self):
        UtilityLibrarian.existing_trees.update(
            {self.new_tree: copy.deepcopy(UtilityLibrarian.existing_trees[self.target_tree])})
        UtilityLibrarian.existing_output.update({self.new_tree: []})

        if self.attributes:
            UtilityLibrarian.existing_sizes.update({self.new_tree: UtilityLibrarian.existing_sizes[self.target_tree]})
            UtilityLibrarian.existing_symbols.update(
                {self.new_tree: UtilityLibrarian.existing_symbols[self.target_tree]})
        else:
            UtilityLibrarian.existing_sizes.update({self.new_tree: 0})
            UtilityLibrarian.existing_symbols.update({self.new_tree: {"line": "┃", "split": "┣━", "end": "┗━"}})
