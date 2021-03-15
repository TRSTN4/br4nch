# Indev phase - br4nch v1.1.1
# desc - Added algorithm class and added a modified version of the old test_structure function to it.


class add:
    def name(self, branch_name):
        get_branch = utility.executor("", "get_branch")
        get_branch.update({branch_name: {}})

    def header(self, branch_name, header_name):
        get_branch = utility.executor("", "get_branch")
        get_branch[branch_name].update({header_name: {}})

    def module(self, branch_name, header_name, module_name):
        get_branch = utility.executor("", "get_branch")
        get_branch[branch_name][header_name].update({module_name: {}})

    def subject(self, branch_name, header_name, module_name, subject_name):
        get_branch = utility.executor("", "get_branch")
        get_branch[branch_name][header_name][module_name].update({subject_name: {}})

    def object(self, branch_name, header_name, module_name, subject_name, object_name):
        get_branch = utility.executor("", "get_branch")
        get_branch[branch_name][header_name][module_name][subject_name].update({object_name: {}})


class set:
    class color:
        def branch(self, selected, color, special1, special2, special3):
            paint_branch = utility.painter("", color.lower(), special1.lower(), special2.lower(), special3.lower())

            add_selected_branch = utility.executor("", "get_selected_branches")
            add_branch_paint = utility.executor("", "get_branch_paint")

            add_selected_branch.append(selected)
            add_branch_paint.append(paint_branch)

        def header(self, branch_name, selected, color, special1, special2, special3):
            paint_header = utility.painter("", color.lower(), special1.lower(), special2.lower(), special3.lower())

            add_selected_header = utility.executor("", "get_selected_headers")
            add_header_paint = utility.executor("", "get_header_paint")

            add_selected_header.append(selected)
            add_header_paint.append(paint_header)

        def module(self, branch_name, selected, color, special1, special2, special3):
            paint_module = utility.painter("", color.lower(), special1.lower(), special2.lower(), special3.lower())

            add_selected_module = utility.executor("", "get_selected_modules")
            add_module_paint = utility.executor("", "get_module_paint")

            add_selected_module.append(selected)
            add_module_paint.append(paint_module)

        def subject(self, branch_name, selected, color, special1, special2, special3):
            paint_subject = utility.painter("", color.lower(), special1.lower(), special2.lower(), special3.lower())

            add_selected_subject = utility.executor("", "get_selected_subjects")
            add_subject_paint = utility.executor("", "get_subject_paint")

            add_selected_subject.append(selected)
            add_subject_paint.append(paint_subject)

        def object(self, branch_name, selected, color, special1, special2, special3):
            paint_object = utility.painter("", color.lower(), special1.lower(), special2.lower(), special3.lower())

            add_selected_object = utility.executor("", "get_selected_objects")
            add_object_paint = utility.executor("", "get_object_paint")

            add_selected_object.append(selected)
            add_object_paint.append(paint_object)


class utility:
    def executor(self, action):
        global branch, names, headers, modules, subjects, objects
        global selected_branches, selected_headers, selected_modules, selected_subjects, selected_objects
        global branch_paint, header_paint, module_paint, subject_paint, object_paint

        if action == "construction":
            branch = {}
            names = []
            headers = []
            modules = []
            subjects = []
            objects = []

            selected_branches = []
            selected_headers = []
            selected_modules = []
            selected_subjects = []
            selected_objects = []
            branch_paint = []
            header_paint = []
            module_paint = []
            subject_paint = []
            object_paint = []

        if action:
            branch_name_list = ["get_branch", "get_names", "get_headers", "get_modules", "get_subjects", "get_objects"]
            branch_action_list = [branch, names, headers, modules, subjects, objects]

            for name in branch:
                for header in branch[name]:
                    for module in branch[name][header]:
                        for subject in branch[name][header][module]:
                            for obj in branch[name][header][module][subject]:
                                names.append(name)
                                headers.append(header)
                                modules.append(module)
                                subjects.append(subject)
                                objects.append(obj)

            for selected in range(6):
                if action == branch_name_list[selected]:
                    return branch_action_list[selected]

        paint_name_list = ["get_selected_branches", "get_selected_headers", "get_selected_modules", "get_selected_subjects",
                           "get_selected_objects", "get_branch_paint", "get_header_paint", "get_module_paint",
                           "get_subject_paint", "get_object_paint"]
        paint_action_list = [selected_branches, selected_headers, selected_modules, selected_subjects, selected_objects,
                             branch_paint, header_paint, module_paint, subject_paint, object_paint]

        for selected in range(10):
            if action == paint_name_list[selected]:
                return paint_action_list[selected]

    def branching(self, action, extender):
        space_x3 = " "*3

        branching_header_end = "\n╻"
        branching_module_extend = "┃\n┣━━"
        branching_module_end = "┃\n┗━━"
        branching_subject_extend = extender + space_x3 + "┃\n" + extender + space_x3 + "┣━━"
        branching_subject_extend_last = extender + space_x3 + "┃\n" + extender + space_x3 + "┣━━"
        branching_subject_end = extender + space_x3 + "┃\n" + extender + space_x3 + "┗━━"
        branching_subject_end_last = extender + space_x3 + "┃\n" + extender + space_x3 + "┗━━"
        branching_object_extend = extender + space_x3 + "┃\n" + extender + space_x3 + "┣━━"
        branching_object_end = extender + space_x3 + "┃\n" + extender + space_x3 + "┗━━"

        branching_action_list = [branching_header_end, branching_module_extend, branching_module_end, branching_subject_extend,
                                 branching_subject_extend_last, branching_subject_end, branching_subject_end_last, branching_object_extend,
                                 branching_object_end]

        branching_name_list = ["header_end", "module_extend", "module_end", "subject_extend", "subject_extend_last",
                               "subject_end", "subject_end_last", "object_extend", "object_end"]

        if action:
            for selected in range(9):
                if action == branching_name_list[selected]:
                    return branching_action_list[selected]

    def painter(self, color, special1, special2, special3):
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

    def initiate(self):
        utility.executor("", "construction")


