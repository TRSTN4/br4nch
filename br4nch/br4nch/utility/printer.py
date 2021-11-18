# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches, output, uids, sizes, symbols, paint_branch, paint_header, paint_layer


def printer(action, package, delete=False):
    branch = package[0]

    if action == "display_export_branch":
        if package[2]:
            if package[3]:
                print("Export Result" + ":\n" + "└─ Branch: " + branch + "\n" + " " * 3 + "├─ Export: "
                      + str(package[1]) + "\n" + " " * 3 + "└─ Package: " + str(package[2]))
            else:
                print(str(package[1]))
                print(str(package[2]))
        else:
            if package[3]:
                print("Export Result" + ":\n" + "└─ Branch: " + branch + "\n" + " " * 3 + "└─ Export: "
                      + str(package[1]))
            else:
                print(str(package[1]))

    if action == "display_pos":
        if package[3]:
            print("Get Position Result" + ":\n" + "└─ Branch: " + branch + "\n" + " " * 3 + "└─ Layer: "
                  + package[1].replace("\n", " ") + "\n" + " " * 6 + "└─ Position: " + package[2])
        else:
            print(package[1])

    if action == "display_layer":
        if package[3]:
            print("Get Layer Result" + ":\n" + "└─ Branch: " + branch + "\n" + " " * 3 + "└─ Layer: "
                  + package[1].replace("\n", " ") + "\n" + " " * 6 + "└─ Position: " + package[2])
        else:
            print(package[2])

    if action == "display_branch":
        for line in output[branch]:
            print(line)

        if delete:
            del output[branch]
            del branches[branch]
            del sizes[branch]
            del symbols[branch]
            del paint_branch[branch]
            del paint_header[branch]
            del paint_layer[branch]
            del uids[branch]
