# Indev phase - br4nch v1.1.6
# desc - Algorithm update, paint bug fixes plus new features and changed paint arguments to optional paint arguments.


# The add class is used for users to add certain tasks.
class add:
    @staticmethod
    # Adds a new name for the branch.
    def name(branch):
        # Adds the name inside the branch dictionary.
        branches.update({branch: {}})

    @staticmethod
    # Adds a new header for the branch.
    def header(branch, header_name):
        # Adds header > name inside the branch dictionary.
        branches[branch].update({header_name: {}})

    @staticmethod
    # Adds a new module for the branch.
    def module(branch, header_name, module_name):
        # Adds the module > header > name inside the branch dictionary.
        branches[branch][header_name].update({module_name: {}})

    @staticmethod
    # Adds a new subject for the branch.
    def subject(branch, header_name, module_name, subject_name):
        # Adds the subject > module > header > name inside the branch dictionary.
        branches[branch][header_name][module_name].update({subject_name: {}})

    @staticmethod
    # Adds a new object for the branch.
    def object(branch, header_name, module_name, subject_name, object_name):
        # Adds the object > subject > module > header > name inside the branch dictionary.
        branches[branch][header_name][module_name][subject_name].update({object_name: {}})


# The set class is used for users to set certain tasks.
class set:
    # The color class can color certain parts of the branch.
    class color:
        @staticmethod
        # Adds the chosen paint to the chosen branch to a list.
        def branch(branch="", color="", special1="", special2="", special3=""):
            # Parses the name, color and specials to the painter. Then the painter returns the paint.
            paint_branch = utility.painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

            # Adds the branch as key and the paint as value to the package dictionary.
            branch_package.update({branch: paint_branch})

        @staticmethod
        # Adds the chosen paint to the chosen header to a list.
        def header(branch="", color="", special1="", special2="", special3=""):
            # Parses the name, color and specials to the painter. Then the painter returns the paint.
            paint_header = utility.painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

            # Adds the branch as key and the paint as value to the package dictionary.
            header_package.update({branch: paint_header})

        @staticmethod
        # Adds the chosen paint to the chosen module to a list.
        def module(branch="", module="", color="", special1="", special2="", special3=""):
            # Parses the name, color and specials to the painter. Then the painter returns the paint.
            paint_module = utility.painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

            # Checks if the current branch value is inside the dictionary.
            if not module_package.get(branch):
                # Adds the current branch value as key and a new dictionary as value to the package dictionary.
                module_package.update({branch: {}})

            # Adds the module as key and the paint as value inside the branch > package dictionary.
            module_package[branch].update({module: paint_module})

        @staticmethod
        # Adds the chosen paint to the chosen subject to a list.
        def subject(branch="", subject="", color="", special1="", special2="", special3=""):
            # Parses the name, color and specials to the painter. Then the painter returns the paint.
            paint_subject = utility.painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

            # Checks if the current branch value is inside the dictionary.
            if not subject_package.get(branch):
                # Adds the current branch value as key and a new dictionary as value to the package dictionary.
                subject_package.update({branch: {}})

            # Adds the subject as key and the paint as value inside the branch > package dictionary.
            subject_package[branch].update({subject: paint_subject})

        @staticmethod
        # Adds the chosen paint to the chosen object to a list.
        def object(branch="", obj="", color="", special1="", special2="", special3=""):
            # Parses the name, color and specials to the painter. Then the painter returns the paint.
            paint_object = utility.painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

            # Checks if the current branch value is inside the dictionary.
            if not object_package.get(branch):
                # Adds the current branch value as key and a new dictionary as value to the package dictionary.
                object_package.update({branch: {}})

            # Adds the object as key and the paint as value inside the branch > package dictionary.
            object_package[branch].update({obj: paint_object})


# The run class is used for users to run certain tasks.
class run:
    @staticmethod
    # Prints the chosen branches.
    def display(branch):
        # Builds the chosen branches.
        utility.builder(branch)
        # Prints the chosen branches.
        utility.printer()


