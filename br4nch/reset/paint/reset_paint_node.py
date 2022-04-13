# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from br4nch.utility.utility_librarian import existing_trees, existing_paint_nodes
from br4nch.utility.utility_handler import InstanceStringError, NotExistingTreeError
from br4nch.utility.utility_positioner import format_position


class ResetPaintNode:
    def __init__(self, tree, parent):
        self.trees = tree
        self.parents = parent

        self.validate_arguments()
        self.build_parent()

    def validate_arguments(self):
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        for index in range(len(self.trees)):
            if not isinstance(self.trees[index], str):
                raise InstanceStringError("tree", self.trees[index])

            if self.trees[index] not in list(map(str.lower, existing_trees)):
                raise NotExistingTreeError(self.trees[index])

            for existing_tree in list(map(str.lower, existing_trees)):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(existing_trees):
                self.trees.append(existing_tree)

        if not isinstance(self.parents, list):
            self.parents = [self.parents]

    def build_parent(self):
        for tree in self.trees:
            for parent in format_position(tree, self.parents):
                self.reset_paint_node(tree, parent, existing_trees[tree][list(existing_trees[tree])[0]])

    def reset_paint_node(self, tree, parent, child):
        count = 0
        for parent_node, child_nodes in child.items():
            count = count + 1

            if count == int(parent[0]):
                if len(parent) == 1:
                    existing_paint_nodes[tree].update({parent_node: []})
                else:
                    parent.pop(0)
                    self.reset_paint_node(tree, parent, child_nodes)
