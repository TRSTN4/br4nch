# Alpha phase - br4nch v1.1.4
# desc - Build layer and add layer files clean-up.

# Imports the br4nch package.
import br4nch

# Creates the "Database" branch.
br4nch.add.branch("Database")
br4nch.add.header("Database", "Business")
br4nch.add.layer("Database", ["Jobs", "Employee\nContacts", "Products"])
br4nch.add.layer("Database", ["Accounting", "International Business\nNational Business"], "Jobs")
br4nch.add.layer("Database", ["Bookkeepers", "Budget analysts"], ["Employee\nContacts", "Accounting"])
br4nch.add.layer("Database", ["Trade specialists", "Import Specialist\nExport Specialist"],
                 ["Employees", "International Business"])
br4nch.add.layer("Database", ["John\nDoe", "Jane\nDoe"], "Bookkeepers")
br4nch.add.layer("Database", ["Email", "Phone"], ["John\nDoe", "Jane\nDoe"], "Employee\nContacts")
br4nch.add.layer("Database", "john.doe@email.com\njohn.doe.alt@email.com", "Email",
                 ["Employee\nContacts", "John\nDoe"])
br4nch.add.layer("Database", "jane.doe@email.com", "Email", ["Employees", "Jane\nDoe"])
br4nch.add.layer("Database", "01 23 45 67 89", "Phone", ["Employees", "John\nDoe"])
br4nch.add.layer("Database", "98 76 54 32 10", "Phone", ["Employees", "Jane\nDoe"])

# Paints the "Test" branch.
br4nch.set.color.branch("Database", "blue")
br4nch.set.color.header("Database", "magenta", "bold")
br4nch.set.color.layer("Database", "Jobs", "green", "bold", "underline")
br4nch.set.color.layer("Database", ["Accounting", "International Business"], "red")
br4nch.set.color.layer("Database", "Test Two", "yellow")

# Changes the branch symbols.
br4nch.set.symbol.branch("Test", "|", "|---", "|_")

# Displays the branches.
br4nch.run.display("all")

# Displays all the logs.
br4nch.run.log()
