# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler
from ..utility.utility_generator import UtilityGenerator
from ..utility.utility_decider import UtilityDecider


class CreateNode:
    def __init__(self, tree, node, parent=""):
        self.trees = tree
        self.nodes = node
        self.parents = parent

        self.validate_arguments()
        self.build_position()

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

        for index in range(len(self.nodes)):
            if not isinstance(self.nodes[index], str):
                raise UtilityHandler.InstanceStringError("node", self.nodes[index])

            while True:
                if self.nodes[index] and self.nodes[index][-1] == "\n":
                    self.nodes[index] = self.nodes[index][:-1]
                else:
                    break

        if not self.parents:
            self.parents = "0"

        if not isinstance(self.parents, list):
            self.parents = [self.parents]

    def build_position(self):
        for tree in self.trees:
            for position in UtilityDecider(tree, "parent", self.parents).get_formatted_positions():
                self.create_node(tree, position,
                                 UtilityLibrarian.existing_trees[tree][list(UtilityLibrarian.existing_trees[tree])[0]])

    def create_node(self, tree, position, nested_dictionary):
        if position[0] == "0":
            for node in self.nodes:
                UtilityLibrarian.existing_trees[tree][list(UtilityLibrarian.existing_trees[tree])[0]].update(
                    {node + UtilityGenerator().generate_uid(): {}})
            return

        count = 0
        for children in nested_dictionary.values():
            count = count + 1

            if count == int(position[0]):
                if len(position) == 1:
                    for node in self.nodes:
                        children.update({node + UtilityGenerator().generate_uid(): {}})
                    return
                else:
                    if children:
                        position.pop(0)
                        return self.create_node(tree, position, children)
