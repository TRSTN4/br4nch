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
        self.trees = tree
        self.delete = delete

        self.validate_arguments()
        self.display_tree()

    def validate_arguments(self):
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(UtilityLibrarian.existing_trees):
                self.trees.append(existing_tree)

        for index in range(len(self.trees)):
            if not isinstance(self.trees[index], str):
                raise UtilityHandler.InstanceStringError("tree", self.trees[index])

            if self.trees[index].lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise UtilityHandler.NotExistingTreeError(self.trees[index])

            for existing_tree in list(UtilityLibrarian.existing_trees):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if self.delete:
            if not isinstance(self.delete, bool):
                raise UtilityHandler.InstanceBooleanError("delete", self.delete)

    def display_tree(self):
        for tree in self.trees:
            UtilityBuilder(tree)

            for line in UtilityLibrarian.existing_output[tree]:
                print(line)
            UtilityLibrarian.existing_output[tree].clear()

            if self.delete:
                del UtilityLibrarian.existing_trees[tree]
                del UtilityLibrarian.existing_output[tree]
                del UtilityLibrarian.existing_sizes[tree]
                del UtilityLibrarian.existing_symbols[tree]
