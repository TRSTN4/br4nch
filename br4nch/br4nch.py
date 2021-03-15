# Indev phase - br4nch v1.0.3
# desc - Checks and adds branch.


def executor(action):
    global new_branch

    if action == "new_branch":
        new_branch = []
        return new_branch

    if action == "get_branch":
        return new_branch


def create_branch(branch_name):
    add_name = executor("new_branch")
    add_name.append(branch_name)


def create_header(branch_name, header_name):
    check_existing_branch("my_branch")


def create_module(branch_name, module_name):
    pass


def create_subject(branch_name, module_name, subject_name):
    pass


def create_object(branch_name, module_name, subject_name, object_name):
    pass


def check_existing_branch(branch_name):
    if branch_name in executor("get_branch"):
        print("yes")
    else:
        print("no")


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
