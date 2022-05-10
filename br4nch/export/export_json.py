# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import os
import copy
import json

from br4nch.utility.utility_librarian import UtilityLibrarian
from br4nch.utility.utility_handler import UtilityHandler


class ExportJson:
    def __init__(self, tree, output_folder, data_types=False):
        """
        Required argument(s):
        - tree
        - output_folder

        Optional argument(s):
        - data_types

        :param tree: The tree that will be exported to a json file.
        :param output_folder: The output directory for the json file.
        :param data_types: If this argument is True, then the 'string data types' will be converted into
        'json data types'.
        """
        self.trees = tree
        self.output_folders = output_folder
        self.data_types = data_types

        self.nodes = []
        self.duplicates = []
        self.sorted_duplicates = {}
        self.content = []

        self.validate_arguments()
        self.task_manager()

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

        if not self.data_types:
            # Raises an error when the 'data_types' value is not a bool.
            if not isinstance(self.data_types, bool):
                raise UtilityHandler.InstanceBooleanError("data_types", self.data_types)

    def task_manager(self):
        """
        Runs all main tasks.
        """
        for tree in self.trees:
            # Deep-copies the current tree structure.
            data = copy.deepcopy(UtilityLibrarian.existing_trees[tree][list(UtilityLibrarian.existing_trees[tree])[0]])

            # Calls each needed functions.
            self.get_nodes(data)
            self.sort_duplicates()
            self.update_node(data)
            self.get_content(data)

            # Converts each node value.
            while True:
                self.convert_values(data)
                # Breaks when all values are converted.
                if not self.content:
                    break

            for folder in self.output_folders:
                # Creates the json file.
                with open(folder + "/br4nch-" + tree + ".json", 'w', encoding='utf-8') as file:
                    # Dumps the data in json format.
                    json.dump(data, file, indent=4)

    def get_nodes(self, nested_dictionary):
        """
        Gets each node that must be deleted.
        """
        # Loops through nested dictionary.
        for parent, children in nested_dictionary.copy().items():
            # Appends each node without uid to the list.
            self.nodes.append(parent[:-15])

            if children:
                # Continues the nested loop.
                self.get_nodes(children)

    def sort_duplicates(self):
        """
        Sorts and adds a number to each duplicate node.
        """
        for node in self.nodes:
            # Adds all nodes to the dictionary.
            self.sorted_duplicates.update({node: []})

            # Adds a number going upwards for each duplicate node.
            for count in range(self.nodes.count(node)):
                self.sorted_duplicates[node].append(node + "#" + str(count + 1))

            # If the node name has no duplicates, the node will be removed from the dictionary.
            if len(self.sorted_duplicates[node]) < 2:
                self.sorted_duplicates.pop(node)

    def update_node(self, nested_dictionary):
        """
        Updates the node in the data.
        """
        # Loops through nested dictionary.
        for parent, children in nested_dictionary.copy().items():
            # If the current node has duplicates.
            if parent[:-15] in self.sorted_duplicates and self.sorted_duplicates[parent[:-15]]:
                # Removes the uid from the node and appends the current duplicate number to the node.
                updated_parent = self.sorted_duplicates[parent[:-15]][0]
                # Removes the number node from the list.
                self.sorted_duplicates[parent[:-15]].pop(0)
            else:
                # Removes only the uid from the node.
                updated_parent = parent[:-15]

            # Adds the new updated node to the dictionary and removes the old node.
            nested_dictionary.update({updated_parent: children})
            nested_dictionary.pop(parent)

            # Continues the nested loop.
            self.update_node(children)

    def get_content(self, nested_dictionary):
        """
        Gets each node and value.
        """
        # Loops through nested dictionary.
        for parent, children in nested_dictionary.items():
            # Appends node and value to the list.
            if {parent: children} not in self.content:
                self.content.append({parent: children})

            # Continues the nested loop.
            self.get_content(children)

    def convert_values(self, nested_dictionary):
        """
        Converts and changes each node values.
        """
        if isinstance(nested_dictionary, dict):
            # Loops through nested dictionary.
            for parent, children in nested_dictionary.items():
                if self.content:
                    # Formats the last dictionary in the list first.
                    if {parent: children} == self.content[-1]:
                        saved_children = []
                        change_data_type = False

                        # Removes the last dictionary in the list.
                        self.content.pop(-1)

                        # Appends each dictionary value.
                        for grandchild, great_grandchildren in children.items():
                            saved_children.append({grandchild: great_grandchildren})

                        for index in range(len(saved_children)):
                            for grandchild, great_grandchildren in saved_children[index].items():
                                if isinstance(great_grandchildren, dict) and not great_grandchildren:
                                    # Adds each last node without value.
                                    saved_children[index] = grandchild
                                    change_data_type = True

                        if self.data_types and change_data_type:
                            for index in range(len(saved_children)):
                                # Continues if 'data_types' is 'True' and the current index in the list is a string.
                                if saved_children[index] and isinstance(saved_children[index], str):
                                    # Converts 'none' string to 'None' NoneType.
                                    if saved_children[index].lower() == "none" \
                                            or saved_children[index].lower() == "null":
                                        saved_children[index] = None
                                    # Converts 'true' string to 'True' bool.
                                    elif saved_children[index].lower() == "true":
                                        saved_children[index] = True
                                    # Converts 'false' string to 'False' bool.
                                    elif saved_children[index].lower() == "false":
                                        saved_children[index] = False
                                    # Converts any int string to int.
                                    elif saved_children[index].isdigit():
                                        saved_children[index] = int(saved_children[index])
                                    else:
                                        try:
                                            # Convert the string to float if the string can be a float.
                                            saved_children[index] = float(saved_children[index])
                                        except ValueError:
                                            pass

                            if len(saved_children) > 1:
                                # Sets the whole list as node value.
                                nested_dictionary.update({parent: saved_children})
                            else:
                                if saved_children:
                                    # Sets the node value.
                                    nested_dictionary.update({parent: saved_children[0]})

                    # Continues the nested loop.
                    self.convert_values(children)
