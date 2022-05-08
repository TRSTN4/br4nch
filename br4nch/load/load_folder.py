# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import os

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler
from ..utility.utility_generator import UtilityGenerator


class LoadFolder:
    def __init__(self, new_tree, folder_path, header="", include="", exclude="", unused=True, folder_priority=True):
        self.new_trees = new_tree
        self.folder_path = folder_path
        self.header = header
        self.includes = include
        self.excludes = exclude
        self.unused = unused
        self.folder_priority = folder_priority

        self.validate_arguments()
        self.load_folder()

    def validate_arguments(self):
        if not isinstance(self.new_trees, list):
            self.new_trees = [self.new_trees]

        for tree in self.new_trees:
            if not isinstance(tree, str):
                raise UtilityHandler.InstanceStringError("new_tree", tree)

            if not tree.isalnum():
                raise UtilityHandler.InvalidTreeNameError(tree)

            if tree.lower() in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise UtilityHandler.DuplicateTreeError(tree)

        if not isinstance(self.folder_path, str):
            raise UtilityHandler.InstanceStringError("folder_path", self.folder_path)

        if not os.path.isdir(self.folder_path):
            raise UtilityHandler.NotExistingDirectoryError(self.folder_path)

        if self.header:
            if not isinstance(self.header, str):
                raise UtilityHandler.InstanceStringError("header", self.header)

        if not self.header:
            self.header = self.folder_path

        if self.includes:
            if not isinstance(self.includes, list):
                self.includes = [self.includes]

            for index in range(len(self.includes)):
                if not isinstance(self.includes[index], str):
                    raise UtilityHandler.InstanceStringError("include", self.includes[index])

                if not self.includes[index][0] == ".":
                    self.includes[index] = "." + self.includes[index]

        if self.excludes:
            if not isinstance(self.excludes, list):
                self.excludes = [self.excludes]

            for index in range(len(self.excludes)):
                if not isinstance(self.excludes[index][0], str):
                    raise UtilityHandler.InstanceStringError("exclude", self.excludes[index][0])

                if not self.excludes[index][0] == ".":
                    self.excludes[index] = "." + self.excludes[index]

        if self.unused:
            if not isinstance(self.unused, bool):
                raise UtilityHandler.InstanceBooleanError("unused", self.unused)

        if self.folder_priority:
            if not isinstance(self.folder_priority, bool):
                raise UtilityHandler.InstanceBooleanError("folder_priority", self.folder_priority)

            if self.folder_priority:
                self.folder_priority = False
            else:
                self.folder_priority = True

    def load_folder(self):
        for tree in self.new_trees:
            tree_structure = {self.header: {}}
            queue_delete = []
            paths = []
            roots = []

            for root, directories, files in os.walk(self.folder_path, topdown=self.folder_priority):
                paths.append(root.replace("\\", "/"))
                roots.append(root.replace("\\", "/"))

                for file in files:
                    paths.append(root.replace("\\", "/") + "/" + file)

            path_length = len(self.folder_path.replace("\\", "/").split("/"))

            for index in range(len(paths)):
                if self.excludes:
                    for exclude in self.excludes:
                        if paths[index][-len(exclude):] == exclude:
                            if paths[index] not in queue_delete:
                                queue_delete.append(paths[index])

                if self.includes:
                    for include in self.includes:
                        if paths[index][-len(include):] not in self.includes and paths[index] not in roots:
                            if paths[index] not in queue_delete:
                                queue_delete.append(paths[index])

            for path in queue_delete:
                paths.remove(path)

            if not self.unused:
                for root in roots:
                    hit = 0
                    for path in paths:
                        if root in path:
                            hit = hit + 1
                    if hit == 1:
                        if root in paths:
                            paths.remove(root)

            for path in paths:
                for number in range(len(path.split("/")[path_length:])):
                    previous_file = []

                    if number - 1 >= 0:
                        previous_file = path.split("/")[path_length:number - len(path.split("/")[path_length:])]

                    self.create_tree(
                        path.split("/")[path_length:][number], [self.header] + previous_file, tree_structure)

            UtilityLibrarian.existing_output.update({tree: []})
            UtilityLibrarian.existing_sizes.update({tree: 0})
            UtilityLibrarian.existing_symbols.update({tree: {"line": "┃", "split": "┣━", "end": "┗━"}})

            self.generate_nodes_uid(tree, tree_structure[list(tree_structure)[0]])

            UtilityLibrarian.existing_trees.update({tree: tree_structure})

    def create_tree(self, file, previous_file, child):
        for parent_node, child_nodes in child.items():
            if previous_file and parent_node == previous_file[0]:
                previous_file.pop(0)

                if not previous_file and file not in child_nodes:
                    return child_nodes.update({file: {}})
                else:
                    return self.create_tree(file, previous_file, child_nodes)

    def generate_nodes_uid(self, tree, child):
        for parent_node, child_nodes in child.copy().items():
            parent_node_uid = parent_node + UtilityGenerator().generate_uid()

            child[parent_node_uid] = child.pop(parent_node)

            if child_nodes:
                self.generate_nodes_uid(tree, child_nodes)
