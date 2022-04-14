# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from br4nch.utility.utility_librarian import existing_trees, existing_output, existing_uids, existing_sizes, \
    existing_symbols, existing_paint_trees, existing_paint_headers, existing_paint_nodes
from br4nch.utility.utility_handler import InstanceStringError, NotExistingTreeError


class DeleteTree:
    def __init__(self, tree):
        self.trees = tree

        self.validate_arguments()
        self.delete_tree()

    def validate_arguments(self):
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        for tree in self.trees:
            if not isinstance(tree, str):
                raise InstanceStringError("tree", tree)

            if tree.lower() not in list(map(str.lower, existing_trees)):
                raise NotExistingTreeError(tree)

        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(existing_trees):
                self.trees.append(existing_tree)

    def delete_tree(self):
        for tree in self.trees:
            del existing_trees[tree]
            del existing_output[tree]
            del existing_uids[tree]
            del existing_sizes[tree]
            del existing_symbols[tree]
            del existing_paint_trees[tree]
            del existing_paint_headers[tree]
            del existing_paint_nodes[tree]