class algorithm:
    class branch:
        def __init__(self):
            global end

            end = 0

            self.all_list = ["all", "", " "]

            self.paint_clear = utility.painter("", "clear", "", "", "")
            self.branch_paint = utility.executor("", "get_branch_paint")

            self.selected_branches = utility.executor("", "get_selected_branches")

            self.get_objects = utility.executor("", "get_objects")
            self.get_subjects = utility.executor("", "get_subjects")
            self.get_modules = utility.executor("", "get_modules")
            self.get_headers = utility.executor("", "get_headers")
            self.get_names = utility.executor("", "get_names")
            self.get_branch = utility.executor("", "get_branch")

            self.run_names()

        def run_names(self):
            global end

            if self.get_branch:
                for name in self.get_branch:
                    paint_branch = ""

                    selected_branches = utility.executor("", "get_selected_branches")
                    branch_paint = utility.executor("", "get_branch_paint")

                    for selected_branch in range(len(selected_branches)):
                        if selected_branches[selected_branch] == name:
                            paint_branch = branch_paint[selected_branch]

                    self.run_headers(paint_branch, name)

        def run_headers(self, paint_branch, name):
            global end

            if self.get_branch[name]:
                for header in self.get_branch[name]:
                    paint_header = ""

                    selected_headers = utility.executor("", "get_selected_headers")
                    header_paint = utility.executor("", "get_header_paint")

                    for selected_header in range(len(selected_headers)):
                        if selected_headers[selected_header] == header:
                            paint_header = header_paint[selected_header]

                    print(paint_header + header, self.paint_clear + paint_branch + utility.branching("", "header_end", "") + self.paint_clear)

                    self.run_modules(paint_branch, name, header)

        def run_modules(self, paint_branch, name, header):
            global end

            if self.get_branch[name][header]:
                for module in self.get_branch[name][header]:
                    paint_module = ""
                    lenght = len(self.get_branch[name][header])
                    end = end + 1

                    selected_modules = utility.executor("", "get_selected_modules")
                    module_paint = utility.executor("", "get_module_paint")

                    for selected_module in range(len(selected_modules)):
                        if selected_modules[selected_module] == module:
                            paint_module = module_paint[selected_module]

                    for x in self.all_list:
                        if x in selected_modules:
                            all_num = selected_modules.index(x)
                            paint_module = module_paint[all_num]

                    if end == lenght:
                        print(paint_branch + utility.branching("", "module_end", ""), self.paint_clear + paint_module + module + self.paint_clear)
                    else:
                        print(paint_branch + utility.branching("", "module_extend", ""), self.paint_clear + paint_module + module + self.paint_clear)

                    self.run_subjects(paint_branch, name, header, module)

        def run_subjects(self, paint_branch, name, header, module):
            global end

            if self.get_branch[name][header][module]:
                end1 = 0
                end2 = 0
                for subject in self.get_branch[name][header][module]:
                    paint_subject = ""
                    end = 1
                    end = end + 1

                    selected_subjects = utility.executor("", "get_selected_subjects")
                    subject_paint = utility.executor("", "get_subject_paint")

                    for selected_subject in range(len(selected_subjects)):
                        if selected_subjects[selected_subject] == subject:
                            paint_subject = subject_paint[selected_subject]

                    for x in self.all_list:
                        if x in selected_subjects:
                            all_num = selected_subjects.index(x)
                            paint_subject = subject_paint[all_num]

                    if module == self.get_modules[-1]:
                        extender = " "
                        lenght1 = len(self.get_branch[name][header][module])
                        end1 = end1 + 1

                        if end1 == lenght1:
                            print(paint_branch + utility.branching("", "subject_end", extender), self.paint_clear + paint_subject + subject + self.paint_clear)
                        else:
                            print(paint_branch + utility.branching("", "subject_extend", extender), self.paint_clear + paint_subject + subject + self.paint_clear)
                    else:
                        extender = "┃"
                        lenght2 = len(self.get_branch[name][header][module])
                        end2 = end2 + 1

                        if end2 == lenght2:
                            print(paint_branch + utility.branching("", "subject_end_last", extender), self.paint_clear + paint_subject + subject + self.paint_clear)
                        else:
                            print(paint_branch + utility.branching("", "subject_extend_last", extender), self.paint_clear + paint_subject + subject + self.paint_clear)

                    self.run_objects(paint_branch, name, header, module, subject)

        def run_objects(self, paint_branch, name, header, module, subject):
            global end

            if self.get_branch[name][header][module][subject]:
                end = 0
                for obj in self.get_branch[name][header][module][subject]:
                    paint_object = ""
                    lenght = len(self.get_branch[name][header][module][subject])
                    end = end + 1

                    selected_objects = utility.executor("", "get_selected_objects")
                    object_paint = utility.executor("", "get_object_paint")

                    for selected_object in range(len(selected_objects)):
                        if selected_objects[selected_object] == obj:
                            paint_object = object_paint[selected_object]

                    for x in self.all_list:
                        if x in selected_objects:
                            all_num = selected_objects.index(x)
                            paint_object = object_paint[all_num]

                    if not obj == self.get_objects[-1]:
                        if module == self.get_modules[-1]:
                            if subject == self.get_subjects[-1]:
                                extender = " "
                            else:
                                extender = " "*4 + "┃"
                        else:
                            extender = "┃" + " "*4
                    else:
                        extender = " "*5

                    if end == lenght:
                        print(paint_branch + utility.branching("", "object_end", extender), self.paint_clear + paint_object + obj + self.paint_clear)
                    else:
                        print(paint_branch + utility.branching("", "object_extend", extender), self.paint_clear + paint_object + obj + self.paint_clear)


