# Indev phase - br4nch v1.1.5
# desc - Removing useless utility import code, Fixing paint bugs and adding new pre paint "all" feature.


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
        def branch(branch, color, special1, special2, special3):
            # Parses the name, color and specials to the painter. Then the painter returns the paint.
            paint_branch = utility.painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

            # Appends the given branch to the list of branches.
            list_branches.append(branch)
            # Appends the given branch paint to the list of branch paint.
            branch_paint.append(paint_branch)

            # Appends the branch to the branch paint check list.
            branch_paint_check.append(branch)

        @staticmethod
        # Adds the chosen paint to the chosen header to a list.
        def header(branch, color, special1, special2, special3):
            # Parses the name, color and specials to the painter. Then the painter returns the paint.
            paint_header = utility.painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

            # Appends the given header to the list of headers.
            list_headers.append(branch)
            # Appends the given header paint to the list of header paint.
            header_paint.append(paint_header)

            # Appends the header to the header paint check list.
            header_paint_check.append(branch)

        @staticmethod
        # Adds the chosen paint to the chosen module to a list.
        def module(branch, module, color, special1, special2, special3):
            # Parses the name, color and specials to the painter. Then the painter returns the paint.
            paint_module = utility.painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

            # Appends the given module to the list of modules.
            list_modules.append(module)
            # Appends the given module paint to the list of module paint.
            module_paint.append(paint_module)

            # Adds the object as key and the branch as value to the module paint check dictionary.
            module_paint_check.update({module: branch})

        @staticmethod
        # Adds the chosen paint to the chosen subject to a list.
        def subject(branch, subject, color, special1, special2, special3):
            # Parses the name, color and specials to the painter. Then the painter returns the paint.
            paint_subject = utility.painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

            # Appends the given subject to the list of subjects.
            list_subjects.append(subject)
            # Appends the given subject paint to the list of subject paint.
            subject_paint.append(paint_subject)

            # Adds the object as key and the branch as value to the subject paint check dictionary.
            subject_paint_check.update({subject: branch})

        @staticmethod
        # Adds the chosen paint to the chosen object to a list.
        def object(branch, obj, color, special1, special2, special3):
            # Parses the name, color and specials to the painter. Then the painter returns the paint.
            paint_object = utility.painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

            # Appends the given object to the list of objects.
            list_objects.append(obj)
            # Appends the given object paint to the list of object paint.
            object_paint.append(paint_object)

            # Adds the object as key and the branch as value to the object paint check dictionary.
            object_paint_check.update({obj: branch})


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
        global branch_paint, header_paint, module_paint, subject_paint, object_paint
        global paper
        global branch_paint_check, header_paint_check, module_paint_check, subject_paint_check, object_paint_check

        # Checks if the action is equal to "construction". Construction creates all the global lists and dictionaries.
        if action == "construction":
            # Dictionary to save all the branches.
            branches = {}

            # Lists to save all the branch parts that has paint.
            list_branches = []
            list_headers = []
            list_modules = []
            list_subjects = []
            list_objects = []

            # Lists to save all the branch paint.
            branch_paint = []
            header_paint = []
            module_paint = []
            subject_paint = []
            object_paint = []

            # List to save all the output of the branches.
            paper = []

            # Dictionaries to save all the paint and branch keys and values.
            branch_paint_check = []
            header_paint_check = []
            module_paint_check = {}
            subject_paint_check = {}
            object_paint_check = {}

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
    def painter(color, special1, special2, special3):
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

        # Checks if color has no value.
        if not color:
            # Assigns no value to color.
            color = ""
        # Checks if special1 has no value.
        if not special1:
            # Assigns no value to special1.
            special1 = ""
        # Checks if special2 has no value.
        if not special2:
            # Assigns no value to special2.
            special2 = ""
        # Checks if special3 has no value.
        if not special3:
            # Assigns no value to special3.
            special3 = ""

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
            self.paint_clear = utility.painter("clear", None, None, None)

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
                    paint_branch = ""

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

                    # Checks if "all" is in branch paint check list.
                    if "all" in branch_paint_check:
                        # Branch paint is the current number of "all" in branches list.
                        paint_branch = branch_paint[list_branches.index("all")]
                    # If "all" is not in branch paint check list.
                    else:
                        # Loops through total length of the branch list.
                        for number in range(len(list_branches)):
                            # Checks if the branch variable value is equal to the value in the branch paint check list.
                            if branch in branch_paint_check[number]:
                                # Branch paint is the current number in branch paint list.
                                paint_branch = branch_paint[number]

                    # Runs the next task.
                    self.build_headers(paint_branch, branch, newline)

        # Algorithm to build all the given headers.
        def build_headers(self, paint_branch, branch, newline):
            # Checks if branch key in branch list has any value.
            if branches[branch]:
                # Loops through all headers in the header list.
                for header in branches[branch]:
                    # Resets the paint after every loop.
                    paint_header = ""

                    # Checks if "all" is in header paint check list.
                    if "all" in header_paint_check:
                        # Header paint is the current number of "all" in headers list.
                        paint_header = header_paint[list_headers.index("all")]
                    # If "all" is not in header paint check list.
                    else:
                        # Loops through total length of the header list.
                        for number in range(len(list_headers)):
                            # Checks if the header variable value is equal to the value in the header paint check list.
                            if header in branches.get(header_paint_check[number]):
                                # Header paint is the current number in header paint list.
                                paint_header = header_paint[number]

                    # Uses prefix with the end line symbol and appends the output to the paper list.
                    paper.append(paint_header + newline + header + " " + self.paint_clear + paint_branch +
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
                    paint_module = ""

                    # Adds the current decider value by 1.
                    decider = decider + 1

                    # Loops through total length of the module list.
                    for number in range(len(list_modules)):
                        # Checks if the current module variable value is equal to the value in the module list.
                        if list_modules[number] == module:
                            # Module paint is the current value in module paint list.
                            paint_module = module_paint[number]

                    # Checks if "all" is in module paint check list.
                    if "all" in module_paint_check:
                        # Gets the value of the "key".
                        key = module_paint_check.get("all")

                        # Checks if the key is equal to "all" string.
                        if key == "all":
                            # Module paint is the current number of "all" in modules list.
                            paint_module = module_paint[list_modules.index("all")]
                        # If the key is not equal to "all" string.
                        else:
                            # Tries the loop until KeyError exception.
                            try:
                                # Loops through all elements inside the branches > header dictionary.
                                for _ in branches[key][header]:
                                    # Module paint is the current number of "all" in modules list.
                                    paint_module = module_paint[list_modules.index("all")]
                            # Loops until KeyError.
                            except KeyError:
                                # Passes after KeyError.
                                pass

                    # Checks "decider" number is equal to the length of the total number of branch header entries.
                    if decider == len(branches[branch][header]):
                        # Uses prefix with the end line symbol and appends the output to the paper list.
                        paper.append(paint_branch + utility.branching("module_end", "") + " " + self.paint_clear +
                                     paint_module + module + self.paint_clear)
                    # If "decider" number is not equal to the length of the total number of branch header entries.
                    else:
                        # Uses prefix with the multi line symbol and appends the output to the paper list.
                        paper.append(paint_branch + utility.branching("module_multi", "") + " " +
                                     self.paint_clear + paint_module + module + self.paint_clear)

                    # Runs the next task.
                    self.build_subjects(paint_branch, branch, header, module)

        # Algorithm to build all the given subjects.
        def build_subjects(self, paint_branch, branch, header, module):
            # Checks if module key in branch list has any value.
            if branches[branch][header][module]:
                # Decider decides when to use the straight and end line symbol.
                decider1 = 0
                decider2 = 0

                # Loops through all subjects in the subject list.
                for subject in branches[branch][header][module]:
                    # Resets the paint after every loop.
                    paint_subject = ""

                    # Loops through total length of the subject list.
                    for number in range(len(list_subjects)):
                        # Checks if the current subject variable value is equal to the value in the subject list.
                        if list_subjects[number] == subject:
                            # Subject paint is the current value in subject paint list.
                            paint_subject = subject_paint[number]

                    # Checks if "all" is in subject paint check list.
                    if "all" in subject_paint_check:
                        # Gets the value of the "key".
                        key = subject_paint_check.get("all")

                        # Checks if the key is equal to "all" string.
                        if key == "all":
                            # Subject paint is the current number of "all" in subjects list.
                            paint_subject = subject_paint[list_subjects.index("all")]
                        # If the key is not equal to "all" string.
                        else:
                            # Tries the loop until KeyError exception.
                            try:
                                # Loops through all elements inside the branches > header > module dictionary.
                                for _ in branches[key][header][module]:
                                    # Subject paint is the current number of "all" in subjects list.
                                    paint_subject = subject_paint[list_subjects.index("all")]
                            # Loops until KeyError.
                            except KeyError:
                                # Passes after KeyError.
                                pass

                    # Checks current module value is equal to the value of the last module in the list.
                    if module == list(dict.keys(branches[branch][header]))[-1]:
                        # Extender is equal to one space.
                        extender = " "

                        # Adds the current decider value by 1.
                        decider1 = decider1 + 1

                        # Checks "decider" number is equal to the length of the total number of branch module entries.
                        if decider1 == len(branches[branch][header][module]):
                            # Uses prefix with the end line symbol and appends the output to the paper list.
                            paper.append(paint_branch + utility.branching("subject_end", extender) + " " +
                                         self.paint_clear + paint_subject + subject + self.paint_clear)
                        # If "decider" number is not equal to the length of the total number of branch module entries.
                        else:
                            # Uses prefix with the multi line symbol and appends the output to the paper list.
                            paper.append(paint_branch + utility.branching("subject_multi", extender) + " " +
                                         self.paint_clear + paint_subject + subject + self.paint_clear)
                    # If current module value is not equal to the value of the last module in the list.
                    else:
                        # Extender is equal to one straight line.
                        extender = "┃"

                        # Adds the current decider value by 1.
                        decider2 = decider2 + 1

                        # Checks "decider" number is equal to the length of the total number of branch module entries.
                        if decider2 == len(branches[branch][header][module]):
                            # Uses prefix with the end line symbol and appends the output to the paper list.
                            paper.append(paint_branch + utility.branching("subject_end_last", extender) + " " +
                                         self.paint_clear + paint_subject + subject + self.paint_clear)
                        # If "decider" number is not equal to the length of the total number of branch module entries.
                        else:
                            # Uses prefix with the multi line symbol and appends the output to the paper list.
                            paper.append(paint_branch + utility.branching("subject_multi_last", extender) + " " +
                                         self.paint_clear + paint_subject + subject + self.paint_clear)

                    # Runs the next task.
                    self.build_objects(paint_branch, branch, header, module, subject)

        # Algorithm to build all the given objects.
        def build_objects(self, paint_branch, branch, header, module, subject):
            # Checks if subject key in branch list has any value.
            if branches[branch][header][module][subject]:
                # Decider decides when to use the straight and end line symbol.
                decider = 0

                # Loops through all objects in the object list.
                for obj in branches[branch][header][module][subject]:
                    # Resets the paint after every loop.
                    paint_object = ""

                    # Loops through total length of the object list.
                    for number in range(len(list_objects)):
                        # Checks if the current object variable value is equal to the value in the object list.
                        if list_objects[number] == obj:
                            # Object paint is the current value in object paint list.
                            paint_object = object_paint[number]

                    # Checks if "all" is in object paint check list.
                    if "all" in object_paint_check:
                        # Gets the value of the "key".
                        key = object_paint_check.get("all")

                        # Checks if the key is equal to "all" string.
                        if key == "all":
                            # Object paint is the current number of "all" in objects list.
                            paint_object = object_paint[list_objects.index("all")]
                        # If the key is not equal to "all" string.
                        else:
                            # Tries the loop until KeyError exception.
                            try:
                                # Loops through all elements inside the branches > header > module > subject dictionary.
                                for _ in branches[key][header][module][subject]:
                                    # Object paint is the current number of "all" in objects list.
                                    paint_object = object_paint[list_objects.index("all")]
                            # Loops until KeyError.
                            except KeyError:
                                # Passes after KeyError.
                                pass

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
                                # Extender is equal to one space.
                                extender = " "
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

                    # Checks "decider" number is equal to the length of the total number of branch subject entries.
                    if decider == len(branches[branch][header][module][subject]):
                        # Uses prefix with the end line symbol and appends the output to the paper list.
                        paper.append(paint_branch + utility.branching("object_end", extender) + " " +
                                     self.paint_clear + paint_object + obj + self.paint_clear)
                    # If "decider" number is not equal to the length of the total number of branch subject entries.
                    else:
                        # Uses prefix with the multi line symbol and appends the output to the paper list.
                        paper.append(paint_branch + utility.branching("object_multi", extender) + " " +
                                     self.paint_clear + paint_object + obj + self.paint_clear)

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

    add.name("Computer Branch")
    add.header("Computer Branch", "Gaming")
    add.module("Computer Branch", "Gaming", "Monitors")
    add.module("Computer Branch", "Gaming", "Keyboard & Mouse")
    add.subject("Computer Branch", "Gaming", "Monitors", "LG")
    add.subject("Computer Branch", "Gaming", "Keyboard & Mouse", "Steel Series")
    add.subject("Computer Branch", "Gaming", "Keyboard & Mouse", "Razer")
    add.object("Computer Branch", "Gaming", "Monitors", "LG", "LG 27GN850 Ultragear")
    add.object("Computer Branch", "Gaming", "Keyboard & Mouse", "Razer", "Razer Blackwindow Elite")
    add.object("Computer Branch", "Gaming", "Keyboard & Mouse", "Steel Series", "SteelSeries Apex 3")
    add.object("Computer Branch", "Gaming", "Keyboard & Mouse", "Steel Series", "SteelSeries Apex 5")

    set.color.branch("Computer Branch", "blue", "bold", "", "")
    set.color.header("Computer Branch", "magenta", "reversing", "bold", "underline")
    set.color.module("Computer Branch", "Monitors", "yellow", "bold", "", "")
    set.color.module("Computer Branch", "Keyboard & Mouse", "cyan", "underline", "", "")
    set.color.subject("Computer Branch", "Razer", "blue", "underline", "bold", "")
    set.color.subject("Computer Branch", "all", "green", "underline", "bold", "")
    set.color.subject("Computer Branch", "LG", "red", "underline", "bold", "")
    set.color.object("Computer Branch", "SteelSeries Apex 5", "red", "underline", "reversing", "")
    set.color.object("Computer Branch", "LG 27GN850 Ultragear", "cyan", "", "bold", "")

    add.name("Mall")
    add.header("Mall", "Food")
    add.module("Mall", "Food", "Meat")
    add.module("Mall", "Food", "Vegetarian")
    add.module("Mall", "Food", "Vegan")
    add.subject("Mall", "Food", "Meat", "Cow")
    add.subject("Mall", "Food", "Meat", "Pig")
    add.subject("Mall", "Food", "Vegetarian", "Cheese")
    add.subject("Mall", "Food", "Vegetarian", "Milk")
    add.subject("Mall", "Food", "Vegetarian", "Bread")
    add.subject("Mall", "Food", "Vegan", "Vegetables")
    add.object("Mall", "Food", "Meat", "Cow", "Beef")
    add.object("Mall", "Food", "Meat", "Pig", "Pork")
    add.object("Mall", "Food", "Meat", "Pig", "Tail")
    add.object("Mall", "Food", "Vegetarian", "Cheese", "Goat Cheese")
    add.object("Mall", "Food", "Vegetarian", "Cheese", "Blue Cheese")
    add.object("Mall", "Food", "Vegetarian", "Milk", "Cow Milk")
    add.object("Mall", "Food", "Vegetarian", "Bread", "Brown Bread")
    add.object("Mall", "Food", "Vegetarian", "Bread", "White Bread")
    add.object("Mall", "Food", "Vegetarian", "Bread", "Baguette")
    add.object("Mall", "Food", "Vegan", "Vegetables", "Carrot")
    add.object("Mall", "Food", "Vegan", "Vegetables", "Potato")
    add.object("Mall", "Food", "Vegan", "Vegetables", "Onion")
    add.object("Mall", "Food", "Vegan", "Vegetables", "Broccoli")

    set.color.branch("Mall", "magenta", "", "", "")
    set.color.header("Mall", "magenta", "bold", "", "")

    # Bugs with "all" arguments: (Fixing in next few updates.)
    # Bug 1: Bugging on 2 "all" arguments in different branch.
    # set.color.subject("Computer Branch", "all", "green", "underline", "bold", "")
    # set.color.subject("Mall", "all", "blue", "underline", "bold", "")

    # Bug 2: Paints the same modules with same name in other branch too.
    # add.module("Mall", "Food", "Monitors")
    # add.subject("Mall", "Food", "Monitors", "Test")
    # add.object("Mall", "Food", "Monitors", "Test", "123")

    run.display("all")
