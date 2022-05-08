# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler


class CreateTree:
    def __init__(self, tree, header):
        self.trees = tree
        self.header = header

        self.validate_arguments()
        self.create_tree()

    def validate_arguments(self):
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        for tree in self.trees:
            if not isinstance(tree, str):
                raise UtilityHandler.InstanceStringError("tree", tree)

            if not tree.isalnum():
                raise UtilityHandler.InvalidTreeNameError(tree)

            if tree.lower() in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise UtilityHandler.DuplicateTreeError(tree)

        if not isinstance(self.header, str):
            raise UtilityHandler.InstanceStringError("header", self.header)

    def create_tree(self):
        for tree in self.trees:
            UtilityLibrarian.existing_trees.update({tree: {self.header: {}}})
            UtilityLibrarian.existing_output.update({tree: []})
            UtilityLibrarian.existing_sizes.update({tree: 0})
            UtilityLibrarian.existing_symbols.update({tree: {"line": "┃", "split": "┣━", "end": "┗━"}})
