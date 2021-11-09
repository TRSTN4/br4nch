# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

class StringInstanceError(Exception):
    __module__ = Exception.__module__

    def __init__(self, argument, parsed):
        self.argument = argument
        self.parsed = parsed

    def __str__(self):
        return "The " + str(self.argument) + " argument '" + str(self.parsed) + "' must be an instance of a "\
               + "'string' and not '" + str(type(self.parsed).__name__) + "'."


class IntegerInstanceError(Exception):
    __module__ = Exception.__module__

    def __init__(self, argument, parsed):
        self.argument = argument
        self.parsed = parsed

    def __str__(self):
        return "The " + str(self.argument) + " argument '" + str(self.parsed) + "' must be an instance of a "\
               + "'integer' and not '" + str(type(self.parsed).__name__) + "'."


class DictionaryInstanceError(Exception):
    __module__ = Exception.__module__

    def __init__(self, argument, parsed):
        self.argument = argument
        self.parsed = parsed

    def __str__(self):
        return "The " + str(self.argument) + " argument '" + str(self.parsed) + "' must be an instance of a "\
               + "'dictionary' and not '" + str(type(self.parsed).__name__) + "'."


class BooleanInstanceError(Exception):
    __module__ = Exception.__module__

    def __init__(self, argument, parsed):
        self.argument = argument
        self.parsed = parsed

    def __str__(self):
        return "The " + str(self.argument) + " argument '" + str(self.parsed) + "' must be an instance of a "\
               + "'boolean' and not '" + str(type(self.parsed).__name__) + "'."


class DuplicateBranchError(Exception):
    __module__ = Exception.__module__

    def __init__(self, branch):
        self.branch = branch

    def __str__(self):
        return "The branch '" + str(self.branch) + "' already exists."


class InvalidBranchError(Exception):
    __module__ = Exception.__module__

    def __str__(self):
        return "Only numbers and/or letters may be used to add a branch."


class NotExistingBranchError(Exception):
    __module__ = Exception.__module__

    def __init__(self, branch):
        self.branch = branch

    def __str__(self):
        return "The branch '" + str(self.branch) + "' does not exists."


class NotExistingPaintError(Exception):
    __module__ = Exception.__module__

    def __init__(self, paint):
        self.paint = paint

    def __str__(self):
        return "The paint '" + str(self.paint) + "' does not exists."


class InvalidSizeError(Exception):
    __module__ = Exception.__module__

    def __init__(self, size):
        self.size = size

    def __str__(self):
        return "The size argument '" + str(self.size) + "' is not a integer."


class InvalidDeleteError(Exception):
    __module__ = Exception.__module__

    def __init__(self, delete):
        self.delete = delete

    def __str__(self):
        return "The delete argument '" + str(self.delete) + "' is not equal to true or false."


class InvalidDirectoryError(Exception):
    __module__ = Exception.__module__

    def __init__(self, directory):
        self.directory = directory

    def __str__(self):
        return "The directory '" + str(self.directory) + "' does not exist."


class InvalidBranchFileError(Exception):
    __module__ = Exception.__module__

    def __init__(self, file):
        self.file = file

    def __str__(self):
        return "The branch file '" + str(self.file) + "' does not exist."


class InvalidPackageFileError(Exception):
    __module__ = Exception.__module__

    def __init__(self, file):
        self.file = file

    def __str__(self):
        return "The package file '" + str(self.file) + "' does not exist."
