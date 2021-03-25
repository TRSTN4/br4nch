# Adds a new header for the branch.
def header(branch, header_name):
    # Adds header > name inside the branch dictionary.
    branches[branch].update({header_name: {}})
