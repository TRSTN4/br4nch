# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler


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

        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(UtilityLibrarian.existing_trees):
                self.trees.append(existing_tree)

        for index in range(len(self.trees)):
            if not isinstance(self.trees[index], str):
                raise UtilityHandler.InstanceStringError("tree", self.trees[index])

            if self.trees[index].lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise UtilityHandler.NotExistingTreeError(self.trees[index])

            for existing_tree in list(UtilityLibrarian.existing_trees):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if self.line:
            if not isinstance(self.line, bool):
                raise UtilityHandler.InstanceBooleanError("line", self.line)

        if self.split:
            if not isinstance(self.split, bool):
                raise UtilityHandler.InstanceBooleanError("split", self.split)

        if self.end:
            if not isinstance(self.end, bool):
                raise UtilityHandler.InstanceBooleanError("end", self.end)

    def reset_symbol(self):
        for tree in self.trees:
            if self.line:
                self.line = "┃"
            else:
                self.line = UtilityLibrarian.existing_symbols[tree]["line"]
            if self.split:
                self.split = "┣━"
            else:
                self.split = UtilityLibrarian.existing_symbols[tree]["split"]
            if self.end:
                self.end = "┗━"
            else:
                self.end = UtilityLibrarian.existing_symbols[tree]["end"]

            UtilityLibrarian.existing_symbols.update({tree: {"line": self.line, "split": self.split, "end": self.end}})
