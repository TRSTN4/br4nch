# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import InstanceStringError, InvalidTreeNameError, DuplicateTreeError, \
    NotExistingTreeError


class ReplaceTree:
    def __init__(self, tree, sibling):
        self.tree = tree
        self.sibling = sibling

        self.validate_arguments()
        self.replace_tree()

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

    def replace_tree(self):
        index = list(UtilityLibrarian.existing_trees).index(self.sibling)

        UtilityLibrarian.existing_trees[self.tree] = UtilityLibrarian.existing_trees.pop(self.sibling)
        UtilityLibrarian.existing_output[self.tree] = UtilityLibrarian.existing_output.pop(self.sibling)
        UtilityLibrarian.existing_uids[self.tree] = UtilityLibrarian.existing_uids.pop(self.sibling)
        UtilityLibrarian.existing_sizes[self.tree] = UtilityLibrarian.existing_sizes.pop(self.sibling)
        UtilityLibrarian.existing_symbols[self.tree] = UtilityLibrarian.existing_symbols.pop(self.sibling)

        for position in list(UtilityLibrarian.existing_trees)[index:-1]:
            UtilityLibrarian.existing_trees[position] = UtilityLibrarian.existing_trees.pop(position)
            UtilityLibrarian.existing_output[position] = UtilityLibrarian.existing_output.pop(position)
            UtilityLibrarian.existing_uids[position] = UtilityLibrarian.existing_uids.pop(position)
            UtilityLibrarian.existing_sizes[position] = UtilityLibrarian.existing_sizes.pop(position)
            UtilityLibrarian.existing_symbols[position] = UtilityLibrarian.existing_symbols.pop(position)
