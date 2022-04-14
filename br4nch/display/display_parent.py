# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from br4nch.utility.utility_librarian import existing_trees, existing_output, existing_uids, existing_sizes, \
    existing_symbols
from br4nch.utility.utility_handler import InstanceStringError, InstanceBooleanError, NotExistingTreeError
from br4nch.utility.utility_generator import UtilityGenerator
from br4nch.utility.utility_positioner import UtilityPositioner
from br4nch.display.display_tree import DisplayTree


class DisplayParent:
    def __init__(self, tree, parent, beautify=True):
        self.trees = tree
        self.parents = parent
        self.beautify = beautify

        self.validate_arguments()
        self.get_package()

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

        if not isinstance(self.parents, list):
            self.parents = [self.parents]

        if not isinstance(self.beautify, bool):
            raise InstanceBooleanError("beautify", self.beautify)

    def get_package(self):
        tree_package = []

        for tree in self.trees:
            for parent in UtilityPositioner(tree, self.parents.copy()):
                string_position = ""

                for character in parent:
                    string_position = string_position + "." + character

                tree_package = self.get_parent(
                    tree, parent, string_position[1:], existing_trees[tree][list(existing_trees[tree])[0]],
                    tree_package)

        if tree_package and self.beautify:
            while True:
                tree_uid = UtilityGenerator("-")
                if tree_uid not in existing_trees:
                    break

            existing_trees.update({tree_uid: {"Get Parent Result:": {}}})
            existing_output.update({tree_uid: []})
            existing_uids.update({tree_uid: []})
            existing_sizes.update({tree_uid: 0})
            existing_symbols.update({tree_uid: {"line": "┃", "split": "┣━", "end": "┗━"}})

            for box in tree_package:
                if box[0] not in existing_trees[tree_uid][list(existing_trees[tree_uid])[0]]:
                    existing_trees[tree_uid][list(existing_trees[tree_uid])[0]].update({box[0]: {}})

                if box[1] not in existing_trees[tree_uid][list(existing_trees[tree_uid])[0]][box[0]]:
                    existing_trees[tree_uid][list(existing_trees[tree_uid])[0]][box[0]].update({box[1]: {}})

                if box[2] not in existing_trees[tree_uid][list(existing_trees[tree_uid])[0]][box[0]][box[1]]:
                    existing_trees[tree_uid][list(existing_trees[tree_uid])[0]][box[0]][box[1]].update({box[2]: {}})

            self.update_tree(tree_uid, existing_trees[tree_uid])

            DisplayTree(tree_uid, True)

    def get_parent(self, tree, parent, position, child, tree_package):
        count = 0
        for parent_node, child_nodes in child.items():
            count = count + 1

            if count == int(parent[0]):
                if len(parent) == 1:
                    if self.beautify:
                        tree_package.append([tree, position, parent_node[:-15]])
                    else:
                        print(parent_node[:-15])
                else:
                    if child_nodes:
                        parent.pop(0)
                        return self.get_parent(tree, parent, position, child_nodes, tree_package)

        return tree_package

    def update_tree(self, tree, child, height=0):
        for parent_node, child_nodes in child.copy().items():
            if height == 1:
                child["Tree: " + parent_node + UtilityGenerator(tree)] = child.pop(parent_node)

            if height == 2:
                child["Parent: " + parent_node + UtilityGenerator(tree)] = child.pop(parent_node)

            if height == 3:
                child["Node: " + parent_node + UtilityGenerator(tree)] = child.pop(parent_node)

            if child_nodes:
                self.update_tree(tree, child_nodes, height + 1)
