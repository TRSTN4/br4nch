# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from br4nch.utility.utility_librarian import UtilityLibrarian
from br4nch.utility.utility_handler import UtilityHandler
from br4nch.utility.utility_generator import UtilityGenerator
from br4nch.display.display_tree import DisplayTree


class GetPosition:
    def __init__(self, tree, node="", match_node=False, include="", exclude="", match_include=False,
                 match_exclude=False, beautify=True):
        """
        Required argument(s):
        - tree

        Optional argument(s):
        - position
        - include
        - exclude
        - match_include
        - match_exclude
        - beautify

        :param tree: The tree(s) to display a position(s) for.
        :param node: The node(s) to display the corresponding position(s).
        :param match_node: If this argument is 'True', then the filled in node must be case-sensitive and words.
        :param include: If the given word(s) are in the node, the node(s) will be displayed. Else, it will not be
        displayed.
        :param exclude: If the given word(s) are in the node, the node(s) will not be displayed. Else, it will be
        displayed.
        :param match_include: If this argument is 'True', then the filled in word(s) must be case-sensitive and words.
        :param match_exclude: If this argument is 'True', then the filled in word(s) must be case-sensitive and words.
        :param beautify: If this argument is 'True', then the result will be displayed with a special tree format.
        """
        self.trees = tree
        self.nodes = node
        self.match_node = match_node
        self.includes = include
        self.excludes = exclude
        self.match_include = match_include
        self.match_exclude = match_exclude
        self.beautify = beautify

        self.validate_arguments()
        self.manage_package()

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

        if self.nodes:
            # If the value is not an instance of a list, set the value in the list.
            if not isinstance(self.nodes, list):
                self.nodes = [self.nodes]

            for node in self.nodes:
                # Raises an error when a node value is not a string.
                if not isinstance(node, str):
                    raise UtilityHandler.InstanceStringError("node", node)

        if self.match_node:
            # Raises an error when each 'match_node' value is not a bool.
            if not isinstance(self.match_node, bool):
                raise UtilityHandler.InstanceBooleanError("match_node", self.match_node)

        if self.includes:
            # If the value is not an instance of a list, set the value in the list.
            if not isinstance(self.includes, list):
                self.includes = [self.includes]

            for include in self.includes:
                # Raises an error when each 'include' value is not a string.
                if not isinstance(include, str):
                    raise UtilityHandler.InstanceStringError("include", include)

        if self.excludes:
            # If the value is not an instance of a list, set the value in the list.
            if not isinstance(self.excludes, list):
                self.excludes = [self.excludes]

            for exclude in self.excludes:
                # Raises an error when each 'exclude' value is not a string.
                if not isinstance(exclude, str):
                    raise UtilityHandler.InstanceStringError("exclude", exclude)

        if self.match_include:
            # Raises an error when each 'match_include' value is not a bool.
            if not isinstance(self.match_include, bool):
                raise UtilityHandler.InstanceBooleanError("match_include", self.match_include)

        if self.match_exclude:
            # Raises an error when each 'match_exclude' value is not a bool.
            if not isinstance(self.match_exclude, bool):
                raise UtilityHandler.InstanceBooleanError("match_exclude", self.match_exclude)

        if self.beautify:
            # Raises an error when the 'beautify' value is not a bool.
            if not isinstance(self.beautify, bool):
                raise UtilityHandler.InstanceBooleanError("beautify", self.beautify)

    def manage_package(self):
        """
        Calls the tasks and displays the position(s).
        """
        tree_package = []
        for tree in self.trees:
            # Gets each height and stores it in the 'levels' list.
            levels = [0]
            self.elevator(levels, UtilityLibrarian.existing_trees[tree][list(UtilityLibrarian.existing_trees[tree])[0]])
            levels.append(0)

            if self.nodes:
                for node in self.nodes:
                    # Gets all specific data that is needed.
                    tree_package = self.get_specific_data(tree, node, levels, [0],
                                                          UtilityLibrarian.existing_trees[tree][list(
                                                              UtilityLibrarian.existing_trees[tree])[0]], tree_package,
                                                          "")
            else:
                # Gets all data that is needed.
                tree_package = self.get_all_data(tree, levels, [0],
                                                 UtilityLibrarian.existing_trees[tree][list(
                                                     UtilityLibrarian.existing_trees[tree])[0]], tree_package, "")

        if tree_package and self.beautify:
            # Generates a new tree name.
            tree_uid = UtilityGenerator(True).generate_uid()

            # Creates each required dictionary for the tree.
            UtilityLibrarian.existing_trees.update({tree_uid: {"Get Position Result:": {}}})
            UtilityLibrarian.existing_sizes.update({tree_uid: 0})
            UtilityLibrarian.existing_symbols.update({tree_uid: {"line": "┃", "split": "┣━", "end": "┗━"}})

            for box in tree_package:
                # Adds current tree value in the box to the tree.
                if box[0] not in UtilityLibrarian.existing_trees[tree_uid][list(
                        UtilityLibrarian.existing_trees[tree_uid])[0]]:
                    UtilityLibrarian.existing_trees[tree_uid][list(
                        UtilityLibrarian.existing_trees[tree_uid])[0]].update({box[0]: {}})

                # Adds current node value in the box to the tree.
                if box[1] not in UtilityLibrarian.existing_trees[tree_uid][list(
                        UtilityLibrarian.existing_trees[tree_uid])[0]][box[0]]:
                    UtilityLibrarian.existing_trees[tree_uid][list(
                        UtilityLibrarian.existing_trees[tree_uid])[0]][box[0]].update({box[1]: {}})

                # Adds current position value in the box to the tree.
                if box[2] not in UtilityLibrarian.existing_trees[tree_uid][list(
                        UtilityLibrarian.existing_trees[tree_uid])[0]][box[0]][box[1]]:
                    UtilityLibrarian.existing_trees[tree_uid][list(
                        UtilityLibrarian.existing_trees[tree_uid])[0]][box[0]][box[1]].update({box[2]: {}})

            # Adds uids and other visual elements to the tree.
            self.update_tree(tree_uid, UtilityLibrarian.existing_trees[tree_uid])

            # Prints the tree and deletes it after.
            DisplayTree(tree_uid, True)

    def elevator(self, levels, nested_dictionary, height=0):
        """
        Appends each height to a list.
        """
        # Loops through nested dictionary.
        for children in nested_dictionary.values():
            # Appends the current 'height' value to the list.
            levels.append(height)
            # Appends the current 'height' value with '+1' and continues nesting the loop.
            self.elevator(levels, children, height + 1)

    def get_specific_data(self, tree, node, levels, trace, nested_dictionary, tree_package, visual_position):
        """
        Gets all specific data and prints if beautify is 'False'.
        """
        count = 0
        # Loops through nested dictionary.
        for parent, children in nested_dictionary.items():
            count = count + 1
            trace[0] = trace[0] + 1
            skip = False

            # If the 'level'/'height' of the current value in the loop is equal to or smaller than the previous
            # 'level'/'height' value in the loop, then the last number and dot in the 'visual_position' variable is
            # removed.
            if levels[trace[0]] <= levels[trace[0] - 1]:
                visual_position = visual_position[:-2]
            # Variable is added with the value of 'count' separated by a dot to the 'visual_position' variable.
            visual_position = visual_position + "." + str(count)

            if self.includes:
                for include in self.includes:
                    # Continues if the given 'include' value is in the parent value.
                    if not self.match_include and include.lower() not in parent[:-15].lower():
                        skip = True

                    # Continues if the given 'include' value is an exact match with the parent value.
                    if self.match_include and include != parent[:-15]:
                        skip = True

            if self.excludes:
                for exclude in self.excludes:
                    # Continues if the given 'exclude' value is in the parent value.
                    if not self.match_exclude and exclude.lower() in parent[:-15].lower():
                        skip = True

                    # Continues if the given 'exclude' value is an exact match with the parent value.
                    if self.match_exclude and exclude == parent[:-15]:
                        skip = True

            if not skip:
                if self.match_node:
                    # Checks if the parent node without uid is equal to the current node is case-sensitive and words.
                    if parent[:-15] == node:
                        # If the first character contains a dot, it will be removed.
                        for character in visual_position:
                            if character == ".":
                                # Removes the dot in the first character.
                                visual_position = visual_position[1:]
                            else:
                                break

                        if self.beautify:
                            # Adds the tree, node and position to the dictionary.
                            tree_package.append([tree, parent[:-15], visual_position])
                        else:
                            # Displays the position without tree format.
                            print(visual_position)
                else:
                    # Checks if the parent node without uid is equal to the current node.
                    if parent[:-15].lower() == node.lower():
                        # If the first character contains a dot, it will be removed.
                        for character in visual_position:
                            if character == ".":
                                # Removes the dot in the first character.
                                visual_position = visual_position[1:]
                            else:
                                break

                        if self.beautify:
                            # Adds the tree, node and position to the dictionary.
                            tree_package.append([tree, parent[:-15], visual_position])
                        else:
                            # Displays the position without tree format.
                            print(visual_position)

            if children:
                # Continues the nested loop.
                self.get_specific_data(tree, node, levels, trace, children, tree_package, visual_position)

        return tree_package

    def get_all_data(self, tree, levels, trace, nested_dictionary, tree_package, visual_position):
        """
        Gets all needed data and prints if beautify is 'False'.
        """
        count = 0
        # Loops through nested dictionary.
        for parent, children in nested_dictionary.items():
            count = count + 1
            trace[0] = trace[0] + 1
            skip = False

            # If the 'level'/'height' of the current value in the loop is equal to or smaller than the previous
            # 'level'/'height' value in the loop, then the last number and dot in the 'visual_position' variable is
            # removed.
            if levels[trace[0]] <= levels[trace[0] - 1]:
                visual_position = visual_position[:-2]
            # Variable is added with the value of 'count' separated by a dot to the 'visual_position' variable.
            visual_position = visual_position + "." + str(count)

            # If the first character contains a dot, it will be removed.
            for character in visual_position:
                if character == ".":
                    # Removes the dot in the first character.
                    visual_position = visual_position[1:]
                else:
                    break

            if self.includes:
                for include in self.includes:
                    # Continues if the given 'include' value is in the parent value.
                    if not self.match_include and include.lower() not in parent[:-15].lower():
                        skip = True

                    # Continues if the given 'include' value is an exact match with the parent value.
                    if self.match_include and include != parent[:-15]:
                        skip = True

            if self.excludes:
                for exclude in self.excludes:
                    # Continues if the given 'exclude' value is in the parent value.
                    if not self.match_exclude and exclude.lower() in parent[:-15].lower():
                        skip = True

                    # Continues if the given 'exclude' value is an exact match with the parent value.
                    if self.match_exclude and exclude == parent[:-15]:
                        skip = True

            if not skip:
                if self.beautify:
                    # Adds the tree, node and position to the dictionary.
                    tree_package.append([tree, parent[:-15], visual_position])
                else:
                    # Displays the position without tree format.
                    print(visual_position)

            if children:
                # Continues the nested loop.
                self.get_all_data(tree, levels, trace, children, tree_package, visual_position)

        return tree_package

    def update_tree(self, tree, nested_dictionary, height=0):
        """
        Adds elements and uids to the tree.
        """
        # Loops through nested dictionary.
        for parent, children in nested_dictionary.copy().items():
            if height == 1:
                # Adds each tree to the first height.
                nested_dictionary["Tree: " + parent + UtilityGenerator().generate_uid()] = \
                    nested_dictionary.pop(parent)

            if height == 2:
                # Centers the node in the output if it contains a newline.
                updated_parent = parent.replace("\n", "\n>>>>> ")

                # Adds each node to the third height
                nested_dictionary["Node: " + updated_parent + UtilityGenerator().generate_uid()] = \
                    nested_dictionary.pop(parent)

            if height == 3:
                # Adds each position to the second height
                nested_dictionary["Position: " + parent + UtilityGenerator().generate_uid()] = \
                    nested_dictionary.pop(parent)

            if children:
                # Continues the nested loop.
                self.update_tree(tree, children, height + 1)
