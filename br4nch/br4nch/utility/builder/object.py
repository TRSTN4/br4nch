# Imports all files.
from br4nch.utility.librarian import librarian
from br4nch.utility.branching import branching


# Algorithm to build all the given objects.
def build_object(paint_branch, branch, header, module, subject, send_subject1, send_subject2, send_subject3):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    object_package = librarian("object_package")
    paper = librarian("paper")

    # Resets the paint.
    paint_clear = "\u001b[0m"

    # Checks if subject key in branch list has any value.
    if branches[branch][header][module][subject]:
        # Decider decides when to use the straight and end line symbol.
        decider = 0

        # Loops through all objects in the object list.
        for obj in branches[branch][header][module][subject]:
            # Resets the paint after every loop.
            paint_object = paint_clear

            # Loops through all keys in the object > branch directory.
            for key in object_package[branch]:
                # Checks if the key is equal to the value of object.
                if key == obj:
                    # Object paint is equal to the value of the key inside the object > branch package.
                    paint_object = object_package[branch].get(key)

                # Checks if the first four characters are equal to "all-".
                if key[:4] == "all-":
                    # Modified key removes the "all-" from the key.
                    modified_key = key[4:]
                    # Checks if the modified key is equal to the value of subject.
                    if modified_key == subject:
                        # Loops through all keys in branches > branch > header > module > subject dictionary.
                        for package in branches[branch][header][module][subject]:
                            # Check if the value of package is equal to the value of object.
                            if package == obj:
                                # Object paint is equal to the value of the key in object > branch package.
                                paint_object = object_package[branch].get(key)

            # Loops through all given packages inside the object package dictionary.
            for package in object_package:
                # Checks if the package is equal to "all" string.
                if package == "all":
                    # Loops through all keys inside the "all" package.
                    for key in object_package["all"]:
                        # Checks if the key is equal to the "all" string.
                        if key == "all":
                            # Object paint is equal to the value of "all" inside object > "all" package.
                            paint_object = object_package["all"].get("all")
                        # If the key is not equal to the "all" string.
                        else:
                            # Checks if the key is equal to the value of object.
                            if key == obj:
                                # Object paint is equal to the value of object inside object > "all" package.
                                paint_object = object_package["all"].get(obj)
                # If the package is not equal to "all" string.
                else:
                    # Loops through all keys inside the module > branch package.
                    for key in object_package[branch]:
                        # Checks if the key is equal to the "all" string.
                        if key == "all":
                            # Object paint is equal to the value of the key in the object > branch package.
                            paint_object = object_package[branch].get(key)

            # Assigns the last module in the header list to a variable.
            last_module = list(dict.keys(branches[branch][header]))[-1]
            # Assigns the last subject in the last_module list to a variable.
            last_subject = list(dict.keys(branches[branch][header][last_module]))[-1]
            # Assigns the last object in the last_subject list to a variable.
            last_object = list(dict.keys(branches[branch][header][last_module][last_subject]))[-1]

            # Checks current subject value is equal to the value of the last subject in the list.
            if not obj == last_object:
                # Checks current module value is equal to the value of the last module in the list.
                if module == last_module:
                    # Checks current subject value is equal to the value of the last subject in the list.
                    if subject == last_subject:
                        # Extender is equal to five spaces.
                        extender = " " * 5
                    # If current subject value is not equal to the value of the last subject in the list.
                    else:
                        # Extender is equal four spaces and one straight line.
                        extender = " " * 4 + "┃"
                # If current module value is not equal to the value of the last module in the list.
                else:
                    # Extender is equal to one straight line and four spaces.
                    extender = "┃" + " " * 4
            # Checks current subject value is not equal to the value of the last subject in the list.
            else:
                # Extender is equal to five spaces.
                extender = " " * 5

            # Adds the current decider value by 1.
            decider = decider + 1

            # Loops through all subjects in the send subject list.
            for received in send_subject1:
                # Checks if the received value is equal to the value of subject.
                if received == subject:
                    # Checks if "\n"/newline in object.
                    if "\n" in obj:
                        # If decider number not equal to the length of total number of branch subject entries.
                        if not decider == len(branches[branch][header][module][subject]):
                            # Replaces the newline with new branching.
                            obj = obj.replace("\n", paint_clear + paint_branch + "\n┃" + paint_clear +
                                              " " * 3 + paint_branch + "┃" + paint_clear + " " * 3 +
                                              paint_branch + "┃" + paint_clear + " " * 3 + paint_object)
                        # Checks decider number is equal to length of total number of branch subject entries.
                        else:
                            # Replaces the newline with new branching.
                            obj = obj.replace("\n", paint_clear + paint_branch + "\n┃" + paint_clear +
                                              " " * 3 + paint_branch + "┃" + paint_clear + " " * 7 +
                                              paint_object)

                    # Extender is equal to one straight line, three spaces and one more straight line.
                    extender = "┃" + " " * 3 + "┃"

            # Loops through all subjects in the send subject list.
            for received in send_subject2:
                # Checks if the received value is equal to the value of subject.
                if received == subject:
                    # Checks if "\n"/newline in object.
                    if "\n" in obj:
                        # If decider number not equal to the length of total number of branch subject entries.
                        if not decider == len(branches[branch][header][module][subject]):
                            # Replaces the newline with new branching.
                            obj = obj.replace("\n", paint_clear + paint_branch + "\n┃" + paint_clear +
                                              " " * 7 + paint_branch + "┃" + paint_clear + " " * 3 +
                                              paint_object)
                        # Checks decider number is equal to length of total number of branch subject entries.
                        else:
                            # Replaces the newline with new branching.
                            obj = obj.replace("\n", paint_clear + paint_branch + "\n┃" + paint_clear +
                                              " " * 11 + paint_object)

            # Loops through all subjects in the send subject list.
            for received in send_subject3:
                # Checks if the received value is equal to the value of subject.
                if received == subject:
                    # Checks if "\n"/newline in object.
                    if "\n" in obj:
                        # If decider number not equal to the length of total number of branch subject entries.
                        if not decider == len(branches[branch][header][module][subject]):
                            # Replaces the newline with new branching.
                            obj = obj.replace("\n", paint_clear + "\n" + " " * 8 + paint_branch + "┃" +
                                              paint_clear + " " * 3 + paint_object)
                        # Checks decider number is equal to length of total number of branch subject entries.
                        else:
                            # Replaces the newline with new branching.
                            obj = obj.replace("\n", paint_clear + "\n" + " " * 12 + paint_object)

            # Checks decider number is equal to the length of the total number of branch subject entries.
            if decider == len(branches[branch][header][module][subject]):
                # Uses prefix with the end line symbol and appends the output to the paper list.
                paper.append(paint_clear + paint_branch + branching("object_end", extender) +
                             paint_clear + " " + paint_object + obj + paint_clear)
            # If decider number is not equal to the length of the total number of branch subject entries.
            else:
                # Uses prefix with the multi line symbol and appends the output to the paper list.
                paper.append(paint_clear + paint_branch + branching("object_multi", extender) +
                             paint_clear + " " + paint_object + obj + paint_clear)
