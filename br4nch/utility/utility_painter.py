# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.utility_handler import MaximumPaintSlotsError


def painter(paint):
    """
    Errors:
      - If the length of the 'paint' list is bigger than '4', then it raises a 'MaximumPaintSlotsError' error.

    - Then is calculated how many times the loop should be run and adding element with an empty string as value to the
      list 'paint' until the length of the list is equal to '4'.

    Length 'paint' list loop:
      - The current value of position in the 'paint' list will be set as the requested paint.

    - Then all paint is returned.
    """
    if len(paint) > 4:
        raise MaximumPaintSlotsError

    for _ in range(4 - len(paint)):
        paint.append("")

    for position in range(len(paint)):
        if paint[position]:
            paint[position] = ["\u001b[31m", "\u001b[33m", "\u001b[32m", "\u001b[36m", "\u001b[34m", "\u001b[35m",
                               "\u001b[30m", "\u001b[37m", "\u001b[1m", "\u001b[4m", "\u001b[7m", "\u001b[0m"][
                ["red", "yellow", "green", "cyan", "blue", "magenta", "black", "white", "bold", "underline",
                 "reversing", "clear"].index(paint[position].lower())]

    return paint[0] + paint[1] + paint[2] + paint[3]
