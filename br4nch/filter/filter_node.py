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

        :param tree:
        :param include:
        :param exclude:
        :param match_include:
        :param match_exclude:
        """
        self.trees = tree
        self.includes = include
        self.excludes = exclude
        self.match_include = match_include
        self.match_exclude = match_exclude

        self.content = []

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
        for tree in self.trees:
            tree_structure = UtilityLibrarian.existing_trees[tree][list(UtilityLibrarian.existing_trees[tree])[0]]

            if self.includes:
                self.handle_includes(tree_structure)

                if self.excludes:
                    self.handle_excludes(tree_structure)

                filtered_tree = {}
                self.build_tree(tree_structure, filtered_tree)

                tree_structure.clear()
                tree_structure.update(filtered_tree)

            if not self.includes and self.excludes:
                self.remove_excludes(tree_structure)

    def handle_includes(self, nested_dictionary):
        for parent, children in nested_dictionary.copy().items():
            for include in self.includes:
                if not self.match_include and include.lower() in parent[:-15].lower():
                    if parent not in self.content:
                        self.content.append(parent)

                if self.match_include and include == parent[:-15]:
                    if parent not in self.content:
                        self.content.append(parent)

            if children:
                self.handle_includes(children)

    def get_nested(self, nested_dictionary):
        for parent, children in nested_dictionary.copy().items():
            if parent not in self.content:
                self.content.append(parent)

            if children:
                self.handle_excludes(children)

    def handle_excludes(self, nested_dictionary):
        for parent, children in nested_dictionary.copy().items():
            for exclude in self.excludes:
                if not self.match_exclude and exclude.lower() in parent[:-15].lower():
                    if parent in self.content:
                        self.content.remove(parent)

                if self.match_exclude and exclude == parent[:-15]:
                    if parent in self.content:
                        self.content.remove(parent)

            if children:
                self.handle_excludes(children)

    def build_tree(self, nested_dictionary, filtered_tree):
        for parent, children in nested_dictionary.items():
            for node in self.content:
                if parent == node:
                    self.exclude_nested(children)
                    filtered_tree.update({parent: children})

            if children:
                self.build_tree(children, filtered_tree)

    def exclude_nested(self, nested_dictionary):
        for parent, children in nested_dictionary.copy().items():
            for exclude in self.excludes:
                if not self.match_exclude and exclude.lower() in parent[:-15].lower():
                    nested_dictionary.pop(parent)

                if self.match_exclude and exclude == parent[:-15]:
                    nested_dictionary.pop(parent)

            if children:
                self.handle_excludes(children)

    def remove_excludes(self, nested_dictionary):
        for parent, children in nested_dictionary.copy().items():
            for exclude in self.excludes:
                if not self.match_exclude and exclude.lower() in parent[:-15].lower():
                    nested_dictionary.pop(parent)

                if self.match_exclude and exclude == parent[:-15]:
                    nested_dictionary.pop(parent)

            if children:
                self.remove_excludes(children)
