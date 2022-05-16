# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler


class FilterNode:
    def __init__(self, tree, include="", exclude="", match_include=False, match_exclude=False):
        """
        Required argument(s):
        - tree

        Optional argument(s):
        - include
        - exclude
        - match_include
        - match_exclude

        :param tree: The tree that will be filtered.
        :param include: If the given word(s) are in the node, the node will be included. Else, it will not be excluded.
        :param exclude: If the given word(s) are in the node, the node will not be excluded. Else, it will be included.
        :param match_include: If this argument is 'True', then the filled in word(s) must be case-sensitive and words.
        :param match_exclude: If this argument is 'True', then the filled in word(s) must be case-sensitive and words.
        """
        self.trees = tree
        self.includes = include
        self.excludes = exclude
        self.match_include = match_include
        self.match_exclude = match_exclude

        self.build_nodes = []

        self.validate_arguments()
        self.task_manager()

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

        if self.match_include:
            # Raises an error when the value is not a bool.
            if not isinstance(self.match_include, bool):
                raise UtilityHandler.InstanceBooleanError("match_include", self.match_include)

        if self.match_exclude:
            # Raises an error when the value is not a bool.
            if not isinstance(self.match_exclude, bool):
                raise UtilityHandler.InstanceBooleanError("match_exclude", self.match_exclude)

    def task_manager(self):
        """
        Runs the head tasks to build the new filtered tree.
        """
        for tree in self.trees:
            # The current tree structure.
            tree_structure = UtilityLibrarian.existing_trees[tree][list(UtilityLibrarian.existing_trees[tree])[0]]

            if self.includes:
                # Adds all matching 'include' nodes in the list.
                self.handle_includes(tree_structure)

                if self.excludes:
                    # Removes all matching 'exclude' nodes in the list.
                    self.handle_excludes(tree_structure)

                filtered_tree = {}
                # Builds the new filtered tree.
                self.build_tree(tree_structure, filtered_tree)

                tree_structure.clear()
                # Replaces the old tree with the new filtered tree.
                tree_structure.update(filtered_tree)

            # Continues if there is no given 'includes'.
            if not self.includes and self.excludes:
                # Removes all matching 'exclude' nodes.
                self.exclude_nested(tree_structure)

    def handle_includes(self, nested_dictionary):
        """
        Adds the given 'include' value nodes.
        """
        # Loops through nested dictionary.
        for parent, children in nested_dictionary.copy().items():
            for include in self.includes:
                # Continues if the given 'include' value is in the parent value.
                if not self.match_include and include.lower() in parent[:-15].lower():
                    if parent not in self.build_nodes:
                        # Adds the parent/node to the build list.
                        self.build_nodes.append(parent)

                # Continues if the given 'include' value is an exact match with the parent value.
                if self.match_include and include == parent[:-15]:
                    if parent not in self.build_nodes:
                        # Adds the parent/node to the build list.
                        self.build_nodes.append(parent)

            if children:
                # Continue the nested loop.
                self.handle_includes(children)

    def handle_excludes(self, nested_dictionary):
        """
        Removes the given 'exclude' value nodes.
        """
        # Loops through nested dictionary.
        for parent, children in nested_dictionary.copy().items():
            for exclude in self.excludes:
                # Continues if the given 'exclude' value is in the parent value.
                if not self.match_exclude and exclude.lower() in parent[:-15].lower():
                    if parent in self.build_nodes:
                        # Removes the parent/node from the build list.
                        self.build_nodes.remove(parent)

                # Continues if the given 'exclude' value is an exact match with the parent value.
                if self.match_exclude and exclude == parent[:-15]:
                    if parent in self.build_nodes:
                        # Removes the parent/node from the build list.
                        self.build_nodes.remove(parent)

            if children:
                # Continue the nested loop.
                self.handle_excludes(children)

    def build_tree(self, nested_dictionary, filtered_tree):
        """
        Builds the filtered tree.
        """
        # Loops through nested dictionary.
        for parent, children in nested_dictionary.items():
            for node in self.build_nodes:
                # Matching nodes.
                if parent == node:
                    # Removes matching 'exclude' nodes.
                    self.exclude_nested(children)
                    # Adds the node and children to the new tree.
                    filtered_tree.update({parent: children})

            if children:
                # Continue the nested loop.
                self.build_tree(children, filtered_tree)

    def exclude_nested(self, nested_dictionary):
        """
        Removes all matching 'exclude' nodes in the nested children value.
        """
        # Loops through nested dictionary.
        for parent, children in nested_dictionary.copy().items():
            for exclude in self.excludes:
                # Continues if the given 'exclude' value is in the parent value.
                if not self.match_exclude and exclude.lower() in parent[:-15].lower():
                    # Removes matching 'exclude' parent/node.
                    nested_dictionary.pop(parent)

                # Continues if the given 'exclude' value is an exact match with the parent value.
                if self.match_exclude and exclude == parent[:-15]:
                    # Removes matching 'exclude' parent/node.
                    nested_dictionary.pop(parent)

            if children:
                # Continue the nested loop.
                self.exclude_nested(children)
