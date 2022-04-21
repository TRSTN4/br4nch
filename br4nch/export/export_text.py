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
    def __init__(self, tree, output_folder):
        self.trees = tree
        self.output_folder = output_folder

        self.validate_arguments()
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

        if not isinstance(self.output_folder, str):
            raise InstanceStringError("output_folder", self.output_folder)

        if not os.path.isdir(self.output_folder):
            raise NotExistingDirectoryError(self.output_folder)

    def export_text(self):
        for tree in self.trees:
            with open(self.output_folder + "/br4nch-" + tree + ".txt", 'w', encoding='utf-8') as file:
                UtilityBuilder(tree)

                for line in UtilityLibrarian.existing_output[tree]:
                    file.write(line + "\n")
                UtilityLibrarian.existing_output[tree].clear()
