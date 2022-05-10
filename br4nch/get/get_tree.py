# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from br4nch.utility.utility_librarian import UtilityLibrarian
from br4nch.utility.utility_handler import UtilityHandler
from br4nch.utility.utility_generator import UtilityGenerator
from br4nch.display.display_tree import DisplayTree


class GetTree:
    def __init__(self, include="", exclude="", beautify=True):
        """
        Optional argument(s):
        - node
        - sensitive
        - include

        :param include: If the given word(s) are in the tree, the tree will be displayed. Else, it will not be
        displayed.
        :param exclude: If the given word(s) are in the tree, the tree will not be displayed. Else, it will be
        displayed.
        :param beautify: If this argument is 'True', then the result will be displayed with a special branch format.
        """
        self.includes = include
        self.excludes = exclude
        self.beautify = beautify

        self.validate_arguments()
        self.get_tree()

    def validate_arguments(self):
        """
        Validates the arguments.
        """
        if self.includes:
            # If the value is not an instance of a list, set the value in the list.
            if not isinstance(self.includes, list):
                self.includes = [self.includes]

            for include in self.includes:
                # Raises an error when each 'include' value is not a string.
                if not isinstance(include, str):
                    raise UtilityHandler.InstanceStringError("include", include)

        if self.excludes:
            # If the value is not an instance of a list, set the value in the list.
            if not isinstance(self.excludes, list):
                self.excludes = [self.excludes]

            for exclude in self.excludes:
                # Raises an error when each 'exclude' value is not a string.
                if not isinstance(exclude, str):
                    raise UtilityHandler.InstanceStringError("exclude", exclude)

        if self.beautify:
            # Raises an error when the 'beautify' value is not a bool.
            if not isinstance(self.beautify, bool):
                raise UtilityHandler.InstanceBooleanError("beautify", self.beautify)

    def get_tree(self):
        """
        Gets and prints the trees.
        """
        trees = []
        for tree in list(UtilityLibrarian.existing_trees):
            # Appends each tree to the list.
            trees.append(tree)

        for tree in trees.copy():
            if self.includes:
                for include in self.includes:
                    # Removes the tree from displaying if it does not contain the value of 'include'.
                    if include not in tree:
                        trees.remove(tree)

            if self.excludes:
                for exclude in self.excludes:
                    # Removes the tree from displaying if it does contain the value of 'exclude'.
                    if exclude in tree:
                        if tree in trees:
                            trees.remove(tree)

        if self.beautify:
            # Generates a new tree name.
            tree_uid = UtilityGenerator(True).generate_uid()

            # Creates each required dictionary for the tree.
            UtilityLibrarian.existing_trees.update({tree_uid: {"Get Tree Result:": {}}})
            UtilityLibrarian.existing_output.update({tree_uid: []})
            UtilityLibrarian.existing_sizes.update({tree_uid: 0})
            UtilityLibrarian.existing_symbols.update({tree_uid: {"line": "┃", "split": "┣━", "end": "┗━"}})

            for tree in trees:
                # Adds each tree that is left from the list to the dictionary.
                UtilityLibrarian.existing_trees[tree_uid][list(UtilityLibrarian.existing_trees[tree_uid])[0]]\
                    .update({tree + UtilityGenerator().generate_uid(): {}})

            # Prints the tree and deletes it after.
            DisplayTree(tree_uid, True)
        else:
            for tree in trees:
                # Displays the tree without tree format.
                print(tree)
