# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import os
import json

from br4nch.utility.utility_librarian import UtilityLibrarian
from br4nch.utility.utility_handler import UtilityHandler


class ExportJson:
    def __init__(self, tree, output_folder, data_types=False):
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
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(UtilityLibrarian.existing_trees):
                self.trees.append(existing_tree)

        for index in range(len(self.trees)):
            if not isinstance(self.trees[index], str):
                raise UtilityHandler.InstanceStringError("tree", self.trees[index])

            if self.trees[index].lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise UtilityHandler.NotExistingTreeError(self.trees[index])

            for existing_tree in list(UtilityLibrarian.existing_trees):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if not isinstance(self.output_folders, list):
            self.output_folders = [self.output_folders]

        for folder in self.output_folders:
            if not isinstance(folder, str):
                raise UtilityHandler.InstanceStringError("output_folder", folder)

            if not os.path.isdir(folder):
                raise UtilityHandler.NotExistingDirectoryError(folder)

        if not self.data_types:
            if not isinstance(self.data_types, bool):
                raise UtilityHandler.InstanceBooleanError("data_types", self.data_types)

    def task_manager(self):
        for tree in self.trees:
            structure = UtilityLibrarian.existing_trees[tree][list(UtilityLibrarian.existing_trees[tree])[0]]

            self.get_nodes(structure)
            self.sort_duplicates()
            self.update_node(structure)
            self.get_content(structure)

            while True:
                self.convert_to_dict(structure)
                if not self.content:
                    break

            for folder in self.output_folders:
                with open(folder + "/br4nch-" + tree + ".json", 'w', encoding='utf-8') as file:
                    json.dump(structure, file, indent=4)

    def get_nodes(self, nested_dictionary):
        for parent, children in nested_dictionary.copy().items():
            if children:
                self.nodes.append(parent[:-15])
                self.get_nodes(children)

    def sort_duplicates(self):
        for node in self.nodes:
            self.sorted_duplicates.update({node: []})

            for count in range(self.nodes.count(node)):
                self.sorted_duplicates[node].append(node + "#" + str(count + 1))

            if len(self.sorted_duplicates[node]) < 2:
                self.sorted_duplicates.pop(node)

    def update_node(self, nested_dictionary):
        for parent, children in nested_dictionary.copy().items():
            if parent[:-15] in self.sorted_duplicates and self.sorted_duplicates[parent[:-15]]:
                updated_parent = self.sorted_duplicates[parent[:-15]][0]
                self.sorted_duplicates[parent[:-15]].pop(0)
            else:
                updated_parent = parent[:-15]

            nested_dictionary.update({updated_parent: children})
            nested_dictionary.pop(parent)
            self.update_node(children)

    def get_content(self, nested_dictionary):
        for parent, children in nested_dictionary.items():
            if {parent: children} not in self.content:
                self.content.append({parent: children})

            self.get_content(children)

    def convert_to_dict(self, nested_dictionary):
        if isinstance(nested_dictionary, dict):
            for parent, children in nested_dictionary.items():
                if self.content:
                    if {parent: children} == self.content[-1]:
                        saved_children = []
                        set_list = False

                        self.content.pop(-1)

                        for grandchild, great_grandchildren in children.items():
                            saved_children.append({grandchild: great_grandchildren})

                        for index in range(len(saved_children)):
                            for grandchild, great_grandchildren in saved_children[index].items():
                                if isinstance(great_grandchildren, dict) and not great_grandchildren:
                                    set_list = True
                                    saved_children[index] = grandchild

                        if set_list:
                            for index in range(len(saved_children)):
                                if self.data_types:
                                    if saved_children[index] and isinstance(saved_children[index], str):
                                        if saved_children[index].lower() == "none" \
                                                or saved_children[index].lower() == "null":
                                            saved_children[index] = None
                                        elif saved_children[index].lower() == "true":
                                            saved_children[index] = True
                                        elif saved_children[index].lower() == "false":
                                            saved_children[index] = False
                                        elif saved_children[index].isdigit():
                                            saved_children[index] = int(saved_children[index])
                                        else:
                                            try:
                                                saved_children[index] = float(saved_children[index])
                                            except ValueError:
                                                pass

                            if len(saved_children) > 1:
                                nested_dictionary.update({parent: saved_children})
                            else:
                                if saved_children:
                                    nested_dictionary.update({parent: saved_children[0]})

                    self.convert_to_dict(children)
