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
        """
        Required argument(s):
        - tree
        - new_node
        - target_node

        :param tree: The name of the tree(s) whose node(s) will be replaced.
        :param new_node: The new name for the node(s).
        :param new_node: The position(s) where the node(s) in the tree(s) will be replaced.
        """
        self.trees = tree
        self.new_node = new_node
        self.target_nodes = target_node

        self.validate_arguments()
        self.replace_node()

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

        # Raises an error when the 'new_node' value is not a string.
        if not isinstance(self.new_node, str):
            raise UtilityHandler.InstanceStringError("new_node", self.new_node)

        # Removes the last character in each node if it contains the newline character.
        while True:
            if self.new_node and self.new_node[-1] == "\n":
                self.new_node = self.new_node[:-1]
            else:
                break

        # If the value is not an instance of a list, set the value in the list.
        if not isinstance(self.target_nodes, list):
            self.target_nodes = [self.target_nodes]

    def replace_node(self):
        """
        Replaces the given tree node(s).
        """
        for tree in self.trees:
            # Gets each position from each node and parses them to the 'get_nodes' function.
            for position in UtilityDecider(tree, "node", self.target_nodes.copy()).get_formatted_positions():
                child = self.get_nodes(position,
                                       UtilityLibrarian.existing_trees[tree][list(
                                           UtilityLibrarian.existing_trees[tree])[0]])
                if child:
                    # Loops through the given nodes.
                    for grandchild, great_grandchild in child.items():
                        # Generates a new uid for each new node.
                        parent_node_uid = self.new_node + UtilityGenerator().generate_uid()

                        # Gets the index of the grandchild in the list.
                        index = list(great_grandchild).index(grandchild)

                        # Replaces the old tree name with the new tree name.
                        great_grandchild[parent_node_uid] = great_grandchild.pop(grandchild)

                        # Reindexing to the original position from the old grandchild.
                        for index in list(great_grandchild)[index:-1]:
                            great_grandchild[index] = great_grandchild.pop(index)

    def get_nodes(self, position, nested_dictionary):
        """
        Gets each node that must be deleted.
        """
        count = 0
        # Loops through nested dictionary.
        for parent, children in nested_dictionary.items():
            count = count + 1

            # If the 'count' value is equal to the right value in the position list, pass.
            if count == int(position[0]):
                # If the length of the 'position' list equals one, the current parent and dictionary where the parent is
                # located in will be returned.
                if len(position) == 1:
                    return {parent: nested_dictionary}
                else:
                    # If there is value, remove the first position in the list and continue the nested loop.
                    if children:
                        position.pop(0)
                        return self.get_nodes(position, children)
