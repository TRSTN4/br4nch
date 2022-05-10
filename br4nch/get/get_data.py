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
        """
        Required argument(s):
        - tree

        Optional argument(s):
        - include_header

        :param tree: The tree which data will be retrieved.
        :param include_header: If this argument is True, then the header from the tree will be included in the data.
        """
        self.tree = tree
        self.include_header = include_header

        # Deep-copies the current tree structure.
        self.data = copy.deepcopy(UtilityLibrarian.existing_trees[self.tree])

        if self.include_header:
            # Adds the header to the data with '15' useless characters to bypass slice.
            self.data.update({list(self.data)[0] + ":uid=xxxxxxxxxx": copy.deepcopy(self.data[list(self.data)[0]])})
            # Removes the old header.
            self.data.pop(list(self.data)[0])
        else:
            # Removes the header.
            self.data = self.data[list(self.data)[0]]

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
        # Raises an error when the tree value is not a string.
        if not isinstance(self.tree, str):
            raise UtilityHandler.InstanceStringError("tree", self.tree)

        # Raises an error when the given tree does not exist.
        if self.tree.lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
            raise UtilityHandler.NotExistingTreeError(self.tree)

        # Sets the tree to the exact tree name.
        for existing_tree in list(UtilityLibrarian.existing_trees):
            if self.tree.lower() == existing_tree.lower():
                self.tree = existing_tree

    def task_manager(self):
        """
        Runs all main tasks.
        """
        # Calls each needed functions.
        self.get_nodes(self.data)
        self.sort_duplicates()
        self.update_node(self.data)
        self.get_content(self.data)

        # Converts each node value.
        while True:
            self.convert_values(self.data)
            # Breaks when all values are converted.
            if not self.content:
                break

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

                            if len(saved_children) > 1:
                                # Sets the whole list as node value.
                                nested_dictionary.update({parent: saved_children})
                            else:
                                if saved_children:
                                    # Sets the node value.
                                    nested_dictionary.update({parent: saved_children[0]})

                    # Continues the nested loop.
                    self.convert_values(children)

    def return_data(self):
        """
        Returns the data.
        """
        return self.data


def get_data(tree, include_header=False):
    """
    Required argument(s):
    - tree

    Optional argument(s):
    - include_header

    :param tree: The tree which data will be retrieved.
    :param include_header: If this argument is True, then the header from the tree will be included in the data.
    """
    return GetData(tree, include_header).return_data()