if __name__ == '__main__':
    utility.initiate("")

    add.name("", "Computer Branch")
    add.header("", "Computer Branch", "Gaming")
    add.module("", "Computer Branch", "Gaming", "Monitors")
    add.module("", "Computer Branch", "Gaming", "Keyboard & Mouse")
    add.subject("", "Computer Branch", "Gaming", "Monitors", "LG")
    add.subject("", "Computer Branch", "Gaming", "Keyboard & Mouse", "Steel Series")
    add.subject("", "Computer Branch", "Gaming", "Keyboard & Mouse", "Razer")
    add.object("", "Computer Branch", "Gaming", "Monitors", "LG", "LG 27GN850 Ultragear")
    add.object("", "Computer Branch", "Gaming", "Keyboard & Mouse", "Razer", "Razer Blackwindow Elite")
    add.object("", "Computer Branch", "Gaming", "Keyboard & Mouse", "Steel Series", "SteelSeries Apex 3")
    add.object("", "Computer Branch", "Gaming", "Keyboard & Mouse", "Steel Series", "SteelSeries Apex 5")

    set.color.branch("", "Computer Branch", "blue", "bold", "", "")
    set.color.header("", "Computer Branch", "Gaming", "magenta", "reversing", "bold", "underline")
    set.color.module("", "Computer Branch", "Monitors", "yellow", "bold", "", "")
    set.color.module("", "Computer Branch", "Keyboard & Mouse", "cyan", "underline", "", "")
    set.color.subject("", "Computer Branch", "Razer", "blue", "underline", "bold", "")
    set.color.subject("", "Computer Branch", "all", "green", "underline", "bold", "")
    set.color.subject("", "Computer Branch", "LG", "red", "underline", "bold", "")
    set.color.object("", "Computer Branch", "SteelSeries Apex 5", "red", "underline", "reversing", "")
    set.color.object("", "Computer Branch", "LG 27GN850 Ultragear", "cyan", "", "bold", "")

    algorithm.branch()
