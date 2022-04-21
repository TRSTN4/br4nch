# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import InstanceStringError, InstanceBooleanError, InvalidTreeNameError, \
    DuplicateTreeError, NotExistingTreeError


class DuplicateTree:
    def __init__(self, tree, sibling, attributes=False):
        self.tree = tree
        self.sibling = sibling
        self.attributes = attributes

        self.validate_arguments()
        self.duplicate_tree()

    def validate_arguments(self):
        if not isinstance(self.tree, str):
            raise InstanceStringError("tree", self.tree)

        if not self.tree.isalnum():
            raise InvalidTreeNameError(self.tree)

        if self.tree.lower() in list(map(str.lower, UtilityLibrarian.existing_trees)):
            raise DuplicateTreeError(self.tree)

        if not isinstance(self.sibling, str):
            raise InstanceStringError("sibling", self.sibling)

        if self.sibling.lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
            raise NotExistingTreeError(self.sibling)

        for existing_tree in list(UtilityLibrarian.existing_trees):
            if self.sibling.lower() == existing_tree.lower():
                self.sibling = existing_tree

        if self.attributes:
            if not isinstance(self.attributes, bool):
                raise InstanceBooleanError("attributes", self.attributes)

    def duplicate_tree(self):
        UtilityLibrarian.existing_trees.update({self.tree: UtilityLibrarian.existing_trees[self.sibling]})
        UtilityLibrarian.existing_output.update({self.tree: []})

        if self.attributes:
            UtilityLibrarian.existing_uids.update({self.tree: UtilityLibrarian.existing_uids[self.sibling]})
            UtilityLibrarian.existing_sizes.update({self.tree: UtilityLibrarian.existing_sizes[self.sibling]})
            UtilityLibrarian.existing_symbols.update({self.tree: UtilityLibrarian.existing_symbols[self.sibling]})
        else:
            UtilityLibrarian.existing_uids.update({self.tree: []})
            UtilityLibrarian.existing_sizes.update({self.tree: 0})
            UtilityLibrarian.existing_symbols.update({self.tree: {"line": "┃", "split": "┣━", "end": "┗━"}})
