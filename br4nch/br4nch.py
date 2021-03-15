# Indev phase - br4nch v1.0.6
# desc - First prototype of the structure and testing structure with sample text.


def testing_structure():
    get_branch = executor("get_branch")

    for name in get_branch:
        for header in get_branch[name]:
            print("", header)
            for module in get_branch[name][header]:
                print(" ", module)
                for subject in get_branch[name][header][module]:
                    print("  ", subject)
                    for obj in get_branch[name][header][module][subject]:
                        print("   ", obj)


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
    global branch

    if action == "new_branch":
        branch = {}

    if action == "get_branch":
        return branch


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
