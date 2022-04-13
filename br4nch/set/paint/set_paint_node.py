# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from br4nch.utility.utility_librarian import existing_trees, existing_paint_nodes
from br4nch.utility.utility_handler import InstanceStringError, NotExistingTreeError, NotExistingPaintError
from br4nch.utility.utility_positioner import format_position


class SetPaintNode:
    def __init__(self, tree, parent, paint):
        self.trees = tree
        self.parents = parent
        self.paint = paint

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

        if not isinstance(self.paint, list):
            self.paint = [self.paint]

        for paint in self.paint:
            if not isinstance(paint, str):
                raise InstanceStringError("paint", paint)

            if paint.lower() not in ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white", "bold",
                                     "underline"]:
                raise NotExistingPaintError(paint)

    def build_parent(self):
        for tree in self.trees:
            for position in format_position(tree, self.parents.copy()):
                self.set_paint_layer(tree, position, existing_trees[tree][list(existing_trees[tree])[0]])

    def set_paint_layer(self, tree, parent, child):
        count = 0
        for parent_node, child_nodes in child.items():
            count = count + 1

            if count == int(parent[0]):
                if len(parent) == 1:
                    existing_paint_nodes[tree].update({parent_node: self.paint})
                else:
                    if child_nodes:
                        parent.pop(0)
                        return self.set_paint_layer(tree, parent, child_nodes)
