# Beta phase - br4nch v1.0.1
# desc - Introducing the newly redesigned "add layer" algorithm.

# Imports the br4nch package.
import br4nch

# Creates the "Database" branch.
br4nch.add.branch(branch="Database")
br4nch.add.header(branch="Database", header="Company")
br4nch.add.layer(branch="Database", layer=["Jobs", "Employee\nContacts", "Products"], pos="0")
br4nch.add.layer(branch="Database", layer=["Accounting", "International Business\nNational Business"], pos="1")
br4nch.add.layer(branch="Database", layer=["Bookkeepers", "Budget analysts"], pos=["1.1", "2"])
br4nch.add.layer(branch="Database", layer=["Trade operators", "Import specialist\nExport specialist"], pos=["1.2", "2"])
br4nch.add.layer(branch="Database", layer=["John\nDoe", "Jane\nDoe"], pos="2.1")
br4nch.add.layer(branch="Database", layer=["Email", "Phone"], pos=["2.1.1", "2.1.2"])
br4nch.add.layer(branch="Database", layer="01 23 45 67 89", pos="2.1.1.2")
br4nch.add.layer(branch="Database", layer="jane.doe@email.com", pos="2.1.2.1")
br4nch.add.layer(branch="Database", layer="Database", pos="3")
br4nch.add.layer(branch="Database", layer=["MySQL", "MariaDB"], pos="3.1")

# Creates the "Test" branch.
br4nch.add.branch(branch="Test")
br4nch.add.header(branch="Test", header="Sample")
br4nch.add.layer(branch="Test", layer=["Text 1", "Text 2", "Text 3"])
br4nch.add.layer(branch="Test", layer=["Sub Text 1", "Sub Text 2"], pos=["2", "3"])
br4nch.add.layer(branch="Test", layer="Sub Text 3", pos="3")
br4nch.add.layer(branch="Test", layer=["Last Text 1", "Last Text 2", "Last Text 3"], pos="3.2")

# Displays the branches.
br4nch.run.display()
