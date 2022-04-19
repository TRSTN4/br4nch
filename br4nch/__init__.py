# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

__version__ = "1.2.1"
__author__ = "TRSTN4"
__author_email__ = "tristan@trstn4.com"
__description__ = "Data Structure Tree Builder"
__url__ = "https://github.com/TRSTN4/br4nch"

import os
import imp
import json
import urllib.request

from datetime import datetime, timedelta, date

import br4nch.create
import br4nch.duplicate
import br4nch.move
import br4nch.replace
import br4nch.delete
import br4nch.set
import br4nch.reset
import br4nch.load
import br4nch.export
import br4nch.display
import br4nch.utility


def check_version():
    if not os.path.isfile(imp.find_module('br4nch')[1] + "/update_check.br4nch"):
        create_update_check_file()

    update_check_file = open(imp.find_module('br4nch')[1] + "/update_check.br4nch", "rt")

    file_data = update_check_file.readlines()

    if file_data[0][8:-1] != __version__ and file_data[0][8:-1] != "None":
        file_data[0] = file_data[0].replace(file_data[0][8:-1], "None")
        file_data[1] = file_data[1].replace(file_data[1][16:-1], "None")
        file_data[2] = file_data[2].replace(file_data[2][17:-1], "None")
        file_data[3] = file_data[3].replace(file_data[3][17:], "None")

    if file_data[0][8:-1] == "None":
        file_data[0] = file_data[0].replace(file_data[0][8:-1], __version__)

    if str(file_data[1][16:-1]) == "None" or datetime.now().strftime("%H") not in file_data[2][17:-1].split(",") or \
            datetime.now().strftime("%H") in file_data[2][17:-1].split(",") and \
            date.today().strftime("%d") != file_data[1][16:-1]:
        file_data[1] = file_data[1].replace(file_data[1][16:-1], date.today().strftime("%d"))

        skip_check = []
        for hour in range(4):
            skip_check.append((datetime.strptime(
                datetime.now().strftime("%H"), "%H") + timedelta(hours=hour)).strftime("%H"))
        file_data[2] = file_data[2].replace(file_data[2][17:-1], ",".join(skip_check))

        file_data[3] = file_data[3].replace(file_data[3][17:], json.loads(urllib.request.urlopen(
            "https://api.github.com/repos/TRSTN4/br4nch/releases/latest").read())["tag_name"])

    if file_data[3][17:] != __version__:
        print("[!] There is a new br4nch version (" + file_data[3][17:] + ") available, The current installed br4nch "
              + "version (" + __version__ + ") is outdated.")

    update_check_file.close()

    update_check_file = open(imp.find_module('br4nch')[1] + "/update_check.br4nch", "wt")
    update_check_file.write(file_data[0] + file_data[1] + file_data[2] + file_data[3])
    update_check_file.close()


def create_update_check_file():
    with open(imp.find_module('br4nch')[1] + "/update_check.br4nch", 'w', encoding='utf-8') as file:
        file.write("version=None\n")
        file.write("last-check-date=None\n")
        file.write("skip-check-hours=None\n")
        file.write("update-available=None")


try:
    check_version()
except:
    pass
