# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler


class SetSymbol:
    def __init__(self, tree, line="", split="", end=""):
        """
        Required argument(s):
        - tree

        Optional argument(s):
        - line
        - split
        - end

        :param tree: The tree where the symbols are set.
        :param line: The line symbol.
        :param split: The split symbol.
        :param end: The end symbol.
        """
        self.trees = tree
        self.line = line
        self.split = split
        self.end = end

        self.validate_arguments()
        self.set_symbol()

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

        if self.line:
            # Raises an error when the line value is not a string.
            if not isinstance(self.line, str):
                raise UtilityHandler.InstanceStringError("line", self.line)

        if self.split:
            # Raises an error when the split value is not a string.
            if not isinstance(self.split, str):
                raise UtilityHandler.InstanceStringError("split", self.split)

        if self.end:
            # Raises an error when the end value is not a string.
            if not isinstance(self.end, str):
                raise UtilityHandler.InstanceStringError("end", self.end)

        # Raises an error when there are no symbol changes.
        if not self.line and not self.split and not self.end:
            raise UtilityHandler.RequiredSymbolChangeError

        for tree in self.trees:
            # Raises an error if the size is changed and is not the default size.
            if UtilityLibrarian.existing_sizes[tree] > 0:
                raise UtilityHandler.NotChangeableError

    def set_symbol(self):
        """
        Sets each symbol.
        """
        for tree in self.trees:
            # Gets each old symbol if that symbol has not changed.
            if not self.line:
                self.line = UtilityLibrarian.existing_symbols[tree]["line"]
            if not self.split:
                self.split = UtilityLibrarian.existing_symbols[tree]["split"]
            if not self.end:
                self.end = UtilityLibrarian.existing_symbols[tree]["end"]

            # Sets the symbols.
            UtilityLibrarian.existing_symbols[tree].update({"line": self.line, "split": self.split, "end": self.end})
