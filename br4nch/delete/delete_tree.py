# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler


class DeleteTree:
    def __init__(self, tree):
        """
        Required argument(s):
        - tree

        :param tree: The name of the tree(s) that will be deleted.
        """
        self.trees = tree

        self.validate_arguments()
        self.delete_tree()

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

        for tree in self.trees:
            # Raises an error when the tree value is not a string.
            if not isinstance(tree, str):
                raise UtilityHandler.InstanceStringError("tree", tree)

            # Raises an error when the given tree does not exist.
            if tree.lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise UtilityHandler.NotExistingTreeError(tree)

    def delete_tree(self):
        """
        Deletes each tree.
        """
        # Deletes all dictionaries from each tree that must be deleted.
        for tree in self.trees:
            del UtilityLibrarian.existing_trees[tree]
            del UtilityLibrarian.existing_sizes[tree]
            del UtilityLibrarian.existing_symbols[tree]
