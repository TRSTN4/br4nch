# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import InstanceStringError, InstanceBooleanError, NotExistingTreeError
from ..utility.utility_generator import UtilityGenerator
from ..display.display_tree import DisplayTree


class DisplayNode:
    def __init__(self, tree, node, sensitive=False, beautify=True):
        self.trees = tree
        self.nodes = node
        self.sensitive = sensitive
        self.beautify = beautify

        self.validate_arguments()
        self.manage_package()

    def validate_arguments(self):
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        if "*" in self.trees:
            self.trees.clear()
            for existing_tree in list(UtilityLibrarian.existing_trees):
                self.trees.append(existing_tree)

        for index in range(len(self.trees)):
            if not isinstance(self.trees[index], str):
                raise InstanceStringError("tree", self.trees[index])

            if self.trees[index].lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise NotExistingTreeError(self.trees[index])

            for existing_tree in list(UtilityLibrarian.existing_trees):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if not isinstance(self.nodes, list):
            self.nodes = [self.nodes]

        for node in self.nodes:
            if not isinstance(node, str):
                raise InstanceStringError("node", node)

        if self.sensitive:
            if not isinstance(self.sensitive, bool):
                raise InstanceBooleanError("sensitive", self.sensitive)

        if self.beautify:
            if not isinstance(self.beautify, bool):
                raise InstanceBooleanError("beautify", self.beautify)

    def manage_package(self):
        tree_package = []

        for tree in self.trees:
            levels = [0]
            self.elevator(levels, UtilityLibrarian.existing_trees[tree][list(UtilityLibrarian.existing_trees[tree])[0]])
            levels.append(0)

            for node in self.nodes:
                tree_package = self.get_node(
                    tree, node, levels, [0],
                    UtilityLibrarian.existing_trees[tree][list(
                        UtilityLibrarian.existing_trees[tree])[0]], tree_package, "")

        if tree_package and self.beautify:
            tree_uid = UtilityGenerator("-").generate_uid()

            UtilityLibrarian.existing_trees.update({tree_uid: {"Get Node Result:": {}}})
            UtilityLibrarian.existing_output.update({tree_uid: []})
            UtilityLibrarian.existing_uids.update({tree_uid: []})
            UtilityLibrarian.existing_sizes.update({tree_uid: 0})
            UtilityLibrarian.existing_symbols.update({tree_uid: {"line": "┃", "split": "┣━", "end": "┗━"}})

            for box in tree_package:
                if box[0] not in UtilityLibrarian.existing_trees[tree_uid][list(
                        UtilityLibrarian.existing_trees[tree_uid])[0]]:
                    UtilityLibrarian.existing_trees[tree_uid][list(
                        UtilityLibrarian.existing_trees[tree_uid])[0]].update({box[0]: {}})

                if box[1] not in UtilityLibrarian.existing_trees[tree_uid][list(
                        UtilityLibrarian.existing_trees[tree_uid])[0]][box[0]]:
                    UtilityLibrarian.existing_trees[tree_uid][list(
                        UtilityLibrarian.existing_trees[tree_uid])[0]][box[0]].update({box[1]: {}})

                if box[2] not in UtilityLibrarian.existing_trees[tree_uid][list(
                        UtilityLibrarian.existing_trees[tree_uid])[0]][box[0]][box[1]]:
                    UtilityLibrarian.existing_trees[tree_uid][list(
                        UtilityLibrarian.existing_trees[tree_uid])[0]][box[0]][box[1]].update({box[2]: {}})

            self.update_tree(tree_uid, UtilityLibrarian.existing_trees[tree_uid])

            DisplayTree(tree_uid, True)

    def elevator(self, levels, child, height=0):
        for child_nodes in child.values():
            levels.append(height)
            self.elevator(levels, child_nodes, height + 1)

    def get_node(self, tree, node, levels, trace, child, tree_package, position):
        count = 0
        for parent_node, child_nodes in child.items():
            count = count + 1

            trace[0] = trace[0] + 1

            if levels[trace[0]] <= levels[trace[0] - 1]:
                position = position[:-2]

            position = position + "." + str(count)

            if self.sensitive:
                if parent_node[:-15] == node:
                    tree_package.append([tree, parent_node[:-15], position[1:]])
                    if not self.beautify:
                        print(position[1:])
            else:
                if parent_node[:-15].lower() == node.lower():
                    tree_package.append([tree, parent_node[:-15], position[1:]])
                    if not self.beautify:
                        print(position[1:])

            if child_nodes:
                self.get_node(tree, node, levels, trace, child_nodes, tree_package, position)

        return tree_package

    def update_tree(self, tree, child, height=0):
        for parent_node, child_nodes in child.copy().items():
            if height == 1:
                child["Tree: " + parent_node + UtilityGenerator(tree).generate_uid()] = child.pop(parent_node)

            if height == 2:
                child["Node: " + parent_node + UtilityGenerator(tree).generate_uid()] = child.pop(parent_node)

            if height == 3:
                child["Position: " + parent_node + UtilityGenerator(tree).generate_uid()] = child.pop(parent_node)

            if child_nodes:
                self.update_tree(tree, child_nodes, height + 1)
