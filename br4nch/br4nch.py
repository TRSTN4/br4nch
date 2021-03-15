# Indev phase - br4nch v1.0.4
# desc - Testing info on structure.


def executor(action):
    global branch_list, header_list, module_list, subject_list, object_list

    if action == "new_structure":
        branch_list = []
        header_list = []
        module_list = []
        subject_list = []
        object_list = []

    if action == "get_branch":
        return branch_list

    if action == "get_header":
        return header_list

    if action == "get_module":
        return module_list

    if action == "get_subject":
        return subject_list

    if action == "get_object":
        return object_list


def initiate():
    executor("new_structure")


def create_branch(branch_name):
    get_branch = executor("get_branch")
    get_branch.append(branch_name)


def create_header(branch_name, header_name):
    if check_existing_branch(branch_name):
        get_header = executor("get_header")
        get_header.append(header_name)


def create_module(branch_name, module_name):
    if check_existing_branch(branch_name):
        get_module = executor("get_module")
        get_module.append(module_name)


def create_subject(branch_name, module_name, subject_name):
    pass


def create_object(branch_name, module_name, subject_name, object_name):
    pass


def check_existing_branch(branch_name):
    if branch_name in executor("get_branch"):
        return True
    else:
        return False


initiate()

create_branch("my_branch")
create_header("my_branch", "just a header")
create_module("my_branch", "sample header")
create_subject("my_branch", "sample header", "some kind of subject")
create_object("my_branch", "sample header", "some kind of subject", "this is a object")

# br4nch.create(arg1)
# br4nch.header(arg1, arg2)
# br4nch.module(arg1, arg2)
# br4nch.subject(arg1, arg2, arg3)
# br4nch.object(arg1, arg2, arg3, arg4)
