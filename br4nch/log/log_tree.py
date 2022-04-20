# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import existing_trees
from ..utility.utility_handler import InstanceStringError


class LogTree:
    def __init__(self, include="", exclude=""):
        self.include = include
        self.exclude = exclude

        self.validate_arguments()
        self.log_tree()

    def validate_arguments(self):
        if self.include:
            if not isinstance(self.include, list):
                self.include = [self.include]

            for include in self.include:
                if not isinstance(include, str):
                    raise InstanceStringError("include", include)

        if self.exclude:
            if not isinstance(self.exclude, list):
                self.exclude = [self.exclude]

            for exclude in self.exclude:
                if not isinstance(exclude, str):
                    raise InstanceStringError("exclude", exclude)

    def log_tree(self):
        trees = []
        for tree in list(existing_trees):
            trees.append(tree)

        for tree in trees.copy():
            if self.include:
                for include in self.include:
                    if include not in tree:
                        trees.remove(tree)

            if self.exclude:
                for exclude in self.exclude:
                    if exclude in tree:
                        if tree in trees:
                            trees.remove(tree)

        for tree in trees:
            print(tree)