# Contains all helper functions and classes.
class utility:
    @staticmethod
    # Manager runs all the needed tasks on start.
    def manager():
        # Executes the "construction" action.
        utility.executor("construction")

    @staticmethod
    # The executor class executes and stores certain tasks.
    def executor(action):
        # Globalizes all the lists and dictionaries.
        global branches
        global list_branches, list_headers, list_modules, list_subjects, list_objects
        global branch_package, header_package, module_package, subject_package, object_package
        global paper

        # Checks if the action is equal to "construction". Construction creates all the global lists and dictionaries.
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

    @staticmethod
    # Creates the branching part of the code.
    def branching(action, extender):
        # Stores three spaces in a row.
        space_x3 = " " * 3

        # Stores all actions to variables.
        header_end = "\n╻"
        module_multi = "┃\n┣━━"
        module_end = "┃\n┗━━"
        subject_multi = extender + space_x3 + "┃\n" + extender + space_x3 + "┣━━"
        subject_multi_last = extender + space_x3 + "┃\n" + extender + space_x3 + "┣━━"
        subject_end = extender + space_x3 + "┃\n" + extender + space_x3 + "┗━━"
        subject_end_last = extender + space_x3 + "┃\n" + extender + space_x3 + "┗━━"
        object_multi = extender + space_x3 + "┃\n" + extender + space_x3 + "┣━━"
        object_end = extender + space_x3 + "┃\n" + extender + space_x3 + "┗━━"

        # Saves all the actions in a list.
        branching_action = [header_end, module_multi, module_end, subject_multi, subject_multi_last, subject_end,
                            subject_end_last, object_multi, object_end]

        # Saves all the action ids in a list.
        branching_id = ["header_end", "module_multi", "module_end", "subject_multi", "subject_multi_last",
                        "subject_end", "subject_end_last", "object_multi", "object_end"]

        # Checks if the action list has any value.
        if action:
            # Loops through total length of the branching action list.
            for number in range(len(branching_action)):
                # Checks if the parsed action is equal to a id in the id list.
                if action == branching_id[number]:
                    # Returns the requested action.
                    return branching_action[number]

    @staticmethod
    # Returns paint with the given paint and specials.
    def painter(color="", special1="", special2="", special3=""):
        # Stores all the colors and specials.
        black = "\u001b[30m"        # Black
        red = "\u001b[31m"          # Red
        green = "\u001b[32m"        # Green
        yellow = "\u001b[33m"       # Yellow
        blue = "\u001b[34m"         # Blue
        magenta = "\u001b[35m"      # Magenta
        cyan = "\u001b[36m"         # Cyan
        white = "\u001b[37m"        # White
        bold = "\u001b[1m"          # Bold
        underline = "\u001b[4m"     # Underline
        reversing = "\u001b[4m"     # Reversing
        clear = "\u001b[0m"         # Clear

        # Saves all the color actions in a list.
        colors_action = [black, red, green, yellow, blue, magenta, cyan, white, clear]

        # Saves all the color action ids in a list.
        colors_id = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white", "clear"]

        # Saves all the special actions in a list.
        specials_action = [bold, underline, reversing]

        # Saves all the special action ids in a list.
        specials_id = ["bold", "underline", "reversing"]

        # Checks if the color variable has any value.
        if color:
            # Loops through total length of the colors action list.
            for number in range(len(colors_action)):
                # Checks if the parsed color is equal to a id in the id list.
                if color == colors_id[number]:
                    # Sets the requested color action to the color variable.
                    color = colors_action[number]

        # Checks if the special1, special2 or special3 variables has any value.
        if special1 or special2 or special3:
            # Loops through total length of the specials action list.
            for number in range(len(specials_action)):
                # Checks if the parsed special1 is equal to a id in the id list.
                if special1 == specials_id[number]:
                    # Sets the requested special1 action to the special1 variable.
                    special1 = specials_action[number]
                # Checks if the parsed special2 is equal to a id in the id list.
                if special2 == specials_id[number]:
                    # Sets the requested special2 action to the special2 variable.
                    special2 = specials_action[number]
                # Checks if the parsed special3 is equal to a id in the id list.
                if special3 == specials_id[number]:
                    # Sets the requested special3 action to the special3 variable.
                    special3 = specials_action[number]

        # Returns the requested action.
        return color + special1 + special2 + special3

    # Uses algorithms to build the final branch result.
    class builder:
        # Loads all required variables.
        def __init__(self, branch_name):
            # Variable to clear all paint.
            self.paint_clear = utility.painter("clear", "", "", "")

            # Runs the next task.
            self.build_branches(branch_name)

        # Algorithm to build all the given branches.
        def build_branches(self, branch_name):
            # Checks if the branch list has any value.
            if branches:
                # "stop" is equal to false.
                stop = False

                # Loops through all branches in the branch list.
                for branch in branches:
                    # Resets the paint after every loop.
                    paint_branch = "\u001b[0m"

                    # Resets the newline after every loop.
                    newline = ""

                    # Checks if there are multiple branches in the list.
                    if len(list(dict.keys(branches))) > 1:
                        # Passes through every branch except first branch.
                        if not branch == list(dict.keys(branches))[0]:
                            # When printing multiple branches, add a newline between every new branch.
                            newline = "\n"

                    # Checks if "stop" is equal to true.
                    if stop:
                        # Breaks the loop and stops the algorithm.
                        break

                    # Checks the branch name argument is equal to "all".
                    if branch_name == "all":
                        # Passes all the break statements and stops when the loop is complete.
                        pass

                    # If the branch name argument is not equal to "all".
                    else:
                        # Changes the current branch value to the value of the given branch name argument.
                        branch = branch_name
                        # "stop" is set to true.
                        stop = True

                    # Loops through all keys in the package directory.
                    for key in branch_package:
                        # Checks if the key is equal to the value of branch.
                        if key == branch:
                            # Branch paint is equal to the value of the key inside the branch package.
                            paint_branch = branch_package.get(branch)

                    # Loops through all given packages inside the branch package dictionary.
                    for key in branch_package:
                        # Checks if the key is equal to "all" string.
                        if key == "all":
                            # Branch paint is equal to the value of "all" inside the branch package.
                            paint_branch = branch_package.get("all")

                    # Runs the next task.
                    self.build_headers(paint_branch, branch, newline)

        # Algorithm to build all the given headers.
        def build_headers(self, paint_branch, branch, newline):
            # Checks if branch key in branch list has any value.
            if branches[branch]:
                # Loops through all headers in the header list.
                for header in branches[branch]:
                    # Resets the paint after every loop.
                    paint_header = "\u001b[0m"

                    # Loops through all given packages inside the header package dictionary.
                    for key in header_package:
                        # Checks if the key is equal to the value of branch.
                        if key == branch:
                            # Header paint is equal to the value of the branch inside the header package.
                            paint_header = header_package.get(branch)

                    # Loops through all keys in the package directory.
                    for key in header_package:
                        # Checks if the key is equal to "all" string.
                        if key == "all":
                            # Header paint is equal to the "all" value inside the header package.
                            paint_header = header_package.get("all")

                    # Uses prefix with the end line symbol and appends the output to the paper list.
                    paper.append(self.paint_clear + paint_header + newline + header + self.paint_clear + paint_branch +
                                 utility.branching("header_end", "") + self.paint_clear)

                    # Runs the next task.
                    self.build_modules(paint_branch, branch, header)

        # Algorithm to build all the given modules.
        def build_modules(self, paint_branch, branch, header):
            # Checks if header key in branch list has any value.
            if branches[branch][header]:
                # Decider decides when to use the straight and end line symbol.
                decider = 0

                # Loops through all modules in the module list.
                for module in branches[branch][header]:
                    # Resets the paint after every loop.
                    paint_module = "\u001b[0m"

                    # Saves the current state of module.
                    saved_module = module

                    # Adds the current decider value by 1.
                    decider = decider + 1

                    # Loops through all keys in the module > branch directory.
                    for key in module_package[branch]:
                        # Checks if the key is equal to the value of module.
                        if key == module:
                            # Module paint is equal to the value of the key inside the module > branch package.
                            paint_module = module_package[branch].get(key)

                    # Loops through all given packages inside the module package dictionary.
                    for package in module_package:
                        # Checks if the package is equal to "all" string.
                        if package == "all":
                            # Loops through all keys inside the "all" package.
                            for key in module_package["all"]:
                                # Checks if the key is equal to the "all" string.
                                if key == "all":
                                    # Module paint is equal to the value of "all" inside module > "all" package.
                                    paint_module = module_package["all"].get("all")
                                # If the key is not equal to the "all" string.
                                else:
                                    # Checks if the key is equal to the value of module.
                                    if key == module:
                                        # Module paint is equal to the value of module inside module > "all" package.
                                        paint_module = module_package["all"].get(module)
                        # If the package is not equal to "all" string.
                        else:
                            # Loops through all keys inside the module > branch package.
                            for key in module_package[branch]:
                                # Checks if the key is equal to the "all" string.
                                if key == "all":
                                    # Module paint is equal to the value of the key in the module > branch package.
                                    paint_module = module_package[branch].get(key)

                    # Checks decider number is equal to the length of the total number of branch header entries.
                    if decider == len(branches[branch][header]):
                        # Checks if "\n"/newline in module.
                        if "\n" in module:
                            module = module.replace("\n",  self.paint_clear + "\n" + " " * 4 + paint_module)
                        # If "\n"/newline not in module.
                        else:
                            module = module.replace(module, self.paint_clear + paint_module + module)

                        # Uses prefix with the end line symbol and appends the output to the paper list.
                        paper.append(self.paint_clear + paint_branch + utility.branching("module_end", "") +
                                     self.paint_clear + " " + paint_module + module + self.paint_clear)

                    # If decider number is not equal to the length of the total number of branch header entries.
                    else:
                        # Checks if "\n"/newline in module.
                        if "\n" in module:
                            # Replaces the newline with new branching.
                            module = module.replace("\n", self.paint_clear + paint_branch + "\n┃" + self.paint_clear +
                                                    " " * 3 + paint_module)
                        # If "\n"/newline not in module.
                        else:
                            # Replaces the newline with new branching.
                            module = module.replace(module, self.paint_clear + paint_module + module)

                        # Uses prefix with the multi line symbol and appends the output to the paper list.
                        paper.append(self.paint_clear + paint_branch + utility.branching("module_multi", "") +
                                     self.paint_clear + " " + paint_module + module + self.paint_clear)

                    # Reverts the old state of module.
                    module = saved_module

                    # Runs the next task.
                    self.build_subjects(paint_branch, branch, header, module)

        # Algorithm to build all the given subjects.
        def build_subjects(self, paint_branch, branch, header, module):
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
                    paint_subject = "\u001b[0m"

                    # Saves the current state of subject.
                    saved_subject = subject

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
                                subject = subject.replace("\n", self.paint_clear + "\n" + self.paint_clear + " " * 8 +
                                                          paint_subject)

                        # Checks decider number is equal to the length of the total number of branch module entries.
                        if decider1 == len(branches[branch][header][module]):
                            # Uses prefix with the end line symbol and appends the output to the paper list.
                            paper.append(self.paint_clear + paint_branch + utility.branching("subject_end", " ") +
                                         self.paint_clear + " " + paint_subject + subject + self.paint_clear)

                            # Reverts the old state of subject.
                            subject = saved_subject

                            # Appends the current value of subject to the send subject list.
                            send_subject3.append(subject)
                        # If decider number is not equal to the length of the total number of branch module entries.
                        else:
                            # Uses prefix with the multi line symbol and appends the output to the paper list.
                            paper.append(self.paint_clear + paint_branch + utility.branching("subject_multi", " ") +
                                         self.paint_clear + " " + paint_subject + subject + self.paint_clear)

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
                                subject = subject.replace("\n", self.paint_clear + paint_branch + "\n┃" +
                                                          self.paint_clear + " " * 3 + paint_branch + "┃" +
                                                          self.paint_clear + " " * 3 + paint_subject)
                            # Checks decider number is equal to the length of the total number of branch module entries.
                            else:
                                # Replaces the newline with new branching.
                                subject = subject.replace("\n", self.paint_clear + paint_branch + "\n┃" +
                                                          self.paint_clear + " " * 7 + paint_subject)

                        # Checks decider number is equal to the length of the total number of branch module entries.
                        if decider2 == len(branches[branch][header][module]):
                            # Uses prefix with the end line symbol and appends the output to the paper list.
                            paper.append(self.paint_clear + paint_branch + utility.branching("subject_end_last", "┃") +
                                         self.paint_clear + " " + paint_subject + subject + self.paint_clear)

                            # Reverts the old state of subject.
                            subject = saved_subject

                            # Appends the current value of subject to the send subject list.
                            send_subject2.append(subject)
                        # If decider number is not equal to the length of the total number of branch module entries.
                        else:
                            # Uses prefix with the multi line symbol and appends the output to the paper list.
                            paper.append(self.paint_clear + paint_branch + utility.branching("subject_multi_last", "┃")
                                         + self.paint_clear + " " + paint_subject + subject + self.paint_clear)

                            # Reverts the old state of subject.
                            subject = saved_subject

                            # Appends the current value of subject to the send subject list.
                            send_subject1.append(subject)

                    # Runs the next task.
                    self.build_objects(paint_branch, branch, header, module, subject, send_subject1, send_subject2,
                                       send_subject3)

        # Algorithm to build all the given objects.
        def build_objects(self, paint_branch, branch, header, module, subject, send_subject1, send_subject2,
                          send_subject3):
            # Checks if subject key in branch list has any value.
            if branches[branch][header][module][subject]:
                # Decider decides when to use the straight and end line symbol.
                decider = 0

                # Loops through all objects in the object list.
                for obj in branches[branch][header][module][subject]:
                    # Resets the paint after every loop.
                    paint_object = "\u001b[0m"

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
                                    obj = obj.replace("\n", self.paint_clear + paint_branch + "\n┃" + self.paint_clear +
                                                      " " * 3 + paint_branch + "┃" + self.paint_clear + " " * 3 +
                                                      paint_branch + "┃" + self.paint_clear + " " * 3 + paint_object)
                                # Checks decider number is equal to length of total number of branch subject entries.
                                else:
                                    # Replaces the newline with new branching.
                                    obj = obj.replace("\n", self.paint_clear + paint_branch + "\n┃" + self.paint_clear +
                                                      " " * 3 + paint_branch + "┃" + self.paint_clear + " " * 7 +
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
                                    obj = obj.replace("\n", self.paint_clear + paint_branch + "\n┃" + self.paint_clear +
                                                      " " * 7 + paint_branch + "┃" + self.paint_clear + " " * 3 +
                                                      paint_object)
                                # Checks decider number is equal to length of total number of branch subject entries.
                                else:
                                    # Replaces the newline with new branching.
                                    obj = obj.replace("\n", self.paint_clear + paint_branch + "\n┃" + self.paint_clear +
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
                                    obj = obj.replace("\n", self.paint_clear + "\n" + " " * 8 + paint_branch + "┃" +
                                                      self.paint_clear + " " * 3 + paint_object)
                                # Checks decider number is equal to length of total number of branch subject entries.
                                else:
                                    # Replaces the newline with new branching.
                                    obj = obj.replace("\n", self.paint_clear + "\n" + " " * 12 + paint_object)

                    # Checks decider number is equal to the length of the total number of branch subject entries.
                    if decider == len(branches[branch][header][module][subject]):
                        # Uses prefix with the end line symbol and appends the output to the paper list.
                        paper.append(self.paint_clear + paint_branch + utility.branching("object_end", extender) +
                                     self.paint_clear + " " + paint_object + obj + self.paint_clear)
                    # If decider number is not equal to the length of the total number of branch subject entries.
                    else:
                        # Uses prefix with the multi line symbol and appends the output to the paper list.
                        paper.append(self.paint_clear + paint_branch + utility.branching("object_multi", extender) +
                                     self.paint_clear + " " + paint_object + obj + self.paint_clear)

    @staticmethod
    # The printer prints all the results.
    def printer():
        # Loops through all elements in the paper list.
        for ink in paper:
            # Prints the ink from the paper list.
            print(ink)

        # Clears the paper list.
        paper.clear()


# Running tasks manually. (Will be removed once it leaves the indev phase.)
if __name__ == '__main__':
    utility.manager()

    add.name("Computer")
    add.header("Computer", "Gaming")
    add.module("Computer", "Gaming", "Monitors")
    add.module("Computer", "Gaming", "Keyboard & Mouse")
    add.subject("Computer", "Gaming", "Monitors", "LG")
    add.subject("Computer", "Gaming", "Keyboard & Mouse", "Steel Series")
    add.subject("Computer", "Gaming", "Keyboard & Mouse", "Razer")
    add.object("Computer", "Gaming", "Monitors", "LG", "LG 27GN850 Ultragear")
    add.object("Computer", "Gaming", "Keyboard & Mouse", "Razer", "Razer Blackwindow Elite")
    add.object("Computer", "Gaming", "Keyboard & Mouse", "Steel Series", "SteelSeries Apex 3")
    add.object("Computer", "Gaming", "Keyboard & Mouse", "Steel Series", "SteelSeries Apex 5")

    set.color.branch("Computer", "blue", "bold")
    set.color.header("Computer", "red", "reversing", "bold", "underline")
    set.color.module("Computer", "Monitors", "yellow", "bold")
    set.color.module("Computer", "Keyboard & Mouse", "cyan", "underline")
    set.color.subject("Computer", "Razer", "blue", "underline", "bold")
    set.color.subject("Computer", "all", "green", "underline", "bold")
    set.color.subject("Computer", "LG", "red", "underline", "bold")
    set.color.object("Computer", "SteelSeries Apex 5", "red", "underline", "reversing")
    set.color.object("Computer", "LG 27GN850 Ultragear", "cyan", "", "bold")

    add.name("Mall")
    add.header("Mall", "Food\nStore")
    add.module("Mall", "Food\nStore", "Meat")
    add.module("Mall", "Food\nStore", "Vegetarian")
    add.module("Mall", "Food\nStore", "Vegan\nVegy")
    add.subject("Mall", "Food\nStore", "Meat", "Cow")
    add.subject("Mall", "Food\nStore", "Meat", "Pig")
    add.subject("Mall", "Food\nStore", "Vegetarian", "Cheese")
    add.subject("Mall", "Food\nStore", "Vegetarian", "Milk")
    add.subject("Mall", "Food\nStore", "Vegetarian", "Bread")
    add.subject("Mall", "Food\nStore", "Vegan\nVegy", "Vegetables\nFruits")
    add.object("Mall", "Food\nStore", "Meat", "Cow", "Beef")
    add.object("Mall", "Food\nStore", "Meat", "Pig", "Pork")
    add.object("Mall", "Food\nStore", "Meat", "Pig", "Tail")
    add.object("Mall", "Food\nStore", "Vegetarian", "Cheese", "Goat Cheese\nMolten Goat Cheese")
    add.object("Mall", "Food\nStore", "Vegetarian", "Cheese", "Blue Cheese")
    add.object("Mall", "Food\nStore", "Vegetarian", "Milk", "Cow Milk\nGoat Milk")
    add.object("Mall", "Food\nStore", "Vegetarian", "Bread", "Brown Bread")
    add.object("Mall", "Food\nStore", "Vegetarian", "Bread", "White Bread")
    add.object("Mall", "Food\nStore", "Vegetarian", "Bread", "Baguette")
    add.object("Mall", "Food\nStore", "Vegan\nVegy", "Vegetables\nFruits", "Carrot")
    add.object("Mall", "Food\nStore", "Vegan\nVegy", "Vegetables\nFruits", "Potato")
    add.object("Mall", "Food\nStore", "Vegan\nVegy", "Vegetables\nFruits", "Onion")
    add.object("Mall", "Food\nStore", "Vegan\nVegy", "Vegetables\nFruits", "Broccoli")
    add.object("Mall", "Food\nStore", "Vegan\nVegy", "Vegetables\nFruits", "Tomato")
    add.object("Mall", "Food\nStore", "Vegan\nVegy", "Vegetables\nFruits", "Red Apple\nGreen Apple")

    set.color.branch("Mall", "magenta")
    set.color.header("Mall", "magenta", "bold")
    set.color.module("Mall", "Meat", "red", "bold", "underline")
    set.color.module("Mall", "Vegetarian", "green", "bold", "underline")
    set.color.module("Mall", "Vegan\nVegy", "cyan", "bold", "underline")
    set.color.subject("Mall", "Cheese", "yellow")
    set.color.subject("Mall", "all-Meat", "cyan")
    set.color.object("Mall", "all-Bread", "yellow", "bold")
    set.color.object("Mall", "Tomato", "red", "bold")
    set.color.object("Mall", "Broccoli", "green")
    set.color.object("Mall", "Blue Cheese", "blue", "underline")

    run.display("all")
