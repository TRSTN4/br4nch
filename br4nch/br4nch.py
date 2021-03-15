# Indev phase - br4nch v1.0.8
# desc - Prefix improvements.


def testing_structure():
    get_branch = executor("get_branch")

    get_modules = executor("get_modules")
    get_subjects = executor("get_subjects")
    get_objects = executor("get_objects")

    if get_branch:
        for name in get_branch:
            for header in get_branch[name]:
                print(header + "\n╻")

                if get_branch[name][header]:
                    end = 0
                    for module in get_branch[name][header]:
                        lenght = len(get_branch[name][header])
                        end = end + 1

                        if end == lenght:
                            print(prefix("module_end", None), module)
                        else:
                            print(prefix("module_extend", None), module)

                        if get_branch[name][header][module]:
                            end1 = 0
                            end2 = 0
                            for subject in get_branch[name][header][module]:
                                end = end + 1

                                if module == get_modules[-1]:
                                    extender = " "
                                    lenght1 = len(get_branch[name][header][module])
                                    end1 = end1 + 1

                                    if end1 == lenght1:
                                        print(prefix("subject_end", extender), module)
                                    else:
                                        print(prefix("subject_extend", extender), module)
                                else:
                                    extender = "┃"
                                    lenght2 = len(get_branch[name][header][module])
                                    end2 = end2 + 1

                                    if end2 == lenght2:
                                        print(prefix("subject_end_last", extender), subject)
                                    else:
                                        print(prefix("subject_extend_last", extender), subject)

                                if get_branch[name][header][module][subject]:
                                    end = 0
                                    for obj in get_branch[name][header][module][subject]:
                                        lenght = len(get_branch[name][header][module][subject])
                                        end = end + 1
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
                                            print(prefix("object_end", extender), obj)
                                        else:
                                            print(prefix("object_extend", extender), obj)


def create_name(branch_name):
    get_branch = executor("get_branch")
    get_branch.update({branch_name: {}})


def create_header(branch_name, header_name):
    get_branch = executor("get_branch")
    get_branch[branch_name].update({header_name: {}})


def create_module(branch_name, header_name, module_name):
    get_branch = executor("get_branch")
    get_branch[branch_name][header_name].update({module_name: {}})


def create_subject(branch_name, header_name, module_name, subject_name):
    get_branch = executor("get_branch")
    get_branch[branch_name][header_name][module_name].update({subject_name: {}})


def create_object(branch_name, header_name, module_name, subject_name, object_name):
    get_branch = executor("get_branch")
    get_branch[branch_name][header_name][module_name][subject_name].update({object_name: {}})


def check_existing_branch(branch_name):
    if branch_name in executor("get_branch"):
        return True
    else:
        return False


def executor(action):
    global branch, modules, subjects, objects

    if action == "new_branch":
        branch = {}

    if branch:
        modules = []
        subjects = []
        objects = []
        for name in branch:
            for header in branch[name]:
                for module in branch[name][header]:
                    for subject in branch[name][header][module]:
                        for obj in branch[name][header][module][subject]:
                            modules.append(module)
                            subjects.append(subject)
                            objects.append(obj)

    if action == "get_branch":
        return branch

    if action == "get_modules":
        return modules

    if action == "get_subjects":
        return subjects

    if action == "get_objects":
        return objects


def prefix(action, extender):
    space_x3 = " "*3

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


def initiate():
    executor("new_branch")


if __name__ == '__main__':
    initiate()

    create_name("Computer Branch")
    create_header("Computer Branch", "Gaming")
    create_module("Computer Branch", "Gaming", "Monitors")
    create_module("Computer Branch", "Gaming", "Keyboard & Mouse")
    create_subject("Computer Branch", "Gaming", "Monitors", "LG")
    create_subject("Computer Branch", "Gaming", "Keyboard & Mouse", "Steel Series")
    create_subject("Computer Branch", "Gaming", "Keyboard & Mouse", "Razer")
    create_object("Computer Branch", "Gaming", "Monitors", "LG", "LG 27GN850 Ultragear")
    create_object("Computer Branch", "Gaming", "Keyboard & Mouse", "Razer", "Razer Blackwindow Elite")
    create_object("Computer Branch", "Gaming", "Keyboard & Mouse", "Steel Series", "SteelSeries Apex 3")
    create_object("Computer Branch", "Gaming", "Keyboard & Mouse", "Steel Series", "SteelSeries Apex 5")

    testing_structure()

# br4nch.add.branch(arg1)
# br4nch.add.header(arg1, arg2)
# br4nch.add.module(arg1, arg2, arg3)
# br4nch.add.subject(arg1, arg2, arg3, arg4)
# br4nch.add.object(arg1, arg2, arg3, arg4, arg5)
