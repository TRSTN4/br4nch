# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

import os
import ast

from br4nch.utility.utility_handler import NotExistingBranchFileError, InvalidBranchFileError, \
    NotExistingPackageFileError, InvalidPackageFileError, DuplicateBranchError
from br4nch.utility.utility_librarian import branches, output, uids, sizes, symbols, paint_branch, paint_header, \
    paint_layer


def arguments(branch_file, package_file=""):
    """
    - Gets the arguments and parses them to the 'load_branch' function.
    """
    load_branch(branch_file, package_file)


def load_branch(argument_branch_file, argument_package_file):
    """
    Load branch:
      Errors:
        - Raises an 'NotExistingBranchFileError' error if the instance of the 'argument_branch_file' variable is a
          string and the given directory does not exists.
        - If given branch file does not have the required branch id tag or the length of the total lines is not equal to
          '2', then it raises an 'InvalidBranchFileError' error.
        - If the 'argument_branch_file' is not a instance of a string and/or the given directory does not exists, the
          content of the branch file will be assigned to the 'argument_branch_file' variable. then it raises an
          'InstanceDictionaryError' error.

    Load package:
      Errors:
        - Raises an 'NotExistingPackageFileError' error if there is value in the the 'argument_package_file' variable
          and is instance of string and the given directory does not exists.
        - If given package file does not have the required package id tag or the length of the total lines is not equal
          to '2', then it raises an 'InvalidPackageFileError' error.
        - If there is a value in the 'argument_package_file' variable and is not a instance of a string and/or the given
          directory does not exists, then it raises an 'InstanceDictionaryError' error.

    Branches list loop:
      Errors:
        - If the branch is already in the 'branches' dictionary, then it raises a 'DuplicateBranchError' error.

    - If the value of the 'argument_package_file' variable is true, then update the values of all required dictionaries
      with the values of the given package argument.
    - If the value of the 'argument_package_file' variable is false, then update the values of all required dictionaries
      with the default values for a new branch.
    """
    if isinstance(argument_branch_file, str) and not os.path.isfile(argument_branch_file):
        raise NotExistingBranchFileError(argument_branch_file)
    elif isinstance(argument_branch_file, str) and os.path.isfile(argument_branch_file):
        with open(argument_branch_file, 'r', encoding="utf8") as file:
            file = file.readlines()

            if len(file) != 2:
                raise InvalidBranchFileError(argument_branch_file)

            if str(file[0][:-1]) != "id=:br4nch-branch:":
                raise InvalidBranchFileError(argument_branch_file)

            argument_branch_file = ast.literal_eval(file[1])

    if argument_package_file and isinstance(argument_package_file, str) and not os.path.isfile(argument_package_file):
        raise NotExistingPackageFileError(argument_package_file)
    elif argument_package_file and isinstance(argument_package_file, str) and os.path.isfile(argument_package_file):
        with open(argument_package_file, 'r', encoding="utf8") as file:
            file = file.readlines()

            if len(file) != 2:
                raise InvalidPackageFileError(argument_package_file)

            if str(file[0][:-1]) != "id=:br4nch-package:":
                raise InvalidPackageFileError(argument_package_file)

            argument_package_file = ast.literal_eval(file[1])

    if argument_branch_file:
        for branches_branch in list(branches):
            if list(argument_branch_file)[0].lower() == branches_branch.lower():
                raise DuplicateBranchError(list(argument_branch_file)[0])

        branches.update({list(argument_branch_file)[0]: list(argument_branch_file.values())[0]})
        output.update({list(argument_branch_file)[0]: []})

        if argument_package_file and list(argument_package_file)[0] == list(argument_branch_file)[0] and len(list(argument_package_file.values())[0]) == 6:
            uids.update({list(argument_branch_file)[0]: list(argument_package_file.values())[0][0]})
            sizes.update({list(argument_branch_file)[0]: list(argument_package_file.values())[0][1]})
            symbols.update({list(argument_branch_file)[0]: list(argument_package_file.values())[0][2]})
            paint_branch.update({list(argument_branch_file)[0]: list(argument_package_file.values())[0][3]})
            paint_header.update({list(argument_branch_file)[0]: list(argument_package_file.values())[0][4]})
            paint_layer.update({list(argument_branch_file)[0]: list(argument_package_file.values())[0][5]})
        else:
            uids.update({list(argument_branch_file)[0]: []})
            sizes.update({list(argument_branch_file)[0]: 0})
            symbols.update({list(argument_branch_file)[0]: {"line": "┃", "split": "┣━", "end": "┗━"}})
            paint_branch.update({list(argument_branch_file)[0]: []})
            paint_header.update({list(argument_branch_file)[0]: []})
            paint_layer.update({list(argument_branch_file)[0]: {}})
