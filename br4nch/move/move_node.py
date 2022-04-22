# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import InstanceStringError, InstanceBooleanError, InvalidPositionError, \
    NotExistingTreeError
from ..utility.utility_generator import UtilityGenerator
from ..utility.utility_decider import UtilityDecider


class MoveNode:
    def __init__(self, tree, node, parent, target_tree="", attributes=False):
        self.trees = tree
        self.nodes = node
        self.parent = parent
        self.target_tree = target_tree
        self.attributes = attributes

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
                raise InstanceStringError("tree", self.trees[index])

            if self.trees[index].lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise NotExistingTreeError(self.trees[index])

            for existing_tree in list(UtilityLibrarian.existing_trees):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if not isinstance(self.nodes, list):
            self.nodes = [self.nodes]

        if not isinstance(self.parent, str):
            raise InstanceStringError("parent", self.parent)

        for parent in self.parent.split("."):
            if not parent.isnumeric():
                raise InvalidPositionError("parent", self.parent)

        if self.target_tree:
            if not isinstance(self.target_tree, str):
                raise InstanceStringError("target_tree", self.target_tree)

            if self.target_tree.lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise NotExistingTreeError(self.target_tree)

            for existing_tree in list(UtilityLibrarian.existing_trees):
                if self.target_tree.lower() == existing_tree.lower():
                    self.target_tree = existing_tree

        if self.attributes:
            if not isinstance(self.attributes, bool):
                raise InstanceBooleanError("attributes", self.attributes)

    def move_node(self):
        for tree in self.trees:
            queue_delete = []
            queue_add = []

            for node_position in UtilityDecider(tree, "node", self.nodes.copy()).get_formatted_positions():
                children = self.get_nodes(tree, node_position, [],
                                          UtilityLibrarian.existing_trees[tree][list(
                                              UtilityLibrarian.existing_trees[tree])[0]])

                if children:
                    queue_delete.append(children[1])

                    if self.target_tree:
                        tree = self.target_tree

                    queue_add.append([children[0], self.get_nodes(tree, [], self.parent.split("."),
                                                                  UtilityLibrarian.existing_trees[tree][list(
                                                                      UtilityLibrarian.existing_trees[tree])[0]])])

            for delete_node in queue_delete:
                if delete_node:
                    for parent_node, child_nodes in delete_node.items():
                        del child_nodes[parent_node]

            for add_node in queue_add:
                if add_node and add_node[0] and add_node[1]:
                    self.change_nodes_uid(list(add_node[1])[0], add_node[0])
                    add_node[1][list(add_node[1])[0]].update(add_node[0])

    def get_nodes(self, tree, node_position, parent_position, nested_dictionary):
        if parent_position and parent_position[0] == "0":
            return {tree: UtilityLibrarian.existing_trees[tree][list(UtilityLibrarian.existing_trees[tree])[0]]}

        count = 0
        for parent, children in nested_dictionary.items():
            count = count + 1

            if node_position and count == int(node_position[0]):
                if len(node_position) == 1:
                    return [{parent: children}, {parent: nested_dictionary}]
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

    def change_nodes_uid(self, tree, nested_dictionary):
        for parent_node, children in nested_dictionary.copy().items():
            parent_node_uid = parent_node[:-15] + UtilityGenerator(tree).generate_uid()

            nested_dictionary[parent_node_uid] = nested_dictionary.pop(parent_node)

            if children:
                self.change_nodes_uid(tree, children)
