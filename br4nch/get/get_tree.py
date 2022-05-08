# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from br4nch.utility.utility_librarian import UtilityLibrarian
from br4nch.utility.utility_handler import UtilityHandler
from br4nch.utility.utility_generator import UtilityGenerator
from br4nch.display.display_tree import DisplayTree


class GetTree:
    def __init__(self, include="", exclude="", beautify=True):
        self.includes = include
        self.excludes = exclude
        self.beautify = beautify

        self.validate_arguments()
        self.log_tree()

    def validate_arguments(self):
        if self.includes:
            if not isinstance(self.includes, list):
                self.includes = [self.includes]

            for include in self.includes:
                if not isinstance(include, str):
                    raise UtilityHandler.InstanceStringError("include", include)

        if self.excludes:
            if not isinstance(self.excludes, list):
                self.excludes = [self.excludes]

            for exclude in self.excludes:
                if not isinstance(exclude, str):
                    raise UtilityHandler.InstanceStringError("exclude", exclude)

        if self.beautify:
            if not isinstance(self.beautify, bool):
                raise UtilityHandler.InstanceBooleanError("beautify", self.beautify)

    def log_tree(self):
        trees = []
        for tree in list(UtilityLibrarian.existing_trees):
            trees.append(tree)

        for tree in trees.copy():
            if self.includes:
                for include in self.includes:
                    if include not in tree:
                        trees.remove(tree)

            if self.excludes:
                for exclude in self.excludes:
                    if exclude in tree:
                        if tree in trees:
                            trees.remove(tree)

        if self.beautify:
            tree_uid = UtilityGenerator(True).generate_uid()

            UtilityLibrarian.existing_trees.update({tree_uid: {"Get Tree Result:": {}}})
            UtilityLibrarian.existing_output.update({tree_uid: []})
            UtilityLibrarian.existing_sizes.update({tree_uid: 0})
            UtilityLibrarian.existing_symbols.update({tree_uid: {"line": "┃", "split": "┣━", "end": "┗━"}})

            for tree in trees:
                UtilityLibrarian.existing_trees[tree_uid][list(UtilityLibrarian.existing_trees[tree_uid])[0]]\
                    .update({tree + UtilityGenerator().generate_uid(): {}})

            DisplayTree(tree_uid, True)
        else:
            for tree in trees:
                print(tree)
