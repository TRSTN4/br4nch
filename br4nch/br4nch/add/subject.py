# Adds a new subject for the branch.
def subject(branch, header_name, module_name, subject_name):
    # Adds the subject > module > header > name inside the branch dictionary.
    branches[branch][header_name][module_name].update({subject_name: {}})
