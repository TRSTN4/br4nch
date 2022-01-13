# Copyright 2021-2022 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

"""br4nch - Data Structure Tree Builder for Python."""

__version__ = "1.1.3"
__author__ = "TRSTN4"
__author_email__ = "tristan@trstn4.com"
__description__ = "Data Structure Tree Generator for Python."
__url__ = "https://github.com/TRSTN4/br4nch"

import json
import urllib.request

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
    """
    - Captures the response from the github api after which json loads the data and stores the value of the last
      released tag.
    - Prints a notification if the currently installed version is not equal to the latest version.
    """
    try:
        response = urllib.request.urlopen("https://api.github.com/repos/TRSTN4/br4nch/releases/latest")
    except urllib.error.URLError:
        return

    data = json.loads(response.read())
    latest_version = data["tag_name"]

    if __version__ != latest_version:
        print("[!] There is a new br4nch version (" + latest_version + ") available, The current installed br4nch "
              + "version (" + __version__ + ") is outdated.")


check_version()
