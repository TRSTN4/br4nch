# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import copy

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler
from ..utility.utility_generator import UtilityGenerator
from ..utility.utility_decider import UtilityDecider


class DuplicateNode:
    def __init__(self, tree, duplicate_node, to_parent="", target_tree="", delete=False):
        """
        Required argument(s):
        - tree
        - duplicate_node

        Optional argument(s):
        - to_parent
        - target_tree
        - delete

        :param tree: The tree(s) where the node(s) to be copied are located.
        :param duplicate_node: The node(s) to be duplicated.
        :param to_parent: The parent(s) where to add the duplicated node(s).
        :param target_tree: The tree(s) where the copied node(s) will be placed at the chosen parents(s).
        :param delete: If this argument is 'True', then the node(s) in the original place will be deleted.
        """
        self.trees = tree
        self.duplicate_nodes = duplicate_node
        self.to_parents = to_parent
        self.target_trees = target_tree
        self.delete = delete

        self.validate_arguments()
        self.duplicate_node()

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
        if not isinstance(self.duplicate_nodes, list):
            self.duplicate_nodes = [self.duplicate_nodes]

        # If the value is not an instance of a list, set the value in the list.
        if not isinstance(self.to_parents, list):
            self.to_parents = [self.to_parents]

        if self.target_trees:
            # If the value is not an instance of a list, set the value in the list.
            if not isinstance(self.target_trees, list):
                self.target_trees = [self.target_trees]

            # If there is a '*' in the tree value, add all existing trees to the list.
            if "*" in self.target_trees:
                self.target_trees.clear()
                for existing_tree in list(UtilityLibrarian.existing_trees):
                    self.target_trees.append(existing_tree)

            for index in range(len(self.target_trees)):
                # Raises an error when the tree value is not a string.
                if not isinstance(self.target_trees[index], str):
                    raise UtilityHandler.InstanceStringError("target_tree", self.target_trees[index])

                # Raises an error when the given tree does not exist.
                if self.target_trees[index].lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                    raise UtilityHandler.NotExistingTreeError(self.target_trees[index])

                # Sets the tree to the exact tree name.
                for existing_tree in list(UtilityLibrarian.existing_trees):
                    if self.target_trees[index].lower() == existing_tree.lower():
                        self.target_trees[index] = existing_tree

        if self.delete:
            # Raises an error when the 'delete' value is not a bool.
            if not isinstance(self.delete, bool):
                raise UtilityHandler.InstanceBooleanError("delete", self.delete)

    def duplicate_node(self):
        """
        Duplicates each given node and parses them to the parent node.
        """
        for tree in self.trees:
            queue_delete = []
            queue_add = []

            # Parses each duplicate node to the 'UtilityDecider' class that returns the right position to copy the
            # node/position dictionary.
            for node_position in UtilityDecider(tree, "duplicate_node",
                                                self.duplicate_nodes.copy()).get_formatted_positions():
                # Parses each parent node to the 'UtilityDecider' class that returns the right position to copy the
                # value of the parent dictionary.
                for parent_position in UtilityDecider(tree, "to_parent",
                                                      self.to_parents.copy()).get_formatted_positions():
                    # Gets the parent dictionary value to add the duplicated nodes in.
                    children = self.get_nodes(tree, node_position, [],
                                              UtilityLibrarian.existing_trees[tree][list(
                                                  UtilityLibrarian.existing_trees[tree])[0]])

                    if children:
                        if self.delete:
                            # Queues for old node position dictionary deletion.
                            queue_delete.append(children[1])

                        if self.target_trees:
                            # If the 'target_trees' has a value, the nodes will be duplicated to the target tree.
                            for sibling in self.target_trees:
                                # Adds the copied node value dictionary and adds the parent value dictionary to the
                                # list.
                                queue_add.append([children[0], self.get_nodes(
                                    sibling, [], parent_position,
                                    UtilityLibrarian.existing_trees[sibling][list(
                                        UtilityLibrarian.existing_trees[sibling])[0]])])
                        else:
                            # Adds the copied node value dictionary and adds the parent value dictionary to the list.
                            queue_add.append([children[0], self.get_nodes(
                                tree, [], parent_position, UtilityLibrarian.existing_trees[tree][list(
                                    UtilityLibrarian.existing_trees[tree])[0]])])

            if self.delete:
                # Deletes all old node positions if the 'delete' value is True.
                for delete_node in queue_delete:
                    if delete_node:
                        for parent_node, child_nodes in delete_node.items():
                            del child_nodes[parent_node]

            for add_node in queue_add:
                if add_node and add_node[0] and add_node[1]:
                    # Changes each node uid.
                    self.change_node_uid(list(add_node[1])[0], add_node[0])
                    # Adds each node to the right parent position.
                    add_node[1][list(add_node[1])[0]].update(add_node[0])

    def get_nodes(self, tree, node_position, parent_position, nested_dictionary):
        """
        Gets the dictionary value of the given node/position.
        """
        # If the position value equals zero, the first height value dictionary will be returned.
        if parent_position and parent_position[0] == "0":
            return {tree: UtilityLibrarian.existing_trees[tree][list(UtilityLibrarian.existing_trees[tree])[0]]}

        count = 0
        # Loops through nested dictionary.
        for parent, children in nested_dictionary.items():
            count = count + 1

            # If the 'count' value is equal to the right value in the position list, pass.
            if node_position and count == int(node_position[0]):
                # If the length of the node position list equals one, the current node position value dictionary will be
                # returned.
                if len(node_position) == 1:
                    return [{parent: copy.deepcopy(children)}, {parent: nested_dictionary}]
                else:
                    # If there is value, remove the first node position in the list and continue the nested loop.
                    if children:
                        node_position.pop(0)
                        return self.get_nodes(tree, node_position, parent_position, children)

            # If the 'count' value is equal to the right value in the position list, pass.
            if parent_position and count == int(parent_position[0]):
                # If the length of the parent position list equals one, the current parent position value dictionary
                # will be returned.
                if len(parent_position) == 1:
                    return {tree: children}
                else:
                    # If there is value, remove the first parent position in the list and continue the nested loop.
                    if children:
                        parent_position.pop(0)
                        return self.get_nodes(tree, node_position, parent_position, children)

    def change_node_uid(self, tree, nested_dictionary):
        """
        Changes each node in the given dictionary.
        """
        # Loops through nested dictionary.
        for parent, children in nested_dictionary.copy().items():
            # Changes each node uid in the nested dictionary.
            parent_node_uid = parent[:-15] + UtilityGenerator().generate_uid()
            nested_dictionary[parent_node_uid] = nested_dictionary.pop(parent)

            if children:
                # Continue the nested loop.
                self.change_node_uid(tree, children)
