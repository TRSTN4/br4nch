# Imports all files.
from br4nch.utility.builder.subject import build_subject
from br4nch.utility.librarian import librarian
from br4nch.utility.branching import branching


# Algorithm to build all the given modules.
def build_module(branch, header, paint_branch):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    module_package = librarian("module_package")
    paper = librarian("paper")

    # Checks if content in package.
    if module_package:
        # Resets the paint.
        paint_clear = "\u001b[0m"
    # If content not in package.
    else:
        # Sets the paint to nothing.
        paint_clear = ""

    # Checks if header key in branch list has any value.
    if branches[branch][header]:
        # Decider decides when to use the straight and end line symbol.
        decider = 0

        # Loops through all modules in the module list.
        for module in branches[branch][header]:
            # Resets the paint after every loop.
            paint_module = paint_clear

            # Saves the current state of module.
            saved_module = module

            # Adds the current decider value by 1.
            decider = decider + 1

            # Tries to run loop.
            try:
                # Loops through all keys in the module > branch directory.
                for key in module_package[branch]:
                    # Checks if the key is equal to the value of module.
                    if key == module:
                        # Module paint is equal to the value of the key inside the module > branch package.
                        paint_module = module_package[branch].get(key)
            # If KeyError in loop.
            except KeyError:
                # Passes through.
                pass

            # Loops through all given packages inside the module package dictionary.
            for package in module_package:
                # Checks if the package is equal to "all" string.
                if package == "all":
                    # Loops through all keys inside the "all" package.
                    for key in module_package["all"]:
                        # Checks if the key is equal to the "all" string.
                        if key == "all":
                            # Module paint is equal to the value of "all" inside module > "all" package.
                            paint_module = module_package["all"].get("all")
                        # If the key is not equal to the "all" string.
                        else:
                            # Checks if the key is equal to the value of module.
                            if key == module:
                                # Module paint is equal to the value of module inside module > "all" package.
                                paint_module = module_package["all"].get(module)
                # If the package is not equal to "all" string.
                else:
                    # Loops through all keys inside the module > branch package.
                    for key in module_package[branch]:
                        # Checks if the key is equal to the "all" string.
                        if key == "all":
                            # Module paint is equal to the value of the key in the module > branch package.
                            paint_module = module_package[branch].get(key)

            # Checks decider number is equal to the length of the total number of branch header entries.
            if decider == len(branches[branch][header]):
                # Checks if "\n"/newline in module.
                if "\n" in module:
                    module = module.replace("\n", paint_clear + "\n" + " " * 4 + paint_module)
                # If "\n"/newline not in module.
                else:
                    module = module.replace(module, paint_clear + paint_module + module)

                # Uses prefix with the end line symbol and appends the output to the paper list.
                paper.append(paint_clear + paint_branch + branching("module_end", "") +
                             paint_clear + " " + paint_module + module + paint_clear)

            # If decider number is not equal to the length of the total number of branch header entries.
            else:
                # Checks if "\n"/newline in module.
                if "\n" in module:
                    # Replaces the newline with new branching.
                    module = module.replace("\n", paint_clear + paint_branch + "\n┃" + paint_clear +
                                            " " * 3 + paint_module)
                # If "\n"/newline not in module.
                else:
                    # Replaces the newline with new branching.
                    module = module.replace(module, paint_clear + paint_module + module)

                # Uses prefix with the multi line symbol and appends the output to the paper list.
                paper.append(paint_clear + paint_branch + branching("module_multi", "") +
                             paint_clear + " " + paint_module + module + paint_clear)

            # Reverts the old state of module.
            module = saved_module

            # Runs the next task.
            build_subject(branch, header, module, paint_branch)
