# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler


class DeleteTree:
    def __init__(self, tree):
        self.trees = tree

        self.validate_arguments()
        self.delete_tree()

    def validate_arguments(self):
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(UtilityLibrarian.existing_trees):
                self.trees.append(existing_tree)

        for tree in self.trees:
            if not isinstance(tree, str):
                raise UtilityHandler.InstanceStringError("tree", tree)

            if tree.lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise UtilityHandler.NotExistingTreeError(tree)

    def delete_tree(self):
        for tree in self.trees:
            del UtilityLibrarian.existing_trees[tree]
            del UtilityLibrarian.existing_output[tree]
            del UtilityLibrarian.existing_sizes[tree]
            del UtilityLibrarian.existing_symbols[tree]
