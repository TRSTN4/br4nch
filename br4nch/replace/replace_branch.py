# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

from br4nch.utility.utility_handler import InstanceStringError, InvalidBranchNameError, DuplicateBranchError, \
    NotExistingBranchError
from br4nch.utility.utility_librarian import branches, output, uids, sizes, symbols, paint_branch, paint_header, \
    paint_layer


def arguments(branch, replace):
    """
    - Gets the arguments and parses them to the 'replace_branch' function.
    """
    replace_branch(branch, replace)


def replace_branch(argument_branch, argument_replace):
    """
    Errors:
      - If the branch value is not an instance of a string, then it raises an 'InstanceStringError' error.
      - If the replace value is not an instance of a string, then it raises an 'InstanceStringError' error.
      - If the replace value contains a character that is not a letter or number, then it raises an
        'InvalidBranchNameError' error.

    Branches list loop:
      Errors:
        - If the branch is already in the 'branches' dictionary, then it raises a 'DuplicateBranchError' error.

    Branches list loop:
      Errors:
        - If the branch value is not an instance of a string, then it raises an 'InstanceStringError' error.
        - If the branch is not in the 'branches' dictionary, it will throw a 'NotExistingBranchError' error.

      - The index of the given branch in the 'branches' list is stored in the variable 'index'.
      - Deletes the given branch and creates a new one with the given replace and the copied values from the given branch.
      - To keep the order the same, a loop will be made that loops through the branches with the given slice values,
        removing all values and adding them again.
    """
    if not isinstance(argument_branch, str):
        raise InstanceStringError("branch", argument_branch)

    if not isinstance(argument_replace, str):
        raise InstanceStringError("replace", argument_replace)

    if not argument_replace.isalnum():
        raise InvalidBranchNameError(argument_replace)

    for branches_branch in list(branches):
        if argument_replace.lower() == branches_branch.lower():
            raise DuplicateBranchError(argument_replace)

    error = 0
    for branches_branch in list(branches):
        if argument_branch.lower() == branches_branch.lower():
            error = error + 1

            index = list(branches).index(branches_branch)

            branches[argument_replace] = branches.pop(branches_branch)
            output[argument_replace] = output.pop(branches_branch)
            sizes[argument_replace] = sizes.pop(branches_branch)
            symbols[argument_replace] = symbols.pop(branches_branch)
            paint_branch[argument_replace] = paint_branch.pop(branches_branch)
            paint_header[argument_replace] = paint_header.pop(branches_branch)
            paint_layer[argument_replace] = paint_layer.pop(branches_branch)
            uids[argument_replace] = uids.pop(branches_branch)

            for position in list(branches)[index:-1]:
                branches[position] = branches.pop(position)
                output[position] = output.pop(position)
                sizes[position] = sizes.pop(position)
                symbols[position] = symbols.pop(position)
                paint_branch[position] = paint_branch.pop(position)
                paint_header[position] = paint_header.pop(position)
                paint_layer[position] = paint_layer.pop(position)
                uids[position] = uids.pop(position)

    if error == 0:
        if argument_branch:
            raise NotExistingBranchError(argument_branch)
