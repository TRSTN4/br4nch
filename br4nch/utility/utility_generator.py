# Copyright 2021 by TRSTN4. All rights reserved.
# This file is part of the br4nch python package, and is released under the "GNU General Public License v3.0".
# Please see the LICENSE file that should have been included as part of this package.

import uuid

from br4nch.utility.utility_librarian import uids


def generate_uid(branch, length=10):
    """
    - Generates the uid.

    While loop:
      - If the uid exists in the current branch uids list, a new one is generated.
      - If the uid does not exist in the current branch uids list, then the uid is added to the branch uids list.

    - Returns the generated uid.
    """

    uid = str(uuid.uuid4()).replace("-", "")[0:length]

    while True:
        if uid in uids[branch]:
            return generate_uid(branch, length)
        else:
            uids[branch].append(uid)
            break

    return ":uid=" + uid
