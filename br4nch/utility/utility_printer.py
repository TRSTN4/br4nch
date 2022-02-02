# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

from br4nch.utility.utility_librarian import branches, output, uids, sizes, symbols, paint_branch, paint_header, paint_layer


def printer(action, package, delete=False):
    """
    display_branch:
      - Prints the output in the given 'output' list and clears the 'output' list. If the 'delete' variable is 'True',
        then all necessary dictionaries containing the key value of the value of 'branch' will be deleted.
    display_pos:
      - Prints the results of the found layers of the given positions. If the 'package[3]'/beautify element is 'False',
        then the output will be printed without modified print.
    display_layer:
      - Prints the results of the found positions of the given layers. If the 'package[3]'/beautify element is 'False',
        then the output will be printed without modified print.
    export_branch:
      - If the 'package[2]' has a value, then it prints the exported branch dictionary with package. If the
        'package[3]'/beautify element is 'False', then the output will be printed without modified print.
      - If the 'package[2]' does not have a value, then it prints the exported branch dictionary without package. If the
        'package[3]'/beautify element is 'False', then the output will be printed without modified print.
    """
    branch = package[0]

    if action == "display_branch":
        for line in output[branch]:
            print(line)

        output[branch].clear()

        if delete:
            del branches[branch]
            del output[branch]
            del sizes[branch]
            del symbols[branch]
            del paint_branch[branch]
            del paint_header[branch]
            del paint_layer[branch]
            del uids[branch]

    if action == "display_pos":
        if package[3]:
            print("Get Position Result" + ":\n" + "┗━ Branch: " + branch + "\n" + " " * 3 + "┗━ Layer: "
                  + package[1].replace("\n", " ") + "\n" + " " * 6 + "┗━ Position: " + package[2])
        else:
            print(package[1])

    if action == "display_layer":
        if package[3]:
            print("Get Layer Result" + ":\n" + "┗━ Branch: " + branch + "\n" + " " * 3 + "┗━ Layer: "
                  + package[1].replace("\n", " ") + "\n" + " " * 6 + "┗━ Position: " + package[2])
        else:
            print(package[2])

    if action == "export_branch":
        if package[2]:
            if package[3]:
                print("Export Result" + ":\n" + "┗━ Branch: " + branch + "\n" + " " * 3 + "┣━ Export: "
                      + str(package[1]) + "\n" + " " * 3 + "┗━ Package: " + str(package[2]))
            else:
                print(str(package[1]))
                print(str(package[2]))
        else:
            if package[3]:
                print("Export Result" + ":\n" + "┗━ Branch: " + branch + "\n" + " " * 3 + "┗━ Export: "
                      + str(package[1]))
            else:
                print(str(package[1]))
