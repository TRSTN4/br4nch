# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import InstanceStringError


class LogTree:
    def __init__(self, include="", exclude=""):
        self.includes = include
        self.excludes = exclude

        self.validate_arguments()
        self.log_tree()

    def validate_arguments(self):
        if self.includes:
            if not isinstance(self.includes, list):
                self.includes = [self.includes]

            for include in self.includes:
                if not isinstance(include, str):
                    raise InstanceStringError("include", include)

        if self.excludes:
            if not isinstance(self.excludes, list):
                self.excludes = [self.excludes]

            for exclude in self.excludes:
                if not isinstance(exclude, str):
                    raise InstanceStringError("exclude", exclude)

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

        for tree in trees:
            print(tree)
