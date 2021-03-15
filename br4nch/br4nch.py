# Indev phase - br4nch v1.0.9
# desc - Introducing: Painter. The painter can color and add specials to selected parts of the branch.


def testing_structure():
    get_branch = executor("get_branch")
    get_modules = executor("get_modules")
    get_subjects = executor("get_subjects")
    get_objects = executor("get_objects")

    paint_reset = '\u001b[0m'

    branch_paint = executor("get_branch_paint")
    header_paint = executor("get_header_paint")

    all_list = ["all", "", " "]

    if branch_paint:
        paint_branch = branch_paint[0]
    else:
        paint_branch = ""

    if header_paint:
        paint_header = header_paint[0]
    else:
        paint_header = ""

    if get_branch:
        for name in get_branch:
            for header in get_branch[name]:
                print(paint_header + header, paint_reset + paint_branch + prefix("header_end", None) + paint_reset)

                if get_branch[name][header]:
                    end = 0
                    for module in get_branch[name][header]:
                        paint_module = ""
                        lenght = len(get_branch[name][header])
                        end = end + 1

                        selected_modules = executor("get_selected_modules")
                        module_paint = executor("get_module_paint")

                        for selected_module in range(len(selected_modules)):
                            if selected_modules[selected_module] == module:
                                paint_module = module_paint[selected_module]

                        for x in all_list:
                            if x in selected_modules:
                                all_num = selected_modules.index(x)
                                paint_module = module_paint[all_num]

                        if end == lenght:
                            print(paint_branch + prefix("module_end", None), paint_reset + paint_module + module + paint_reset)
                        else:
                            print(paint_branch + prefix("module_extend", None), paint_reset + paint_module + module + paint_reset)

                        if get_branch[name][header][module]:
                            end1 = 0
                            end2 = 0
                            for subject in get_branch[name][header][module]:
                                paint_subject = ""
                                end = end + 1

                                selected_subjects = executor("get_selected_subjects")
                                subject_paint = executor("get_subject_paint")

                                for selected_subject in range(len(selected_subjects)):
                                    if selected_subjects[selected_subject] == subject:
                                        paint_subject = subject_paint[selected_subject]

                                for x in all_list:
                                    if x in selected_subjects:
                                        all_num = selected_subjects.index(x)
                                        paint_subject = subject_paint[all_num]

                                if module == get_modules[-1]:
                                    extender = " "
                                    lenght1 = len(get_branch[name][header][module])
                                    end1 = end1 + 1

                                    if end1 == lenght1:
                                        print(paint_branch + prefix("subject_end", extender), paint_reset + paint_subject + subject + paint_reset)
                                    else:
                                        print(paint_branch + prefix("subject_extend", extender), paint_reset + paint_subject + subject + paint_reset)
                                else:
                                    extender = "┃"
                                    lenght2 = len(get_branch[name][header][module])
                                    end2 = end2 + 1

                                    if end2 == lenght2:
                                        print(paint_branch + prefix("subject_end_last", extender), paint_reset + paint_subject + subject + paint_reset)
                                    else:
                                        print(paint_branch + prefix("subject_extend_last", extender), paint_reset + paint_subject + subject + paint_reset)

                                if get_branch[name][header][module][subject]:
                                    end = 0
                                    for obj in get_branch[name][header][module][subject]:
                                        paint_object = ""
                                        lenght = len(get_branch[name][header][module][subject])
                                        end = end + 1

                                        selected_objects = executor("get_selected_objects")
                                        object_paint = executor("get_object_paint")

                                        for selected_object in range(len(selected_objects)):
                                            if selected_objects[selected_object] == obj:
                                                paint_object = object_paint[selected_object]

                                        for x in all_list:
                                            if x in selected_objects:
                                                all_num = selected_objects.index(x)
                                                paint_object = object_paint[all_num]

                                        if not obj == get_objects[-1]:
                                            if module == get_modules[-1]:
                                                if subject == get_subjects[-1]:
                                                    extender = " "
                                                else:
                                                    extender = "    ┃"
                                            else:
                                                extender = "┃    "
                                        else:
                                            extender = "     "

                                        if end == lenght:
                                            print(paint_branch + prefix("object_end", extender), paint_reset + paint_object + obj + paint_reset)
                                        else:
                                            print(paint_branch + prefix("object_extend", extender), paint_reset + paint_object + obj + paint_reset)


