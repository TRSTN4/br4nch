# The librarian class stores most of the lists and dictionary.
def librarian(action):
    # All global statements.
    global branches, branch_package, header_package, module_package, subject_package, object_package, paper

    # Checks if the action is equal to "construction". Construction creates all the lists and dictionaries.
    if action == "construction":
        # Dictionary to save all the branches.
        branches = {}

        # Package directories to save all paint keys and values.
        branch_package = {}
        header_package = {}
        module_package = {}
        subject_package = {}
        object_package = {}

        # List to save all the output of the branches.
        paper = []

    storage = [branches, branch_package, header_package, module_package, subject_package, object_package, paper]
    identity = ["branches", "branch_package", "header_package", "module_package", "subject_package", "object_package",
                "paper"]

    for number in range(len(storage)):
        if identity[number] == action:
            return storage[number]
