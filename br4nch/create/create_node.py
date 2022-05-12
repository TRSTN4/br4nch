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
        """
        Required argument(s):
        - tree
        - node

        Optional argument(s):
        - parent

        :param tree: The name of the tree(s) where the node(s) will be created.
        :param node: The name for the node(s).
        :param parent: The parent(s) where the node(s) in the tree(s) are created.
        """
        self.trees = tree
        self.nodes = node
        self.parents = parent

        self.validate_arguments()
        self.build_position()

    def validate_arguments(self):
        """
        Validates the arguments.
        """
        # If the value is not an instance of a list, set the value in the list.
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        # If there is a '*' in the tree value, add all existing trees to the list.
        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(UtilityLibrarian.existing_trees):
                self.trees.append(existing_tree)

        for index in range(len(self.trees)):
            # Raises an error when the tree value is not a string.
            if not isinstance(self.trees[index], str):
                raise UtilityHandler.InstanceStringError("tree", self.trees[index])

            # Raises an error when the given tree does not exist.
            if self.trees[index].lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise UtilityHandler.NotExistingTreeError(self.trees[index])

            # Sets the tree to the exact tree name.
            for existing_tree in list(UtilityLibrarian.existing_trees):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        # If the value is not an instance of a list, set the value in the list.
        if not isinstance(self.nodes, list):
            self.nodes = [self.nodes]

        for index in range(len(self.nodes)):
            # Raises an error when the node value is not a string.
            if not isinstance(self.nodes[index], str):
                raise UtilityHandler.InstanceStringError("node", self.nodes[index])

            # Removes the last character in each node if it contains the newline character.
            while True:
                if self.nodes[index] and self.nodes[index][-1] == "\n":
                    self.nodes[index] = self.nodes[index][:-1]
                else:
                    break

        # If the there is no value in parents, add all nodes to the first height.
        if not self.parents:
            self.parents = "0"

        # If the value is not an instance of a list, set the value in the list.
        if not isinstance(self.parents, list):
            self.parents = [self.parents]

    def build_position(self):
        """
        Builds each position for each node.
        """
        for tree in self.trees:
            # Parses each parent to the 'UtilityDecider' class that returns the right position to add each node to.
            for position in UtilityDecider(tree, "parent", self.parents).get_formatted_positions():
                self.create_node(tree, position,
                                 UtilityLibrarian.existing_trees[tree][list(UtilityLibrarian.existing_trees[tree])[0]])

    def create_node(self, tree, position, nested_dictionary):
        """
        Creates each node.
        """
        # If the position value equals zero, the node(s) will be added to the first height from the tree.
        if position[0] == "0":
            for node in self.nodes:
                UtilityLibrarian.existing_trees[tree][list(UtilityLibrarian.existing_trees[tree])[0]].update(
                    {node + UtilityGenerator().generate_uid(): {}})
            return

        count = 0
        # Loops through nested dictionary.
        for children in nested_dictionary.values():
            count = count + 1

            # If the 'count' value is equal to the right value in the position list, pass.
            if count == int(position[0]):
                # If the length of the 'position' list equals one, add each node to the position.
                if len(position) == 1:
                    for node in self.nodes:
                        children.update({node + UtilityGenerator().generate_uid(): {}})
                    return
                else:
                    if children:
                        # Remove the first position in the list and continue the nested loop.
                        position.pop(0)
                        return self.create_node(tree, position, children)
