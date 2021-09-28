# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.painter import painter
from br4nch.utility.positioner import build_pos
from br4nch.utility.generator import get_uid


def executor_calculate(action, package, value=""):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    paint_package_layer = librarian("paint_package_layer")

    branch = package[0]
    pos = package[1]

    # Checks if there is no content in value.
    if not value:
        # Value is equal to the value of all nested layers.
        value = branches[branch][list(branches[branch])[0]]

    if action == "add_layer":
        if pos[0] == "0" or not pos[0]:
            # Loops through all layers in layer list.
            for lay in package[2]:
                # Updates the current value and adds the layer with uid and new dictionary as value.
                branches[branch][list(branches[branch])[0]].update({lay + get_uid(branch): {}})
            return

    # Creates the num variable.
    count = 0

    prev_value = value

    # Gets the layer/key and value of the current value variable.
    for layer, value in value.items():
        # Num is equal to current value of num plus one.
        count = count + 1

        # Checks if the current value of num is equal to the integer of the first entry in the pos list.
        if count == int(pos[0]):
            # Checks if length of entries in pos is smaller then 2.
            if len(pos) < 2:
                if action == "add_layer":
                    # Loops through all layers in layer list.
                    for lay in package[2]:
                        # Updates the current value and adds the layer with uid and new dictionary as value.
                        value.update({lay + get_uid(branch): {}})
                if action == "delete_layer" or action == "replace_layer":
                    num = 0
                    # Loops through all layers in layer list.
                    for lay in list(prev_value):
                        num = num + 1
                        if num == int(pos[0]):
                            package[2].update({lay: prev_value})
                    return package[2]
                if action == "delete_color_layer":
                    paint_package_layer[branch].pop(package[2])
                if action == "replace_color_layer":
                    paint_package_layer[branch].update({package[2]: painter(package[3], branch)})
                if action == "set_color_layer":
                    # Adds the current value of pos and the requested paint to the current branch paint package.
                    paint_package_layer[branch].update({package[2]: painter(package[3], branch, layer)})
            # If length of entries in pos is not smaller then 2.
            else:
                # Removes the first entry of pos list.
                pos.pop(0)
                # Calls the calculate function.
                executor_calculate(action, package, value)
                # Returns nothing and stops the loop.
                return


