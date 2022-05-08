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
        self.trees = tree
        self.move_nodes = move_node
        self.to_parent = to_parent
        self.target_tree = target_tree

        self.validate_arguments()
        self.move_node()

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

        if not isinstance(self.move_nodes, list):
            self.move_nodes = [self.move_nodes]

        if not self.to_parent:
            self.to_parent = "0"

        if not isinstance(self.to_parent, str):
            raise UtilityHandler.InstanceStringError("to_parent", self.to_parent)

        for parent in self.to_parent.split("."):
            if not parent.isnumeric():
                raise UtilityHandler.InvalidPositionError("to_parent", self.to_parent)

        if self.target_tree:
            if not isinstance(self.target_tree, str):
                raise UtilityHandler.InstanceStringError("target_tree", self.target_tree)

            if self.target_tree.lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise UtilityHandler.NotExistingTreeError(self.target_tree)

            for existing_tree in list(UtilityLibrarian.existing_trees):
                if self.target_tree.lower() == existing_tree.lower():
                    self.target_tree = existing_tree

    def move_node(self):
        for tree in self.trees:
            queue_delete = []
            queue_add = []

            for node_position in UtilityDecider(tree, "move_node", self.move_nodes.copy()).get_formatted_positions():
                children = self.get_nodes(tree, node_position, [],
                                          UtilityLibrarian.existing_trees[tree][list(
                                              UtilityLibrarian.existing_trees[tree])[0]])

                if children:
                    queue_delete.append(children[1])

                    if self.target_tree:
                        tree = self.target_tree

                    queue_add.append([children[0], self.get_nodes(tree, [], self.to_parent.split("."),
                                                                  UtilityLibrarian.existing_trees[tree][list(
                                                                      UtilityLibrarian.existing_trees[tree])[0]])])

            for delete_node in queue_delete:
                if delete_node:
                    for parent_node, child_nodes in delete_node.items():
                        del child_nodes[parent_node]

            for add_node in queue_add:
                if add_node and add_node[0] and add_node[1]:
                    add_node[1][list(add_node[1])[0]].update(add_node[0])

    def get_nodes(self, tree, node_position, parent_position, nested_dictionary):
        if parent_position and parent_position[0] == "0":
            return {tree: UtilityLibrarian.existing_trees[tree][list(UtilityLibrarian.existing_trees[tree])[0]]}

        count = 0
        for parent, children in nested_dictionary.items():
            count = count + 1

            if node_position and count == int(node_position[0]):
                if len(node_position) == 1:
                    return [{parent: copy.deepcopy(children)}, {parent: nested_dictionary}]
                else:
                    if children:
                        node_position.pop(0)
                        return self.get_nodes(tree, node_position, parent_position, children)

            if parent_position and count == int(parent_position[0]):
                if len(parent_position) == 1:
                    return {tree: children}
                else:
                    if children:
                        parent_position.pop(0)
                        return self.get_nodes(tree, node_position, parent_position, children)
