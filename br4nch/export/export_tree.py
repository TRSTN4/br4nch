# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import os

from br4nch.utility.utility_librarian import existing_trees, existing_uids, existing_sizes, existing_symbols, \
    existing_paint_trees, existing_paint_headers, existing_paint_nodes
from br4nch.utility.utility_handler import InstanceBooleanError, InstanceStringError, NotExistingDirectoryError, \
    NotExistingTreeError


class ExportTree:
    def __init__(self, tree, directory, attributes=False):
        self.trees = tree
        self.directory = directory
        self.attributes = attributes

        self.validate_arguments()
        self.export_tree()

    def validate_arguments(self):
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        for index in range(len(self.trees)):
            if not isinstance(self.trees[index], str):
                raise InstanceStringError("tree", self.trees[index])

            if self.trees[index].lower() not in list(map(str.lower, existing_trees)):
                raise NotExistingTreeError(self.trees[index])

            for existing_tree in list(map(str.lower, existing_trees)):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(existing_trees):
                self.trees.append(existing_tree)

        if not isinstance(self.directory, str):
            raise InstanceStringError("directory", self.directory)

        if not os.path.isdir(self.directory):
            raise NotExistingDirectoryError(self.directory)

        if not isinstance(self.attributes, bool):
            raise InstanceBooleanError("attributes", self.attributes)

    def export_tree(self):
        for tree in self.trees:
            export_attributes = {existing_paint_trees: [existing_uids[tree], existing_sizes[tree],
                                                        existing_symbols[tree], existing_paint_trees[tree],
                                                        existing_paint_headers[tree], existing_paint_nodes[tree]]}

            if not os.path.isdir(self.directory + "/br4nch-" + tree):
                os.mkdir(self.directory + "/br4nch-" + tree)

            with open(self.directory + "/br4nch-" + tree + "/branch-" + tree + ".br4nch", 'w', encoding='utf-8') \
                    as file:
                file.write("tag=tree\n")
                file.write(str({tree: existing_trees[tree]}))

            if self.attributes:
                with open(self.directory + "/br4nch-" + tree + "/package-" + tree + ".br4nch", 'w', encoding='utf-8') \
                        as file:
                    file.write("tag=attributes\n")
                    file.write(str(export_attributes))
