# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from br4nch.utility.utility_librarian import existing_trees, existing_output, existing_uids, existing_sizes, \
    existing_symbols
from br4nch.utility.utility_handler import InstanceStringError, InvalidTreeNameError, DuplicateTreeError


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
                raise InstanceStringError("tree", tree)

            if not tree.isalnum():
                raise InvalidTreeNameError(tree)

            if tree.lower() in list(map(str.lower, existing_trees)):
                raise DuplicateTreeError(tree)

        if not isinstance(self.header, str):
            raise InstanceStringError("header", self.header)

    def create_tree(self):
        for tree in self.trees:
            existing_trees.update({tree: {self.header: {}}})
            existing_output.update({tree: []})
            existing_uids.update({tree: []})
            existing_sizes.update({tree: 0})
            existing_symbols.update({tree: {"line": "┃", "split": "┣━", "end": "┗━"}})
