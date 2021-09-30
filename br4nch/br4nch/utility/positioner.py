# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian


# Calculates the given operator(s) and replaces the operator(s) with the calculated numbers in different positions.
def calculate_operator(branch, pos, value=""):
    # Gets the needed lists/dictionaries.
    branches = librarian("branches")

    # Checks if there is no content in value.
    if not value:
        # Value is equal to the value of all nested layers.
        value = branches[branch][list(branches[branch])[0]]

    # Creates the numbers list and count variable.
    numbers = []
    count = 0

    # Copies the current value of pos and value.
    pos = pos.copy()
    prev_value = value.copy()

    # Gets the layer/key and value of the current value variable.
    for layer, value in value.items():
        # Count is equal to the value of count plus one.
        count = count + 1
        # Checks if the "*", ">" or "<" exists in the current value of the first element in pos.
        if "*" in pos[0] or ">" in pos[0] or "<" in pos[0]:
            # Appends the number to the numbers list.
            numbers.append(count)
            # Checks if the current value of layer is equal to the last layer in the previous value.
            if layer == list(prev_value)[-1]:
                # Returns the numbers list.
                return numbers
        # If the "*", ">" or "<" does not exists in the current value of the first element in pos.
        else:
            # Checks if the count is equal to the integer of the current value of the first element in pos.
            if count == int(pos[0]):
                # Removes the first element in the pos list.
                pos.pop(0)
                # Recalls the function.
                numbers = calculate_operator(branch, pos, value)
                # Returns the numbers list.
                return numbers


# Builds the pos using multiple algorithms.
def build_pos(branch, pos):
    for x in range(len(pos)):
        if not isinstance(pos[x], list):
           pos[x] = str(pos[x])

    # Gets position value based on the length of entries in pos list.
    for position in range(len(pos)):
        # Checks if "." in current value of element in pos.
        if "." in pos[position]:
            # Separates the numbers from the dots in current pos value.
            pos[position] = pos[position].split(".")
        # If "." not in current value of element in pos.
        else:
            # Checks if the current value of the current element in pos not is equal to a list.
            if not isinstance(pos[position], list):
                # Current value of element in pos is equal to current value of element in pos inside a list.
                pos[position] = [pos[position]]

        # Loops through all elements inside the current pos value.
        for element in range(len(pos[position])):
            # Checks if "/" in current value of element in current pos list.
            if "/" in pos[position][element]:
                # Splits at the "/" character.
                split = pos[position][element].split("/")
                # Loops through the total length of all elements in split list.
                for count in range(len(split)):
                    # Appends a copy of the current value of pos list in the pos list to the post list.
                    pos.append(pos[position].copy())
                    # current value of element in current pos list is equal to the value of count.
                    pos[-1][element] = split[count]
                # Removes the current pos list from the pos list.
                pos.pop(position)

            # Checks if "*" in current value of element in current pos list.
            if "*" in pos[position][element]:
                # Gets the numbers list from the calculated_options function.
                numbers = calculate_operator(branch, pos[position])

            # Checks if ">" in current value of element in current pos list.
            if ">" in pos[position][element]:
                # Splits at the ">" character.
                split = pos[position][element].split(">")
                # Checks if the first element in split is smaller then the second element in the list.
                if split[0] < split[1]:
                    # First element in split is smaller and the second element in split is bigger.
                    bigger = split[1]
                    smaller = split[0]
                # If the first element in split not is smaller then the second element in the list.
                else:
                    # First element in split is bigger and the second element in split is smaller.
                    bigger = split[0]
                    smaller = split[1]

                # Gets the numbers list from the calculated_options function.
                numbers = calculate_operator(branch, pos[position])

                test = False
                # Loops through all the numbers between the value of the smaller plus one and the bigger variable.
                for count in numbers.copy():
                    if count == int(smaller):
                        test = True
                    else:
                        if count == int(bigger):
                            test = False
                        else:
                            if not test:
                                numbers.remove(count)

            # Checks if "<" in current value of element in current pos list.
            if "<" in pos[position][element]:
                # Splits at the "<" character.
                split = pos[position][element].split("<")
                # Checks if the first element in split is smaller then the second element in the list.
                if split[0] < split[1]:
                    # First element in split is smaller and the second element in split is bigger.
                    bigger = split[1]
                    smaller = split[0]
                # If the first element in split not is smaller then the second element in the list.
                else:
                    # First element in split is bigger and the second element in split is smaller.
                    bigger = split[0]
                    smaller = split[1]

                # Gets the numbers list from the calculated_options function.
                numbers = calculate_operator(branch, pos[position])

                # Loops through all the numbers between the value of the smaller plus one and the bigger variable.
                for count in range(int(bigger) + 1 - int(smaller)):
                    # Removes the number from the numbers list.
                    numbers.remove(int(int(smaller) + count))

            if "*" in pos[position][element] or ">" in pos[position][element] or "<" in pos[position][element]:
                # Loops through all numbers.
                for num in numbers:
                    # Appends a copy of the current value of pos list in the pos list to the post list.
                    pos.append(pos[position].copy())
                    # current value of element in current pos list is equal to the value of num.
                    pos[-1][element] = int(num)
                    # Creates the variable.
                    string = ""
                    # Loops through all positions in the last pos list in the pos list.
                    for position2 in pos[-1]:
                        # Adds position2 separated by a dot to the string
                        string = string + "." + str(position2)
                    # Removes the last pos list from the pos list.
                    pos.pop(-1)
                    # Appends the created string to the pos list.
                    pos.append(string[1:])
                # Removes the current pos list from the pos list.
                pos.pop(position)
                # Recalls the function.
                build_pos(branch, pos)

    # Returns the pos.
    return pos
