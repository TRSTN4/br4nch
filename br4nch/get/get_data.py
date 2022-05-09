# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import copy

from br4nch.utility.utility_librarian import UtilityLibrarian
from br4nch.utility.utility_handler import UtilityHandler


class GetData:
    def __init__(self, tree, include_header=False):
        self.tree = tree
        self.include_header = include_header

        self.data = copy.deepcopy(UtilityLibrarian.existing_trees[self.tree])

        if self.include_header:
            self.data.update({list(self.data)[0] + ":uid=xxxxxxxxxx": copy.deepcopy(self.data[list(self.data)[0]])})
            self.data.pop(list(self.data)[0])
        else:
            self.data = self.data[list(self.data)[0]]

        self.nodes = []
        self.duplicates = []
        self.sorted_duplicates = {}
        self.content = []

        self.validate_arguments()
        self.task_manager()

    def validate_arguments(self):
        if not isinstance(self.tree, str):
            raise UtilityHandler.InstanceStringError("tree", self.tree)

        if self.tree.lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
            raise UtilityHandler.NotExistingTreeError(self.tree)

        for existing_tree in list(UtilityLibrarian.existing_trees):
            if self.tree.lower() == existing_tree.lower():
                self.tree = existing_tree

    def task_manager(self):
        self.get_nodes(self.data)
        self.sort_duplicates()
        self.update_node(self.data)
        self.get_content(self.data)

        while True:
            self.convert_to_dict(self.data)
            if not self.content:
                break

    def get_nodes(self, nested_dictionary):
        for parent, children in nested_dictionary.copy().items():
            self.nodes.append(parent[:-15])

            if children:
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
                            if len(saved_children) > 1:
                                nested_dictionary.update({parent: saved_children})
                            else:
                                if saved_children:
                                    nested_dictionary.update({parent: saved_children[0]})

                    self.convert_to_dict(children)

    def return_data(self):
        return self.data


def get_data(tree, include_header=False):
    return GetData(tree, include_header).return_data()
