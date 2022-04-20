# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import os

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import InstanceStringError, NotExistingDirectoryError, NotExistingTreeError
from ..utility.utility_builder import UtilityBuilder


class ExportText:
    def __init__(self, tree, directory):
        self.trees = tree
        self.directory = directory

        self.export_text()

    def validate_arguments(self):
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(UtilityLibrarian.existing_trees):
                self.trees.append(existing_tree)

        for index in range(len(self.trees)):
            if not isinstance(self.trees[index], str):
                raise InstanceStringError("tree", self.trees[index])

            if self.trees[index].lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise NotExistingTreeError(self.trees[index])

            for existing_tree in list(UtilityLibrarian.existing_trees):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if not isinstance(self.directory, str):
            raise InstanceStringError("directory", self.directory)

        if not os.path.isdir(self.directory):
            raise NotExistingDirectoryError(self.directory)

    def export_text(self):
        for tree in self.trees:
            with open(self.directory + "/br4nch-" + tree + ".txt", 'w', encoding='utf-8') as file:
                UtilityBuilder(tree)

                for line in UtilityLibrarian.existing_output[tree]:
                    file.write(line + "\n")
                UtilityLibrarian.existing_output[tree].clear()
