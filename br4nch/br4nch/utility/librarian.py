# Part of the br4nch package.

# The librarian class stores most of the lists and dictionary.
def librarian(action):
    # All global statements.
    global branches, paint_package_branch, paint_package_header, paint_package_layer, output, symbols, error, uids,\
        positions, size

    # Checks if the action is equal to "construction", the construction creates all the lists and dictionaries.
    if action == "construction":
        # Dictionary to save all the branches.
        branches = {}

        # Paint package directories to save all paint.
        paint_package_branch = {}
        paint_package_header = {}
        paint_package_layer = {}

        # Dict to save the founded positions.
        positions = {}

        # Stores the parsed symbols for a branch.
        symbols = {}

        # Saves the errors of the branches.
        output = {}

        # Saves the errors of the branches.
        error = {}

        # Stores the given size of the branch.
        size = {}

        # Dict to save UIDS.
        uids = {}

    # Checks if the action list has content.
    if action:
        # Saves all the lists and dictionaries in storage list.
        storage = [branches, paint_package_branch, paint_package_header, paint_package_layer, output, symbols, error,
                   uids, positions, size]

        # Saves all the lists and dictionaries in identity list.
        identity = ["branches", "paint_package_branch", "paint_package_header", "paint_package_layer", "output",
                    "symbols", "error", "uids", "positions", "size"]

        # Loops through total length of the storage list.
        for number in range(len(storage)):
            # Checks if the parsed action is equal to the action identity given by the length number.
            if identity[number] == action:
                # Returns the requested list or dictionary.
                return storage[number]
