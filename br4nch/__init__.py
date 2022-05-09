# br4nch - Data Structure Tree Builder
# Author: https://TRSTN4.com
# Website: https://br4nch.com
# Documentation: https://docs.br4nch.com
# Github Repository: https://github.com/TRSTN4/br4nch

__version__ = "2.2.1"
__description__ = "Data Structure Tree Builder"
__url__ = "https://github.com/TRSTN4/br4nch"

__author__ = "TRSTN4"
__author_email__ = "tristan@trstn4.com"
__author_website__ = "https://TRSTN4.com"

import os
import imp
import json
import urllib.request

from datetime import datetime, timedelta, date

from . import create, duplicate, move, replace, delete, set, reset, load, export, get, display, utility


class CheckVersion:
    def __init__(self):
        self.path = imp.find_module('br4nch')[1] + "/update_check.br4nch"

        self.check_version()

    def check_version(self):
        if not os.path.isfile(self.path):
            self.create_update_check_file()

        update_check_file = open(self.path, "rt")
        file = update_check_file.readlines()

        file_version = file[0]
        file_last_check_date = file[1]
        file_skip_check_hours = file[2]
        file_update_available = file[3]

        if file_version[8:-1] != __version__ and file_version[8:-1] != "None":
            file_version = file_version.replace(file_version[8:-1], "None")
            file_last_check_date = file_last_check_date.replace(file_last_check_date[16:-1], "None")
            file_skip_check_hours = file_skip_check_hours.replace(file_skip_check_hours[17:-1], "None")
            file_update_available = file_update_available.replace(file_update_available[17:], "None")

        if file_version[8:-1] == "None":
            file_version = file_version.replace(file_version[8:-1], __version__)

        if str(file_last_check_date[16:-1]) == "None" or datetime.now().strftime("%H") \
                not in file_skip_check_hours[17:-1].split(",") or datetime.now().strftime("%H") \
                in file_skip_check_hours[17:-1].split(",") \
                and date.today().strftime("%d") != file_last_check_date[16:-1]:
            file_last_check_date = file_last_check_date.replace(
                file_last_check_date[16:-1], date.today().strftime("%d"))

            skip_check = []
            for hour in range(4):
                skip_check.append((datetime.strptime(
                    datetime.now().strftime("%H"), "%H") + timedelta(hours=hour)).strftime("%H"))
            file_skip_check_hours = file_skip_check_hours.replace(file_skip_check_hours[17:-1], ",".join(skip_check))

            file_update_available = file_update_available.replace(file_update_available[17:], json.loads(
                urllib.request.urlopen(
                    "https://api.github.com/repos/TRSTN4/br4nch/releases/latest").read())["tag_name"])

        if file_update_available[17:] != __version__:
            print("[!] There is a new br4nch version (" + file_update_available[17:]
                  + ") available, The current installed br4nch " + "version (" + __version__ + ") is outdated.")

        update_check_file.close()

        update_check_file = open(self.path, "wt")
        update_check_file.write(file_version + file_last_check_date + file_skip_check_hours + file_update_available)
        update_check_file.close()

    def create_update_check_file(self):
        with open(self.path, 'w', encoding='utf-8') as file:
            file.write("version=None\n")
            file.write("last-check-date=None\n")
            file.write("skip-check-hours=None\n")
            file.write("update-available=None")


try:
    CheckVersion()
except:
    pass
