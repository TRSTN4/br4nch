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
        """
        Required argument(s):
        - new_tree
        - folder_path

        folder_path argument(s):
        - header
        - include
        - exclude
        - unused
        - folder_priority

        :param new_tree: The name for the new tree(s) that will be created for the imported folder.
        :param folder_path: The path of the folder that will be imported.
        :param header: The header name for the tree(s).
        :param include: The file extension(s) that will be displayed.
        :param exclude: The file extension(s) that won't be displayed.
        :param unused: If this argument is 'False', all directories with no content will not be displayed.
        :param folder_priority: If this argument is 'False', the files will be displayed at the top instead of the
        directories.
        """
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
        """
        Validates the arguments.
        """
        # If the value is not an instance of a list, set the value in the list.
        if not isinstance(self.new_trees, list):
            self.new_trees = [self.new_trees]

        for tree in self.new_trees:
            # Raises an error when the tree value is not a string.
            if not isinstance(tree, str):
                raise UtilityHandler.InstanceStringError("new_tree", tree)

            # Raises an error when the tree only uses numbers as name.
            if not tree.isalnum():
                raise UtilityHandler.InvalidTreeNameError(tree)

            # Raises an error when the tree already exists.
            if tree.lower() in list(map(str.lower, UtilityLibrarian.existing_trees)):
                raise UtilityHandler.DuplicateTreeError(tree)

        # Raises an error when the 'folder_path' value is not a string.
        if not isinstance(self.folder_path, str):
            raise UtilityHandler.InstanceStringError("folder_path", self.folder_path)

        # Raises an error when the given folder does not exist.
        if not os.path.isdir(self.folder_path):
            raise UtilityHandler.NotExistingDirectoryError(self.folder_path)

        if self.header:
            # Raises an error when the header value is not a string.
            if not isinstance(self.header, str):
                raise UtilityHandler.InstanceStringError("header", self.header)

        if not self.header:
            # Sets the header as the folder path if the given 'header' value is 'False'
            self.header = self.folder_path

        if self.includes:
            # If the value is not an instance of a list, set the value in the list.
            if not isinstance(self.includes, list):
                self.includes = [self.includes]

            for index in range(len(self.includes)):
                # Raises an error when the 'include' value is not a string.
                if not isinstance(self.includes[index], str):
                    raise UtilityHandler.InstanceStringError("include", self.includes[index])

                # Adds a dot to each 'include' value.
                if not self.includes[index][0] == ".":
                    self.includes[index] = "." + self.includes[index]

        if self.excludes:
            # If the value is not an instance of a list, set the value in the list.
            if not isinstance(self.excludes, list):
                self.excludes = [self.excludes]

            for index in range(len(self.excludes)):
                # Raises an error when the 'exclude' value is not a string.
                if not isinstance(self.excludes[index][0], str):
                    raise UtilityHandler.InstanceStringError("exclude", self.excludes[index][0])

                # Adds a dot to each 'exclude' value.
                if not self.excludes[index][0] == ".":
                    self.excludes[index] = "." + self.excludes[index]

        if self.unused:
            # Raises an error when the 'unused' value is not a bool.
            if not isinstance(self.unused, bool):
                raise UtilityHandler.InstanceBooleanError("unused", self.unused)

        if self.folder_priority:
            # Raises an error when the 'folder_priority' value is not a bool.
            if not isinstance(self.folder_priority, bool):
                raise UtilityHandler.InstanceBooleanError("folder_priority", self.folder_priority)

            # Swaps 'True' to 'False' and 'False' to 'True'.
            if self.folder_priority:
                self.folder_priority = False
            else:
                self.folder_priority = True

    def load_folder(self):
        """
        Loads all files in a folder and adds them to a tree.
        """
        for tree in self.new_trees:
            # The tree structure where the folder content will be added.
            tree_structure = {self.header: {}}

            queue_delete = []
            paths = []
            roots = []

            # Loops through the given folder and adds all files to the list of 'paths'.
            for root, _, files in os.walk(self.folder_path, topdown=self.folder_priority):
                # Changes the backslash characters to forward slash characters.
                paths.append(root.replace("\\", "/"))
                roots.append(root.replace("\\", "/"))

                # Adds each file with root path to the 'paths' list.
                for file in files:
                    paths.append(root.replace("\\", "/") + "/" + file)

            # Gets the total length of all folders using the '.split' function.
            paths_length = len(self.folder_path.replace("\\", "/").split("/"))

            for index in range(len(paths)):
                if self.excludes:
                    # Removes each file from adding if it does contain the extension value of 'exclude'.
                    for exclude in self.excludes:
                        if paths[index][-len(exclude):] == exclude:
                            if paths[index] not in queue_delete:
                                queue_delete.append(paths[index])

                if self.includes:
                    # Removes each file from adding if it does not contain the extension value of 'include'.
                    for include in self.includes:
                        if paths[index][-len(include):] not in self.includes and paths[index] not in roots:
                            if paths[index] not in queue_delete:
                                queue_delete.append(paths[index])

            # Removes all the paths that is queued for deletion.
            for path in queue_delete:
                paths.remove(path)

            if not self.unused:
                # Removes each folder that does not contain a used file.
                for root in roots:
                    hit = 0
                    for path in paths:
                        # Saves each same path hit and adds the value by one.
                        if root in path:
                            hit = hit + 1

                    # Removes the root path if it got hit only once.
                    if hit == 1:
                        if root in paths:
                            paths.remove(root)

            for path in paths:
                # Counts through all file parent folders.
                for total_parent_folders in range(len(path.split("/")[paths_length:])):
                    previous_file = []

                    if total_parent_folders - 1 >= 0:
                        # Slices all numbers bigger then the current number in the 'path' split list.
                        previous_file = path.split("/")[paths_length:total_parent_folders - len(
                            path.split("/")[paths_length:])]

                    # Adds each file to the tree structure.
                    self.add_file(path.split("/")[paths_length:][total_parent_folders], [self.header] + previous_file,
                                  tree_structure)

            # Sets all required values for the dictionaries to create the new folder tree.
            UtilityLibrarian.existing_sizes.update({tree: 0})
            UtilityLibrarian.existing_symbols.update({tree: {"line": "┃", "split": "┣━", "end": "┗━"}})

            # Creates new uids for all added nodes.
            self.generate_node_uids(tree, tree_structure[list(tree_structure)[0]])

            # Sets the tree structure as value for the new tree.
            UtilityLibrarian.existing_trees.update({tree: tree_structure})

    def add_file(self, file, previous_file, child):
        """
        Adds a given file to the tree dictionary.
        """
        # Loops through nested dictionary.
        for file_name, children in child.items():
            # Checks if the current file name is equal to the file name in the first element from the 'previous_file'
            # list.
            if previous_file and file_name == previous_file[0]:
                previous_file.pop(0)

                # Adds the given file in the right dictionary position.
                if not previous_file and file not in children:
                    return children.update({file: {}})
                else:
                    # Continue the nested loop.
                    return self.add_file(file, previous_file, children)

    def generate_node_uids(self, tree, nested_dictionary):
        """
        Generates a new uid for each node in the dictionary.
        """
        # Loops through nested dictionary.
        for parent, children in nested_dictionary.copy().items():
            # Changes each node uid in the nested dictionary.
            parent_node_uid = parent + UtilityGenerator().generate_uid()
            nested_dictionary[parent_node_uid] = nested_dictionary.pop(parent)

            if children:
                # Continue the nested loop.
                self.generate_node_uids(tree, children)
