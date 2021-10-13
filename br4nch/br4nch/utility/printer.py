# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

from br4nch.utility.librarian import branches, output, uids, sizes, symbols, paint_branch, paint_header, paint_layer,\
    positions


def printer(action, package=None, delete=False):
    if package is None:
        package = []

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

    if action == "display_found":
        for layer, value in positions.copy().items():
            for key, pos in value.items():
                print("Get Position Result" + ":\n" + "└─ Branch: " + branch + "\n" + " " * 3 + "└─ Layer: "
                      + layer.replace("\n", " ")[:-15] + "\n" + " " * 6 + "└─ Position: " + pos)
            del positions[layer]

    if action == "display_branch":
        for y in list(branches):
            if branch.lower() == y.lower():
                branch = y

                for x in output[branch]:
                    print(x)

                if delete:
                    del output[branch]
                    del branches[branch]
                    del sizes[branch]
                    del symbols[branch]
                    del paint_branch[branch]
                    del paint_header[branch]
                    del paint_layer[branch]
                    del uids[branch]
