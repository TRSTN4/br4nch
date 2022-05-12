# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import UtilityHandler


class UtilityDecider:
    def __init__(self, tree, argument, nodes):
        self.tree = tree
        self.argument = argument
        self.nodes = nodes

        self.nodes = self.FormatNode(self.tree, self.nodes).get_positions()
        self.positions = self.FormatPosition(self.tree, self.argument, self.nodes).get_position_package()

    def get_formatted_positions(self):
        """
        Returns the formatted positions.
        """
        return self.positions

    class FormatNode:
        def __init__(self, tree, nodes):
            self.tree = tree
            self.nodes = nodes

            self.total_duplicates = 0

            self.manage_nodes()

        def manage_nodes(self):
            """
            Runs the format tasks and the calculates the duplicate number character.
            """
            # Gets each height and stores it in the 'levels' list.
            levels = [0]
            self.elevator(levels,
                          UtilityLibrarian.existing_trees[self.tree][list(
                              UtilityLibrarian.existing_trees[self.tree])[0]])
            levels.append(0)

            for node in self.nodes.copy():
                # Creates for every node a position if the node exists.
                self.create_position(node, levels, [0],
                                     UtilityLibrarian.existing_trees[self.tree][list(
                                         UtilityLibrarian.existing_trees[self.tree])[0]], "")

            for node in self.nodes.copy():
                # Checks if the '#' duplicate sign is in the node.
                if "#" in node:
                    valid = True
                    # Validates if the number is a valid number and the characters are in the list.
                    for character in node.split("#")[-1]:
                        if character not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "/", "*", ">", "<"]:
                            valid = False

                    # If the number is valid.
                    if valid:
                        split_node = node.rsplit("#", 1)

                        # Removes all empty strings from the split list.
                        while "" in split_node:
                            split_node.remove("")

                        stripped_node = ""
                        if len(split_node) > 1:
                            # Removes the added number from the node.
                            for part in node.rsplit("#", 1)[:1]:
                                stripped_node = stripped_node + part

                            operator = False
                            # Checks if there is an operator in the given node number.
                            for character in node.split("#")[-1]:
                                if character in ["/", "*", ">", "<"]:
                                    operator = True
                                    break

                            # Continues if there is an operator in the given node number.
                            if operator:
                                serial_numbers = []
                                operators = []

                                # Gets all duplicates from a specific node.
                                self.get_total_duplicates(stripped_node,
                                                          UtilityLibrarian.existing_trees[self.tree][list(
                                                              UtilityLibrarian.existing_trees[self.tree])[0]])

                                # Separates at each '/' operator.
                                if "/" in node.split("#")[-1]:
                                    for separate in node.split("#")[-1].split("/"):
                                        operators.append(separate)
                                else:
                                    # Sets the non node number value in a list.
                                    operators = [node.split("#")[-1]]

                                for number_operator in operators:
                                    # Adds all integer only values to the serial numbers list.
                                    if number_operator.isnumeric():
                                        serial_numbers.append(stripped_node + "#" + str(int(number_operator)))

                                for number_operator in operators:
                                    # Checks if the '>' operator is in the number.
                                    if ">" in number_operator:
                                        if "*" in number_operator.split(">"):
                                            # Adds all existing duplicates to the serial numbers list.
                                            for number in range(self.total_duplicates):
                                                serial_numbers.append(stripped_node + "#" + str(number + 1))

                                            # Removes the operator number.
                                            operators.remove(number_operator)
                                        else:
                                            # Gets both numbers from the '>' operator.
                                            including_numbers = number_operator.split(">")

                                            total_including_numbers = len(including_numbers)

                                            # Adds each number between value "x" and "y".
                                            for count in range(int(min(including_numbers)),
                                                               int(max(including_numbers)) + 1):
                                                including_numbers.append(str(count))

                                            # Removes all old values form the '>' operator.
                                            for _ in range(total_including_numbers):
                                                including_numbers.pop(0)

                                            # Adds all 'including_numbers' numbers to the serial numbers list.
                                            for number in including_numbers:
                                                serial_numbers.append(stripped_node + "#" + str(int(number)))

                                for number_operator in operators:
                                    # Checks if the '<' operator is in the number.
                                    if "<" in number_operator:
                                        if "*" in number_operator.split("<"):
                                            # Removes the operator number.
                                            operators.remove(number_operator)
                                        else:
                                            excluding_numbers = []
                                            # Adds all existing duplicates to the 'excluding_numbers' list.
                                            for number in range(self.total_duplicates):
                                                excluding_numbers.append(str(number + 1))

                                            # Removes each number between value "x" and "y".
                                            for count in range(int(min(number_operator.split("<"))),
                                                               int(max(number_operator.split("<"))) + 1):
                                                if str(count) in excluding_numbers:
                                                    excluding_numbers.remove(str(count))

                                            # Adds all 'excluding_numbers' numbers to the serial numbers list.
                                            for number in excluding_numbers:
                                                serial_numbers.append(stripped_node + "#" + str(int(number)))

                                for number_operator in operators:
                                    # Checks if the '*' operator is in the number.
                                    if "*" in number_operator:
                                        # Adds all existing duplicates to the serial numbers list.
                                        for number in range(self.total_duplicates):
                                            serial_numbers.append(stripped_node + "#" + str(number + 1))

                                        # Removes the operator number.
                                        operators.remove(number_operator)

                                # Resets the variable.
                                self.total_duplicates = 0

                                for node_number in serial_numbers:
                                    # Bypasses node deletion error in 'create_position' function.
                                    self.nodes.append(node_number)

                                    # Creates for the duplicate node a position if the duplicate node exists.
                                    self.create_position(stripped_node, levels, [0],
                                                         UtilityLibrarian.existing_trees[self.tree][list(
                                                             UtilityLibrarian.existing_trees[self.tree])[0]], "",
                                                         node_number, int(node_number.split("#")[-1]))

                                # Removes all remaining nodes.
                                for node_number in serial_numbers:
                                    if node_number in self.nodes:
                                        self.nodes.remove(node_number)

                                # Removes the given node.
                                self.nodes.remove(node)
                            else:
                                # Creates for the duplicate node a position if the duplicate node exists.
                                self.create_position(stripped_node, levels, [0],
                                                     UtilityLibrarian.existing_trees[self.tree][list(
                                                         UtilityLibrarian.existing_trees[self.tree])[0]], "", node,
                                                     int(node.split("#")[-1]))

        def elevator(self, levels, nested_dictionary, height=0):
            """
            Appends each height to a list.
            """
            # Loops through nested dictionary.
            for children in nested_dictionary.values():
                # Appends the current 'height' value to the list.
                levels.append(height)
                # Appends the current 'height' value with '+1' and continues nesting the loop.
                self.elevator(levels, children, height + 1)

        def create_position(self, node, levels, trace, nested_dictionary, visual_position, full_node="", number=0,
                            duplicate_hit=0):
            """
            Creates a position for each given node if the node exists.
            """
            count = 0
            # Loops through nested dictionary.
            for parent, children in nested_dictionary.items():
                count = count + 1
                trace[0] = trace[0] + 1

                # If the 'level'/'height' of the current value in the loop is equal to or smaller than the previous
                # 'level'/'height' value in the loop, then the last number and dot in the 'visual_position' variable is
                # removed.
                if levels[trace[0]] <= levels[trace[0] - 1]:
                    visual_position = visual_position[:-2]
                # Variable is added with the value of 'count' separated by a dot to the 'visual_position' variable.
                visual_position = visual_position + "." + str(count)

                # Passes if the given node is equal to the current parent node.
                if parent[:-15].lower() == node.lower():
                    if full_node:
                        # Adds '+1' for each duplicate hit.
                        duplicate_hit = duplicate_hit + 1

                    # If the 'full_node' has no value, pass. Else, when the given number is equal to the total passed
                    # duplicates.
                    if not full_node or number == duplicate_hit:
                        # If the first character contains a dot, it will be removed.
                        for character in visual_position:
                            if character == ".":
                                # Removes the dot in the first character.
                                visual_position = visual_position[1:]
                            else:
                                break

                        if full_node:
                            # Changes to full node name so that it can be properly removed.
                            node = full_node

                        # Adds the position and removes the old node name from the list.
                        self.nodes.append(visual_position)
                        if node in self.nodes:
                            self.nodes.remove(node)

                if children:
                    # Continue the nested loop.
                    self.create_position(node, levels, trace, children, visual_position, full_node, number,
                                         duplicate_hit)

        def get_total_duplicates(self, node, nested_dictionary):
            """
            # Counts all duplicates from a specific node.
            """
            # Loops through nested dictionary.
            for parent, children in nested_dictionary.items():
                # Passes if the given node is equal to the current parent node.
                if parent[:-15].lower() == node.lower():
                    # Adds '+1' for each duplicate hit.
                    self.total_duplicates = self.total_duplicates + 1

                if children:
                    # Continue the nested loop.
                    self.get_total_duplicates(node, children)

        def get_positions(self):
            """
            Returns the formatted node positions.
            """
            return self.nodes

    class FormatPosition:
        def __init__(self, tree, argument, position_package):
            self.tree = tree
            self.argument = argument
            self.position_package = position_package

            self.format_position(self.position_package)

        def format_position(self, position_package):
            """
            Calculates the position and converts all operators into the right positions.
            """
            for number in range(len(position_package)):
                if isinstance(position_package[number], list):
                    for position in position_package[number]:
                        # Raises an error when the current position value is not a string.
                        if not isinstance(position, str):
                            raise UtilityHandler.InstanceStringError(self.argument, position)
                        else:
                            # Raises an error when there is an invalid character in the current position.
                            for character in position:
                                if character not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "/", "*",
                                                     ">", "<"]:
                                    raise UtilityHandler.InvalidPositionError(self.argument, position_package[number])
                else:
                    # Raises an error when the current position value is not a string.
                    if not isinstance(position_package[number], str):
                        raise UtilityHandler.InstanceStringError("pos", position_package[number])
                    else:
                        # Raises an error when there is an invalid character in the current position.
                        for character in position_package[number]:
                            if character not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "/", "*", ">",
                                                 "<"]:
                                raise UtilityHandler.InvalidPositionError(self.argument, position_package[number])

                # Splits the string into a list if there is a dot in the string.
                if "." in position_package[number]:
                    position_package[number] = position_package[number].split(".")
                else:
                    # If the value is not an instance of a list, set the value in the list.
                    if not isinstance(position_package[number], list):
                        position_package[number] = [position_package[number]]

            for number in range(len(position_package)):
                if number < len(position_package):
                    for position in range(len(position_package[number])):
                        # Checks if the '/' operator is in the current position.
                        if "/" in position_package[number][position]:
                            for multiple_position in position_package[number][position].split("/"):
                                # Raises an error if there are no positions combined with the '/' operator.
                                if not multiple_position:
                                    raise UtilityHandler.InvalidPositionError(self.argument,
                                                                              position_package[number][position])

                            # Loops through all gotten numbers.
                            for count in range(len(position_package[number][position].split("/"))):
                                # Adds all gotten numbers each with the copied parent positions.
                                position_package.append(position_package[number].copy())
                                position_package[-1][position] = position_package[number][position].split("/")[count]

                            # Removes the old/formatted '/' operator position.
                            position_package.pop(number)

                            self.format_position(position_package)

            for number in range(len(position_package)):
                if number < len(position_package):
                    for position in range(len(position_package[number])):
                        # Checks if the '>' operator is in the current position.
                        if ">" in position_package[number][position]:
                            for including_position in position_package[number][position].split(">"):
                                # Raises an error if there are no positions combined with the '>' operator.
                                if not including_position:
                                    raise UtilityHandler.InvalidPositionError(self.argument,
                                                                              position_package[number][position])

                            if "*" in position_package[number][position].split(">"):
                                # Loops through the total length from the nodes in the current position.
                                for count in range(self.get_total_nodes(
                                        position_package[number].copy(),
                                        UtilityLibrarian.existing_trees[self.tree][list(
                                            UtilityLibrarian.existing_trees[self.tree])[0]])):
                                    # Adds all gotten numbers each with the copied parent positions.
                                    position_package.append(position_package[number].copy())
                                    position_package[-1][position] = str(count + 1)

                                # Removes the old/formatted '*' operator position.
                                position_package.pop(number)
                            else:
                                # Gets both numbers from the '>' operator.
                                including_positions = position_package[number][position].split(">")

                                total_including_positions = len(including_positions)

                                # Adds each number between value "x" and "y".
                                for count in range(int(min(including_positions)), int(max(including_positions)) + 1):
                                    including_positions.append(str(count))

                                # Removes all old values form the '>' operator.
                                for _ in range(total_including_positions):
                                    including_positions.pop(0)

                                # Loops through the total length from the 'including_positions' list.
                                for count in range(len(including_positions)):
                                    # Adds all gotten numbers each with the copied parent positions.
                                    position_package.append(position_package[number].copy())
                                    position_package[-1][position] = including_positions[count]

                                # Removes the old/formatted '>' operator position.
                                position_package.pop(number)

            for number in range(len(position_package)):
                if number < len(position_package):
                    for position in range(len(position_package[number])):
                        # Checks if the '<' operator is in the current position.
                        if "<" in position_package[number][position]:
                            for excluding_position in position_package[number][position].split("<"):
                                # Raises an error if there are no positions combined with the '<' operator.
                                if not excluding_position:
                                    raise UtilityHandler.InvalidPositionError(self.argument,
                                                                              position_package[number][position])

                            if "*" in position_package[number][position].split("<"):
                                position_package.append([""])
                                position_package.pop(number)
                            else:
                                excluding_positions = []

                                # Loops through the total length from the nodes in the current position.
                                for count in range(self.get_total_nodes(
                                        position_package[number].copy(),
                                        UtilityLibrarian.existing_trees[self.tree][list(
                                            UtilityLibrarian.existing_trees[self.tree])[0]])):
                                    excluding_positions.append(str(count + 1))

                                # Removes each number between value "x" and "y".
                                for count in range(int(min(position_package[number][position].split("<"))),
                                                   int(max(position_package[number][position].split("<"))) + 1):
                                    if str(count) in excluding_positions:
                                        excluding_positions.remove(str(count))

                                # Loops through the total length from the 'excluding_positions' list.
                                for count in range(len(excluding_positions)):
                                    # Adds all gotten numbers each with the copied parent positions.
                                    position_package.append(position_package[number].copy())
                                    position_package[-1][position] = excluding_positions[count]

                                # Removes the old/formatted '<' operator position.
                                position_package.pop(number)

            for number in range(len(position_package)):
                if number < len(position_package):
                    for position in range(len(position_package[number])):
                        # Checks if the '*' operator is in the current position.
                        if "*" in position_package[number][position]:
                            # If there are no nodes in the tree then the position '0' will be used.
                            if not UtilityLibrarian.existing_trees[self.tree][list(
                                    UtilityLibrarian.existing_trees[self.tree])[0]]:
                                position_package[number].pop(position)
                                position_package[number].append("0")
                            else:
                                # Loops through the total length from the nodes in the current position.
                                for count in range(self.get_total_nodes(
                                        position_package[number].copy(),
                                        UtilityLibrarian.existing_trees[self.tree][list(
                                            UtilityLibrarian.existing_trees[self.tree])[0]])):
                                    # Adds all gotten numbers each with the copied parent positions.
                                    position_package.append(position_package[number].copy())
                                    position_package[-1][position] = str(count + 1)

                                # Removes the old/formatted '*' operator position.
                                position_package.pop(number)

            for number in range(len(position_package)):
                if number < len(position_package):
                    for position in range(len(position_package[number])):
                        # If there is a '/', '*', '>' or '<' in the position character.
                        if "/" in position_package[number][position] or "*" in position_package[number][position] \
                                or ">" in position_package[number][position] or "<" \
                                in position_package[number][position]:
                            # Calls the 'format_position' function to manage the rest of the operators.
                            self.format_position(position_package)

            return position_package

        def get_total_nodes(self, position, nested_dictionary):
            """
            Calculates the operator and returns the length from the height of the given dictionaries.
            """
            count = 0
            # Loops through nested dictionary.
            for parent, children in nested_dictionary.items():
                count = count + 1

                # The '*' or '<' is in the first element in the 'position' list, or if the 'count' variable is equal to
                # the first element in the 'position' list as an integer.
                if "*" in position[0] or "<" in position[0]:
                    # Returns the current node height total positions.
                    return len(nested_dictionary)

                # If there is value and the 'count' value is equal to the right value in the position list.
                if children and count == int(position[0]):
                    # Remove the first position in the list and continue the nested loop.
                    position.pop(0)
                    return self.get_total_nodes(position, children)

        def get_position_package(self):
            """
            Removes the empty strings in the list and returns the formatted positions.
            """
            # Removes all empty strings in the list.
            for package in self.position_package:
                if package == [""] or package == "":
                    self.position_package.remove(package)

            return self.position_package
