# Indev phase - br4nch v1.1.3
# desc - Builder class code clean-up, adding commentary and new sample branch for algorithm testing.


class add:
    def name(self, branch_name):
        get_branch = utility.executor(None, "get_branch")
        get_branch.update({branch_name: {}})

    def header(self, branch_name, header_name):
        get_branch = utility.executor(None, "get_branch")
        get_branch[branch_name].update({header_name: {}})

    def module(self, branch_name, header_name, module_name):
        get_branch = utility.executor(None, "get_branch")
        get_branch[branch_name][header_name].update({module_name: {}})

    def subject(self, branch_name, header_name, module_name, subject_name):
        get_branch = utility.executor(None, "get_branch")
        get_branch[branch_name][header_name][module_name].update({subject_name: {}})

    def object(self, branch_name, header_name, module_name, subject_name, object_name):
        get_branch = utility.executor(None, "get_branch")
        get_branch[branch_name][header_name][module_name][subject_name].update({object_name: {}})


class set:
    class color:
        def branch(self, selected, color, special1, special2, special3):
            paint_branch = utility.painter(None, color.lower(), special1.lower(), special2.lower(), special3.lower())

            add_list_branch = utility.executor(None, "get_list_branches")
            add_list_branch_paint = utility.executor(None, "get_list_branch_paint")

            add_list_branch.append(selected)
            add_list_branch_paint.append(paint_branch)

        def header(self, branch_name, selected, color, special1, special2, special3):
            paint_header = utility.painter(None, color.lower(), special1.lower(), special2.lower(), special3.lower())

            add_list_header = utility.executor(None, "get_list_headers")
            add_header_paint = utility.executor(None, "get_header_paint")

            add_list_header.append(selected)
            add_header_paint.append(paint_header)

        def module(self, branch_name, selected, color, special1, special2, special3):
            paint_module = utility.painter(None, color.lower(), special1.lower(), special2.lower(), special3.lower())

            add_list_module = utility.executor(None, "get_list_modules")
            add_module_paint = utility.executor(None, "get_module_paint")

            add_list_module.append(selected)
            add_module_paint.append(paint_module)

        def subject(self, branch_name, selected, color, special1, special2, special3):
            paint_subject = utility.painter(None, color.lower(), special1.lower(), special2.lower(), special3.lower())

            add_list_subject = utility.executor(None, "get_list_subjects")
            add_subject_paint = utility.executor(None, "get_subject_paint")

            add_list_subject.append(selected)
            add_subject_paint.append(paint_subject)

        def object(self, branch_name, selected, color, special1, special2, special3):
            paint_object = utility.painter(None, color.lower(), special1.lower(), special2.lower(), special3.lower())

            add_list_object = utility.executor(None, "get_list_objects")
            add_object_paint = utility.executor(None, "get_object_paint")

            add_list_object.append(selected)
            add_object_paint.append(paint_object)


class run:
    def branch(self, branch_name):
        utility.builder(None, branch_name)
        utility.printer(None)
        paper.clear()


