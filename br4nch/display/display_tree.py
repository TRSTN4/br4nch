# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler
from ..utility.utility_builder import UtilityBuilder


class DisplayTree:
    def __init__(self, tree, delete=False):
        """
        Required argument(s):
        - tree

        Optional argument(s):
        - delete

        :param tree: The tree(s) to display.
        :param delete: If this argument is 'True', the tree(s) will be deleted after it is printed.
        """
        self.trees = tree
        self.delete = delete

        self.validate_arguments()
        self.display_tree()

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

        for index in range(len(self.trees)):
            # Raises an error when the tree value is not a string.
            if not isinstance(self.trees[index], str):
                raise UtilityHandler.InstanceStringError("tree", self.trees[index])

            # Raises an error when the given tree does not exist.
            if self.trees[index].lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise UtilityHandler.NotExistingTreeError(self.trees[index])

            # Sets the tree to the exact tree name.
            for existing_tree in list(UtilityLibrarian.existing_trees):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if self.delete:
            # Raises an error when the value is not a bool.
            if not isinstance(self.delete, bool):
                raise UtilityHandler.InstanceBooleanError("delete", self.delete)

    def display_tree(self):
        """
        Displays each tree.
        """
        for tree in self.trees:
            # Builds and prints the tree.
            for line in UtilityBuilder(tree).get_output():
                print(line)

            # If true, all linked dictionaries with the tree will be deleted.
            if self.delete:
                del UtilityLibrarian.existing_trees[tree]
                del UtilityLibrarian.existing_sizes[tree]
                del UtilityLibrarian.existing_symbols[tree]
