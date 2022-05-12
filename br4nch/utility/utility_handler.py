# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

class UtilityHandler:
    class InstanceStringError(Exception):
        """
        This error occurs when the given value in the specified argument is not an instance of a string.
        """
        __module__ = Exception.__module__

        def __init__(self, argument, value):
            self.argument = argument
            self.value = value

        def __str__(self):
            return "The " + str(self.argument) + " argument: '" + str(self.value) \
                   + "' must be an instance of a 'str' and not '" + str(type(self.value).__name__) + "'."

    class InstanceBooleanError(Exception):
        """
        This error occurs when the given value in the specified argument is not an instance of an boolean.
        """
        __module__ = Exception.__module__

        def __init__(self, argument, value):
            self.argument = argument
            self.value = value

        def __str__(self):
            return "The " + str(self.argument) + " argument: '" + str(self.value) \
                   + "' must be an instance of a 'bool' and not '" + str(type(self.value).__name__) + "'."

    class InstanceIntegerError(Exception):
        """
        This error occurs when the given value in the specified argument is not an instance of an integer.
        """
        __module__ = Exception.__module__

        def __init__(self, argument, value):
            self.argument = argument
            self.value = value

        def __str__(self):
            return "The " + str(self.argument) + " argument: '" + str(self.value) \
                   + "' must be an instance of a 'int' and not '" + str(type(self.value).__name__) + "'."

    class InvalidTreeNameError(Exception):
        """
        This error occurs when the tree name uses characters other than letters and/or numbers.
        """
        __module__ = Exception.__module__

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return "The tree name: '" + self.value \
                   + "' is not valid. Only numbers and/or letters may be used to add a tree."

    class InvalidPositionError(Exception):
        """
        This error occurs when the given position contains a character other than valid positions, operators and
        existing nodes.
        """
        __module__ = Exception.__module__

        def __init__(self, argument, value):
            self.argument = argument
            self.value = value

        def __str__(self):
            return "The " + self.argument + ": '" + self.value \
                   + "' is not valid. Only valid positions, operators and existing nodes can be used to decide the " \
                     "position for the " + self.argument + " argument."

    class InvalidSizeError(Exception):
        """
        This error occurs when the given size is less than zero or greater than 20.
        """
        __module__ = Exception.__module__

        def __str__(self):
            return "The sizes that can be used is '0-20'."

    class InvalidTreeFileError(Exception):
        """
        This error occurs when the specified tree file is invalid.
        """
        __module__ = Exception.__module__

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return "The file: '" + self.value + "' is not valid as a tree file."

    class InvalidAttributesFileError(Exception):
        """
        This error occurs when the specified attributes file is invalid.
        """
        __module__ = Exception.__module__

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return "The file: '" + self.value + "' is not valid as a attributes file."

    class NotExistingTreeError(Exception):
        """
        This error occurs when the specified tree does not exist.
        """
        __module__ = Exception.__module__

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return "The tree: '" + str(self.value) + "' does not exists."

    class NotExistingDirectoryError(Exception):
        """
        This error occurs when the given directory does not exist.
        """
        __module__ = Exception.__module__

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return "The directory: '" + str(self.value) + "' does not exist."

    class NotExistingTreeFileError(Exception):
        """
        This error occurs when the specified tree file location does not exist.
        """
        __module__ = Exception.__module__

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return "The tree file: '" + str(self.value) + "' does not exist."

    class NotExistingAttributesFileError(Exception):
        """
        This error occurs when the specified attributes file location does not exist.
        """
        __module__ = Exception.__module__

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return "The attributes file: '" + str(self.value) + "' does not exist."

    class NotExistingJsonFileError(Exception):
        """
        This error occurs when the specified json file location does not exist.
        """
        __module__ = Exception.__module__

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return "The json file: '" + str(self.value) + "' does not exist."

    class NotSizeableError(Exception):
        """
        This error occurs when you use the function with modified symbols.
        """
        __module__ = Exception.__module__

        def __str__(self):
            return "You can only use the 'size' function with the default symbols."

    class NotChangeableError(Exception):
        """
        This error occurs when you use the function with modified size.
        """
        __module__ = Exception.__module__

        def __str__(self):
            return "You can only use the 'symbol' function with the default size."

    class DuplicateTreeError(Exception):
        """
        This error occurs when the specified tree name already exists.
        """
        __module__ = Exception.__module__

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return "The tree: '" + str(self.value) + "' already exists."

    class RequiredSymbolChangeError(Exception):
        """
        This error occurs when no symbols are changed.
        """
        __module__ = Exception.__module__

        def __str__(self):
            return "Change at least one of the given symbols: 'line', 'split' or 'end'."
