# Part of the br4nch package.

class MissingBranchError(Exception):
    __module__ = Exception.__module__

    def __str__(self):
        return "The branch argument is missing."


class MissingHeaderError(Exception):
    __module__ = Exception.__module__

    def __str__(self):
        return "The header argument is missing."


class StringInstanceError(Exception):
    __module__ = Exception.__module__

    def __init__(self, argument, parsed):
        self.argument = argument
        self.parsed = parsed

    def __str__(self):
        return "The " + str(self.argument) + " argument '" + str(self.parsed) + "' must be an instance of a "\
               + "'string' and not '" + str(type(self.parsed).__name__) + "'."


class BooleanInstanceError(Exception):
    __module__ = Exception.__module__

    def __init__(self, argument, parsed):
        self.argument = argument
        self.parsed = parsed

    def __str__(self):
        return "The " + str(self.argument) + " argument '" + str(self.parsed) + "' must be an instance of a "\
               + "'boolean' and not '" + str(type(self.parsed).__name__) + "'."


class DictionaryInstanceError(Exception):
    __module__ = Exception.__module__

    def __init__(self, argument, parsed):
        self.argument = argument
        self.parsed = parsed

    def __str__(self):
        return "The " + str(self.argument) + " argument '" + str(self.parsed) + "' must be an instance of a "\
               + "'dictionary' and not '" + str(type(self.parsed).__name__) + "'."


class MissingNameError(Exception):
    __module__ = Exception.__module__

    def __str__(self):
        return "The name argument is missing."


class MissingPaintError(Exception):
    __module__ = Exception.__module__

    def __str__(self):
        return "The paint argument is missing."


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
