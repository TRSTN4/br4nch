# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

class UtilityHandler:
    class InstanceStringError(Exception):
        __module__ = Exception.__module__

        def __init__(self, argument, value):
            self.argument = argument
            self.value = value

        def __str__(self):
            return "The " + str(self.argument) + " argument: '" + str(self.value) \
                   + "' must be an instance of a 'str' and not '" + str(type(self.value).__name__) + "'."

    class InstanceBooleanError(Exception):
        __module__ = Exception.__module__

        def __init__(self, argument, value):
            self.argument = argument
            self.value = value

        def __str__(self):
            return "The " + str(self.argument) + " argument: '" + str(self.value) \
                   + "' must be an instance of a 'bool' and not '" + str(type(self.value).__name__) + "'."

    class InstanceIntegerError(Exception):
        __module__ = Exception.__module__

        def __init__(self, argument, value):
            self.argument = argument
            self.value = value

        def __str__(self):
            return "The " + str(self.argument) + " argument: '" + str(self.value) \
                   + "' must be an instance of a 'int' and not '" + str(type(self.value).__name__) + "'."

    class InvalidTreeNameError(Exception):
        __module__ = Exception.__module__

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return "The tree name: '" + self.value \
                   + "' is not valid. Only numbers and/or letters may be used to add a tree."

    class InvalidPositionError(Exception):
        __module__ = Exception.__module__

        def __init__(self, argument, value):
            self.argument = argument
            self.value = value

        def __str__(self):
            return "The " + self.argument + ": '" + self.value \
                   + "' is not valid. Only valid positions, operators and existing nodes can be used to decide the " \
                     "position for the " + self.argument + " argument."

    class InvalidSizeError(Exception):
        __module__ = Exception.__module__

        def __str__(self):
            return "The sizes that can be used is '0-20'."

    class InvalidTreeFileError(Exception):
        __module__ = Exception.__module__

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return "The file: '" + self.value + "' is not valid as a tree file."

    class InvalidAttributesFileError(Exception):
        __module__ = Exception.__module__

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return "The file: '" + self.value + "' is not valid as a attributes file."

    class NotExistingTreeError(Exception):
        __module__ = Exception.__module__

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return "The tree: '" + str(self.value) + "' does not exists."

    class NotExistingDirectoryError(Exception):
        __module__ = Exception.__module__

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return "The directory: '" + str(self.value) + "' does not exist."

    class NotExistingTreeFileError(Exception):
        __module__ = Exception.__module__

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return "The tree file: '" + str(self.value) + "' does not exist."

    class NotExistingAttributesFileError(Exception):
        __module__ = Exception.__module__

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return "The attributes file: '" + str(self.value) + "' does not exist."

    class NotExistingJsonFileError(Exception):
        __module__ = Exception.__module__

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return "The json file: '" + str(self.value) + "' does not exist."

    class NotSizeableError(Exception):
        __module__ = Exception.__module__

        def __str__(self):
            return "You can only use the 'size' function with the default symbols."

    class DuplicateTreeError(Exception):
        __module__ = Exception.__module__

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return "The tree: '" + str(self.value) + "' already exists."

    class RequiredSymbolChangeError(Exception):
        __module__ = Exception.__module__

        def __str__(self):
            return "Change at least one of the given symbols: 'line', 'split' or 'end'."