def add_name(branch_name):
    get_branch = executor("get_branch")
    get_branch.update({branch_name: {}})


def add_header(branch_name, header_name):
    get_branch = executor("get_branch")
    get_branch[branch_name].update({header_name: {}})


def add_module(branch_name, header_name, module_name):
    get_branch = executor("get_branch")
    get_branch[branch_name][header_name].update({module_name: {}})


def add_subject(branch_name, header_name, module_name, subject_name):
    get_branch = executor("get_branch")
    get_branch[branch_name][header_name][module_name].update({subject_name: {}})


def add_object(branch_name, header_name, module_name, subject_name, object_name):
    get_branch = executor("get_branch")
    get_branch[branch_name][header_name][module_name][subject_name].update({object_name: {}})


def set_color_branch(color, special1, special2, special3):
    paint_branch = painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

    add_branch_paint = executor("get_branch_paint")

    add_branch_paint.append(paint_branch)


def set_color_header(color, special1, special2, special3):
    paint_header = painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

    add_header_paint = executor("get_header_paint")

    add_header_paint.append(paint_header)


def set_color_module(selected, color, special1, special2, special3):
    paint_module = painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

    add_selected_module = executor("get_selected_modules")
    add_module_paint = executor("get_module_paint")

    add_selected_module.append(selected)
    add_module_paint.append(paint_module)


def set_color_subject(selected, color, special1, special2, special3):
    paint_subject = painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

    add_selected_subject = executor("get_selected_subjects")
    add_subject_paint = executor("get_subject_paint")

    add_selected_subject.append(selected)
    add_subject_paint.append(paint_subject)


def set_color_object(selected, color, special1, special2, special3):
    paint_object = painter(color.lower(), special1.lower(), special2.lower(), special3.lower())

    add_selected_object = executor("get_selected_objects")
    add_object_paint = executor("get_object_paint")

    add_selected_object.append(selected)
    add_object_paint.append(paint_object)


def executor(action):
    global branch, names, headers, modules, subjects, objects
    global selected_modules, selected_subjects, selected_objects
    global branch_paint, header_paint, module_paint, subject_paint, object_paint

    if action == "new_branch":
        branch = {}

    if branch:
        names = []
        headers = []
        modules = []
        subjects = []
        objects = []
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

    if action == "get_branch":
        return branch

    if action == "get_names":
        return names

    if action == "get_headers":
        return headers

    if action == "get_modules":
        return modules

    if action == "get_subjects":
        return subjects

    if action == "get_objects":
        return objects

    if action == "new_paint":
        selected_modules = []
        selected_subjects = []
        selected_objects = []
        branch_paint = []
        header_paint = []
        module_paint = []
        subject_paint = []
        object_paint = []

    if action == "get_selected_modules":
        return selected_modules

    if action == "get_selected_subjects":
        return selected_subjects

    if action == "get_selected_objects":
        return selected_objects

    if action == "get_branch_paint":
        return branch_paint

    if action == "get_header_paint":
        return header_paint

    if action == "get_module_paint":
        return module_paint

    if action == "get_subject_paint":
        return subject_paint

    if action == "get_object_paint":
        return object_paint


