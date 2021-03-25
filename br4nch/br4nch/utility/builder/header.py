# Algorithm to build all the given headers.
def build_headers(self, paint_branch, branch, newline):
    # Checks if branch key in branch list has any value.
    if branches[branch]:
        # Loops through all headers in the header list.
        for header in branches[branch]:
            # Resets the paint after every loop.
            paint_header = "\u001b[0m"

            # Loops through all given packages inside the header package dictionary.
            for key in header_package:
                # Checks if the key is equal to the value of branch.
                if key == branch:
                    # Header paint is equal to the value of the branch inside the header package.
                    paint_header = header_package.get(branch)

            # Loops through all keys in the package directory.
            for key in header_package:
                # Checks if the key is equal to "all" string.
                if key == "all":
                    # Header paint is equal to the "all" value inside the header package.
                    paint_header = header_package.get("all")

            # Uses prefix with the end line symbol and appends the output to the paper list.
            paper.append(self.paint_clear + paint_header + newline + header + self.paint_clear + paint_branch +
                         utility.branching("header_end", "") + self.paint_clear)

            # Runs the next task.
            self.build_modules(paint_branch, branch, header)