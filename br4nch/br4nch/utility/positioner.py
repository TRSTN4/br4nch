# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches
from br4nch.utility.handler import StringInstanceError


def calculate_operator(branch, position, value=""):
    if not value:
        value = branches[branch][list(branches[branch])[0]]

    count = 0
    numbers = []

    position = position.copy()
    previous_value = value

    for layer, value in value.items():
        count = count + 1

        if position[0] or ">" in position[0] or "<" in position[0]:
            numbers.append(count)

            if layer == list(previous_value)[-1]:
                return numbers
        else:
            if count == int(position[0]):
                position.pop(0)
                numbers = calculate_operator(branch, position, value)
                return numbers


def format_position(branch, position):
    for length in range(len(position)):
        if "." in position[length]:
            position[length] = position[length].split(".")
        else:
            if not isinstance(position[length], list):
                position[length] = [position[length]]

    for length in range(len(position)):
        for element in range(len(position[length])):
            if "/" in position[length][element]:
                split = position[length][element].split("/")
                for count in range(len(split)):
                    position.append(position[length].copy())
                    position[-1][element] = split[count]

                position.pop(length)

            if "*" in position[length][element]:
                numbers = calculate_operator(branch, position[length])

            if ">" in position[length][element]:
                split = position[length][element].split(">")

                if split[0] < split[1]:
                    bigger = split[1]
                    smaller = split[0]
                else:
                    bigger = split[0]
                    smaller = split[1]

                numbers = calculate_operator(branch, position[length])

                test = False

                for count in numbers.copy():
                    if count == int(smaller):
                        test = True
                    else:
                        if count == int(bigger):
                            test = False
                        else:
                            if not test:
                                numbers.remove(count)

            if "<" in position[length][element]:
                split = position[length][element].split("<")

                if split[0] < split[1]:
                    bigger = split[1]
                    smaller = split[0]
                else:
                    bigger = split[0]
                    smaller = split[1]

                numbers = calculate_operator(branch, position[length])

                for count in range(int(bigger) + 1 - int(smaller)):
                    numbers.remove(int(int(smaller) + count))

            if "*" in position[length][element] or ">" in position[length][element] or "<" in position[length][element]:
                for num in numbers:
                    position.append(position[length].copy())
                    position[-1][element] = int(num)
                    string = ""

                    for position2 in position[-1]:
                        string = string + "." + str(position2)
                    position.pop(-1)
                    position.append(string[1:])

                position.pop(length)
                format_position(branch, position)

    return position
