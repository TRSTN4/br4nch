# Adds a new module for the branch.
def module(branch, header_name, module_name):
    # Adds the module > header > name inside the branch dictionary.
    branches[branch][header_name].update({module_name: {}})
