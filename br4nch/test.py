# Alpha phase - br4nch v1.0.8
# desc - Code cleanup: Removed old module, subject and object files and added new color layer file.

# Imports the br4nch package.
import br4nch

# Creates the "Test" branch.
br4nch.add.branch("Test")
br4nch.add.header("Test", "Layers")
br4nch.add.layer("Test", ["First Layer", "Second Layer", "Third Layer"])
br4nch.add.layer("Test", ["Sublayer One", "Sublayer Two", "Sublayer Three"], ["First Layer", "Second Layer"])
br4nch.add.layer("Test", ["Sample One", "Sample Two", "Sample Three"], ["Sublayer One", "Sublayer Two"])
br4nch.add.layer("Test", ["Test One", "Test Two", "Test Three"], ["Sample One", "Sample Two"])
br4nch.add.layer("Test", ["Sub-Final One", "Sub-Final Two", "Sub-Final Three"], ["Test Three"])
br4nch.add.layer("Test", ["Final One", "Final Two", "Final Three"], ["Sub-Final One", "Sub-Final Two"])

# Displays the branches.
br4nch.run.display("all")

# Displays all the logs.
br4nch.run.log()
