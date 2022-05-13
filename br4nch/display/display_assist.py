# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import copy

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler
from ..utility.utility_generator import UtilityGenerator
from ..display.display_tree import DisplayTree


class DisplayAssist:
    def __init__(self, tree):
        """
        Required argument(s):
        - tree

        :param tree: The tree(s) to display an assist for.
        """
        self.trees = tree

        self.validate_arguments()
        self.display_assist()

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

    def display_assist(self):
        """
        Displays the tree assist.
        """
        for tree in self.trees:
            # Gets each height and stores it in the 'levels' list.
            levels = [0]
            self.elevator(levels, UtilityLibrarian.existing_trees[tree][list(UtilityLibrarian.existing_trees[tree])[0]])
            levels.append(0)

            # Generates a new tree name.
            tree_uid = UtilityGenerator(True).generate_uid()

            # Creates each required dictionary for the tree.
            UtilityLibrarian.existing_trees.update({tree_uid: copy.deepcopy(UtilityLibrarian.existing_trees[tree])})
            UtilityLibrarian.existing_trees[tree_uid][str("0: " + list(UtilityLibrarian.existing_trees[tree])[0])] = \
                UtilityLibrarian.existing_trees[tree_uid].pop(list(UtilityLibrarian.existing_trees[tree_uid])[0])
            UtilityLibrarian.existing_sizes.update({tree_uid: 0})
            UtilityLibrarian.existing_symbols.update({tree_uid: {"line": "┃", "split": "┣━", "end": "┗━"}})

            # Calls the function to add each positions for each node to the tree.
            self.set_node_positions(levels, [0],
                                    UtilityLibrarian.existing_trees[tree_uid][list(
                                        UtilityLibrarian.existing_trees[tree_uid])[0]])

            # Prints the tree and deletes it after.
            DisplayTree(tree_uid, True)

    def elevator(self, levels, nested_dictionary, height=0):
        """
        Appends each height to a list.
        """
        # Loops through nested dictionary.
        for children in nested_dictionary.values():
            # Appends the current 'height' value to the list.
            levels.append(height)
            # Appends the current 'height' value with '+1' and continues nesting the loop.
            self.elevator(levels, children, height + 1)

    def set_node_positions(self, levels, trace, nested_dictionary, position=""):
        """
        Appends each position of each node to the tree.
        """
        count = 0
        # Loops through nested dictionary.
        for parent, children in nested_dictionary.copy().items():
            count = count + 1
            trace[0] = trace[0] + 1

            # If the 'level'/'height' of the current value in the loop is equal to or smaller than the previous
            # 'level'/'height' value in the loop, then the last number and dot in the 'position' variable is removed.
            if levels[trace[0]] <= levels[trace[0] - 1]:
                position = position[:-2]
            # Variable is added with the value of 'count' separated by a dot to the 'position' variable.
            position = position + "." + str(count)

            # Combines the position of the node to the node and removes the old node.
            nested_dictionary[position[1:] + ": " + parent] = nested_dictionary.pop(parent)

            if children:
                # Continue the nested loop.
                self.set_node_positions(levels, trace, children, position)
