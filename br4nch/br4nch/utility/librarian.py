# Part of the br4nch package.

# The librarian class stores most of the lists and dictionary.
def librarian(action):
    # All global statements.
    global branches, paint_package_branch, paint_package_header, paint_package_layer, paper, branch_symbols, error

    # Checks if the action is equal to "construction". Construction creates all the lists and dictionaries.
    if action == "construction":
        # Dictionary to save all the branches.
        branches = {}

        # Paint directories to save all paint keys and values.
        paint_package_branch = {}
        paint_package_header = {}
        paint_package_layer = {}

        # Dictionaries to save selected output.
        branch_symbols = {}
        paper = {}
        error = {}

    # Checks if the action list has any value.
    if action:
        # Saves all the actions in a list.
        storage = [branches, paint_package_branch, paint_package_header, paint_package_layer, paper, branch_symbols,
                   error]

        # Saves all the action ids in a list.
        identity = ["branches", "paint_package_branch", "paint_package_header", "paint_package_layer", "paper",
                    "branch_symbols", "error"]

        # Loops through total length of the storage list.
        for number in range(len(storage)):
            # Checks if the parsed action is equal to a id in the identity list.
            if identity[number] == action:
                # Returns the requested action.
                return storage[number]
