# Imports all files.
from br4nch.utility.inspector.paint import inspect_paint_clear
from br4nch.utility.inspector.paint import inspect_paint_base
from br4nch.utility.inspector.paint import inspect_paint_all_base
from br4nch.utility.librarian import librarian
from br4nch.utility.branching import branching


queue = []


# Algorithm to build all the given headers.
def build_layer(branch, value="", pos=0, neg=0):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    paper = librarian("paper")
    logs = librarian("logs")

    # Gets the header of the given branch.
    header = list(branches[branch])[0]

    space = "\t" * pos
    newline = "\n"

    # Checks if there is no content in value.
    if not value:
        # Value is equal to the value of branches > branch > header > value.
        value = branches[branch][header]

    saved_layer = value.copy()

    if value == branches[branch][header]:
        extend = ""
    else:
        pos_neg = pos - neg
        extend = "┃\t" * pos_neg + "\t" * neg

    for key, value in value.items():
        if value:
            queue.append(value)

            if value and key == list(reversed(list(saved_layer)))[0]:
                paper.append(extend + "┃" + newline + extend + "┗━━ " + key)
                neg = 1
            else:
                paper.append(extend + "┃" + newline + extend + "┣━━ " + key)
                neg = 0

            # Adds the state of the building process to the logs dictionary.
            logs.update({key: "[+] Layer: '" + key + "' Successfully Build."})

            build_layer(branch, value, pos + 1, neg)
        else:
            if not value and key != list(reversed(list(saved_layer)))[0]:
                paper.append(extend + "┃" + newline + extend + "┣━━ " + key)
            else:
                paper.append(extend + "┃" + newline + extend + "┗━━ " + key)

            # Adds the state of the building process to the logs dictionary.
            logs.update({key: "[+] Layer: '" + key + "' Successfully Build."})
