# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from br4nch.utility.utility_librarian import UtilityLibrarian
from br4nch.utility.utility_handler import UtilityHandler
from br4nch.utility.utility_generator import UtilityGenerator
from br4nch.utility.utility_decider import UtilityDecider
from br4nch.display.display_tree import DisplayTree


class GetPosition:
    def __init__(self, tree, position="", include="", exclude="", beautify=True):
        self.trees = tree
        self.positions = position
        self.includes = include
        self.excludes = exclude
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
                raise UtilityHandler.InstanceStringError("tree", self.trees[index])

            if self.trees[index].lower() not in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise UtilityHandler.NotExistingTreeError(self.trees[index])

            for existing_tree in list(UtilityLibrarian.existing_trees):
                if self.trees[index].lower() == existing_tree.lower():
                    self.trees[index] = existing_tree

        if self.positions:
            if not isinstance(self.positions, list):
                self.positions = [self.positions]

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

    def manage_package(self):
        tree_package = []

        for tree in self.trees:
            if self.positions:
                for position in UtilityDecider(tree, "position", self.positions.copy()).get_formatted_positions():
                    visual_position = ""
                    for number in position:
                        visual_position = visual_position + "." + number

                    tree_package = self.get_position(tree, position, visual_position[1:],
                                                     UtilityLibrarian.existing_trees[tree][list(
                                                         UtilityLibrarian.existing_trees[tree])[0]], tree_package)
            else:
                levels = [0]
                self.elevator(levels,
                              UtilityLibrarian.existing_trees[tree][list(UtilityLibrarian.existing_trees[tree])[0]])
                levels.append(0)

                tree_package = self.get_all_positions(tree, levels, [0],
                                                      UtilityLibrarian.existing_trees[tree][list(
                                                          UtilityLibrarian.existing_trees[tree])[0]], tree_package, "")

        if tree_package and self.beautify:
            while True:
                tree_uid = UtilityGenerator(True).generate_uid()
                if tree_uid not in UtilityLibrarian.existing_trees:
                    break

            UtilityLibrarian.existing_trees.update({tree_uid: {"Get Position Result:": {}}})
            UtilityLibrarian.existing_output.update({tree_uid: []})
            UtilityLibrarian.existing_sizes.update({tree_uid: 0})
            UtilityLibrarian.existing_symbols.update({tree_uid: {"line": "┃", "split": "┣━", "end": "┗━"}})

            for box in tree_package:
                skip = False

                if self.includes:
                    for include in self.includes:
                        if include not in box[2]:
                            skip = True

                if self.excludes:
                    for exclude in self.excludes:
                        if exclude in box[2]:
                            skip = True

                if not skip:
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
            skip = False

            if self.includes:
                for include in self.includes:
                    if include not in parent[:-15]:
                        skip = True

            if self.excludes:
                for exclude in self.excludes:
                    if exclude in parent[:-15]:
                        skip = True

            if count == int(position[0]):
                if len(position) == 1:
                    if not skip:
                        if self.beautify:
                            tree_package.append([tree, visual_position, parent[:-15]])
                        else:
                            print(parent[:-15])
                else:
                    if children:
                        position.pop(0)
                        return self.get_position(tree, position, visual_position, children, tree_package)

        return tree_package

    def elevator(self, levels, nested_dictionary, height=0):
        for children in nested_dictionary.values():
            levels.append(height)
            self.elevator(levels, children, height + 1)

    def get_all_positions(self, tree, levels, trace, nested_dictionary, tree_package, visual_position):
        count = 0
        for parent, children in nested_dictionary.items():
            count = count + 1
            trace[0] = trace[0] + 1
            skip = False

            if levels[trace[0]] <= levels[trace[0] - 1]:
                visual_position = visual_position[:-2]
            visual_position = visual_position + "." + str(count)

            for character in visual_position:
                if character == ".":
                    visual_position = visual_position[1:]
                else:
                    break

            if self.includes:
                for include in self.includes:
                    if include not in parent[:-15]:
                        skip = True

            if self.excludes:
                for exclude in self.excludes:
                    if exclude in parent[:-15]:
                        skip = True

            if not skip:
                tree_package.append([tree, visual_position, parent[:-15]])
                if not self.beautify:
                    print(visual_position)

            if children:
                self.get_all_positions(tree, levels, trace, children, tree_package, visual_position)

        return tree_package

    def update_tree(self, tree, nested_dictionary, height=0):
        for parent, children in nested_dictionary.copy().items():
            if height == 1:
                nested_dictionary["Tree: " + parent + UtilityGenerator().generate_uid()] = \
                    nested_dictionary.pop(parent)

            if height == 2:
                nested_dictionary["Position: " + parent + UtilityGenerator().generate_uid()] = \
                    nested_dictionary.pop(parent)

            if height == 3:
                nested_dictionary["Node: " + parent + UtilityGenerator().generate_uid()] = \
                    nested_dictionary.pop(parent)

            if children:
                self.update_tree(tree, children, height + 1)
