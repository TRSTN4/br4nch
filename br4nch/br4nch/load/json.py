# Part of the br4nch package.

# Imports all files.
from br4nch.utility.generator import get_uid


# Gets the parsed arguments.
def arguments(branch="", load={}):
    # Parses the arguments to the first task.
    loop(branch, load)


def loop(branch, value=""):
    print(dict(a=value))
    for key, value in value.items():

        test.update({str(key) + get_uid(branch): {}})
        print(test)

        if value and not isinstance(value, str) and not isinstance(value, list):
            loop(value)
            return


test = {}
