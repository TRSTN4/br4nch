# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from ..utility.utility_librarian import UtilityLibrarian
from ..utility.utility_handler import InstanceStringError, InvalidParentError


class UtilityDecider:
    def __init__(self, tree, nodes):
        self.tree = tree
        self.nodes = nodes

        self.positions = FormatNode(self.tree, self.nodes).get_positions()
        self.formatted_positions = FormatPosition(self.tree, self.positions).get_position_package()

    def get_formatted_positions(self):
        return self.formatted_positions


class FormatNode:
    def __init__(self, tree, nodes):
        self.tree = tree
        self.nodes = nodes

        self.positions = []

        self.manage_nodes()

    def manage_nodes(self):
        levels = [0]
        self.elevator(levels,
                      UtilityLibrarian.existing_trees[self.tree][list(
                          UtilityLibrarian.existing_trees[self.tree])[0]])
        levels.append(0)

        for node in self.nodes:
            self.format_node(node, levels, [0],
                             UtilityLibrarian.existing_trees[self.tree][list(
                                 UtilityLibrarian.existing_trees[self.tree])[0]], "")

    def elevator(self, levels, nested_dictionary, height=0):
        for children in nested_dictionary.values():
            levels.append(height)
            self.elevator(levels, children, height + 1)

    def format_node(self, node, levels, trace, nested_dictionary, visual_position):
        count = 0
        for parent, children in nested_dictionary.items():
            count = count + 1
            trace[0] = trace[0] + 1

            if levels[trace[0]] <= levels[trace[0] - 1]:
                visual_position = visual_position[:-2]

            visual_position = visual_position + "." + str(count)

            if parent[:-15].lower() == node.lower():
                for character in visual_position:
                    if character == ".":
                        visual_position = visual_position[1:]
                    else:
                        break

                self.positions.append(visual_position)

            if children:
                self.format_node(node, levels, trace, children, visual_position)

    def get_positions(self):
        return self.positions


class FormatPosition:
    def __init__(self, tree, position_package):
        self.tree = tree
        self.position_package = position_package

        self.format_position(self.position_package)

    def format_position(self, position_package):
        for number in range(len(position_package)):
            if isinstance(position_package[number], list):
                for position in position_package[number]:
                    if not isinstance(position, str):
                        raise InstanceStringError("position", position)
                    else:
                        for character in position:
                            if character not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "/", "*", ">",
                                                 "<"]:
                                print(position_package[number])
                                raise InvalidParentError("position", position_package[number])
            else:
                if not isinstance(position_package[number], str):
                    raise InstanceStringError("pos", position_package[number])
                else:
                    for character in position_package[number]:
                        if character not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "/", "*", ">", "<"]:
                            raise InvalidParentError("position", position_package[number])

            if "." in position_package[number]:
                position_package[number] = position_package[number].split(".")
            else:
                if not isinstance(position_package[number], list):
                    position_package[number] = [position_package[number]]

        for number in range(len(position_package)):
            for position in range(len(position_package[number])):
                if "/" in position_package[number][position]:
                    for multiple_position in position_package[number][position].split("/"):
                        if not multiple_position:
                            raise InvalidParentError("position", position_package[number][position])

                    for count in range(len(position_package[number][position].split("/"))):
                        position_package.append(position_package[number].copy())
                        position_package[-1][position] = position_package[number][position].split("/")[count]
                    position_package.pop(number)

                    self.format_position(position_package)

        for number in range(len(position_package)):
            for position in range(len(position_package[number])):
                if "*" in position_package[number][position]:
                    if not UtilityLibrarian.existing_trees[self.tree][list(
                            UtilityLibrarian.existing_trees[self.tree])[0]]:
                        position_package[number].pop(position)
                        position_package[number].append("0")
                    else:
                        for count in range(self.calculate_operator(
                                position_package[number].copy(),
                                UtilityLibrarian.existing_trees[self.tree][list(
                                    UtilityLibrarian.existing_trees[self.tree])[0]])):
                            position_package.append(position_package[number].copy())
                            position_package[-1][position] = str(count + 1)
                        position_package.pop(number)

                if ">" in position_package[number][position]:
                    if ">" in position_package[number][position]:
                        for including_position in position_package[number][position].split(">"):
                            if not including_position:
                                raise InvalidParentError("position", position_package[number][position])

                    including_positions = position_package[number][position].split(">")
                    total_including_positions = len(including_positions)

                    for count in range(int(min(including_positions)), int(max(including_positions)) + 1):
                        including_positions.append(str(count))

                    for _ in range(total_including_positions):
                        including_positions.pop(0)

                    for count in range(len(including_positions)):
                        position_package.append(position_package[number].copy())
                        position_package[-1][position] = including_positions[count]
                    position_package.pop(number)

                if "<" in position_package[number][position]:
                    if "<" in position_package[number][position]:
                        for excluding_position in position_package[number][position].split("<"):
                            if not excluding_position:
                                raise InvalidParentError("position", position_package[number][position])

                    excluding_positions = []

                    for count in range(self.calculate_operator(
                            position_package[number].copy(),
                            UtilityLibrarian.existing_trees[self.tree][list(
                                UtilityLibrarian.existing_trees[self.tree])[0]])):
                        excluding_positions.append(str(count + 1))

                    for count in range(int(min(position_package[number][position].split("<"))),
                                       int(max(position_package[number][position].split("<"))) + 1):
                        excluding_positions.remove(str(count))

                    for count in range(len(excluding_positions)):
                        position_package.append(position_package[number].copy())
                        position_package[-1][position] = excluding_positions[count]
                    position_package.pop(number)

                if "/" in position_package[number][position] or "*" in position_package[number][position] \
                        or ">" in position_package[number][position] or "<" in position_package[number][position]:
                    self.format_position(position_package)

        return position_package

    def calculate_operator(self, position, nested_dictionary):
        count = 0
        for children in nested_dictionary.values():
            count = count + 1

            if "*" in position[0] or "<" in position[0] or count == int(position[0]):
                return len(nested_dictionary)

            if children and count == int(position[0]):
                position.pop(0)
                return self.calculate_operator(position, children)

    def get_position_package(self):
        return self.position_package
