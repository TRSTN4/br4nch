# Alpha phase - br4nch v1.1.5
# desc - Branching algorithm update and multiple hotfixes.

# Imports the br4nch package.
import br4nch

# Creates the "Database" branch.
br4nch.add.branch("Database")
# Creates the header for the "Database" branch.
br4nch.add.header("Database", "Business")
# Creates the first layers in the "Database" branch.
br4nch.add.layer("Database", ["Jobs", "Employee\nContacts", "Products"])
# Creates the second layers in the "Database" branch and puts them in the "Jobs" layer.
br4nch.add.layer("Database", ["Accounting", "International Business\nNational Business"], "Jobs")
# Creates the third layers in the "Database" branch and puts them in the two selected layers.
br4nch.add.layer("Database", ["Bookkeepers", "Budget analysts"], ["Employee\nContacts", "Accounting"])
br4nch.add.layer("Database", ["Trade specialists", "Import Specialist\nExport Specialist"],
                 ["Employee\nContacts", "International Business\nNational Business"])
# Creates the fourth layers in the "Database" branch and puts them in the selected layer.
br4nch.add.layer("Database", ["John\nDoe", "Jane\nDoe"], "Bookkeepers")
# Creates the fifth layers in the "Database" branch, puts them in the selected layers and todo.
br4nch.add.layer("Database", ["Email", "Phone"], ["John\nDoe", "Jane\nDoe"], "Employee\nContacts")
br4nch.add.layer("Database", "john.doe@email.com\njohn.doe.alt@email.com", "Email",
                 ["Employee\nContacts", "Bookkeepers", "Jane\nDoe"])
br4nch.add.layer("Database", "01 23 45 67 89", "Phone", ["Employee\nContacts", "John\nDoe"])
br4nch.add.layer("Database", "98 76 54 32 10", "Phone", ["Employee\nContacts", "Jane\nDoe"])

# Paints the "Test" branch.
br4nch.set.color.branch("Database", "blue")
br4nch.set.color.header("Database", "magenta", "bold")
br4nch.set.color.layer("Database", ["green", "bold", "underline"], ["Jobs", "Products"])
br4nch.set.color.layer("Database", "red", "John\nDoe")
br4nch.set.color.layer("Database", ["green", "bold", "underline"], "Jane\nDoe")
br4nch.set.color.layer("Database", "Test Two", "yellow")

# Changes the branch symbols.
br4nch.set.symbol.branch("Test", "|", "|-", "|_")

# Displays the branches.
br4nch.run.display("all")

# Displays all the logs.
# br4nch.run.log()
