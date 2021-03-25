# Algorithm to build all the given modules.
def build_modules(self, paint_branch, branch, header):
    # Checks if header key in branch list has any value.
    if branches[branch][header]:
        # Decider decides when to use the straight and end line symbol.
        decider = 0

        # Loops through all modules in the module list.
        for module in branches[branch][header]:
            # Resets the paint after every loop.
            paint_module = "\u001b[0m"

            # Saves the current state of module.
            saved_module = module

            # Adds the current decider value by 1.
            decider = decider + 1

            # Loops through all keys in the module > branch directory.
            for key in module_package[branch]:
                # Checks if the key is equal to the value of module.
                if key == module:
                    # Module paint is equal to the value of the key inside the module > branch package.
                    paint_module = module_package[branch].get(key)

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
                    module = module.replace("\n", self.paint_clear + "\n" + " " * 4 + paint_module)
                # If "\n"/newline not in module.
                else:
                    module = module.replace(module, self.paint_clear + paint_module + module)

                # Uses prefix with the end line symbol and appends the output to the paper list.
                paper.append(self.paint_clear + paint_branch + utility.branching("module_end", "") +
                             self.paint_clear + " " + paint_module + module + self.paint_clear)

            # If decider number is not equal to the length of the total number of branch header entries.
            else:
                # Checks if "\n"/newline in module.
                if "\n" in module:
                    # Replaces the newline with new branching.
                    module = module.replace("\n", self.paint_clear + paint_branch + "\n┃" + self.paint_clear +
                                            " " * 3 + paint_module)
                # If "\n"/newline not in module.
                else:
                    # Replaces the newline with new branching.
                    module = module.replace(module, self.paint_clear + paint_module + module)

                # Uses prefix with the multi line symbol and appends the output to the paper list.
                paper.append(self.paint_clear + paint_branch + utility.branching("module_multi", "") +
                             self.paint_clear + " " + paint_module + module + self.paint_clear)

            # Reverts the old state of module.
            module = saved_module

            # Runs the next task.
            self.build_subjects(paint_branch, branch, header, module)