# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import NotExistingTreeError, InstanceStringError


class LogNode:
    def __init__(self, tree, include="", exclude=""):
        self.trees = tree
        self.includes = include
        self.excludes = exclude

        self.validate_arguments()
        self.log_node()

    def validate_arguments(self):
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        for index in range(len(self.trees)):
            if not isinstance(self.trees[index], str):
                raise InstanceStringError("tree", self.trees[index])

            if self.trees[index].lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise NotExistingTreeError(self.trees[index])

            for existing_tree in list(UtilityLibrarian.existing_trees):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(UtilityLibrarian.existing_trees):
                self.trees.append(existing_tree)

        if self.includes:
            if not isinstance(self.includes, list):
                self.includes = [self.includes]

            for include in self.includes:
                if not isinstance(include, str):
                    raise InstanceStringError("include", include)

        if self.excludes:
            if not isinstance(self.excludes, list):
                self.excludes = [self.excludes]

            for exclude in self.excludes:
                if not isinstance(exclude, str):
                    raise InstanceStringError("exclude", exclude)

    def log_node(self):
        for tree in self.trees:
            nodes = self.get_node(tree,
                                  UtilityLibrarian.existing_trees[tree][list(
                                      UtilityLibrarian.existing_trees[tree])[0]], [])

            for node in nodes.copy():
                if self.includes:
                    for include in self.includes:
                        if include not in node[:-15]:
                            nodes.remove(node)

                if self.excludes:
                    for exclude in self.excludes:
                        if exclude in node[:-15]:
                            if node in nodes:
                                nodes.remove(node)

            for node in nodes:
                print(node[:-15])

    def get_node(self, tree, child, nodes):
        for parent_node, child_nodes in child.items():
            nodes.append(parent_node)

            if child_nodes:
                self.get_node(tree, child_nodes, nodes)

        return nodes
