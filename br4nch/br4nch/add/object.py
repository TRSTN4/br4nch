# Adds a new object for the branch.
def object(branch, header_name, module_name, subject_name, object_name):
    # Adds the object > subject > module > header > name inside the branch dictionary.
    branches[branch][header_name][module_name][subject_name].update({object_name: {}})
