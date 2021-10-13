# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches
from br4nch.utility.handler import StringInstanceError


def calculate_operator(branch, pos, value=""):
    if not value:
        value = branches[branch][list(branches[branch])[0]]

    numbers = []
    count = 0

    pos = pos.copy()
    prev_value = value.copy()

    for layer, value in value.items():
        count = count + 1

        if "*" in pos[0] or ">" in pos[0] or "<" in pos[0]:
            numbers.append(count)

            if layer == list(prev_value)[-1]:
                return numbers
        else:
            if count == int(pos[0]):
                pos.pop(0)
                numbers = calculate_operator(branch, pos, value)
                return numbers


def format_position(branch, pos):
    for position in range(len(pos)):
        if "." in pos[position]:
            pos[position] = pos[position].split(".")
        else:
            if not isinstance(pos[position], list):
                pos[position] = [pos[position]]

        for x in range(len(pos[position])):
            if not isinstance(pos[position][x], str):
                raise StringInstanceError(x)

        for element in range(len(pos[position])):
            if "/" in pos[position][element]:
                split = pos[position][element].split("/")

                for count in range(len(split)):
                    pos.append(pos[position].copy())
                    pos[-1][element] = split[count]
                pos.pop(position)

            if "*" in pos[position][element]:
                numbers = calculate_operator(branch, pos[position])

            if ">" in pos[position][element]:
                split = pos[position][element].split(">")

                if split[0] < split[1]:
                    bigger = split[1]
                    smaller = split[0]
                else:
                    bigger = split[0]
                    smaller = split[1]

                numbers = calculate_operator(branch, pos[position])

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

            if "<" in pos[position][element]:
                split = pos[position][element].split("<")

                if split[0] < split[1]:
                    bigger = split[1]
                    smaller = split[0]
                else:
                    bigger = split[0]
                    smaller = split[1]

                numbers = calculate_operator(branch, pos[position])

                for count in range(int(bigger) + 1 - int(smaller)):
                    numbers.remove(int(int(smaller) + count))

            if "*" in pos[position][element] or ">" in pos[position][element] or "<" in pos[position][element]:
                for num in numbers:
                    pos.append(pos[position].copy())
                    pos[-1][element] = int(num)
                    string = ""

                    for position2 in pos[-1]:
                        string = string + "." + str(position2)
                    pos.pop(-1)
                    pos.append(string[1:])

                pos.pop(position)
                format_position(branch, pos)
    return pos