class utility:
    def manager(self):
        utility.executor(None, "construction")

    def executor(self, action):
        global branches, names, headers, modules, subjects, objects
        global list_branches, list_headers, list_modules, list_subjects, list_objects
        global list_branch_paint, header_paint, module_paint, subject_paint, object_paint
        global paper

        if action == "construction":
            branches = {}
            names = []
            headers = []
            modules = []
            subjects = []
            objects = []

            list_branches = []
            list_headers = []
            list_modules = []
            list_subjects = []
            list_objects = []
            list_branch_paint = []
            header_paint = []
            module_paint = []
            subject_paint = []
            object_paint = []

            paper = []

        if action:
            branch_name_list = ["get_branch", "get_names", "get_headers", "get_modules", "get_subjects", "get_objects"]
            branch_action_list = [branches, names, headers, modules, subjects, objects]

            for branch in branches:
                for header in branches[branch]:
                    for module in branches[branch][header]:
                        for subject in branches[branch][header][module]:
                            for obj in branches[branch][header][module][subject]:
                                names.append(branch)
                                headers.append(header)
                                modules.append(module)
                                subjects.append(subject)
                                objects.append(obj)

            for selected in range(6):
                if action == branch_name_list[selected]:
                    return branch_action_list[selected]

        paint_name_list = ["get_list_branches", "get_list_headers", "get_list_modules", "get_list_subjects",
                           "get_list_objects",
                           "get_list_branch_paint", "get_header_paint", "get_module_paint", "get_subject_paint",
                           "get_object_paint"]
        paint_action_list = [list_branches, list_headers, list_modules, list_subjects, list_objects,
                             list_branch_paint, header_paint, module_paint, subject_paint, object_paint]

        for selected in range(10):
            if action == paint_name_list[selected]:
                return paint_action_list[selected]

        print_list = ["get_paper"]
        print_action_list = [paper]

        for selected in range(1):
            if action == print_list[selected]:
                return print_action_list[selected]

    def branching(self, action, extender):
        space_x3 = " " * 3

        branching_header_end = "\n╻"
        branching_module_multi = "┃\n┣━━"
        branching_module_end = "┃\n┗━━"
        branching_subject_multi = extender + space_x3 + "┃\n" + extender + space_x3 + "┣━━"
        branching_subject_multi_last = extender + space_x3 + "┃\n" + extender + space_x3 + "┣━━"
        branching_subject_end = extender + space_x3 + "┃\n" + extender + space_x3 + "┗━━"
        branching_subject_end_last = extender + space_x3 + "┃\n" + extender + space_x3 + "┗━━"
        branching_object_multi = extender + space_x3 + "┃\n" + extender + space_x3 + "┣━━"
        branching_object_end = extender + space_x3 + "┃\n" + extender + space_x3 + "┗━━"

        branching_action_list = [branching_header_end, branching_module_multi, branching_module_end,
                                 branching_subject_multi,
                                 branching_subject_multi_last, branching_subject_end, branching_subject_end_last,
                                 branching_object_multi,
                                 branching_object_end]

        branching_name_list = ["header_end", "module_multi", "module_end", "subject_multi", "subject_multi_last",
                               "subject_end", "subject_end_last", "object_multi", "object_end"]

        if action:
            for selected in range(9):
                if action == branching_name_list[selected]:
                    return branching_action_list[selected]

    def painter(self, color, special1, special2, special3):
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

        colors_id = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white", "clear"]
        colors = [black, red, green, yellow, blue, magenta, cyan, white, clear]

        specials_id = ["bold", "underline", "reversing"]
        specials = [bold, underline, reversing]

        selected_color = ""
        selected_special1 = ""
        selected_special2 = ""
        selected_special3 = ""

        if color:
            for selected in range(9):
                if color == colors_id[selected]:
                    selected_color = colors[selected]

        if special1 or special2 or special3:
            for selected in range(3):
                if special1 == specials_id[selected]:
                    selected_special1 = specials[selected]
                if special2 == specials_id[selected]:
                    selected_special2 = specials[selected]
                if special3 == specials_id[selected]:
                    selected_special3 = specials[selected]

        return selected_color + selected_special1 + selected_special2 + selected_special3

    # Uses algorithms to build the final branch result.
    class builder:
        # Loads all required variables.
        def __init__(self, branch_name):
            # Variable to clear all paint.
            self.paint_clear = utility.painter(None, "clear", None, None, None)

            # Gets the branch dict and stores it into a variable.
            self.get_branch = utility.executor(None, "get_branch")

            # Runs the next task.
            self.build_branches(branch_name)

        # Algorithm to build all the given branches.
        def build_branches(self, branch_name):
            # Checks if the branch list has any value.
            if self.get_branch:
                # "stop" is equal to false.
                stop = False

                # Loops through all branches in the branch list.
                for branch in self.get_branch:
                    # Resets the paint after every loop.
                    paint_branch = ""

                    # Clears the newline variable.
                    newline = ""

                    # Checks if there are multiple branches in the list.
                    if len(list(dict.keys(self.get_branch))) > 1:
                        # Passes through every branch except first branch.
                        if not branch == list(dict.keys(self.get_branch))[0]:
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

                    # Loops through total length of the branch list.
                    for number in range(len(list_branches)):
                        # Checks if the current branch variable value is equal to the value in the branch list.
                        if list_branches[number] == branch:
                            # Branch paint is the current number in branch paint list.
                            paint_branch = list_branch_paint[number]

                    # Runs the next task.
                    self.build_headers(paint_branch, branch, newline)

        # Algorithm to build all the given headers.
        def build_headers(self, paint_branch, branch, newline):
            # Checks if branch key in branch list has any value.
            if self.get_branch[branch]:
                # Loops through all headers in the header list.
                for header in self.get_branch[branch]:
                    # Resets the paint after every loop.
                    paint_header = ""

                    # Loops through total length of the header list.
                    for number in range(len(list_headers)):
                        # Checks if the current header variable value is equal to the value in the header list.
                        if list_headers[number] == header:
                            # Header paint is the current number in header paint list.
                            paint_header = header_paint[number]

                    # Uses prefix with the end line symbol and appends the output to the paper list.
                    paper.append(paint_header + newline + header + " " + self.paint_clear + paint_branch +
                                 utility.branching(None, "header_end", "") + self.paint_clear)

                    # Runs the next task.
                    self.build_modules(paint_branch, branch, header)

        # Algorithm to build all the given modules.
        def build_modules(self, paint_branch, branch, header):
            # Checks if header key in branch list has any value.
            if self.get_branch[branch][header]:
                # Decider decides when to use the straight and end line symbol.
                decider = 0

                # Loops through all modules in the module list.
                for module in self.get_branch[branch][header]:
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

                    # Checks if "all" in paint argument.
                    if "all" in list_modules:
                        # Gets number where "all" is in modules list.
                        number = list_modules.index("all")
                        # Module paint is the current number in module paint list.
                        paint_module = module_paint[number]

                    # Checks "decider" number is equal to the length of the total number of branch header entries.
                    if decider == len(self.get_branch[branch][header]):
                        # Uses prefix with the end line symbol and appends the output to the paper list.
                        paper.append(paint_branch + utility.branching(None, "module_end", "") + " " + self.paint_clear +
                                     paint_module + module + self.paint_clear)
                    # If "decider" number is not equal to the length of the total number of branch header entries.
                    else:
                        # Uses prefix with the multi line symbol and appends the output to the paper list.
                        paper.append(paint_branch + utility.branching(None, "module_multi", "") + " " +
                                     self.paint_clear + paint_module + module + self.paint_clear)

                    # Runs the next task.
                    self.build_subjects(paint_branch, branch, header, module)

        # Algorithm to build all the given subjects.
        def build_subjects(self, paint_branch, branch, header, module):
            # Checks if module key in branch list has any value.
            if self.get_branch[branch][header][module]:
                # Decider decides when to use the straight and end line symbol.
                decider1 = 0
                decider2 = 0

                # Loops through all subjects in the subject list.
                for subject in self.get_branch[branch][header][module]:
                    # Resets the paint after every loop.
                    paint_subject = ""

                    # Loops through total length of the subject list.
                    for number in range(len(list_subjects)):
                        # Checks if the current subject variable value is equal to the value in the subject list.
                        if list_subjects[number] == subject:
                            # Subject paint is the current value in subject paint list.
                            paint_subject = subject_paint[number]

                    # Checks if "all" in paint argument.
                    if "all" in list_subjects:
                        # Gets number where "all" is in subject list.
                        all_num = list_subjects.index("all")
                        # Subject paint is the current number in subject paint list.
                        paint_subject = subject_paint[all_num]

                    # Checks current module value is equal to the value of the last module in the list.
                    if module == list(dict.keys(self.get_branch[branch][header]))[-1]:
                        # Extender is equal to one space.
                        extender = " "

                        # Adds the current decider value by 1.
                        decider1 = decider1 + 1

                        # Checks "decider" number is equal to the length of the total number of branch module entries.
                        if decider1 == len(self.get_branch[branch][header][module]):
                            # Uses prefix with the end line symbol and appends the output to the paper list.
                            paper.append(paint_branch + utility.branching(None, "subject_end", extender) + " " +
                                         self.paint_clear + paint_subject + subject + self.paint_clear)
                        # If "decider" number is not equal to the length of the total number of branch module entries.
                        else:
                            # Uses prefix with the multi line symbol and appends the output to the paper list.
                            paper.append(paint_branch + utility.branching(None, "subject_multi", extender) + " " +
                                         self.paint_clear + paint_subject + subject + self.paint_clear)
                    # If current module value is not equal to the value of the last module in the list.
                    else:
                        # Extender is equal to one straight line.
                        extender = "┃"

                        # Adds the current decider value by 1.
                        decider2 = decider2 + 1

                        # Checks "decider" number is equal to the length of the total number of branch module entries.
                        if decider2 == len(self.get_branch[branch][header][module]):
                            # Uses prefix with the end line symbol and appends the output to the paper list.
                            paper.append(paint_branch + utility.branching(None, "subject_end_last", extender) + " " +
                                         self.paint_clear + paint_subject + subject + self.paint_clear)
                        # If "decider" number is not equal to the length of the total number of branch module entries.
                        else:
                            # Uses prefix with the multi line symbol and appends the output to the paper list.
                            paper.append(paint_branch + utility.branching(None, "subject_multi_last", extender) + " " +
                                         self.paint_clear + paint_subject + subject + self.paint_clear)

                    # Runs the next task.
                    self.build_objects(paint_branch, branch, header, module, subject)

        # Algorithm to build all the given objects.
        def build_objects(self, paint_branch, branch, header, module, subject):
            # Checks if subject key in branch list has any value.
            if self.get_branch[branch][header][module][subject]:
                # Decider decides when to use the straight and end line symbol.
                decider = 0

                # Loops through all objects in the object list.
                for obj in self.get_branch[branch][header][module][subject]:
                    # Resets the paint after every loop.
                    paint_object = ""

                    # Loops through total length of the object list.
                    for number in range(len(list_objects)):
                        # Checks if the current object variable value is equal to the value in the object list.
                        if list_objects[number] == obj:
                            # Object paint is the current value in object paint list.
                            paint_object = object_paint[number]

                    # Checks if "all" in paint argument.
                    if "all" in list_objects:
                        # Gets number where "all" is in object list.
                        all_num = list_objects.index("all")
                        # Object paint is the current number in object paint list.
                        paint_object = object_paint[all_num]

                    # Assigns the last module in the header list to a variable.
                    last_module = list(dict.keys(self.get_branch[branch][header]))[-1]
                    # Assigns the last subject in the last_module list to a variable.
                    last_subject = list(dict.keys(self.get_branch[branch][header][last_module]))[-1]
                    # Assigns the last object in the last_subject list to a variable.
                    last_object = list(dict.keys(self.get_branch[branch][header][last_module][last_subject]))[-1]

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
                    if decider == len(self.get_branch[branch][header][module][subject]):
                        # Uses prefix with the end line symbol and appends the output to the paper list.
                        paper.append(paint_branch + utility.branching(None, "object_end", extender) + " " +
                                     self.paint_clear + paint_object + obj + self.paint_clear)
                    # If "decider" number is not equal to the length of the total number of branch subject entries.
                    else:
                        # Uses prefix with the multi line symbol and appends the output to the paper list.
                        paper.append(paint_branch + utility.branching(None, "object_multi", extender) + " " +
                                     self.paint_clear + paint_object + obj + self.paint_clear)

    def printer(self):
        paper = utility.executor(None, "get_paper")

        for ink in paper:
            print(ink)


