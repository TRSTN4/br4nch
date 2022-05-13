# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import os
import ast

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler


class LoadTree:
    def __init__(self, tree_file, attributes_file=""):
        """
        Required argument(s):
        - tree_file

        Optional argument(s):
        - attributes_file

        :param tree_file: The exported tree file path.
        :param attributes_file: The exported attributes file path.
        """
        self.tree_file = tree_file
        self.attributes_file = attributes_file

        self.set_attributes = False

        self.validate_arguments()
        self.load_tree()

    def validate_arguments(self):
        """
        Validates the arguments.
        """
        # Raises an error when the 'tree_file' value is not a string.
        if not isinstance(self.tree_file, str):
            raise UtilityHandler.InstanceStringError("tree_file", self.tree_file)

        # Raises an error when the given tree file does not exist.
        if not os.path.isfile(self.tree_file):
            raise UtilityHandler.NotExistingTreeFileError(self.tree_file)

        # Opens the tree file.
        with open(self.tree_file, 'r', encoding="utf8") as file:
            file = file.readlines()

            # Raises an error when the file is missing the br4nch tree tag.
            if str(file[0][:-1]) != "tag=tree":
                raise UtilityHandler.InvalidTreeFileError(self.tree_file)

            # Safely evaluate the file line containing Python values.
            self.tree_file = ast.literal_eval(file[1])

        # Raises an error when the tree already exists.
        if list(self.tree_file)[0].lower() in list(map(str.lower, UtilityLibrarian.existing_trees)):
            raise UtilityHandler.DuplicateTreeError(list(self.tree_file)[0])

        if self.attributes_file:
            # Raises an error when the 'attributes_file' value is not a string.
            if not isinstance(self.attributes_file, str):
                raise UtilityHandler.InstanceStringError("attributes_file", self.attributes_file)

            # Raises an error when the given attributes file does not exist.
            if not os.path.isfile(self.attributes_file):
                raise UtilityHandler.NotExistingAttributesFileError(self.attributes_file)

            # Opens the attributes file.
            with open(self.attributes_file, 'r', encoding="utf8") as file:
                file = file.readlines()

                # Raises an error when the file is missing the br4nch attributes tag.
                if str(file[0][:-1]) != "tag=attributes":
                    raise UtilityHandler.InvalidAttributesFileError(self.attributes_file)

                # Safely evaluate the file line containing Python values.
                self.attributes_file = ast.literal_eval(file[1])
                # Allows to set the tree attributes to the file attributes.
                self.set_attributes = True

    def load_tree(self):
        """
        Loads the tree values and possibly the attributes values.
        """
        # Sets the tree structure data in the tree dictionary.
        UtilityLibrarian.existing_trees.update({list(self.tree_file)[0]: list(self.tree_file.values())[0]})

        if self.set_attributes:
            # Sets all attributes from the attributes file.
            UtilityLibrarian.existing_sizes.update({list(self.tree_file)[0]: list(self.attributes_file.values())[0][0]})
            UtilityLibrarian.existing_symbols.update({list(
                self.tree_file)[0]: list(self.attributes_file.values())[0][1]})
        else:
            # Sets all default attributes.
            UtilityLibrarian.existing_sizes.update({list(self.tree_file)[0]: 0})
            UtilityLibrarian.existing_symbols.update({list(
                self.tree_file)[0]: {"line": "┃", "split": "┣━", "end": "┗━"}})
