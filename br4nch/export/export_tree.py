# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import os

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler


class ExportTree:
    def __init__(self, tree, output_folder, attributes=False):
        """
        Required argument(s):
        - tree
        - output_folder

        Optional argument(s):
        - attributes

        :param tree: The tree that will be exported to a br4nch file.
        :param output_folder: The output folder for the br4nch file.
        :param attributes: If this argument is True, then the size and symbols are copied and linked to the text file.
        """
        self.trees = tree
        self.output_folders = output_folder
        self.attributes = attributes

        self.validate_arguments()
        self.export_tree()

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

        if self.attributes:
            # Raises an error when the attributes value is not a bool.
            if not isinstance(self.attributes, bool):
                raise UtilityHandler.InstanceBooleanError("attributes", self.attributes)

    def export_tree(self):
        """
        Exports the tree structure to a br4nch file.
        """
        for tree in self.trees:
            # The dictionary that contains all attributes from a tree.
            export_attributes = {tree: [UtilityLibrarian.existing_sizes[tree], UtilityLibrarian.existing_symbols[tree]]}

            for folder in self.output_folders:
                # Creates the br4nch directory for the tree if it does not exist.
                if not os.path.isdir(folder + "/br4nch-" + tree):
                    os.mkdir(folder + "/br4nch-" + tree)

                # Parses the tree structure into a file.
                with open(folder + "/br4nch-" + tree + "/tree-" + tree + ".br4nch", 'w', encoding='utf-8') as file:
                    file.write("tag=tree\n")
                    file.write(str({tree: UtilityLibrarian.existing_trees[tree]}))

                if self.attributes:
                    # Parses the attributes into a file.
                    with open(folder + "/br4nch-" + tree + "/attributes-" + tree + ".br4nch", 'w', encoding='utf-8') \
                            as file:
                        file.write("tag=attributes\n")
                        file.write(str(export_attributes))
