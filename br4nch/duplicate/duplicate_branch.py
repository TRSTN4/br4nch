# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

from br4nch.utility.utility_handler import InstanceStringError, InstanceBooleanError, InvalidBranchNameError, \
    DuplicateBranchError, NotExistingBranchError
from br4nch.utility.utility_librarian import branches, output, uids, sizes, symbols, paint_branch, paint_header, \
    paint_layer


def arguments(branch, name, package=False):
    """
    - Gets the arguments and parses them to the 'duplicate_branch' function.
    """
    duplicate_branch(branch, name, package)


def duplicate_branch(argument_branch, argument_name, argument_package):
    """
    Errors:
      - If the branch value is not an instance of a string, then it raises an 'InstanceStringError' error.
      - If the name value is not an instance of a string, then it raises an 'InstanceStringError' error.
      - If the package value is not an instance of a boolean, then it raises an 'InstanceBooleanError' error.
      - If the name value contains a character that is not a letter or number, then it raises an
        'InvalidBranchError' error.

    Branches list loop:
      Errors:
        - If the branch is already in the 'branches' dictionary, then it raises a 'DuplicateBranchError' error.

    Branches list loop:
      Errors:
        - If the branch value is not an instance of a string, then it raises an 'InstanceStringError' error.
        - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

    - If the value of the 'argument_package' variable is true, then update the values of all required dictionaries with
      the values of the given package argument.
    - If the value of the 'argument_package' variable is false, then update the values of all required dictionaries with
      the default values for a new branch.
    """
    if not isinstance(argument_branch, str):
        raise InstanceStringError("branch", argument_branch)

    if not isinstance(argument_name, str):
        raise InstanceStringError("name", argument_name)

    if not isinstance(argument_package, bool):
        raise InstanceBooleanError("package", argument_package)

    if not argument_name.isalnum():
        raise InvalidBranchNameError(argument_name)

    for branches_branch in list(branches):
        if argument_name.lower() == branches_branch.lower():
            raise DuplicateBranchError(argument_name)

    error = 0
    for branches_branch in list(branches):
        if argument_branch.lower() == branches_branch.lower():
            error = error + 1

            branches.update({argument_name: branches[branches_branch]})
            output.update({argument_name: []})

            if argument_package:
                uids.update({argument_name: uids[branches_branch]})
                sizes.update({argument_name: sizes[branches_branch]})
                symbols.update({argument_name: symbols[branches_branch]})
                paint_branch.update({argument_name: paint_branch[branches_branch]})
                paint_header.update({argument_name: paint_header[branches_branch]})
                paint_layer.update({argument_name: paint_layer[branches_branch]})
            else:
                uids.update({argument_name: []})
                sizes.update({argument_name: 0})
                symbols.update({argument_name: {"line": "┃", "split": "┣━", "end": "┗━"}})
                paint_branch.update({argument_name: []})
                paint_header.update({argument_name: []})
                paint_layer.update({argument_name: {}})

    if error == 0:
        if argument_branch:
            raise NotExistingBranchError(argument_branch)
