# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

from br4nch.utility.utility_handler import InstanceStringError, InvalidPositionError
from br4nch.utility.utility_librarian import branches


def format_position(branch, position_package):
    """
    position_package range loop:
      - If the position value is an instance of a list.
        position_package[number] range loop:
          - If the position value is not an instance of a string, then it raises an 'InstanceStringError' error.
          - If the character variable in the position loop is not equal to a number and/or operator, the error
            'InvalidPositionError' is displayed.

      - If the position value is not an instance of a list.
          - If the position_package[number] value is not an instance of a string, then it raises an
            'InstanceStringError' error.
          - If the character variable in the position_package[number] loop is not equal to a number and/or operator, the
            error 'InvalidPositionError' is displayed.

      - If there is a '.' in the 'position_package[number]', then the 'position_package[number]' variable is equal to
        the split 'position_package[number]' list.
      - If there is no '.' in the 'position_package[number]', if the given pos argument is not an instance of a list,
        then the pos argument is set as a list.

    position_package range loop:
      position_package[number] range loop:
        - If there is a '/' in the 'position_package[number][position]' variable, The
          'position_package[number][position]' will be split at the '/' character. If there is a element in the list
          without a value, the 'InvalidPositionError' error will be called. if all the elements in the list has a value,
          a loop is made with the value of the length of the split values. Then in each loop it makes a copy of the
          current value of the 'position_package[number][position]' variable and adds the value to the
          'position_package' list and changes the position to the copied value with the position value of the split
          'position_package[number][position]' value. Then the value of 'number' is removed in the 'position_package'
          list.
        - Calls the 'format_position' function again.

    position_package range loop:
      position_package[number] range loop:
        - If there is a '*' in the 'position_package[number][position]' variable, if there are no existing layers in the
          current branch, then the '*' position will be changed to a '0'. If there are existing layer in the current
          branch, then a loop is made with the value of the length of the returned total layers value in the
          'calculate_operator' function. Then in each loop it makes a copy of the current value of the
          'position_package[number][position]' variable and adds the value to the 'position_package' list. Then it
          changes the position to the copied value with the current number of 'count + 1' value. Then the value of
          'number' is removed in the 'position_package' list.

        - If there is a '>' in the variable 'position_package[number][position]', then the
          'position_package[number][position]' is split and stored in the variable 'including_positions'. Then the
          length of 'including_positions' is also stored in a variable called 'total_including_positions'.
        - A loop is made with the lowest value of 'include_positions' and the highest value of 'include_positions' plus
          one. In each loop, the value 'count' is added to the list 'including_positions'.
        - Then a loop is made of the length of the 'including_positions' variable. In each loop, the first value of the
          'including_positions' list will be removed.
        - A loop is made with the value of the length of the total length of the 'including_positions' variable. Then in
          each loop it makes a copy of the current value of the 'position_package[number][position]' variable and adds
          the value to the 'position_package' list. Then it changes the position to the copied value with the current
          number of 'count' in the 'including_positions' list. Then the value of 'number' is removed in the
          'position_package' list.

        - If there is a '<' in the 'position_package[number][position]' variable, then a loop is made with the value of
          the length of the returned total layers value in the 'calculate_operator' function. Then in each loop it
          appends the string 'count + 1' to the 'excluding_positions' list.
        - A loop is made with the lowest value of the split 'position_package[number][position]' and the highest value
          of the split 'position_package[number][position]' plus one. In each loop, the string value of 'count' will be
          removed from the 'excluding_positions' list.
        - A loop is made with the value of the length of the total length of the 'excluding_positions' variable. Then in
          each loop it makes a copy of the current value of the 'position_package[number][position]' variable and adds
          the value to the 'position_package' list. Then it changes the position to the copied value with the current
          number of 'count' in the 'excluding_positions' list. Then the value of 'number' is removed in the
          'position_package' list.

    - Calls the 'format_position' function to manage the rest of the operators if there is a '/', '*', '>' or '<' in the
      'position_package[number][position]' variable.

    - Returns the 'position_package' variable.
    """
    for number in range(len(position_package)):
        if isinstance(position_package[number], list):
            for position in position_package[number]:
                if not isinstance(position, str):
                    raise InstanceStringError("position", position)
                else:
                    for character in position:
                        if character not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "/", "*", ">", "<"]:
                            print(position_package[number])
                            raise InvalidPositionError("position", position_package[number])
        else:
            if not isinstance(position_package[number], str):
                raise InstanceStringError("pos", position_package[number])
            else:
                for character in position_package[number]:
                    if character not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "/", "*", ">", "<"]:
                        raise InvalidPositionError("position", position_package[number])

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
                        raise InvalidPositionError("position", position_package[number][position])

                for count in range(len(position_package[number][position].split("/"))):
                    position_package.append(position_package[number].copy())
                    position_package[-1][position] = position_package[number][position].split("/")[count]
                position_package.pop(number)

                format_position(branch, position_package)

    for number in range(len(position_package)):
        for position in range(len(position_package[number])):
            if "*" in position_package[number][position]:
                if not branches[branch][list(branches[branch])[0]]:
                    position_package[number].pop(position)
                    position_package[number].append("0")
                else:
                    for count in range(calculate_operator(position_package[number].copy(),
                                                          branches[branch][list(branches[branch])[0]])):
                        position_package.append(position_package[number].copy())
                        position_package[-1][position] = str(count + 1)
                    position_package.pop(number)

            if ">" in position_package[number][position]:
                if ">" in position_package[number][position]:
                    for including_position in position_package[number][position].split(">"):
                        if not including_position:
                            raise InvalidPositionError("position", position_package[number][position])

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
                            raise InvalidPositionError("position", position_package[number][position])

                excluding_positions = []

                for count in range(calculate_operator(position_package[number].copy(),
                                                      branches[branch][list(branches[branch])[0]])):
                    excluding_positions.append(str(count + 1))

                for count in range(int(min(position_package[number][position].split("<"))),
                                   int(max(position_package[number][position].split("<"))) + 1):
                    excluding_positions.remove(str(count))

                for count in range(len(excluding_positions)):
                    position_package.append(position_package[number].copy())
                    position_package[-1][position] = excluding_positions[count]
                position_package.pop(number)

            if "/" in position_package[number][position] or "*" in position_package[number][position]\
                    or ">" in position_package[number][position] or "<" in position_package[number][position]:
                format_position(branch, position_package)

    return position_package


def calculate_operator(position, value):
    """
    Value dictionary loop:
      - For each value of the 'value' variable the 'count' variable is added with plus '1'.

      - If the '*' or '<' is in the first element in the 'position' list, or if the 'count' variable is equal to the
        first element in the 'position' list as an integer, then all layers are returned.

      - If there is a value of the 'value' variable and the 'count' variable is equal to the first element in the
        'position' list as an integer, then the first value is removed from the 'position' list and the
        'calculate_operator' function is called again with the new values of the variable 'value' as argument.
    """
    count = 0
    previous_value = value

    for layer, value in value.items():
        count = count + 1

        if "*" in position[0] or "<" in position[0] or count == int(position[0]):
            return len(previous_value)

        if value and count == int(position[0]):
            position.pop(0)
            return calculate_operator(position, value)
