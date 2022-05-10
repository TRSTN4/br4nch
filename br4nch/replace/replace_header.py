# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler


class ReplaceHeader:
    def __init__(self, tree, new_header):
        """
        Required argument(s):
        - tree
        - new_header

        :param tree: The name of tree(s) whose header will be replaced.
        :param new_header: The new name for the header(s).
        """
        self.trees = tree
        self.new_header = new_header

        self.validate_arguments()
        self.replace_header()

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

        # Raises an error when the 'new_header' value is not a string.
        if not isinstance(self.new_header, str):
            raise UtilityHandler.InstanceStringError("new_header", self.new_header)

    def replace_header(self):
        """
        Replaces the header name.
        """
        for tree in self.trees:
            # Changes the header with the new header name.
            UtilityLibrarian.existing_trees[tree][self.new_header] = \
                UtilityLibrarian.existing_trees[tree].pop(list(
                    UtilityLibrarian.existing_trees[tree])[0])
