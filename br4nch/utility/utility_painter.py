# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

from br4nch.utility.utility_handler import MaximumPaintSlotsError


class UtilityPainter:
    def __init__(self, paint):
        self.paint = paint

        self.validate_arguments()
        self.painter()

    def validate_arguments(self):
        if len(self.paint) > 3:
            raise MaximumPaintSlotsError

    def painter(self):
        for _ in range(3 - len(self.paint)):
            self.paint.append("")

        for index in range(len(self.paint)):
            if self.paint[index]:
                self.paint[index] = ["\u001b[31m", "\u001b[33m", "\u001b[32m", "\u001b[36m", "\u001b[34m", "\u001b[35m",
                                     "\u001b[30m", "\u001b[37m", "\u001b[1m", "\u001b[4m","\u001b[0m"][
                    ["red", "yellow", "green", "cyan", "blue", "magenta", "black", "white", "bold", "underline",
                     "clear"].index(self.paint[index].lower())]

        return self.paint[0] + self.paint[1] + self.paint[2]
