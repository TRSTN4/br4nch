# Alpha phase - br4nch v1.1.2
# desc - New database branch and updating the add layer file.

# Imports the br4nch package.
import br4nch

# Creates the "Database" branch.
br4nch.add.branch("Database")
br4nch.add.header("Database", "Business")
br4nch.add.layer("Database", ["Jobs", "Employees", "Products"])
br4nch.add.layer("Database", ["Accounting", "International Business"], "Jobs")
br4nch.add.layer("Database", ["Bookkeepers", "Budget analysts"], ["Employees", "Accounting"])
br4nch.add.layer("Database", ["Trade specialists", "Import/export specialist"], ["Employees", "International Business"])
br4nch.add.layer("Database", ["John Doe", "Jane Doe"], "Bookkeepers")
br4nch.add.layer("Database", ["Mail", "Phone"], ["John Doe", "Jane Doe"], "Employees")
br4nch.add.layer("Database", "john.doe@email.com", "Mail", ["Employees", "John Doe"])
br4nch.add.layer("Database", "jane.doe@email.com", "Mail", ["Employees", "Jane Doe"])
br4nch.add.layer("Database", "01 23 45 67 89", "Phone", ["Employees", "John Doe"])
br4nch.add.layer("Database", "98 76 54 32 10", "Phone", ["Employees", "Jane Doe"])

# Paints the "Test" branch.
br4nch.set.color.branch("Database", "blue")
br4nch.set.color.header("Database", "magenta", "bold")
br4nch.set.color.layer("Database", "Jobs", "green", "bold", "underline")
br4nch.set.color.layer("Database", ["Accounting", "International Business"], "red")
br4nch.set.color.layer("Database", "Test Two", "yellow")

# Displays the branches.
br4nch.run.display("all")

# Displays all the logs.
br4nch.run.log()