def prefix(action, extender):
    space_x3 = " "*3

    if action == "header_end":
        prefix_header_end = "\n╻"
        return prefix_header_end

    if action == "module_extend":
        prefix_module_extend = "┃\n┣━━"
        return prefix_module_extend

    if action == "subject_extend":
        prefix_subject_extend = extender + space_x3 + "┃\n" + extender + space_x3 + "┣━━"
        return prefix_subject_extend

    if action == "subject_extend_last":
        prefix_subject_extend_last = extender + space_x3 + "┃\n" + extender + space_x3 + "┣━━"
        return prefix_subject_extend_last

    if action == "object_extend":
        prefix_object_extend = extender + space_x3 + "┃\n" + extender + space_x3 + "┣━━"
        return prefix_object_extend

    if action == "module_end":
        prefix_module_end = "┃\n┗━━"
        return prefix_module_end

    if action == "subject_end":
        prefix_subject_end = extender + space_x3 + "┃\n" + extender + space_x3 + "┗━━"
        return prefix_subject_end

    if action == "subject_end_last":
        prefix_subject_end_last = extender + space_x3 + "┃\n" + extender + space_x3 + "┗━━"
        return prefix_subject_end_last

    if action == "object_end":
        prefix_object_end = extender + space_x3 + "┃\n" + extender + space_x3 + "┗━━"
        return prefix_object_end


def painter(color, special1, special2, special3):
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
    # reset = "\u001b[0m"       # Reset

    colors_id = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    colors = [black, red, green, yellow, blue, magenta, cyan, white]

    specials_id = ["bold", "underline", "reversing"]
    specials = [bold, underline, reversing]

    selected_color = ""
    selected_special1 = ""
    selected_special2 = ""
    selected_special3 = ""

    if color:
        for selected in range(8):
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


def initiate():
    executor("new_branch")
    executor("new_paint")


if __name__ == '__main__':
    initiate()

    add_name("Computer Branch")
    add_header("Computer Branch", "Gaming")
    add_module("Computer Branch", "Gaming", "Monitors")
    add_module("Computer Branch", "Gaming", "Keyboard & Mouse")
    add_subject("Computer Branch", "Gaming", "Monitors", "LG")
    add_subject("Computer Branch", "Gaming", "Keyboard & Mouse", "Steel Series")
    add_subject("Computer Branch", "Gaming", "Keyboard & Mouse", "Razer")
    add_object("Computer Branch", "Gaming", "Monitors", "LG", "LG 27GN850 Ultragear")
    add_object("Computer Branch", "Gaming", "Keyboard & Mouse", "Razer", "Razer Blackwindow Elite")
    add_object("Computer Branch", "Gaming", "Keyboard & Mouse", "Steel Series", "SteelSeries Apex 3")
    add_object("Computer Branch", "Gaming", "Keyboard & Mouse", "Steel Series", "SteelSeries Apex 5")

    set_color_branch("blue", "bold", "", "")
    set_color_header("magenta", "reversing", "bold", "underline")
    set_color_module("Monitors", "yellow", "bold", "", "")
    set_color_module("Keyboard & Mouse", "cyan", "underline", "", "")
    set_color_subject("Razer", "blue", "underline", "bold", "")
    set_color_subject("all", "green", "underline", "bold", "")
    set_color_subject("LG", "red", "underline", "bold", "")
    set_color_object("SteelSeries Apex 5", "red", "underline", "reversing", "")
    set_color_object("LG 27GN850 Ultragear", "cyan", "", "bold", "")

    testing_structure()

# br4nch.add.branch(arg1)
# br4nch.add.header(arg1, arg2)
# br4nch.add.module(arg1, arg2, arg3)
# br4nch.add.subject(arg1, arg2, arg3, arg4)
# br4nch.add.object(arg1, arg2, arg3, arg4, arg5)

# br4nch.set.color.branch(arg1, arg2, arg3, arg4)
# br4nch.set.color.header(arg1, arg2, arg3, arg4)
# br4nch.set.color.module(arg1, arg2, arg3, arg4)
# br4nch.set.color.subject(arg1, arg2, arg3, arg4)
# br4nch.set.color.object(arg1, arg2, arg3, arg4)
