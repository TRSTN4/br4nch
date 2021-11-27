# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

class NotExistingBranchError(Exception):
    """
    - If the branch is not in the 'branches' dictionary, it raises a 'NotExistingBranchError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, branch):
        self.branch = branch

    def __str__(self):
        return "The branch '" + str(self.branch) + "' does not exists."


class DuplicateBranchError(Exception):
    """
    - If the branch value is already in the 'branches' dictionary, then it raises a 'DuplicateBranchError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, branch):
        self.branch = branch

    def __str__(self):
        return "The branch '" + str(self.branch) + "' already exists."


class StringInstanceError(Exception):
    """
    - If the given argument value is not an instance of a string, then it raises an 'StringInstanceError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, argument, parsed):
        self.argument = argument
        self.parsed = parsed

    def __str__(self):
        return "The " + str(self.argument) + " argument '" + str(self.parsed) + "' must be an instance of a "\
               + "'string' and not '" + str(type(self.parsed).__name__) + "'."


class IntegerInstanceError(Exception):
    """
    - If the given argument value is not an instance of a integer, then it raises an 'IntegerInstanceError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, argument, parsed):
        self.argument = argument
        self.parsed = parsed

    def __str__(self):
        return "The " + str(self.argument) + " argument '" + str(self.parsed) + "' must be an instance of a "\
               + "'integer' and not '" + str(type(self.parsed).__name__) + "'."


class BooleanInstanceError(Exception):
    """
    - If the given argument value is not an instance of a boolean, then it raises an 'BooleanInstanceError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, argument, parsed):
        self.argument = argument
        self.parsed = parsed

    def __str__(self):
        return "The " + str(self.argument) + " argument '" + str(self.parsed) + "' must be an instance of a "\
               + "'boolean' and not '" + str(type(self.parsed).__name__) + "'."


class DictionaryInstanceError(Exception):
    """
    - If the given argument value is not an instance of a dictionary, then it raises an 'DictionaryInstanceError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, argument, parsed):
        self.argument = argument
        self.parsed = parsed

    def __str__(self):
        return "The " + str(self.argument) + " argument '" + str(self.parsed) + "' must be an instance of a "\
               + "'dictionary' and not '" + str(type(self.parsed).__name__) + "'."


class RequiredChangeError(Exception):
    """
    - If there is no value in the 'line', 'split' and 'end' arguments, then it raises an 'RequiredChangeError' error.
    """
    __module__ = Exception.__module__

    def __str__(self):
        return "Change at least one of the given symbols: 'line', 'split' or 'end'."


class InvalidBranchError(Exception):
    """
    - If the branch value contains a character that is not a letter or number, then it raises an 'InvalidBranchError'
      error.
    """
    __module__ = Exception.__module__

    def __str__(self):
        return "Only numbers and/or letters may be used to add a branch."


class InvalidPositionError(Exception):
    """
    - If the pos argument is not equal to a number and/or operator, then it raises an 'InvalidPositionError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, position, argument):
        self.position = position
        self.argument = argument

    def __str__(self):
        return "The position: '" + self.position + "' is not valid. Only numbers and operators may be used to add a " \
                                                   "position to the '" + self.argument + "' argument."


class InvalidDirectoryError(Exception):
    """
    - If the given directory argument does not exist, it will throw a 'InvalidDirectoryError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, directory):
        self.directory = directory

    def __str__(self):
        return "The directory '" + str(self.directory) + "' does not exist."


class InvalidBranchFileError(Exception):
    """
    - If given branch file does not have the required branch id tag or the length of the total lines is less than '2',
      then it raises an 'InvalidBranchFileError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, file):
        self.file = file

    def __str__(self):
        return "The file: '" + self.file + "' is not valid as a branch file."


class InvalidPackageFileError(Exception):
    """
    - If given package file does not have the required branch id tag or the length of the total lines is less than '2',
      then it raises an 'InvalidPackageFileError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, file):
        self.file = file

    def __str__(self):
        return "The file: '" + self.file + "' is not valid as a package file."


class NotExistingBranchFileError(Exception):
    """
    - Raises an 'NotExistingBranchFileError' error if the instance of the 'argument_branch' variable is a string and the
      given directory does not exists.
    """
    __module__ = Exception.__module__

    def __init__(self, file):
        self.file = file

    def __str__(self):
        return "The branch file '" + str(self.file) + "' does not exist."


class NotExistingPackageFileError(Exception):
    """
    - Raises an 'NotExistingPackageFileError' error if there is value in the the 'argument_package' variable and is
      instance of string and the given directory does not exists.
    """
    __module__ = Exception.__module__

    def __init__(self, file):
        self.file = file

    def __str__(self):
        return "The package file '" + str(self.file) + "' does not exist."


class PositionNotAllowedError(Exception):
    """
    - If the value of position is equal to '0', then it raises a 'PositionNotAllowedError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, argument):
        self.argument = argument

    def __str__(self):
        return "The position '0' is not allowed to use in the '" + self.argument + "' argument."


class MaximumPaintSlotsError(Exception):
    """
    - If the length of the 'paint' list is bigger than '4', then it raises a 'MaximumPaintSlotsError' error.
    """
    __module__ = Exception.__module__

    def __str__(self):
        return "The maximum paint slots that can be used is '4'."


class MaximumSizeError(Exception):
    """
    - If the length of the 'size' argument is bigger than '20', then it raises a 'MaximumSizeError' error.
    """
    __module__ = Exception.__module__

    def __str__(self):
        return "The sizes that can be used is '0-20'."


class NotExistingPaintError(Exception):
    """
    - If the current value of the position in the 'paint' list is not equal to any of the values in the 'paint_id' list,
      then it raises a 'NotExistingPaintError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, paint):
        self.paint = paint

    def __str__(self):
        return "The paint '" + str(self.paint) + "' does not exists."
