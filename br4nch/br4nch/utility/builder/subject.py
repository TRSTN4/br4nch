# Imports all files.
from br4nch.utility.builder.object import build_object
from br4nch.utility.librarian import librarian
from br4nch.utility.branching import branching


# Algorithm to build all the given subjects.
def build_subject(branch, header, module, paint_branch):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    subject_package = librarian("subject_package")
    paper = librarian("paper")

    # Checks if content in package.
    if subject_package:
        # Resets the paint.
        paint_clear = "\u001b[0m"
    # If content not in package.
    else:
        # Sets the paint to nothing.
        paint_clear = ""

    # Checks if module key in branch list has any value.
    if branches[branch][header][module]:
        # Decider decides when to use the straight and end line symbol.
        decider1 = 0
        decider2 = 0

        # Stores all the subjects with the "multi" branching.
        send_subject1 = []
        # Stores all the subjects with the "end last" branching.
        send_subject2 = []
        # Stores all the subjects with the "multi last" branching.
        send_subject3 = []

        # Loops through all subjects in the subject list.
        for subject in branches[branch][header][module]:
            # Resets the paint after every loop.
            paint_subject = paint_clear

            # Saves the current state of subject.
            saved_subject = subject

            # Tries to run loop.
            try:
                # Loops through all keys in the subject > branch directory.
                for key in subject_package[branch]:
                    # Checks if the key is equal to the value of subject.
                    if key == subject:
                        # Subject paint is equal to the value of the key inside the subject > branch package.
                        paint_subject = subject_package[branch].get(key)

                    # Checks if the first four characters are equal to "all-".
                    if key[:4] == "all-":
                        # Modified key removes the "all-" from the key.
                        modified_key = key[4:]
                        # Checks if the modified key is equal to the value of module.
                        if modified_key == module:
                            # Loops through all keys in branches > branch > header > module dictionary.
                            for package in branches[branch][header][module]:
                                # Check if the value of package is equal to the value of subject.
                                if package == subject:
                                    # Subject paint is equal to the value of the key in subject > branch package.
                                    paint_subject = subject_package[branch].get(key)
            # If KeyError in loop.
            except KeyError:
                # Passes through.
                pass

            # Loops through all given packages inside the subject package dictionary.
            for package in subject_package:
                # Checks if the package is equal to "all" string.
                if package == "all":
                    # Loops through all keys inside the "all" package.
                    for key in subject_package["all"]:
                        # Checks if the key is equal to the "all" string.
                        if key == "all":
                            # Subject paint is equal to the value of "all" inside subject > "all" package.
                            paint_subject = subject_package["all"].get("all")
                        # If the key is not equal to the "all" string.
                        else:
                            # Checks if the key is equal to the value of subject.
                            if key == subject:
                                # Subject paint is equal to the value of subject inside subject > "all" package.
                                paint_subject = subject_package["all"].get(subject)
                # If the package is not equal to "all" string.
                else:
                    # Loops through all keys inside the subject > branch package.
                    for key in subject_package[branch]:
                        # Checks if the key is equal to the "all" string.
                        if key == "all":
                            # Subject paint is equal to the value of the key in the subject > branch package.
                            paint_subject = subject_package[branch].get(key)

            # Checks current module value is equal to the value of the last module in the list.
            if module == list(dict.keys(branches[branch][header]))[-1]:
                # Adds the current decider value by 1.
                decider1 = decider1 + 1

                # Checks if "\n"/newline in subject.
                if "\n" in subject:
                    # Checks decider number is equal to the length of the total number of branch module entries.
                    if decider1 == len(branches[branch][header][module]):
                        # Replaces the newline with new branching.
                        subject = subject.replace("\n", paint_clear + "\n" + paint_clear + " " * 8 +
                                                  paint_subject)

                # Checks decider number is equal to the length of the total number of branch module entries.
                if decider1 == len(branches[branch][header][module]):
                    # Uses prefix with the end line symbol and appends the output to the paper list.
                    paper.append(paint_clear + paint_branch + branching("subject_end", " ") +
                                 paint_clear + " " + paint_subject + subject + paint_clear)

                    # Reverts the old state of subject.
                    subject = saved_subject

                    # Appends the current value of subject to the send subject list.
                    send_subject3.append(subject)
                # If decider number is not equal to the length of the total number of branch module entries.
                else:
                    # Uses prefix with the multi line symbol and appends the output to the paper list.
                    paper.append(paint_clear + paint_branch + branching("subject_multi", " ") +
                                 paint_clear + " " + paint_subject + subject + paint_clear)

                    # Reverts the old state of subject.
                    subject = saved_subject

            # If current module value is not equal to the value of the last module in the list.
            else:
                # Adds the current decider value by 1.
                decider2 = decider2 + 1

                # Checks if "\n"/newline in subject.
                if "\n" in subject:
                    # If decider number is not equal to the length of the total number of branch module entries.
                    if not decider2 == len(branches[branch][header][module]):
                        # Replaces the newline with new branching.
                        subject = subject.replace("\n", paint_clear + paint_branch + "\n┃" +
                                                  paint_clear + " " * 3 + paint_branch + "┃" +
                                                  paint_clear + " " * 3 + paint_subject)
                    # Checks decider number is equal to the length of the total number of branch module entries.
                    else:
                        # Replaces the newline with new branching.
                        subject = subject.replace("\n", paint_clear + paint_branch + "\n┃" +
                                                  paint_clear + " " * 7 + paint_subject)

                # Checks decider number is equal to the length of the total number of branch module entries.
                if decider2 == len(branches[branch][header][module]):
                    # Uses prefix with the end line symbol and appends the output to the paper list.
                    paper.append(paint_clear + paint_branch + branching("subject_end_last", "┃") +
                                 paint_clear + " " + paint_subject + subject + paint_clear)

                    # Reverts the old state of subject.
                    subject = saved_subject

                    # Appends the current value of subject to the send subject list.
                    send_subject2.append(subject)
                # If decider number is not equal to the length of the total number of branch module entries.
                else:
                    # Uses prefix with the multi line symbol and appends the output to the paper list.
                    paper.append(paint_clear + paint_branch + branching("subject_multi_last", "┃")
                                 + paint_clear + " " + paint_subject + subject + paint_clear)

                    # Reverts the old state of subject.
                    subject = saved_subject

                    # Appends the current value of subject to the send subject list.
                    send_subject1.append(subject)

            # Runs the next task.
            build_object(branch, header, module, subject, paint_branch, send_subject1, send_subject2, send_subject3)
