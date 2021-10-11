# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import uids
import uuid


# Generates a unique UID.
def get_uid(branch, length=10):
    # Creates the UID.
    uid = str(uuid.uuid4()).replace("-", "")[0:length]

    # Loops until a unique UID is created.
    while True:
        # Checks if UID in UIDS list.
        if uid in uids[branch]:
            # Recalls the function and creates a new UID.
            get_uid(branch, length)
            # Returns nothing.
            return
        # If UID not in UIDS list.
        else:
            # Appends the UID to the UIDS list.
            uids[branch].append(uid)
            # Breaks the loop.
            break

    # Returns the UID.
    return ":uid=" + uid
