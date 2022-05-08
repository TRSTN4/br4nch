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
        self.trees = tree
        self.duplicate_nodes = duplicate_node
        self.to_parents = to_parent
        self.target_trees = target_tree
        self.delete = delete

        self.validate_arguments()
        self.duplicate_node()

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

        if not isinstance(self.duplicate_nodes, list):
            self.duplicate_nodes = [self.duplicate_nodes]

        if not isinstance(self.to_parents, list):
            self.to_parents = [self.to_parents]

        if self.target_trees:
            if not isinstance(self.target_trees, list):
                self.target_trees = [self.target_trees]

            if "*" in self.target_trees:
                self.target_trees.clear()
                for existing_tree in list(UtilityLibrarian.existing_trees):
                    self.target_trees.append(existing_tree)

            for index in range(len(self.target_trees)):
                if not isinstance(self.target_trees[index], str):
                    raise UtilityHandler.InstanceStringError("target_tree", self.target_trees[index])

                if self.target_trees[index].lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                    raise UtilityHandler.NotExistingTreeError(self.target_trees[index])

                for existing_tree in list(UtilityLibrarian.existing_trees):
                    if self.target_trees[index].lower() == existing_tree.lower():
                        self.target_trees[index] = existing_tree

        if self.delete:
            if not isinstance(self.delete, bool):
                raise UtilityHandler.InstanceBooleanError("delete", self.delete)

    def duplicate_node(self):
        for tree in self.trees:
            queue_delete = []
            queue_add = []

            for node_position in UtilityDecider(tree, "to_parent",
                                                self.duplicate_nodes.copy()).get_formatted_positions():
                for parent_position in UtilityDecider(tree, "to_parent",
                                                      self.to_parents.copy()).get_formatted_positions():
                    children = self.get_nodes(tree, node_position, [],
                                              UtilityLibrarian.existing_trees[tree][list(
                                                  UtilityLibrarian.existing_trees[tree])[0]])

                    if children:
                        queue_delete.append(children[1])

                        queue_add.append([children[0], self.get_nodes(
                            tree, [], parent_position, UtilityLibrarian.existing_trees[tree][list(
                                UtilityLibrarian.existing_trees[tree])[0]])])

                        if self.target_trees:
                            for sibling in self.target_trees:
                                queue_add.append([children[0], self.get_nodes(
                                    sibling, [], parent_position,
                                    UtilityLibrarian.existing_trees[sibling][list(
                                        UtilityLibrarian.existing_trees[sibling])[0]])])

            if self.delete:
                for delete_node in queue_delete:
                    if delete_node:
                        for parent_node, child_nodes in delete_node.items():
                            del child_nodes[parent_node]

            for add_node in queue_add:
                if add_node and add_node[0] and add_node[1]:
                    self.change_node_uid(list(add_node[1])[0], add_node[0])
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

    def change_node_uid(self, tree, nested_dictionary):
        for parent, children in nested_dictionary.copy().items():
            parent_node_uid = parent[:-15] + UtilityGenerator().generate_uid()

            nested_dictionary[parent_node_uid] = nested_dictionary.pop(parent)

            if children:
                self.change_node_uid(tree, children)
