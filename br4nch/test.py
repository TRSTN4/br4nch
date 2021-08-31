# Alpha phase - br4nch v1.1.6
# desc - Adding/updating comments to all scripts, removing the log script, adding new test branch and multiple hotfixes.

# Imports the br4nch package.
import br4nch


# Creates the "Database" branch.
br4nch.add.branch("Database")
# Creates the header for the "Database" branch.
br4nch.add.header("Database", "Business")
# Creates the layers in the "Database" branch.
br4nch.add.layer("Database", ["Jobs", "Employee\nContacts", "Products"])
br4nch.add.layer("Database", ["Accounting", "International Business\nNational Business"], "Jobs")
br4nch.add.layer("Database", ["Bookkeepers", "Budget analysts"], ["Employee\nContacts", "Accounting"])
br4nch.add.layer("Database", ["Trade specialists", "Import Specialist\nExport Specialist"],
                 ["Employee\nContacts", "International Business\nNational Business"])
br4nch.add.layer("Database", ["John\nDoe", "Jane\nDoe"], "Bookkeepers")
br4nch.add.layer("Database", ["Email", "Phone"], ["John\nDoe", "Jane\nDoe"], "Employee\nContacts")
br4nch.add.layer("Database", "john.doe@email.com\njohn.doe.alt@email.com", "Email",
                 ["Employee\nContacts", "Bookkeepers", "Jane\nDoe"])
br4nch.add.layer("Database", "01 23 45 67 89", "Phone", ["Employee\nContacts", "John\nDoe"])
br4nch.add.layer("Database", "98 76 54 32 10", "Phone", ["Employee\nContacts", "Jane\nDoe"])

# Creates the "Test" branch.
br4nch.add.branch("Test")
# Creates the header for the "Test" branch.
br4nch.add.header("Test", "Sample")
# Creates the layers in the "Test" branch.
br4nch.add.layer("Test", ["Text 1", "Text 2", "Text 3"])
br4nch.add.layer("Test", ["Sub Text 1", "Sub Text 2"], "Text 1")
br4nch.add.layer("Test", ["Sub Text 1", "Sub Text 2", "Sub Text 3"], "Text 2")
br4nch.add.layer("Test", ["Last Text 1", "Last Text 2", "Last Text 3"], "Sub Text 2")

# Paints the "Database" branch.
br4nch.set.color.branch("Database", "blue")
br4nch.set.color.header("Database", ["magenta", "bold"])
br4nch.set.color.layer("Database", ["green", "bold", "underline"], ["Jobs", "Products"])
br4nch.set.color.layer("Database", "red", "John\nDoe")
br4nch.set.color.layer("Database", ["green", "bold", "underline"], "Jane\nDoe")
br4nch.set.color.layer("Database", "Test Two", "yellow")

# Changes the branch symbols.
br4nch.set.symbol.branch("Test", "|", "|-", "|_")

# Displays the branches.
br4nch.run.display("Database")
