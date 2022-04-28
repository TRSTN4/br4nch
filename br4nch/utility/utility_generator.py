# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import uuid

from ..utility.utility_librarian import UtilityLibrarian


class UtilityGenerator:
    def __init__(self, tree=False):
        self.tree = tree

        self.generate_uid()

    def generate_uid(self):
        uid = str(uuid.uuid4()).replace("-", "")[0:10]

        if self.tree == "-":
            if uid not in list(UtilityLibrarian.existing_trees):
                return uid
        else:
            return ":uid=" + uid
