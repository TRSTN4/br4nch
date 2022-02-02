# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

class InstanceStringError(Exception):
    """
    - If the given argument value is not an instance of a string, then it raises an 'InstanceStringError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, argument, value):
        self.argument = argument
        self.value = value

    def __str__(self):
        return "The " + str(self.argument) + " argument: '" + str(self.value) + "' must be an instance of a 'str' and" \
                                                                                " not '" \
               + str(type(self.value).__name__) + "'."


class InstanceBooleanError(Exception):
    """
    - If the given argument value is not an instance of a boolean, then it raises an 'InstanceBooleanError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, argument, value):
        self.argument = argument
        self.value = value

    def __str__(self):
        return "The " + str(self.argument) + " argument: '" + str(self.value) + "' must be an instance of a 'bool' " \
                                                                               "and not '" \
               + str(type(self.value).__name__) + "'."


class InstanceIntegerError(Exception):
    """
    - If the given argument value is not an instance of a integer, then it raises an 'InstanceIntegerError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, argument, value):
        self.argument = argument
        self.value = value

    def __str__(self):
        return "The " + str(self.argument) + " argument: '" + str(self.value) + "' must be an instance of a 'int' and" \
                                                                                " not '" \
               + str(type(self.value).__name__) + "'."


class InstanceDictionaryError(Exception):
    """
    - If the given argument value is not an instance of a dictionary, then it raises an 'InstanceDictionaryError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, argument, value):
        self.argument = argument
        self.value = value

    def __str__(self):
        return "The " + str(self.argument) + " argument: '" + str(self.value) + "' must be an instance of a 'dict' " \
                                                                                "and not '" \
               + str(type(self.value).__name__) + "'."


class InvalidBranchNameError(Exception):
    """
    - If the branch value contains a character that is not a letter or number, then it raises an
      'InvalidBranchNameError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "The branch name: '" + self.value + "' is not valid. Only numbers and/or letters may be used to add a" \
                                                   "branch."


class InvalidPositionError(Exception):
    """
    - If the pos argument is not equal to a number and/or operator, then it raises an 'InvalidPositionError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, argument, position):
        self.argument = argument
        self.position = position

    def __str__(self):
        return "The position: '" + self.position + "' is not valid. Only numbers and operators may be used to add a " \
                                                   "position to the " + self.argument + " argument."


class InvalidSizeError(Exception):
    """
    - If the size value is smaller than '0' or bigger than '20', then it raises an 'InvalidSizeError' error.
    """
    __module__ = Exception.__module__

    def __str__(self):
        return "The sizes that can be used is '0-20'."


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


class NotExistingBranchError(Exception):
    """
    - If the branch is not in the 'branches' dictionary, it raises a 'NotExistingBranchError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, branch):
        self.branch = branch

    def __str__(self):
        return "The branch: '" + str(self.branch) + "' does not exists."


class NotExistingDirectoryError(Exception):
    """
    - If the given directory argument does not exist, it will throw a 'NotExistingDirectoryError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, directory):
        self.directory = directory

    def __str__(self):
        return "The directory: '" + str(self.directory) + "' does not exist."


class NotExistingBranchFileError(Exception):
    """
    - Raises an 'NotExistingBranchFileError' error if the instance of the 'argument_branch' variable is a string and the
      given directory does not exists.
    """
    __module__ = Exception.__module__

    def __init__(self, file):
        self.file = file

    def __str__(self):
        return "The branch file: '" + str(self.file) + "' does not exist."


class NotExistingPackageFileError(Exception):
    """
    - Raises an 'NotExistingPackageFileError' error if there is value in the the 'argument_package' variable and is
      instance of string and the given directory does not exists.
    """
    __module__ = Exception.__module__

    def __init__(self, file):
        self.file = file

    def __str__(self):
        return "The package file: '" + str(self.file) + "' does not exist."


class NotExistingPaintError(Exception):
    """
    - If the current value of the position in the 'paint' list is not equal to any of the values in the 'paint_id' list,
      then it raises a 'NotExistingPaintError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, paint):
        self.paint = paint

    def __str__(self):
        return "The paint: '" + str(self.paint) + "' does not exists."


class MaximumPaintSlotsError(Exception):
    """
    - If the length of the 'paint' list is bigger than '3', then it raises a 'MaximumPaintSlotsError' error.
    """
    __module__ = Exception.__module__

    def __str__(self):
        return "The maximum paint slots that can be used is '3'."


class DuplicateBranchError(Exception):
    """
    - If the branch value is already in the 'branches' dictionary, then it raises a 'DuplicateBranchError' error.
    """
    __module__ = Exception.__module__

    def __init__(self, branch):
        self.branch = branch

    def __str__(self):
        return "The branch: '" + str(self.branch) + "' already exists."


class RequiredSymbolChangeError(Exception):
    """
    - If there is no value in the 'line', 'split' and 'end' arguments, then it raises an 'RequiredSymbolChangeError'
      error.
    """
    __module__ = Exception.__module__

    def __str__(self):
        return "Change at least one of the given symbols: 'line', 'split' or 'end'."
