# Imports all files.
from br4nch.utility.inspector.paint import inspect_paint_clear
from br4nch.utility.inspector.paint import inspect_paint_base
from br4nch.utility.inspector.paint import inspect_paint_all_base
from br4nch.utility.librarian import librarian
from br4nch.utility.branching import branching


keys = []
queue = []


# Algorithm to build all the given headers.
def build_layer(branch, value=""):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    paper = librarian("paper")
    logs = librarian("logs")
    positions = librarian("positions")

    # Gets the header of the given branch.
    header = list(branches[branch])[0]

    # Checks if there is no content in value.
    if not value:
        # Value is equal to the value of branches > branch > header > value.
        value = branches[branch][header]

    num = 1
    saved_value = value.copy()

    if queue:
        for value in queue:
            value = value
            break
        queue.remove(value)

    for key, value in value.items():
        for layer, pos in positions[branch].items():
            if key == layer:
                print(pos)
                paper.append(key)

        if value:
            queue.append(value)
        if value:
            # print("in value:", key)
            # Adds the state of the building process to the logs dictionary.
            logs.update({key: "[+] Layer: '" + key + "' Successfully Build."})

            if num == len(saved_value):
                build_layer(branch)
                break

            if 1 < len(saved_value) != num:
                num = num + 1
                continue

            # Breaks the loop.
            break
        elif not value and num > 1:
            # print("in-out value", key)
            # Adds the state of the building process to the logs dictionary.
            logs.update({key: "[+] Layer: '" + key + "' Successfully Build."})

            if num == len(saved_value):
                build_layer(branch)
                break
        else:
            # print("out value", key)
            # Adds the state of the building process to the logs dictionary.
            logs.update({key: "[+] Layer: '" + key + "' Successfully Build."})
            break
