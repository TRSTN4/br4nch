# br4nch - Data Structure Tree Builder
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

import os

from br4nch.utility.utility_librarian import output, uids, sizes, symbols, paint_branch, paint_header, paint_layer, \
    branches
from br4nch.utility.utility_generator import generate_uid
from br4nch.utility.utility_handler import InstanceStringError, InstanceBooleanError, NotExistingDirectoryError, \
    InvalidBranchNameError, DuplicateBranchError


def arguments(branch, directory, header="", include="", exclude="", unused=True, folder_priority=True):
    """
    - Gets the arguments and parses them to the 'LoadFolder' class.
    """
    LoadFolder(branch, directory, header, include, exclude, unused, folder_priority)


class LoadFolder:
    def __init__(self, argument_branch, argument_directory, argument_header, argument_include, argument_exclude,
                 argument_unused, argument_folder_priority):
        """
        - Gets the arguments and parses them to the 'load_folder' function.
        """
        self.load_folder(argument_branch, argument_directory, argument_header, argument_include, argument_exclude,
                         argument_unused, argument_folder_priority)

    def load_folder(self, argument_branch, argument_directory, argument_header, argument_include, argument_exclude,
                    argument_unused, argument_folder_priority):
        """
        Lists:
          - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.
          - If the given include argument is not an instance of a list, then the include argument will be set as a list.
          - If the given exclude argument is not an instance of a list, then the exclude argument will be set as a list.
          - Raises an 'NotExistingDirectoryError' error if the given 'argument_branch' value directory does not exists.

        Errors:
          - If the directory value is not an instance of a string, then it raises an 'InstanceStringError' error.
          - If the header value is not an instance of a string, then it raises an 'InstanceStringError' error.
          - If the unused value is not an instance of a boolean, then it raises an 'InstanceBooleanError' error.
          - If the folder_priority value is not an instance of a boolean, then it raises an 'InstanceBooleanError'
            error.

        - If the 'argument_header' argument does not have a value, then the root 'argument_directory' argument will be
          used as header value.

        - If the 'argument_folder_priority' variable is True, then it changes 'True' to 'False' and if the
          'argument_folder_priority' variable is False, then it changes 'False' to 'True'.

        Argument branch list loop:
          Errors:
            - If the branch value is not an instance of a string, then it raises an 'InstanceStringError' error.
            - If the branch value contains a character that is not a letter or number, then it raises an
              'InvalidBranchError' error.

          Branches list loop:
            Errors:
              - If the branch is already in the 'branches' dictionary, then it raises a 'DuplicateBranchError' error.

          - Loops through the given folder and adds all files to the list of 'paths'.

          - The 'path_length' variable is used to get the total length of all folders in the 'argument_directory'
            variable using the '.split' function. The 'path_length' variable is then used to slice all folders except
            the last one in the 'argument_directory' variable.

          Paths length loop:
            If 'argument_exclude':
              argument_exclude list loop:
                - If the first character in the 'extension' variable is equal to '.', then a '.' will be appended to the
                  'extension' value.
                - If the current extension from the 'path' value is equal to the 'extension' value, then it appends the
                  current path to the 'delete' list.

            If 'argument_exclude':
              argument_include range loop:
                - If the first character in the 'argument_include[extension]' value is equal to '.', then a '.' will be
                  appended to the 'argument_include[extension]' value.
                - If the current extension from the 'path' value is equal to the current loop extension value and the
                  current path is not in the 'roots' list, then it appends the current path to the 'delete' list.

          - Loops through every path and removes every path in the 'paths' list.

          If 'argument_unused' variable is 'False':
            Variable 'roots' loop:
              Variable 'paths' loop:
                - If the 'root' value is in the 'path' value, the 'hit' value will be '+1'. If the 'hit' value equals
                  '1', the 'root' value is removed from the 'paths' list.

          Paths list loop:
            Path number split loop:
              - If the 'number' value '-1' is bigger or equal to '0', then it will slice all numbers bigger then the
                current number in the 'path' split list.
              - Calls the 'create_structure' function to calculate and add the current path part to the 'structure'
                dictionary.

          - Then it will add the current 'branch' key in all the mandatory dictionaries with the needed value.
          - It will then call the 'generate_layers_uids' function that adds a uid to all layers in the 'structure'
            dictionary.
          - Then it will add the current 'structure' dictionary with the 'branch' value as key to the 'branches'
            dictionary.
        """
        if not isinstance(argument_branch, list):
            argument_branch = [argument_branch]

        if not isinstance(argument_include, list):
            argument_include = [argument_include]

        if not isinstance(argument_exclude, list):
            argument_exclude = [argument_exclude]

        if not isinstance(argument_directory, str):
            raise InstanceStringError("directory", argument_directory)

        if not isinstance(argument_header, str):
            raise InstanceStringError("header", argument_header)

        if not isinstance(argument_unused, bool):
            raise InstanceBooleanError("unused", argument_unused)

        if not isinstance(argument_folder_priority, bool):
            raise InstanceBooleanError("folder_priority", argument_folder_priority)

        if not os.path.isdir(argument_directory):
            raise NotExistingDirectoryError(argument_directory)

        if not argument_header:
            argument_header = argument_directory

        if argument_folder_priority:
            argument_folder_priority = False
        else:
            argument_folder_priority = True

        for branch in argument_branch:
            if not isinstance(branch, str):
                raise InstanceStringError("branch", branch)

            if not branch.isalnum():
                raise InvalidBranchNameError(branch)

            for branches_branch in list(branches):
                if branch.lower() == branches_branch.lower():
                    raise DuplicateBranchError(branch)

            structure = {argument_header: {}}

            paths = []
            roots = []
            delete = []

            for root, dirs, files in os.walk(argument_directory, topdown=argument_folder_priority):
                paths.append(root.replace("\\", "/"))
                roots.append(root.replace("\\", "/"))

                for file in files:
                    paths.append(root.replace("\\", "/") + "/" + file)

            path_length = len(argument_directory.replace("\\", "/").split("/"))

            for number in range(len(paths)):
                if argument_exclude:
                    for extension in argument_exclude:
                        if extension:
                            if not extension[0] == ".":
                                extension = "." + extension

                            if paths[number][-len(extension):] == extension:
                                if paths[number] not in delete:
                                    delete.append(paths[number])

                if argument_include:
                    for extension in range(len(argument_include)):
                        if argument_include[extension]:
                            if not argument_include[extension][0] == ".":
                                argument_include[extension] = "." + argument_include[extension]

                            if paths[number][-len(argument_include[extension]):] not in argument_include and \
                                    paths[number] not in roots:
                                if paths[number] not in delete:
                                    delete.append(paths[number])

            for path in delete:
                paths.remove(path)

            if not argument_unused:
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

                    self.create_structure(path.split("/")[path_length:][number], [argument_header] + previous_file,
                                          structure)

            output.update({branch: []})
            uids.update({branch: []})
            sizes.update({branch: 0})
            symbols.update({branch: {"line": "┃", "split": "┣━", "end": "┗━"}})
            paint_branch.update({branch: []})
            paint_header.update({branch: []})
            paint_layer.update({branch: {}})

            self.generate_layers_uids(branch, structure[list(structure)[0]])

            branches.update({branch: structure})

    def create_structure(self, file, previous_file, value):
        """
        Value dictionary loop:
          - If the first element in the 'previous_file' list is equal to the 'layer' value, then the first element
            in the 'previous_file' list is popped.
          - If there is no value in the 'previous_file' list and the 'file' value is not in the current value of
            'value', then the 'file' variable is added to the 'value' dictionary as key and an empty dictionary as
            value to the key.
          - If there is an value in the 'previous_file' list and/or the 'file' value exists in the current value of
            'value', then the 'create_structure' function is called with the new 'value' value.
        """
        for layer, value in value.items():
            if previous_file and layer == previous_file[0]:
                previous_file.pop(0)

                if not previous_file and file not in value:
                    return value.update({file: {}})
                else:
                    return self.create_structure(file, previous_file, value)

    def generate_layers_uids(self, branch, value):
        """
        Value dictionary loop:
          - Generates a new uid for the current 'layer' value and replaces it in all required dictionaries.
          - If there is a value in the 'value' variable, then the 'generate_layers_uids' function is called again with
            the new 'value' value as argument.
        """
        previous_value = value

        for layer, value in value.copy().items():
            uid_layer = layer + generate_uid(branch)

            previous_value[uid_layer] = previous_value.pop(layer)
            paint_layer[branch].update({uid_layer: []})

            if value:
                self.generate_layers_uids(branch, value)
