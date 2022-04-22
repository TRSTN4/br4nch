# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import copy

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import InstanceBooleanError, InstanceStringError, NotExistingTreeError
from ..utility.utility_generator import UtilityGenerator
from ..utility.utility_decider import UtilityDecider


class DuplicateNode:
    def __init__(self, tree, node, parent, target_tree="", attributes=False, delete=False):
        self.trees = tree
        self.nodes = node
        self.parents = parent
        self.target_trees = target_tree
        self.attributes = attributes
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
                raise InstanceStringError("tree", self.trees[index])

            if self.trees[index].lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise NotExistingTreeError(self.trees[index])

            for existing_tree in list(UtilityLibrarian.existing_trees):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if not isinstance(self.nodes, list):
            self.nodes = [self.nodes]

        if not isinstance(self.parents, list):
            self.parents = [self.parents]

        if self.target_trees:
            if not isinstance(self.target_trees, list):
                self.target_trees = [self.target_trees]

        if "*" in self.target_trees:
            self.target_trees.clear()
            for existing_tree in list(UtilityLibrarian.existing_trees):
                self.target_trees.append(existing_tree)

        for index in range(len(self.target_trees)):
            if not isinstance(self.target_trees[index], str):
                raise InstanceStringError("target_tree", self.target_trees[index])

            if self.target_trees[index].lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise NotExistingTreeError(self.target_trees[index])

            for existing_tree in list(UtilityLibrarian.existing_trees):
                if self.target_trees[index].lower() == existing_tree.lower():
                    self.target_trees[index] = existing_tree

        if self.attributes:
            if not isinstance(self.attributes, bool):
                raise InstanceBooleanError("attributes", self.attributes)

        if self.delete:
            if not isinstance(self.delete, bool):
                raise InstanceBooleanError("delete", self.delete)

    def duplicate_node(self):
        for tree in self.trees:
            queue_delete = []
            queue_add = []

            for node_position in UtilityDecider(tree, "node", self.nodes.copy()).get_formatted_positions():
                for parent_position in UtilityDecider(tree, "parent", self.parents.copy()).get_formatted_positions():
                    children = self.get_nodes(tree, node_position, [],
                                              UtilityLibrarian.existing_trees[tree][list(
                                                  UtilityLibrarian.existing_trees[tree])[0]])

                    if children:
                        queue_delete.append(children[1])

                        for sibling in self.target_trees:
                            queue_add.append([children[0], self.get_nodes(
                                sibling, [], parent_position,
                                UtilityLibrarian.existing_trees[sibling][list(
                                    UtilityLibrarian.existing_trees[sibling])[0]])])

            if self.delete:
                for delete_node in queue_delete:
                    if delete_node:
                        for parent_node, child_nodes in delete_node.items():
                            UtilityLibrarian.existing_uids[tree].remove(str(parent_node[-10:]))

                            self.delete_node_attributes(tree, child_nodes[parent_node])
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

    def delete_node_attributes(self, tree, nested_dictionary):
        for parent, children in nested_dictionary.items():
            if parent[-10:] in UtilityLibrarian.existing_uids[tree]:
                UtilityLibrarian.existing_uids[tree].remove(str(parent[-10:]))

            if children:
                self.delete_node_attributes(tree, children)

    def change_node_uid(self, tree, nested_dictionary):
        for parent, children in nested_dictionary.copy().items():
            parent_node_uid = parent[:-15] + UtilityGenerator(tree).generate_uid()

            nested_dictionary[parent_node_uid] = nested_dictionary.pop(parent)

            if children:
                self.change_node_uid(tree, children)
