# br4nch - Data Structure Tree Builder
# Github Repository: https://github.com/TRSTN4/br4nch
# Documentation: https://docs.br4nch.com

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