# Running tasks manually. (Will be removed once it leaves the indev phase.)
if __name__ == '__main__':
    utility.manager(None)

    add.name(None, "Computer Branch")
    add.header(None, "Computer Branch", "Gaming")
    add.module(None, "Computer Branch", "Gaming", "Monitors")
    add.module(None, "Computer Branch", "Gaming", "Keyboard & Mouse")
    add.subject(None, "Computer Branch", "Gaming", "Monitors", "LG")
    add.subject(None, "Computer Branch", "Gaming", "Keyboard & Mouse", "Steel Series")
    add.subject(None, "Computer Branch", "Gaming", "Keyboard & Mouse", "Razer")
    add.object(None, "Computer Branch", "Gaming", "Monitors", "LG", "LG 27GN850 Ultragear")
    add.object(None, "Computer Branch", "Gaming", "Keyboard & Mouse", "Razer", "Razer Blackwindow Elite")
    add.object(None, "Computer Branch", "Gaming", "Keyboard & Mouse", "Steel Series", "SteelSeries Apex 3")
    add.object(None, "Computer Branch", "Gaming", "Keyboard & Mouse", "Steel Series", "SteelSeries Apex 5")

    set.color.branch(None, "Computer Branch", "blue", "bold", "", "")
    set.color.header(None, "Computer Branch", "Gaming", "magenta", "reversing", "bold", "underline")
    set.color.module(None, "Computer Branch", "Monitors", "yellow", "bold", "", "")
    set.color.module(None, "Computer Branch", "Keyboard & Mouse", "cyan", "underline", "", "")
    set.color.subject(None, "Computer Branch", "Razer", "blue", "underline", "bold", "")
    set.color.subject(None, "Computer Branch", "all", "green", "underline", "bold", "")
    set.color.subject(None, "Computer Branch", "LG", "red", "underline", "bold", "")
    set.color.object(None, "Computer Branch", "SteelSeries Apex 5", "red", "underline", "reversing", "")
    set.color.object(None, "Computer Branch", "LG 27GN850 Ultragear", "cyan", "", "bold", "")

    add.name(None, "Mall")
    add.header(None, "Mall", "Food")
    add.module(None, "Mall", "Food", "Meat")
    add.module(None, "Mall", "Food", "Vegetarian")
    add.module(None, "Mall", "Food", "Vegan")
    add.subject(None, "Mall", "Food", "Meat", "Cow")
    add.subject(None, "Mall", "Food", "Meat", "Pig")
    add.subject(None, "Mall", "Food", "Vegetarian", "Cheese")
    add.subject(None, "Mall", "Food", "Vegetarian", "Milk")
    add.subject(None, "Mall", "Food", "Vegetarian", "Bread")
    add.subject(None, "Mall", "Food", "Vegan", "Vegetables")
    add.object(None, "Mall", "Food", "Meat", "Cow", "Beef")
    add.object(None, "Mall", "Food", "Meat", "Pig", "Pork")
    add.object(None, "Mall", "Food", "Meat", "Pig", "Tail")
    add.object(None, "Mall", "Food", "Vegetarian", "Cheese", "Goat Cheese")
    add.object(None, "Mall", "Food", "Vegetarian", "Cheese", "Blue Cheese")
    add.object(None, "Mall", "Food", "Vegetarian", "Milk", "Cow Milk")
    add.object(None, "Mall", "Food", "Vegetarian", "Bread", "Brown Bread")
    add.object(None, "Mall", "Food", "Vegetarian", "Bread", "White Bread")
    add.object(None, "Mall", "Food", "Vegetarian", "Bread", "Baguette")
    add.object(None, "Mall", "Food", "Vegan", "Vegetables", "Carrot")
    add.object(None, "Mall", "Food", "Vegan", "Vegetables", "Potato")
    add.object(None, "Mall", "Food", "Vegan", "Vegetables", "Onion")
    add.object(None, "Mall", "Food", "Vegan", "Vegetables", "Broccoli")

    set.color.branch(None, "Mall", "magenta", "", "", "")
    set.color.header(None, "Mall", "Food", "magenta", "bold", "", "")

    utility.builder("all")
    utility.printer(None)
    paper.clear()
