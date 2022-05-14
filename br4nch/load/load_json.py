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
        """
        Required argument(s):
        - new_tree
        - header
        - json_file

        :param new_tree: The name for the new tree(s) that will be created for the imported json file.
        :param header: The header name for the tree(s).
        :param json_file: The path of the json file that will be imported.
        """
        self.new_trees = new_tree
        self.header = header
        self.json_file = json_file

        self.existing = []

        self.validate_arguments()
        self.task_manager()

    def validate_arguments(self):
        """
        Validates the arguments.
        """
        # If the value is not an instance of a list, set the value in the list.
        if not isinstance(self.new_trees, list):
            self.new_trees = [self.new_trees]

        for tree in self.new_trees:
            # Raises an error when the tree value is not a string.
            if not isinstance(tree, str):
                raise UtilityHandler.InstanceStringError("new_tree", tree)

            # Raises an error when the tree only uses numbers as name.
            if not tree.isalnum():
                raise UtilityHandler.InvalidTreeNameError(tree)

            # Raises an error when the tree already exists.
            if tree.lower() in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise UtilityHandler.DuplicateTreeError(tree)

        # Raises an error when the header value is not a string.
        if not isinstance(self.header, str):
            raise UtilityHandler.InstanceStringError("header", self.header)

        # Raises an error when the 'json_file' value is not a string.
        if not isinstance(self.json_file, str):
            raise UtilityHandler.InstanceStringError("json_file", self.json_file)

        # Raises an error when the given json file does not exist.
        if not os.path.isfile(self.json_file):
            raise UtilityHandler.NotExistingJsonFileError(self.json_file)

    def task_manager(self):
        """
        Runs the main tasks and adds the tree.
        """
        # Loads the json structure in the file.
        with open(self.json_file, 'r', encoding="utf-8-sig") as default_file:
            json_content = json.loads(json.dumps(json.load(default_file)))

        save = []
        # Bypass 'AttributeError' error.
        if isinstance(json_content, list):
            # Saves each value in the given json list.
            for dictionary in json_content:
                save.append(dictionary)

            # Resets json structure.
            json_content = {}
            # Adds all content in the 'save' list and adds an entry number to each value.
            for number in range(len(save)):
                json_content.update({"Entry: #" + str(number + 1): save[number]})

        while True:
            # Converts all values to string values.
            self.convert_non_strings(json_content)
            # Places all values into dictionaries.
            converted = self.convert_lists(self.get_lists(json_content))

            # Breaks loop then all values have been converted.
            if not converted:
                break

        # Adds a new uid for all nodes.
        self.add_uid(json_content)

        # Creates the new tree with the needed dictionaries.
        for tree in self.new_trees:
            UtilityLibrarian.existing_sizes.update({tree: 0})
            UtilityLibrarian.existing_symbols.update({tree: {"line": "┃", "split": "┣━", "end": "┗━"}})
            UtilityLibrarian.existing_trees.update({tree: {self.header: json_content}})

    def convert_non_strings(self, nested_dictionary):
        """
        Converts all non dictionary and non list values to string values.
        """
        # Converts the non dictionary value to a dictionary value.
        if not isinstance(nested_dictionary, dict):
            nested_dictionary = {str(nested_dictionary): {}}

        # Loops through nested dictionary.
        for parent, children in nested_dictionary.items():
            # Converts the data-types to the json datatypes in string form.
            if children is None:
                children = "null"
            if isinstance(children, bool) and children is True:
                children = "true"
            if isinstance(children, bool) and children is False:
                children = "false"

            if not isinstance(children, dict) and not isinstance(children, list):
                if children not in self.existing:
                    # Adds a new uid to the 'children' value.
                    children = str(children) + UtilityGenerator().generate_uid()

                    self.existing.append(children)

                # Adds the updated 'children' value.
                nested_dictionary.update({parent: {str(children): {}}})

            # Continue the nested loop.
            self.convert_non_strings(children)

    def get_lists(self, nested_dictionary):
        """
        Gets each list and returns them.
        """
        # Loops through nested dictionary.
        for parent, children in nested_dictionary.items():
            # Returns the found list if the value is instance of a list.
            if isinstance(children, list):
                return nested_dictionary
            else:
                # Continue the nested loop.
                returned_dictionary = self.get_lists(children)

                # Returns the list.
                if returned_dictionary:
                    return returned_dictionary

    def convert_lists(self, nested_dictionary):
        """
        Converts all values in a list to separate values in a dictionary.
        """
        # Quits the function if there is no value.
        if not nested_dictionary:
            return

        converted = False

        # Loops through nested dictionary.
        for parent, children in nested_dictionary.items():
            saved_children = []

            if isinstance(children, dict):
                # Loops through nested dictionary.
                for grandchild, great_grandchildren in children.items():
                    saved_children.append({grandchild: great_grandchildren})
            else:
                # Adds each value to the list.
                for child in children:
                    saved_children.append(child)

            # Clears the parent value.
            nested_dictionary.update({parent: {}})

            if saved_children:
                converted = True

                for saved_child in saved_children:
                    # Sets the value to a string and dictionary.
                    if not isinstance(saved_child, dict) and not isinstance(saved_child, list):
                        saved_child = {str(saved_child): {}}

                    # Loops through nested dictionary.
                    for grandchild, great_grandchildren in saved_child.items():
                        # Sets the value to a string and dictionary.
                        if not isinstance(great_grandchildren, dict) and not isinstance(great_grandchildren, list):
                            great_grandchildren = {str(great_grandchildren): {}}

                        if grandchild not in self.existing:
                            # Adds a new uid to the 'grandchild' value.
                            grandchild = str(grandchild) + UtilityGenerator().generate_uid()

                            self.existing.append(grandchild)

                        # Adds the "updated" 'grandchild' value.
                        nested_dictionary[parent].update({str(grandchild): great_grandchildren})

        return converted

    def add_uid(self, nested_dictionary):
        """
        Adds an uid to all "non-uid" values.
        """
        # Loops through nested dictionary.
        for parent, children in nested_dictionary.copy().items():
            if not isinstance(parent, dict) and not isinstance(parent, list):
                nested_dictionary.pop(parent)

                if parent not in self.existing:
                    # Adds a new uid to the 'parent' value.
                    parent = str(parent) + UtilityGenerator().generate_uid()

                    self.existing.append(parent)

                # Adds the "updated" 'parent' value.
                nested_dictionary.update({parent: children})

            # Continue the nested loop.
            self.add_uid(children)
