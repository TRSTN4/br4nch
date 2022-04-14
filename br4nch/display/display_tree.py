# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from br4nch.utility.utility_librarian import existing_trees, existing_output, existing_uids, existing_sizes, \
    existing_symbols, existing_paint_trees, existing_paint_headers, existing_paint_nodes
from br4nch.utility.utility_handler import InstanceBooleanError, InstanceStringError, NotExistingTreeError
from br4nch.utility.utility_builder import UtilityBuilder


class DisplayTree:
    def __init__(self, tree, delete=False):
        self.trees = tree
        self.delete = delete

        self.validate_arguments()
        self.display_tree()

    def validate_arguments(self):
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        for index in range(len(self.trees)):
            if not isinstance(self.trees[index], str):
                raise InstanceStringError("tree", self.trees[index])

            if self.trees[index].lower() not in list(map(str.lower, existing_trees)):
                raise NotExistingTreeError(self.trees[index])

            for existing_tree in list(existing_trees):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(existing_trees):
                self.trees.append(existing_tree)

        if not isinstance(self.delete, bool):
            raise InstanceBooleanError("delete", self.delete)

    def display_tree(self):
        for tree in self.trees:
            total = [0]
            if not existing_paint_trees[tree]:
                total[0] = total[0] + 1

            if not existing_paint_headers[tree]:
                total[0] = total[0] + 1

            no_paint = 0
            for layer in existing_paint_nodes[tree]:
                if not existing_paint_nodes[tree][layer]:
                    no_paint = no_paint + 1

            if no_paint == len(existing_paint_nodes[tree]):
                total[0] = total[0] + 1

            if total[0] == 3:
                colored = False
            else:
                colored = True

            UtilityBuilder(tree, colored)

            for line in existing_output[tree]:
                print(line)
            existing_output[tree].clear()

            if self.delete:
                del existing_trees[tree]
                del existing_output[tree]
                del existing_uids[tree]
                del existing_sizes[tree]
                del existing_symbols[tree]
                del existing_paint_trees[tree]
                del existing_paint_headers[tree]
                del existing_paint_nodes[tree]
