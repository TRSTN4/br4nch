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
        """
        Required argument(s):
        - tree
        - node

        :param tree: The name of the tree(s) where the node(s) will be deleted.
        :param node: The node(s) that will be deleted.
        """
        self.trees = tree
        self.nodes = node

        self.validate_arguments()
        self.delete_node()

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

    def delete_node(self):
        """
        Deletes the given nodes.
        """
        for tree in self.trees:
            queue_delete = []

            # Gets each position from each node and parses them to the 'get_nodes' function.
            for position in UtilityDecider(tree, "node", self.nodes.copy()).get_formatted_positions():
                child = self.get_nodes(tree, position,
                                       UtilityLibrarian.existing_trees[tree][list(
                                           UtilityLibrarian.existing_trees[tree])[0]])
                queue_delete.append(child)

            # Deletes each node from the tree.
            for delete_child in queue_delete:
                if delete_child:
                    for parent_node, child_nodes in delete_child.items():
                        del child_nodes[parent_node]

    def get_nodes(self, tree, position, nested_dictionary):
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
                    # Remove the first position in the list and continue the nested loop.
                    if children:
                        position.pop(0)
                        return self.get_nodes(tree, position, children)
