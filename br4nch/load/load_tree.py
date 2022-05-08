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
        self.tree_file = tree_file
        self.attributes_file = attributes_file

        self.validate_arguments()
        self.load_tree()

    def validate_arguments(self):
        if not isinstance(self.tree_file, str):
            raise UtilityHandler.InstanceStringError("tree_file", self.tree_file)

        if not self.tree_file or self.tree_file and not os.path.isfile(self.tree_file):
            raise UtilityHandler.NotExistingTreeFileError(self.tree_file)

        with open(self.tree_file, 'r', encoding="utf8") as file:
            file = file.readlines()

            if str(file[0][:-1]) != "tag=tree":
                raise UtilityHandler.InvalidTreeFileError(self.tree_file)

            self.tree_file = ast.literal_eval(file[1])

        if list(self.tree_file)[0].lower() in list(map(str.lower, UtilityLibrarian.existing_trees)):
            raise UtilityHandler.DuplicateTreeError(list(self.tree_file)[0])

        if self.attributes_file:
            if not isinstance(self.attributes_file, str):
                raise UtilityHandler.InstanceStringError("attributes_file", self.attributes_file)

            if not self.attributes_file or self.attributes_file and not os.path.isfile(self.attributes_file):
                raise UtilityHandler.NotExistingAttributesFileError(self.attributes_file)

    def load_tree(self):
        if self.attributes_file:
            with open(self.attributes_file, 'r', encoding="utf8") as file:
                file = file.readlines()

                if str(file[0][:-1]) != "tag=attributes":
                    raise UtilityHandler.InvalidAttributesFileError(self.attributes_file)

                self.attributes_file = ast.literal_eval(file[1])

        UtilityLibrarian.existing_trees.update({list(self.tree_file)[0]: list(self.tree_file.values())[0]})
        UtilityLibrarian.existing_output.update({list(self.tree_file)[0]: []})

        if self.attributes_file and list(self.attributes_file)[0] == list(self.tree_file)[0] \
                and len(list(self.attributes_file.values())[0]) == 6:
            UtilityLibrarian.existing_sizes.update({list(self.tree_file)[0]: list(self.attributes_file.values())[0][0]})
            UtilityLibrarian.existing_symbols.update({list(
                self.tree_file)[0]: list(self.attributes_file.values())[0][1]})
        else:
            UtilityLibrarian.existing_sizes.update({list(self.tree_file)[0]: 0})
            UtilityLibrarian.existing_symbols.update({list(
                self.tree_file)[0]: {"line": "┃", "split": "┣━", "end": "┗━"}})
