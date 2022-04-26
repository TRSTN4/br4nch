# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import InstanceStringError, InstanceBooleanError, NotExistingTreeError
from ..utility.utility_generator import UtilityGenerator
from ..utility.utility_decider import UtilityDecider
from ..display.display_tree import DisplayTree


class DisplayPosition:
    def __init__(self, tree, position, beautify=True):
        self.trees = tree
        self.positions = position
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

        if not isinstance(self.positions, list):
            self.positions = [self.positions]

        if self.beautify:
            if not isinstance(self.beautify, bool):
                raise InstanceBooleanError("beautify", self.beautify)

    def manage_package(self):
        tree_package = []

        for tree in self.trees:
            for position in UtilityDecider(tree, "position", self.positions.copy()).get_formatted_positions():
                visual_position = ""
                for number in position:
                    visual_position = visual_position + "." + number

                tree_package = self.get_position(tree, position, visual_position[1:],
                                                 UtilityLibrarian.existing_trees[tree][list(
                                                     UtilityLibrarian.existing_trees[tree])[0]], tree_package)

        if tree_package and self.beautify:
            while True:
                tree_uid = UtilityGenerator("-").generate_uid()
                if tree_uid not in UtilityLibrarian.existing_trees:
                    break

            UtilityLibrarian.existing_trees.update({tree_uid: {"Get Position Result:": {}}})
            UtilityLibrarian.existing_output.update({tree_uid: []})
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

    def get_position(self, tree, position, visual_position, nested_dictionary, tree_package):
        count = 0
        for parent, children in nested_dictionary.items():
            count = count + 1

            if count == int(position[0]):
                if len(position) == 1:
                    if self.beautify:
                        tree_package.append([tree, visual_position, parent[:-15]])
                    else:
                        print(parent[:-15])
                else:
                    if children:
                        position.pop(0)
                        return self.get_position(tree, position, visual_position, children, tree_package)

        return tree_package

    def update_tree(self, tree, nested_dictionary, height=0):
        for parent, children in nested_dictionary.copy().items():
            if height == 1:
                nested_dictionary["Tree: " + parent + UtilityGenerator(tree).generate_uid()] = \
                    nested_dictionary.pop(parent)

            if height == 2:
                nested_dictionary["Position: " + parent + UtilityGenerator(tree).generate_uid()] = \
                    nested_dictionary.pop(parent)

            if height == 3:
                nested_dictionary["Node: " + parent + UtilityGenerator(tree).generate_uid()] = \
                    nested_dictionary.pop(parent)

            if children:
                self.update_tree(tree, children, height + 1)
