# Part of the br4nch package.

# Imports all files.
from br4nch.utility.librarian import librarian


# Prints all the logs.
def log():
    # Imports the logs dictionary.
    logs = librarian("logs")

    # If content in logs dictionary.
    if logs:
        # Prints blank line.
        print()

    # Loops through all output of the logs dictionary.
    for key, value in logs.items():
        # Prints the value.
        print(value)
