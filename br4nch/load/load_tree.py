# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import os
import ast

from br4nch.utility.utility_librarian import existing_trees, existing_output, existing_uids, existing_sizes, \
    existing_symbols
from br4nch.utility.utility_handler import InstanceStringError, DuplicateTreeError, NotExistingTreeFileError, \
    InvalidTreeFileError, NotExistingAttributesFileError, InvalidAttributesFileError


class LoadTree:
    def __init__(self, tree_file, attributes_file=""):
        self.tree_file = tree_file
        self.attributes_file = attributes_file

        self.validate_arguments()
        self.load_tree()

    def validate_arguments(self):
        if not isinstance(self.tree_file, str):
            raise InstanceStringError("tree_file", self.tree_file)

        if not self.tree_file or self.tree_file and not os.path.isfile(self.tree_file):
            raise NotExistingTreeFileError(self.tree_file)

        with open(self.tree_file, 'r', encoding="utf8") as file:
            file = file.readlines()

            if str(file[0][:-1]) != "tag=tree":
                raise InvalidTreeFileError(self.tree_file)

            self.tree_file = ast.literal_eval(file[1])

        if self.tree_file.lower() in list(map(str.lower, existing_trees)):
            raise DuplicateTreeError(self.tree_file)

        if not isinstance(self.attributes_file, str):
            raise InstanceStringError("attributes_file", self.attributes_file)

        if not self.attributes_file or self.attributes_file and not os.path.isfile(self.attributes_file):
            raise NotExistingAttributesFileError(self.attributes_file)

        if self.attributes_file:
            with open(self.attributes_file, 'r', encoding="utf8") as file:
                file = file.readlines()

                if str(file[0][:-1]) != "tag=attributes":
                    raise InvalidAttributesFileError(self.attributes_file)

                self.attributes_file = ast.literal_eval(file[1])

    def load_tree(self):
        existing_trees.update({list(self.tree_file)[0]: list(self.tree_file.values())[0]})
        existing_output.update({list(self.tree_file)[0]: []})

        if self.attributes_file and list(self.attributes_file)[0] == list(self.tree_file)[0] \
                and len(list(self.attributes_file.values())[0]) == 6:
            existing_uids.update({list(self.tree_file)[0]: list(self.attributes_file.values())[0][0]})
            existing_sizes.update({list(self.tree_file)[0]: list(self.attributes_file.values())[0][1]})
            existing_symbols.update({list(self.tree_file)[0]: list(self.attributes_file.values())[0][2]})
        else:
            existing_uids.update({list(self.tree_file)[0]: []})
            existing_sizes.update({list(self.tree_file)[0]: 0})
            existing_symbols.update({list(self.tree_file)[0]: {"line": "┃", "split": "┣━", "end": "┗━"}})
