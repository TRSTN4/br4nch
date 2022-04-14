# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from br4nch.utility.utility_librarian import existing_trees, existing_output, existing_uids, existing_sizes, \
    existing_symbols, existing_paint_trees, existing_paint_headers, existing_paint_nodes
from br4nch.utility.utility_handler import InstanceStringError, InvalidTreeNameError, DuplicateTreeError, \
    NotExistingTreeError


class ReplaceTree:
    def __init__(self, tree, sibling):
        self.tree = tree
        self.sibling = sibling

        self.validate_arguments()
        self.replace_tree()

    def validate_arguments(self):
        if not isinstance(self.tree, str):
            raise InstanceStringError("tree", self.tree)

        if not self.tree.isalnum():
            raise InvalidTreeNameError(self.tree)

        if self.tree.lower() in list(map(str.lower, existing_trees)):
            raise DuplicateTreeError(self.tree)

        if not isinstance(self.sibling, str):
            raise InstanceStringError("sibling", self.sibling)

        if self.sibling.lower() not in list(map(str.lower, existing_trees)):
            raise NotExistingTreeError(self.sibling)

        for existing_tree in list(existing_trees):
            if self.sibling.lower() == existing_tree.lower():
                self.sibling = existing_tree

    def replace_tree(self):
        index = list(existing_trees).index(self.sibling)

        existing_trees[self.tree] = existing_trees.pop(self.sibling)
        existing_output[self.tree] = existing_output.pop(self.sibling)
        existing_uids[self.tree] = existing_uids.pop(self.sibling)
        existing_sizes[self.tree] = existing_sizes.pop(self.sibling)
        existing_symbols[self.tree] = existing_symbols.pop(self.sibling)
        existing_paint_trees[self.tree] = existing_paint_trees.pop(self.sibling)
        existing_paint_headers[self.tree] = existing_paint_headers.pop(self.sibling)
        existing_paint_nodes[self.tree] = existing_paint_nodes.pop(self.sibling)

        for position in list(existing_trees)[index:-1]:
            existing_trees[position] = existing_trees.pop(position)
            existing_output[position] = existing_output.pop(position)
            existing_uids[position] = existing_uids.pop(position)
            existing_sizes[position] = existing_sizes.pop(position)
            existing_symbols[position] = existing_symbols.pop(position)
            existing_paint_trees[position] = existing_paint_trees.pop(position)
            existing_paint_headers[position] = existing_paint_headers.pop(position)
            existing_paint_nodes[position] = existing_paint_nodes.pop(position)
