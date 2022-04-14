# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import os

from br4nch.utility.utility_librarian import existing_trees, existing_output
from br4nch.utility.utility_handler import InstanceStringError, NotExistingDirectoryError, NotExistingTreeError
from br4nch.utility.utility_builder import UtilityBuilder


class ExportText:
    def __init__(self, tree, directory):
        self.trees = tree
        self.directory = directory

        self.export_text()

    def validate_arguments(self):
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        for index in range(len(self.trees)):
            if not isinstance(self.trees[index], str):
                raise InstanceStringError("tree", self.trees[index])

            if self.trees[index] not in list(map(str.lower, existing_trees)):
                raise NotExistingTreeError(self.trees[index])

            for existing_tree in list(map(str.lower, existing_trees)):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(existing_trees):
                self.trees.append(existing_tree)

        if not isinstance(self.directory, str):
            raise InstanceStringError("directory", self.directory)

        if not os.path.isdir(self.directory):
            raise NotExistingDirectoryError(self.directory)

    def export_text(self):
        for tree in self.trees:
            with open(self.directory + "/br4nch-" + tree + ".txt", 'w', encoding='utf-8') as file:
                UtilityBuilder(tree, False)

                for line in existing_output[tree]:
                    file.write(line + "\n")
                existing_output[tree].clear()
