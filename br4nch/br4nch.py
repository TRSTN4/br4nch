# Indev phase - br4nch v1.0.5
# desc - Working with dictionaries for better structure.


def executor(action):
    global branch

    if action == "new_branch":
        branch = {}

    if action == "get_branch":
        return branch


def initiate():
    executor("new_branch")


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
    print(get_branch)


def check_existing_branch(branch_name):
    if branch_name in executor("get_branch"):
        return True
    else:
        return False


if __name__ == '__main__':
    initiate()

    create_name("my_branch")
    create_header("my_branch", "just a header")
    create_module("my_branch", "just a header", "sample header")
    create_subject("my_branch", "just a header", "sample header", "some kind of subject")
    create_object("my_branch", "just a header", "sample header", "some kind of subject", "this is a object")

# br4nch.create(arg1)
# br4nch.header(arg1, arg2)
# br4nch.module(arg1, arg2, arg3)
# br4nch.subject(arg1, arg2, arg3, arg4)
# br4nch.object(arg1, arg2, arg3, arg4, arg5)
