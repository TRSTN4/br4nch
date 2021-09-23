# Beta phase - br4nch v1.0.6
# desc - Introducing the "position assist" feature that displays all current layer positions in a branch.

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
br4nch.add.layer(branch="database", layer=["MySQL", "MariaDB"], pos="3.1")

# Creates the "Test" branch.
br4nch.add.branch(branch="Test")
br4nch.add.header(branch="Test", header="Sample")
br4nch.add.layer(branch="Test", layer=["Text 1", "Text 2", "Text 3"])
br4nch.add.layer(branch="Test", layer=["Sub Text 1", "Sub Text 2"], pos="2/3")
br4nch.add.layer(branch="Test", layer="Sub Text 3", pos="3")
br4nch.add.layer(branch="Test", layer=["Last Text 1", "Last Text 2", "Last Text 3"], pos="3.2")

# Paints the "Database" branch.
br4nch.set.color.branch(branch="Database", paint="blue")
br4nch.set.color.header(branch="Database", paint="cyan")
br4nch.set.color.layer(branch="Database", paint=["green", "bold"], pos="*")
br4nch.set.color.layer(branch="Database", paint=["red", "underline"], pos=["1.1.1", "2.2<3"])
br4nch.set.color.layer(branch="Database", paint=["cyan", "underline"], pos="2.1.1.2.1")
br4nch.set.color.layer(branch="Database", paint=["yellow", "bold"], pos=["2.1.2.1.1", "3.1.1"])
br4nch.set.color.layer(branch="Database", paint=["blue", "underline"], pos="2.*.1>2")

# Changes the "Test" branch symbols.
br4nch.set.symbol(branch="Test", line="|", split="}---->", end="!-->")
br4nch.set.symbol(branch="Database", line="┃", split="┣━━", end="┗━━")

# Sets the total size of the branch.
br4nch.set.size(branch="Test", size=0)

# Displays the given positions and/or layers.
br4nch.display.pos(branch="Test", pos="3.2.3", layer="Sub Text 1")

# Displays all layer positions in a branch.
br4nch.display.assist()

# Displays the branches.
br4nch.display.branch()
