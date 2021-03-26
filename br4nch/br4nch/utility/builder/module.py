# Imports all files.
from br4nch.utility.builder.subject import build_subject
from br4nch.utility.inspector.paint import inspect_paint_clear
from br4nch.utility.inspector.paint import inspect_paint_all_layer
from br4nch.utility.librarian import librarian
from br4nch.utility.branching import branching


# Algorithm to build all the given modules.
def build_module(branch, header, paint_branch):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")
    module_package = librarian("module_package")
    paper = librarian("paper")

    # Checks if content in package and returns the right paint clear value.
    paint_clear = inspect_paint_clear(module_package)

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

            # Checks if inspect paint layer all returns a value.
            if inspect_paint_all_layer(branch, module, module_package):
                # Paint is equal to the returned inspect paint layer all value.
                paint_module = inspect_paint_all_layer(branch, module, module_package)

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

            # Adds the current decider value by 1.
            decider = decider + 1

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
