# The librarian class stores most of the lists and dictionary.
def librarian(action):
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
