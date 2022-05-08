# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler


class ReplaceTree:
    def __init__(self, new_tree, target_tree):
        self.new_tree = new_tree
        self.target_tree = target_tree

        self.validate_arguments()
        self.replace_tree()

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

    def replace_tree(self):
        index = list(UtilityLibrarian.existing_trees).index(self.target_tree)

        UtilityLibrarian.existing_trees[self.new_tree] = UtilityLibrarian.existing_trees.pop(self.target_tree)
        UtilityLibrarian.existing_output[self.new_tree] = UtilityLibrarian.existing_output.pop(self.target_tree)
        UtilityLibrarian.existing_sizes[self.new_tree] = UtilityLibrarian.existing_sizes.pop(self.target_tree)
        UtilityLibrarian.existing_symbols[self.new_tree] = UtilityLibrarian.existing_symbols.pop(self.target_tree)

        for index in list(UtilityLibrarian.existing_trees)[index:-1]:
            UtilityLibrarian.existing_trees[index] = UtilityLibrarian.existing_trees.pop(index)
            UtilityLibrarian.existing_output[index] = UtilityLibrarian.existing_output.pop(index)
            UtilityLibrarian.existing_sizes[index] = UtilityLibrarian.existing_sizes.pop(index)
            UtilityLibrarian.existing_symbols[index] = UtilityLibrarian.existing_symbols.pop(index)
