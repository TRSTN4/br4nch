# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler
from ..utility.utility_generator import UtilityGenerator
from ..utility.utility_decider import UtilityDecider


class ReplaceNode:
    def __init__(self, tree, new_node, target_node):
        self.trees = tree
        self.new_node = new_node
        self.target_nodes = target_node

        self.validate_arguments()
        self.replace_node()

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

        if not isinstance(self.new_node, str):
            raise UtilityHandler.InstanceStringError("new_node", self.new_node)

        while True:
            if self.new_node and self.new_node[-1] == "\n":
                self.new_node = self.new_node[:-1]
            else:
                break

        if not isinstance(self.target_nodes, list):
            self.target_nodes = [self.target_nodes]

    def replace_node(self):
        for tree in self.trees:
            for position in UtilityDecider(tree, "node", self.target_nodes.copy()).get_formatted_positions():
                child = self.get_nodes(position,
                                       UtilityLibrarian.existing_trees[tree][list(
                                           UtilityLibrarian.existing_trees[tree])[0]])
                if child:
                    for parent_node, child_nodes in child.items():
                        parent_node_uid = self.new_node + UtilityGenerator().generate_uid()

                        index = list(child_nodes).index(parent_node)
                        child_nodes[parent_node_uid] = child_nodes.pop(parent_node)

                        for index in list(child_nodes)[index:-1]:
                            child_nodes[index] = child_nodes.pop(index)

    def get_nodes(self, position, nested_dictionary):
        count = 0
        for parent, children in nested_dictionary.items():
            count = count + 1

            if count == int(position[0]):
                if len(position) == 1:
                    return {parent: nested_dictionary}
                else:
                    if children:
                        position.pop(0)
                        return self.get_nodes(position, children)
