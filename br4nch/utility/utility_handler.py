# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

class InstanceStringError(Exception):
    __module__ = Exception.__module__

    def __init__(self, argument, value):
        self.argument = argument
        self.value = value

    def __str__(self):
        return "The " + str(self.argument) + " argument: '" + str(self.value) + "' must be an instance of a 'str' and" \
                                                                                " not '" \
               + str(type(self.value).__name__) + "'."


class InstanceBooleanError(Exception):
    __module__ = Exception.__module__

    def __init__(self, argument, value):
        self.argument = argument
        self.value = value

    def __str__(self):
        return "The " + str(self.argument) + " argument: '" + str(self.value) + "' must be an instance of a 'bool' " \
                                                                               "and not '" \
               + str(type(self.value).__name__) + "'."


class InstanceIntegerError(Exception):
    __module__ = Exception.__module__

    def __init__(self, argument, value):
        self.argument = argument
        self.value = value

    def __str__(self):
        return "The " + str(self.argument) + " argument: '" + str(self.value) + "' must be an instance of a 'int' and" \
                                                                                " not '" \
               + str(type(self.value).__name__) + "'."


class InvalidTreeNameError(Exception):
    __module__ = Exception.__module__

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "The tree name: '" + self.value + "' is not valid. Only numbers and/or letters may be used to add a" \
                                                   "tree."


class InvalidParentError(Exception):
    __module__ = Exception.__module__

    def __init__(self, argument, position):
        self.argument = argument
        self.position = position

    def __str__(self):
        return "The parent: '" + self.position + "' is not valid. Only numbers and operators may be used to add a " \
                                                   "parent to the " + self.argument + " argument."


class InvalidSizeError(Exception):
    __module__ = Exception.__module__

    def __str__(self):
        return "The sizes that can be used is '0-20'."


class InvalidTreeFileError(Exception):
    __module__ = Exception.__module__

    def __init__(self, file):
        self.file = file

    def __str__(self):
        return "The file: '" + self.file + "' is not valid as a tree file."


class InvalidAttributesFileError(Exception):
    __module__ = Exception.__module__

    def __init__(self, file):
        self.file = file

    def __str__(self):
        return "The file: '" + self.file + "' is not valid as a attributes file."


class NotExistingTreeError(Exception):
    __module__ = Exception.__module__

    def __init__(self, tree):
        self.tree = tree

    def __str__(self):
        return "The tree: '" + str(self.tree) + "' does not exists."


class NotExistingDirectoryError(Exception):
    __module__ = Exception.__module__

    def __init__(self, directory):
        self.directory = directory

    def __str__(self):
        return "The directory: '" + str(self.directory) + "' does not exist."


class NotExistingTreeFileError(Exception):
    __module__ = Exception.__module__

    def __init__(self, file):
        self.file = file

    def __str__(self):
        return "The tree file: '" + str(self.file) + "' does not exist."


class NotExistingAttributesFileError(Exception):
    __module__ = Exception.__module__

    def __init__(self, file):
        self.file = file

    def __str__(self):
        return "The attributes file: '" + str(self.file) + "' does not exist."


class NotExistingPaintError(Exception):
    __module__ = Exception.__module__

    def __init__(self, paint):
        self.paint = paint

    def __str__(self):
        return "The paint: '" + str(self.paint) + "' does not exists."


class MaximumPaintSlotsError(Exception):
    __module__ = Exception.__module__

    def __str__(self):
        return "The maximum paint slots that can be used is '3'."


class DuplicateTreeError(Exception):
    __module__ = Exception.__module__

    def __init__(self, tree):
        self.tree = tree

    def __str__(self):
        return "The tree: '" + str(self.tree) + "' already exists."


class RequiredSymbolChangeError(Exception):
    __module__ = Exception.__module__

    def __str__(self):
        return "Change at least one of the given symbols: 'line', 'split' or 'end'."
