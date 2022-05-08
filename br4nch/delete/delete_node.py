# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler
from ..utility.utility_decider import UtilityDecider


class DeleteNode:
    def __init__(self, tree, node):
        self.trees = tree
        self.nodes = node

        self.validate_arguments()
        self.manage_node()

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

        if not isinstance(self.nodes, list):
            self.nodes = [self.nodes]

    def manage_node(self):
        for tree in self.trees:
            queue_delete = []

            for position in UtilityDecider(tree, "node", self.nodes.copy()).get_formatted_positions():
                child = self.get_nodes(tree, position,
                                       UtilityLibrarian.existing_trees[tree][list(
                                           UtilityLibrarian.existing_trees[tree])[0]])
                queue_delete.append(child)

            for delete_child in queue_delete:
                if delete_child:
                    for parent_node, child_nodes in delete_child.items():
                        del child_nodes[parent_node]

    def get_nodes(self, tree, position, nested_dictionary):
        count = 0
        for parent, children in nested_dictionary.items():
            count = count + 1

            if count == int(position[0]):
                if len(position) == 1:
                    return {parent: nested_dictionary}
                else:
                    if children:
                        position.pop(0)
                        return self.get_nodes(tree, position, children)
