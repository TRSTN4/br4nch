# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from br4nch.utility.utility_librarian import existing_trees
from br4nch.utility.utility_handler import InstanceStringError, InvalidParentError


class UtilityPositioner:
    def __init__(self, tree, position_package):
        self.tree = tree
        self.position_package = position_package

        self.validate_arguments()
        self.format_position()

    def validate_arguments(self):
        for index in range(len(self.position_package)):
            if isinstance(self.position_package[index], list):
                for position in self.position_package[index]:
                    if not isinstance(position, str):
                        raise InstanceStringError("parent", position)
                    else:
                        for character in position:
                            if character not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "/", "*", ">",
                                                 "<"]:
                                print(self.position_package[index])
                                raise InvalidParentError("parent", self.position_package[index])
            else:
                if not isinstance(self.position_package[index], str):
                    raise InstanceStringError("pos", self.position_package[index])
                else:
                    for character in self.position_package[index]:
                        if character not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "/", "*", ">", "<"]:
                            raise InvalidParentError("parent", self.position_package[index])

            for position in range(len(self.position_package[index])):
                if "/" in self.position_package[index][position]:
                    for multiple_position in self.position_package[index][position].split("/"):
                        if not multiple_position:
                            raise InvalidParentError("parent", self.position_package[index][position])

                if ">" in self.position_package[index][position]:
                    if ">" in self.position_package[index][position]:
                        for including_position in self.position_package[index][position].split(">"):
                            if not including_position:
                                raise InvalidParentError("parent", self.position_package[index][position])

                if "<" in self.position_package[index][position]:
                    if "<" in self.position_package[index][position]:
                        for excluding_position in self.position_package[index][position].split("<"):
                            if not excluding_position:
                                raise InvalidParentError("parent", self.position_package[index][position])

    def format_position(self):
        for index in range(len(self.position_package)):
            if "." in self.position_package[index]:
                self.position_package[index] = self.position_package[index].split(".")
            else:
                if not isinstance(self.position_package[index], list):
                    self.position_package[index] = [self.position_package[index]]

        for index in range(len(self.position_package)):
            for position in range(len(self.position_package[index])):
                if "/" in self.position_package[index][position]:
                    for count in range(len(self.position_package[index][position].split("/"))):
                        self.position_package.append(self.position_package[index].copy())
                        self.position_package[-1][position] = self.position_package[index][position].split("/")[count]
                    self.position_package.pop(index)

                    self.format_position()

        for index in range(len(self.position_package)):
            for position in range(len(self.position_package[index])):
                if "*" in self.position_package[index][position]:
                    if not existing_trees[self.tree][list(existing_trees[self.tree])[0]]:
                        self.position_package[index].pop(position)
                        self.position_package[index].append("0")
                    else:
                        for count in range(self.calculate_operator(self.position_package[index].copy(),
                                                                   existing_trees[self.tree]
                                                                   [list(existing_trees[self.tree])[0]])):
                            self.position_package.append(self.position_package[index].copy())
                            self.position_package[-1][position] = str(count + 1)
                        self.position_package.pop(index)

                if ">" in self.position_package[index][position]:
                    including_positions = self.position_package[index][position].split(">")
                    total_including_positions = len(including_positions)

                    for count in range(int(min(including_positions)), int(max(including_positions)) + 1):
                        including_positions.append(str(count))

                    for _ in range(total_including_positions):
                        including_positions.pop(0)

                    for count in range(len(including_positions)):
                        self.position_package.append(self.position_package[index].copy())
                        self.position_package[-1][position] = including_positions[count]
                    self.position_package.pop(index)

                if "<" in self.position_package[index][position]:
                    excluding_positions = []

                    for count in range(self.calculate_operator(self.position_package[index].copy(),
                                                               existing_trees[self.tree]
                                                               [list(existing_trees[self.tree])[0]])):
                        excluding_positions.append(str(count + 1))

                    for count in range(int(min(self.position_package[index][position].split("<"))),
                                       int(max(self.position_package[index][position].split("<"))) + 1):
                        excluding_positions.remove(str(count))

                    for count in range(len(excluding_positions)):
                        self.position_package.append(self.position_package[index].copy())
                        self.position_package[-1][position] = excluding_positions[count]
                    self.position_package.pop(index)

                if "/" in self.position_package[index][position] or "*" in self.position_package[index][position] \
                        or ">" in self.position_package[index][position] or "<" \
                        in self.position_package[index][position]:
                    self.format_position()

        return self.position_package

    def calculate_operator(self, position, child):
        count = 0
        for child_nodes in child.values():
            count = count + 1

            if "*" in position[0] or "<" in position[0] or count == int(position[0]):
                return len(child)

            if child_nodes and count == int(position[0]):
                position.pop(0)
                return self.calculate_operator(position, child_nodes)
