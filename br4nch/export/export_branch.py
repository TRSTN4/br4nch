# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

import os

from br4nch.utility.utility_handler import InstanceBooleanError, InstanceStringError, NotExistingDirectoryError, \
    NotExistingBranchError
from br4nch.utility.utility_librarian import branches, uids, sizes, symbols, paint_branch, paint_header, paint_layer


def arguments(branch, directory, package=False):
    """
    - Gets the arguments and parses them to the 'export_branch' function.
    """
    export_branch(branch, directory, package)


def export_branch(argument_branch, argument_directory, argument_package):
    """
    Lists:
      - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.

    Errors:
      - If the package value is not an instance of a boolean, then it raises an 'InstanceBooleanError' error.
      - If the directory value is not an instance of a string, then it raises an 'InstanceStringError' error.

    Operators:
      - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
        list.

    Argument branch list loop:
      Errors:
        - If the branch value is not an instance of a string, then it raises an 'InstanceStringError' error.
        - If and the branch value is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

      Branches list loop:
        - If the branch is in the 'branches' dictionary, then it is checked whether the variable 'argument_package' is
          equal to true, if the variable is equal to true, then a dictionary is created with the values of all necessary
          dictionaries.

        If the given directory exists:
          - Creates the custom br4nch directory if it does not exist in the given directory argument.
          - Appends the value of the branch in the 'branches' directory to a custom file with the id line for a
            exported branch file in the custom br4nch folder.
          - If there is a value in the 'argument_package' argument, then adds the values of all required directories
            to a custom file with the id line for a exported package file in the custom br4nch folder.

        - If the given directory argument does not exist, it will throw a 'NotExistingDirectoryError' error.
    """
    if not isinstance(argument_branch, list):
        argument_branch = [argument_branch]

    if not isinstance(argument_package, bool):
        raise InstanceBooleanError("package", argument_package)

    if not isinstance(argument_directory, str):
        raise InstanceStringError("directory", argument_directory)

    if "*" in argument_branch:
        argument_branch.clear()
        for branches_branch in list(branches):
            argument_branch.append(branches_branch)

    for branch in argument_branch:
        error = 0

        if not isinstance(branch, str):
            raise InstanceStringError("branch", branch)

        for branches_branch in list(branches):
            if branch.lower() == branches_branch.lower():
                error = error + 1

                export_package = {}

                if argument_package:
                    export_package = {branches_branch: [uids[branches_branch], sizes[branches_branch],
                                                        symbols[branches_branch], paint_branch[branches_branch],
                                                        paint_header[branches_branch], paint_layer[branches_branch]]}

                if os.path.isdir(argument_directory):
                    if not os.path.isdir(argument_directory + "/br4nch-" + branches_branch):
                        os.mkdir(argument_directory + "/br4nch-" + branches_branch)

                    with open(argument_directory + "/br4nch-" + branches_branch + "/branch-" + branches_branch, 'w',
                              encoding='utf-8') as file:
                        file.write("id=:br4nch-branch:\n")
                        file.write(str({branches_branch: branches[branches_branch]}))

                    if argument_package:
                        with open(argument_directory + "/br4nch-" + branches_branch + "/package-" + branches_branch,
                                  'w', encoding='utf-8') as file:
                            file.write("id=:br4nch-package:\n")
                            file.write(str(export_package))
                else:
                    raise NotExistingDirectoryError(argument_directory)

        if error == 0:
            if branch:
                raise NotExistingBranchError(branch)
