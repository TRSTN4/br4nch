# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import InstanceStringError, RequiredSymbolChangeError, NotExistingTreeError


class SetSymbol:
    def __init__(self, tree, line="", split="", end=""):
        self.trees = tree
        self.line = line
        self.split = split
        self.end = end

        self.validate_arguments()
        self.set_symbol()

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

        if not isinstance(self.line, str):
            raise InstanceStringError("line", self.line)

        if not isinstance(self.split, str):
            raise InstanceStringError("split", self.split)

        if not isinstance(self.end, str):
            raise InstanceStringError("end", self.end)

        if not self.line and not self.split and not self.end:
            raise RequiredSymbolChangeError

    def set_symbol(self):
        for tree in self.trees:
            if not self.line:
                self.line = UtilityLibrarian.existing_symbols[tree]["line"]
            if not self.split:
                self.split = UtilityLibrarian.existing_symbols[tree]["split"]
            if not self.end:
                self.end = UtilityLibrarian.existing_symbols[tree]["end"]

            UtilityLibrarian.existing_symbols[tree].update({"line": self.line, "split": self.split, "end": self.end})
