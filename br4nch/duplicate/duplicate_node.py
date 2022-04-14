# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import copy

from br4nch.utility.utility_librarian import existing_trees, existing_uids
from br4nch.utility.utility_handler import InstanceBooleanError, InstanceStringError, NotExistingTreeError
from br4nch.utility.utility_generator import UtilityGenerator
from br4nch.utility.utility_decider import UtilityDecider


class DuplicateNode:
    def __init__(self, tree, node, parent, sibling="", attributes=False, delete=False):
        self.trees = tree
        self.nodes = node
        self.parents = parent
        self.siblings = sibling
        self.attributes = attributes
        self.delete = delete

        self.validate_arguments()
        self.duplicate_node()

    def validate_arguments(self):
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        if not isinstance(self.nodes, list):
            self.nodes = [self.nodes]

        if not isinstance(self.parents, list):
            self.parents = [self.parents]

        if not isinstance(self.siblings, list):
            self.siblings = [self.siblings]

        if not isinstance(self.attributes, bool):
            raise InstanceBooleanError("attributes", self.attributes)

        if not isinstance(self.delete, bool):
            raise InstanceBooleanError("delete", self.delete)

        for trees in [self.trees + self.siblings]:
            for index in range(len(trees)):
                if not isinstance(trees[index], str):
                    raise InstanceStringError("tree", trees[index])

                if self.trees[index].lower() not in list(map(str.lower, existing_trees)):
                    raise NotExistingTreeError(self.trees[index])

                for existing_tree in list(existing_trees):
                    if trees[index].lower() == existing_tree.lower():
                        trees[index] = existing_tree

            if "*" in trees:
                trees.clear()
                for existing_tree in list(existing_trees):
                    trees.append(existing_tree)

    def duplicate_node(self):
        for tree in self.trees:
            queue_delete = []
            queue_add = []

            for node in UtilityDecider(tree, self.nodes.copy()):
                for parent in UtilityDecider(tree, self.parents.copy()):
                    children = self.get_nodes(tree, node, [], existing_trees[tree][list(existing_trees[tree])[0]])

                    if children:
                        queue_delete.append(children[1])

                        for sibling in self.siblings:
                            queue_add.append([children[0], self.get_nodes(
                                sibling, [], parent, existing_trees[sibling][list(existing_trees[sibling])[0]])])

            if self.delete:
                for delete_node in queue_delete:
                    if delete_node:
                        for parent_node, child_nodes in delete_node.items():
                            existing_uids[tree].remove(str(parent_node[-10:]))

                            self.delete_node_attributes(tree, child_nodes[parent_node])
                            del child_nodes[parent_node]

            for add_node in queue_add:
                if add_node and add_node[0] and add_node[1]:
                    self.change_node_uid(list(add_node[1])[0], add_node[0])
                    add_node[1][list(add_node[1])[0]].update(add_node[0])

    def get_nodes(self, tree, node, parent, child):
        if parent and parent[0] == "0":
            return {tree: existing_trees[tree][list(existing_trees[tree])[0]]}

        count = 0
        for parent_node, child_nodes in child.items():
            count = count + 1

            if node and count == int(node[0]):
                if len(node) == 1:
                    return [{parent_node: copy.deepcopy(child_nodes)}, {parent_node: child}]
                else:
                    if child_nodes:
                        node.pop(0)
                        return self.get_nodes(tree, node, parent, child_nodes)

            if parent and count == int(parent[0]):
                if len(parent) == 1:
                    return {tree: child_nodes}
                else:
                    if child_nodes:
                        parent.pop(0)
                        return self.get_nodes(tree, node, parent, child_nodes)

    def delete_node_attributes(self, tree, child):
        for parent_node, child_nodes in child.items():
            if parent_node[-10:] in existing_uids[tree]:
                existing_uids[tree].remove(str(parent_node[-10:]))

            if child_nodes:
                self.delete_node_attributes(tree, child_nodes)

    def change_node_uid(self, tree, child):
        for parent_node, child_nodes in child.copy().items():
            parent_node_uid = parent_node[:-15] + UtilityGenerator(tree)

            child[parent_node_uid] = child.pop(parent_node)

            if child_nodes:
                self.change_node_uid(tree, child_nodes)
