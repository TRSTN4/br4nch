# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler


class ResetSymbol:
    def __init__(self, tree, line=True, split=True, end=True):
        """
        Required argument(s):
        - tree

        Optional argument(s):
        - line
        - split
        - end

        :param tree: The tree(s) whose symbol(s) should be reset.
        :param line: If 'True', the line symbol is reset to the default line symbol.
        :param split: If 'True', the split symbol is reset to the default split symbol.
        :param end: If 'True', the end symbol is reset to the default end symbol.
        """
        self.trees = tree
        self.line = line
        self.split = split
        self.end = end

        self.validate_arguments()
        self.reset_symbol()

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
            # Raises an error when the line value is not a bool.
            if not isinstance(self.line, bool):
                raise UtilityHandler.InstanceBooleanError("line", self.line)

        if self.split:
            # Raises an error when the split value is not a bool.
            if not isinstance(self.split, bool):
                raise UtilityHandler.InstanceBooleanError("split", self.split)

        if self.end:
            # Raises an error when the end value is not a bool.
            if not isinstance(self.end, bool):
                raise UtilityHandler.InstanceBooleanError("end", self.end)

    def reset_symbol(self):
        """
        Resets the given symbols.
        """
        for tree in self.trees:
            # If a symbol is 'True', the default symbol will be used, else the current symbol will stay.
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

            # Sets the symbol values.
            UtilityLibrarian.existing_symbols.update({tree: {"line": self.line, "split": self.split, "end": self.end}})
