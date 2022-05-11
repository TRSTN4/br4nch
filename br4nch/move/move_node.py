# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import copy

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler
from ..utility.utility_decider import UtilityDecider


class MoveNode:
    def __init__(self, tree, move_node, to_parent="", target_tree=""):
        """
        Required argument(s):
        - tree
        - move_node

        Optional argument(s):
        - to_parent
        - target_tree

        :param tree: The tree(s) where the node(s) that will be moved are located.
        :param move_node: The position(s) of the node(s) that will be moved.
        :param to_parent: The position/parent where to move the node(s) to.
        :param target_tree: The tree where the copied node(s) will get placed at the chosen position.
        """
        self.trees = tree
        self.move_nodes = move_node
        self.to_parent = to_parent
        self.target_tree = target_tree

        self.validate_arguments()
        self.move_node()

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
        if not isinstance(self.move_nodes, list):
            self.move_nodes = [self.move_nodes]

        if not self.to_parent:
            # Sets the position to the first height.
            self.to_parent = "0"

        # Raises an error when the 'to_parent' value is not a string.
        if not isinstance(self.to_parent, str):
            raise UtilityHandler.InstanceStringError("to_parent", self.to_parent)

        for parent in self.to_parent.split("."):
            # Validates the parent position(s).
            if not parent.isnumeric():
                raise UtilityHandler.InvalidPositionError("to_parent", self.to_parent)

        if self.target_tree:
            # Raises an error when the tree value is not a string.
            if not isinstance(self.target_tree, str):
                raise UtilityHandler.InstanceStringError("target_tree", self.target_tree)

            # Raises an error when the given tree does not exist.
            if self.target_tree.lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise UtilityHandler.NotExistingTreeError(self.target_tree)

            # Sets the tree to the exact tree name.
            for existing_tree in list(UtilityLibrarian.existing_trees):
                if self.target_tree.lower() == existing_tree.lower():
                    self.target_tree = existing_tree

    def move_node(self):
        """
        Moves each given node and parses them to the parent node.
        """
        for tree in self.trees:
            queue_delete = []
            queue_add = []

            # Parses each node to the 'UtilityDecider' class that returns the right position to move the node/position
            # dictionary.
            for node_position in UtilityDecider(tree, "move_node", self.move_nodes.copy()).get_formatted_positions():
                # Gets the parent dictionary value to add the nodes in.
                children = self.get_nodes(tree, node_position, [],
                                          UtilityLibrarian.existing_trees[tree][list(
                                              UtilityLibrarian.existing_trees[tree])[0]])

                if children:
                    # If the 'target_tree' has a value, the nodes will be duplicated to the target tree.
                    if self.target_tree:
                        tree = self.target_tree

                    # Queues for old node position dictionary deletion.
                    queue_delete.append(children[1])
                    # Adds the copied node value dictionary and adds the parent value dictionary to the list.
                    queue_add.append([children[0], self.get_nodes(tree, [], self.to_parent.split("."),
                                                                  UtilityLibrarian.existing_trees[tree][list(
                                                                      UtilityLibrarian.existing_trees[tree])[0]])])

            # Deletes all old node positions.
            for delete_node in queue_delete:
                if delete_node:
                    for parent_node, child_nodes in delete_node.items():
                        del child_nodes[parent_node]

            for add_node in queue_add:
                if add_node and add_node[0] and add_node[1]:
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
