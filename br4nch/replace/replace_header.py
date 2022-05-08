# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler


class ReplaceHeader:
    def __init__(self, tree, new_header):
        self.trees = tree
        self.new_header = new_header

        self.validate_arguments()
        self.replace_header()

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

        if not isinstance(self.new_header, str):
            raise UtilityHandler.InstanceStringError("new_header", self.new_header)

    def replace_header(self):
        for tree in self.trees:
            UtilityLibrarian.existing_trees[tree][self.new_header] = UtilityLibrarian.existing_trees[tree].pop(list(
                UtilityLibrarian.existing_trees[tree])[0])
