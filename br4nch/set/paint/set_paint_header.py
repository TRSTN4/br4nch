# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from br4nch.utility.utility_librarian import existing_trees, existing_paint_headers
from br4nch.utility.utility_handler import InstanceStringError, NotExistingPaintError, NotExistingTreeError


class SetPaintHeader:
    def __init__(self, tree, paint):
        self.trees = tree
        self.paint = paint

        self.validate_arguments()
        self.set_paint_header()

    def validate_arguments(self):
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        for index in range(len(self.trees)):
            if not isinstance(self.trees[index], str):
                raise InstanceStringError("tree", self.trees[index])

            if self.trees[index].lower() not in list(map(str.lower, existing_trees)):
                raise NotExistingTreeError(self.trees[index])

            for existing_tree in list(map(str.lower, existing_trees)):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(existing_trees):
                self.trees.append(existing_tree)

        if not isinstance(self.paint, list):
            self.paint = [self.paint]

        for paint in self.paint:
            if not isinstance(paint, str):
                raise InstanceStringError("paint", paint)

            if paint.lower() not in ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white", "bold",
                                     "underline"]:
                raise NotExistingPaintError(paint)

    def set_paint_header(self):
        for tree in self.trees:
            existing_paint_headers.update({tree: self.paint})
