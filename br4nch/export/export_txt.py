# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

import os

from br4nch.utility.utility_handler import InstanceStringError, NotExistingDirectoryError, NotExistingBranchError
from br4nch.utility.utility_librarian import branches, output
from br4nch.utility.utility_builder import Builder


def arguments(branch, directory):
    """
    - Gets the arguments and parses them to the 'export_text' function.
    """
    export_text(branch, directory)


def export_text(argument_branch, argument_directory):
    """
    Lists:
      - If the given branch argument is not an instance of a list, then the branch argument will be set as a list.

    Errors:
      - If the directory value is not an instance of a string, then it raises an 'InstanceStringError' error.

    Operators:
      - If there a '*' in the 'argument_branch' list, Then it appends all existing branches to the 'argument_branch'
        list.

    Argument branch list loop:
      Errors:
        - If the branch value is not an instance of a string, then it raises an 'InstanceStringError' error.
        - If and the branch value is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

      Branches list loop:
        Errors:
          - If the given directory argument does not exist, it will throw a 'NotExistingDirectoryError' error.

        If the given directory exists:
          - Creates a new file with a custom name of the value of branch
          - Calls the 'Builder' class to create the branch's 'output' variable.
          - Loops through the output of the branch and appends each element in the last to the file with a new line.
          - Clears the output list from the value of branch.
    """

    if not isinstance(argument_branch, list):
        argument_branch = [argument_branch]

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

                if os.path.isdir(argument_directory):
                    with open(argument_directory + "/br4nch-" + branches_branch + ".txt", 'w', encoding='utf-8')\
                            as file:
                        Builder(branches_branch, False)
                        for line in output[branches_branch]:
                            file.write(line + "\n")
                        output[branches_branch].clear()
                else:
                    raise NotExistingDirectoryError(argument_directory)

        if error == 0:
            if branch:
                raise NotExistingBranchError(branch)
