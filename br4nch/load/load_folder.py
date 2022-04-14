# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import os

from br4nch.utility.utility_librarian import existing_trees, existing_output, existing_uids, existing_sizes, \
    existing_symbols, existing_paint_trees, existing_paint_headers, existing_paint_nodes
from br4nch.utility.utility_handler import InstanceStringError, InstanceBooleanError, NotExistingDirectoryError, \
    InvalidTreeNameError, DuplicateTreeError
from br4nch.utility.utility_generator import UtilityGenerator


class LoadFolder:
    def __init__(self, tree, directory, header="", exclude="", include="", unused=True, folder_priority=True):
        self.trees = tree
        self.directory = directory
        self.header = header
        self.excludes = exclude
        self.includes = include
        self.unused = unused
        self.folder_priority = folder_priority

        self.validate_arguments()
        self.load_folder()

    def validate_arguments(self):
        if not isinstance(self.trees, list):
            self.trees = [self.trees]

        for tree in self.trees:
            if not isinstance(tree, str):
                raise InstanceStringError("tree", tree)

            if not tree.isalnum():
                raise InvalidTreeNameError(tree)

            for existing_tree in list(existing_trees):
                if tree.lower() == existing_tree.lower():
                    raise DuplicateTreeError(tree)

        if not isinstance(self.directory, str):
            raise InstanceStringError("directory", self.directory)

        if not os.path.isdir(self.directory):
            raise NotExistingDirectoryError(self.directory)

        if not isinstance(self.header, str):
            raise InstanceStringError("header", self.header)

        if not self.header:
            self.header = self.directory

        if not isinstance(self.excludes, list):
            self.excludes = [self.excludes]

        if not isinstance(self.includes, list):
            self.includes = [self.includes]

        if not isinstance(self.unused, bool):
            raise InstanceBooleanError("unused", self.unused)

        if not isinstance(self.folder_priority, bool):
            raise InstanceBooleanError("folder_priority", self.folder_priority)

        if self.folder_priority:
            self.folder_priority = False
        else:
            self.folder_priority = True

    def load_folder(self):
        for tree in self.trees:
            tree_structure = {self.header: {}}
            queue_delete = []
            paths = []
            roots = []

            for root, directories, files in os.walk(self.directory, topdown=self.folder_priority):
                paths.append(root.replace("\\", "/"))
                roots.append(root.replace("\\", "/"))

                for file in files:
                    paths.append(root.replace("\\", "/") + "/" + file)

            path_length = len(self.directory.replace("\\", "/").split("/"))

            for index in range(len(paths)):
                if self.excludes:
                    for extension in self.excludes:
                        if extension:
                            if not extension[0] == ".":
                                extension = "." + extension

                            if paths[index][-len(extension):] == extension:
                                if paths[index] not in queue_delete:
                                    queue_delete.append(paths[index])

                if self.includes:
                    for extension in range(len(self.includes)):
                        if self.includes[extension]:
                            if not self.includes[extension][0] == ".":
                                self.includes[extension] = "." + self.includes[extension]

                            if paths[index][-len(self.includes[extension]):] not in self.includes and \
                                    paths[index] not in roots:
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

                    self.create_tree(path.split("/")[path_length:][number], [self.header] + previous_file,
                                     tree_structure)

            existing_output.update({tree: []})
            existing_uids.update({tree: []})
            existing_sizes.update({tree: 0})
            existing_symbols.update({tree: {"line": "┃", "split": "┣━", "end": "┗━"}})
            existing_paint_trees.update({tree: []})
            existing_paint_headers.update({tree: []})
            existing_paint_nodes.update({tree: {}})

            self.generate_nodes_uid(tree, tree_structure[list(tree_structure)[0]])

            existing_trees.update({tree: tree_structure})

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
            parent_node_uid = parent_node + UtilityGenerator(tree)

            child[parent_node_uid] = child.pop(parent_node)
            existing_paint_nodes[tree].update({parent_node_uid: []})

            if child_nodes:
                self.generate_nodes_uid(tree, child_nodes)
