# Part of the br4nch package.

# The librarian class stores most of the lists and dictionary.
def librarian(action):
    # All global statements.
    global branches, branch_package, header_package, layer_package, paper, logs

    # Checks if the action is equal to "construction". Construction creates all the lists and dictionaries.
    if action == "construction":
        # Dictionary to save all the branches.
        branches = {}

        # Package directories to save all paint keys and values.
        branch_package = {}
        header_package = {}
        layer_package = {}

        # List to save all the output of the branches.
        paper = []

        # Saves all the logs of the actions.
        logs = {}

    # Checks if the action list has any value.
    if action:
        # Saves all the actions in a list.
        storage = [branches, branch_package, header_package, layer_package, paper, logs]

        # Saves all the action ids in a list.
        identity = ["branches", "branch_package", "header_package", "layer_package", "paper", "logs"]

        # Loops through total length of the storage list.
        for number in range(len(storage)):
            # Checks if the parsed action is equal to a id in the identity list.
            if identity[number] == action:
                # Returns the requested action.
                return storage[number]
