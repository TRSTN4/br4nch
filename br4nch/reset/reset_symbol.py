# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import existing_trees, existing_symbols
from ..utility.utility_handler import InstanceBooleanError, InstanceStringError, NotExistingTreeError


class ResetSymbol:
    def __init__(self, tree, line=True, split=True, end=True):
        self.trees = tree
        self.line = line
        self.split = split
        self.end = end

        self.validate_arguments()
        self.reset_symbol()

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

        if not isinstance(self.line, bool):
            raise InstanceBooleanError("line", self.line)

        if not isinstance(self.split, bool):
            raise InstanceBooleanError("split", self.split)

        if not isinstance(self.end, bool):
            raise InstanceBooleanError("end", self.end)

    def reset_symbol(self):
        for tree in self.trees:
            if self.line:
                self.line = "┃"
            else:
                self.line = existing_symbols[tree]["line"]
            if self.split:
                self.split = "┣━"
            else:
                self.split = existing_symbols[tree]["split"]
            if self.end:
                self.end = "┗━"
            else:
                self.end = existing_symbols[tree]["end"]

            existing_symbols.update({tree: {"line": self.line, "split": self.split, "end": self.end}})
