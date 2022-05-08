# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import os
import json

from br4nch.utility.utility_librarian import UtilityLibrarian
from br4nch.utility.utility_handler import UtilityHandler
from br4nch.utility.utility_generator import UtilityGenerator


class LoadJson:
    def __init__(self, new_tree, header, json_file):
        self.new_trees = new_tree
        self.header = header
        self.json_file = json_file

        self.existing = []

        self.validate_arguments()
        self.task_manager()

    def validate_arguments(self):
        if not isinstance(self.new_trees, list):
            self.new_trees = [self.new_trees]

        for tree in self.new_trees:
            if not isinstance(tree, str):
                raise UtilityHandler.InstanceStringError("new_trees", tree)

            if not tree.isalnum():
                raise UtilityHandler.InvalidTreeNameError(tree)

            if tree.lower() in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise UtilityHandler.DuplicateTreeError(tree)

        if not isinstance(self.header, str):
            raise UtilityHandler.InstanceStringError("header", self.header)

        if not isinstance(self.json_file, str):
            raise UtilityHandler.InstanceStringError("json_file", self.json_file)

        if not os.path.isfile(self.json_file):
            raise UtilityHandler.NotExistingJsonFileError(self.json_file)

    def task_manager(self):
        file = open(self.json_file)
        json_content = json.loads(json.dumps(json.load(file)))
        file.close()

        while True:
            self.convert_non_strings(json_content)
            converted = self.convert_lists(self.get_lists(json_content))

            if not converted:
                break

        self.add_uid(json_content)

        for tree in self.new_trees:
            UtilityLibrarian.existing_output.update({tree: []})
            UtilityLibrarian.existing_sizes.update({tree: 0})
            UtilityLibrarian.existing_symbols.update({tree: {"line": "┃", "split": "┣━", "end": "┗━"}})
            UtilityLibrarian.existing_trees.update({tree: {self.header: json_content}})

    def convert_non_strings(self, nested_dictionary):
        if not isinstance(nested_dictionary, dict):
            nested_dictionary = {str(nested_dictionary): {}}

        for parent, children in nested_dictionary.items():
            if children is None:
                children = "null"
            if isinstance(children, bool) and children is True:
                children = "true"
            if isinstance(children, bool) and children is False:
                children = "false"

            if not isinstance(children, dict) and not isinstance(children, list):
                if children not in self.existing:
                    children = str(children) + UtilityGenerator().generate_uid()
                    self.existing.append(children)

                nested_dictionary.update({parent: {str(children): {}}})

            self.convert_non_strings(children)

    def get_lists(self, nested_dictionary):
        for parent, children in nested_dictionary.items():
            if isinstance(children, list):
                return nested_dictionary
            else:
                returned_dictionary = self.get_lists(children)
                if returned_dictionary:
                    return returned_dictionary

    def convert_lists(self, nested_dictionary):
        if not nested_dictionary:
            return

        converted = False
        for parent, children in nested_dictionary.items():
            saved_children = []

            if isinstance(children, dict):
                for grandchild, great_grandchildren in children.items():
                    saved_children.append({grandchild: great_grandchildren})
            else:
                for child in children:
                    saved_children.append(child)

            nested_dictionary.update({parent: {}})

            if saved_children:
                converted = True
                for saved_child in saved_children:
                    if not isinstance(saved_child, dict) and not isinstance(saved_child, list):
                        saved_child = {str(saved_child): {}}

                    for grandchild, great_grandchildren in saved_child.items():
                        if not isinstance(great_grandchildren, dict) and not isinstance(great_grandchildren, list):
                            great_grandchildren = {str(great_grandchildren): {}}

                        if grandchild not in self.existing:
                            grandchild = str(grandchild) + UtilityGenerator().generate_uid()
                            self.existing.append(grandchild)

                        nested_dictionary[parent].update({str(grandchild): great_grandchildren})

        return converted

    def add_uid(self, nested_dictionary):
        for parent, children in nested_dictionary.copy().items():
            if not isinstance(parent, dict) and not isinstance(parent, list):
                nested_dictionary.pop(parent)

                if parent not in self.existing:
                    parent = str(parent) + UtilityGenerator().generate_uid()
                    self.existing.append(parent)

                nested_dictionary.update({parent: children})

            self.add_uid(children)
