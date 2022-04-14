# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from br4nch.utility.utility_librarian import existing_trees
from br4nch.utility.utility_handler import InstanceStringError, InstanceBooleanError, InvalidParentError, \
    NotExistingTreeError
from br4nch.utility.utility_generator import UtilityGenerator
from br4nch.utility.utility_positioner import UtilityPositioner


class MoveNode:
    def __init__(self, tree, node, parent, sibling="", attributes=False):
        self.trees = tree
        self.nodes = node
        self.parent = parent
        self.sibling = sibling
        self.attributes = attributes

        self.move_node()

    def validate_arguments(self):
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        for index in range(len(self.trees)):
            if not isinstance(self.trees[index], str):
                raise InstanceStringError("tree", self.trees[index])

            if self.trees[index].lower() not in list(map(str.lower, existing_trees)):
                raise NotExistingTreeError(self.trees[index])

            for existing_tree in list(existing_trees):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(existing_trees):
                self.trees.append(existing_tree)

        if not isinstance(self.nodes, list):
            self.nodes = [self.nodes]

        if not isinstance(self.parent, str):
            raise InstanceStringError("parent", self.parent)

        for parent in self.parent.split("."):
            if not parent.isnumeric():
                raise InvalidParentError("parent", self.parent)

        if not isinstance(self.sibling, str):
            raise InstanceStringError("sibling", self.sibling)

        if self.sibling.lower() not in list(map(str.lower, existing_trees)):
            raise NotExistingTreeError(self.sibling)

        for existing_tree in list(existing_trees):
            if self.sibling.lower() == existing_tree.lower():
                self.sibling = existing_tree

        if not isinstance(self.attributes, bool):
            raise InstanceBooleanError("attributes", self.attributes)

    def move_node(self):
        for tree in self.trees:
            queue_delete = []
            queue_add = []

            for node in UtilityPositioner(tree, self.nodes.copy()):
                children = self.get_nodes(tree, node, [], existing_trees[tree][list(existing_trees[tree])[0]])

                if children:
                    queue_delete.append(children[1])

                    if self.sibling:
                        tree = self.sibling

                    queue_add.append([children[0], self.get_nodes(
                        tree, [], self.parent.split("."), existing_trees[tree][list(existing_trees[tree])[0]])])

            for delete_node in queue_delete:
                if delete_node:
                    for parent_node, child_nodes in delete_node.items():
                        del child_nodes[parent_node]

            for add_node in queue_add:
                if add_node and add_node[0] and add_node[1]:
                    self.change_nodes_uid(list(add_node[1])[0], add_node[0])
                    add_node[1][list(add_node[1])[0]].update(add_node[0])

    def get_nodes(self, tree, node, parent, child):
        if parent and parent[0] == "0":
            return {tree: existing_trees[tree][list(existing_trees[tree])[0]]}

        count = 0
        for parent_node, child_nodes in child.items():
            count = count + 1

            if node and count == int(node[0]):
                if len(node) == 1:
                    return [{parent_node: child_nodes}, {parent_node: child}]
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

    def change_nodes_uid(self, tree, child):
        for parent_node, child_nodes in child.copy().items():
            parent_node_uid = parent_node[:-15] + UtilityGenerator(tree)

            child[parent_node_uid] = child.pop(parent_node)

            if child_nodes:
                self.change_nodes_uid(tree, child_nodes)
