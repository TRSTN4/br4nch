# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.handler import MaximumPaintSlots, NotExistingPaintError


def painter(paint):
    """
    Lists:
      - If the given paint argument is not an instance of a list, then the paint argument will be set as a list.

    Errors:
      - If the length of the 'paint' list is bigger than '4', then it raises a 'MaximumPaintSlots' error.

    - Then is calculated how many times the loop should be run and adding element with an empty string as value to the
      list 'paint' until the length of the list is equal to '4'.

    Length 'paint' list loop:
      - If the current value of the position in the 'paint' list is equal to one of the values in the 'paint_id' list,
        then the current value of position in the 'paint' list becomes the value of the given index of the position in
        the 'paint' list for the given list.

      Errors:
        - If the current value of the position in the 'paint' list is not equal to any of the values in the 'paint_id'
          list, then it raises a 'NotExistingPaintError' error.

    - Then all paint is returned.
    """
    if not isinstance(paint, list):
        paint = [paint]

    if len(paint) > 4:
        raise MaximumPaintSlots

    for _ in range(4 - len(paint)):
        paint.append("")

    paint_id = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white", "bold", "underline", "reversing",
                "clear"]

    for position in range(len(paint)):
        if paint[position].lower() in paint_id:
            paint[position] = ["\u001b[30m", "\u001b[31m", "\u001b[32m", "\u001b[33m", "\u001b[34m", "\u001b[35m",
                               "\u001b[36m", "\u001b[37m", "\u001b[1m", "\u001b[4m", "\u001b[4m",
                               "\u001b[0m"][paint_id.index(paint[position])]
        else:
            if paint[position]:
                raise NotExistingPaintError(paint[position])

    return paint[0] + paint[1] + paint[2] + paint[3]
