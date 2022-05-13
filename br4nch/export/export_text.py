# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import os

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler
from ..utility.utility_builder import UtilityBuilder


class ExportText:
    def __init__(self, tree, output_folder):
        """
        Required argument(s):
        - tree
        - output_folder

        :param tree: The tree that will be exported to a text file.
        :param output_folder: The output directory for the text file.
        """
        self.trees = tree
        self.output_folders = output_folder

        self.validate_arguments()
        self.export_text()

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

        # If the value is not an instance of a list, set the value in the list.
        if not isinstance(self.output_folders, list):
            self.output_folders = [self.output_folders]

        for folder in self.output_folders:
            # Raises an error when the folder value is not a string.
            if not isinstance(folder, str):
                raise UtilityHandler.InstanceStringError("output_folder", folder)

            # Raises an error when the given folder path does not exist.
            if not os.path.isdir(folder):
                raise UtilityHandler.NotExistingDirectoryError(folder)

    def export_text(self):
        """
        Exports the tree output to a text file.
        """
        for tree in self.trees:
            for folder in self.output_folders:
                # Creates the text file.
                with open(folder + "/br4nch-" + tree + ".txt", 'w', encoding='utf-8') as file:
                    # Builds and writes each line from the output.
                    for line in UtilityBuilder(tree).get_output():
                        file.write(line + "\n")