def executor(action, package):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    paint_package_branch = librarian("paint_package_branch")
    paint_package_header = librarian("paint_package_header")
    paint_package_layer = librarian("paint_package_layer")
    symbols = librarian("symbols")
    output = librarian("output")
    error = librarian("error")
    size = librarian("size")
    uids = librarian("uids")

    branch = package[0]

    if action == "replace_branch":
        for y in list(branches):
            if branch.lower() == y.lower():
                branch = y

                branches[package[1]] = branches.pop(y)
                output[package[1]] = output.pop(y)
                error[package[1]] = error.pop(y)
                size[package[1]] = size.pop(y)
                symbols[package[1]] = symbols.pop(y)
                paint_package_branch[package[1]] = paint_package_branch.pop(y)
                paint_package_header[package[1]] = paint_package_header.pop(y)
                paint_package_layer[package[1]] = paint_package_layer.pop(y)
                uids[package[1]] = uids.pop(y)

                for x in list(branches)[:-1]:
                    branches[x] = branches.pop(x)
                    output[x] = output.pop(x)
                    error[x] = error.pop(x)
                    size[x] = size.pop(x)
                    symbols[x] = symbols.pop(x)
                    paint_package_branch[x] = paint_package_branch.pop(x)
                    paint_package_header[x] = paint_package_header.pop(x)
                    paint_package_layer[x] = paint_package_layer.pop(x)
                    uids[x] = uids.pop(x)

                output[package[1]].clear()
                error[package[1]].clear()
    else:
        # Checks if branch is not a instance of list.
        if not isinstance(branch, list):
            # Branch will be equal to a list that contains the value of branch.
            branch = [branch]

        if action != "add_branch":
            if not branch[0]:
                for value in list(branches):
                    branch.append(value)
                branch.pop(0)

        # Loops through all branches in the branch list.
        for branch in branch:
            if action == "add_branch":
                # Adds the branch values inside the dictionaries.
                branches.update({branch: {}})

                # Log lists to save output with branch as key and list as value.
                output.update({branch: []})
                error.update({branch: []})

                size.update({branch: 1})

                uids.update({branch: []})

                # Sets the symbols to default symbols.
                symbols.update({branch: {"line": "┃", "split": "┣━━", "end": "┗━━"}})

                # Checks if the current branch value is inside the paint package.
                if not paint_package_branch.get(branch):
                    # Adds the current branch value as key and a new dictionary as value to the paint package.
                    paint_package_branch.update({branch: {}})
            else:
                for y in list(branches):
                    if branch.lower() == y.lower():
                        branch = y

                        # Branch

                        if action == "delete_branch":
                            del branches[branch]
                            del paint_package_branch[branch]
                            del paint_package_header[branch]
                            del paint_package_layer[branch]
                            del symbols[branch]
                            del output[branch]
                            del error[branch]
                            del size[branch]
                            del uids[branch]

                        if action == "set_color_branch" or action == "replace_color_branch":
                            # Adds the branch as key and the paint as value to the paint package.
                            paint_package_branch.update({branch: painter(package[1], branch)})

                        if action == "delete_color_branch":
                            paint_package_branch.update({branch: {}})

                        # Header

                        if action == "add_header":
                            # Adds header inside the selected branch dictionary.
                            branches[branch].update({package[1]: {}})

                            # Checks if the current branch value is inside the paint package.
                            if not paint_package_header.get(branch):
                                paint_package_header.update({branch: {}})

                        if action == "delete_header":
                            del branches[branch][list(branches[branch])[0]]

                        if action == "replace_header":
                            branches[branch][package[1]] = branches[branch].pop(list(branches[branch])[0])

                        if action == "set_color_header" or action == "replace_color_header":
                            # Adds the branch as key and the paint as value to the paint package.
                            paint_package_header.update({branch: painter(package[1], branch)})

                        if action == "delete_color_header":
                            paint_package_header.update({branch: {}})

                        # Layer

                        if action == "add_layer" or action == "delete_layer" or action == "replace_layer"\
                                or action == "set_color_layer" or action == "delete_color_layer"\
                                or action == "replace_color_layer":
                            position = package[1]

                            # Checks if pos is not a instance of list.
                            if not isinstance(position, list):
                                # Pos will be equal to a list that contains the value of pos.
                                position = [position]

                        if action == "add_layer":
                            layer = package[2]

                            # Checks if layer is not a instance of list.
                            if not isinstance(layer, list):
                                # Layer will be equal to a list that contains the value of layer.
                                layer = [layer]

                            # Calls the operator function and gets the returned pos.
                            position = build_pos(branch, position)

                            # Loops through all positions in the pos list.
                            for pos in position:
                                # Calls the calculate_position function.
                                executor_calculate("add_layer", [branch, pos.copy(), layer])

                            # Checks if the current branch value is inside the paint package.
                            if not paint_package_layer.get(branch):
                                paint_package_layer.update({branch: {}})

                        if action == "delete_layer" or action == "replace_layer":
                            # Calls the operator function and gets the returned pos.
                            position = build_pos(branch, position)

                            # Loops through all positions in the pos list.
                            for pos in position:
                                # Calls the calculate_position function.
                                queue = executor_calculate(action, [branch, pos.copy(), {}])

                            for key, value in queue.items():
                                uids[branch].remove(key[-10:])
                                if action == "delete_layer":
                                    del value[key]
                                if action == "replace_layer":
                                    value[package[2] + get_uid(branch)] = value.pop(key)

                        if action == "delete_color_layer" or action == "replace_color_layer"\
                                or action == "set_color_layer":
                            # Gets num value based on the length of entries in pos list.
                            for num in range(len(position)):
                                # Separates the numbers from the dots in current pos value.
                                position[num] = position[num].split(".")

                            # Calls the operator function and gets the returned pos.
                            position = build_pos(branch, position.copy())

                            for pos in position:
                                match = ""
                                # Loops through all values of pos list.
                                for value in pos:
                                    # Creates the match variable.
                                    for x in value:
                                        # Match is equal to current value of match plus the value.
                                        match = match + x

                                if action == "replace_color_layer" or action == "set_color_layer":
                                    # Calls the calculate function.
                                    executor_calculate(action, [branch, pos.copy(), match, package[2]])
                                if action == "delete_color_layer":
                                    # Calls the calculate function.
                                    executor_calculate("delete_color_layer", [branch, pos.copy(), match])

                        # Symbol

                        if action == "set_symbol" or action == "replace_symbol":
                            line = package[1]
                            split = package[2]
                            end = package[3]

                            if action == "set_symbol":
                                # Checks if not line.
                                if not line:
                                    # Line symbol is equal to one space.
                                    line = " "
                                # Checks if not split.
                                if not split:
                                    # Split symbol is equal to one space.
                                    split = " "
                                # Checks if not end.
                                if not end:
                                    # End symbol is equal to one space.
                                    end = " "

                            if action == "replace_symbol":
                                if not line:
                                    line = symbols[branch]["line"]
                                if not split:
                                    split = symbols[branch]["split"]
                                if not end:
                                    end = symbols[branch]["end"]

                            # Checks if branch is in the symbols dictionary.
                            if branch in symbols:
                                # Updates the branch line symbol to the given input.
                                symbols[branch].update({"line": line})
                                # Updates the branch split symbol to the given input.
                                symbols[branch].update({"split": split})
                                # Updates the branch end symbol to the given input.
                                symbols[branch].update({"end": end})

                        if action == "delete_symbol":
                            symbols.update({branch: {"line": "┃", "split": "┣━━", "end": "┗━━"}})

                        # Size

                        if action == "set_size":
                            if symbols[branch]["split"] == "┣━━":
                                symbols[branch]["split"] = "┣━" + "━" * package[1]
                            if symbols[branch]["end"] == "┗━━":
                                symbols[branch]["end"] = "┗━" + "━" * package[1]

                            size.update({branch: package[1]})

                        if action == "reset_size":
                            size.update({branch: 1})

                        # Clear

                        if action != "delete_branch":
                            output[branch].clear()
                            error[branch].clear()
