# Alpha phase - br4nch v1.0.2
# desc - Fixed error when using no colors and added checks for clear paint. (Terminals that not support colors.)

# Imports the br4nch package.
import br4nch

# Creates the Computer branch.
br4nch.add.branch("Computer")
br4nch.add.header("Computer", "Gaming")
br4nch.add.module("Computer", "Gaming", "Monitors")
br4nch.add.module("Computer", "Gaming", "Keyboard & Mouse")
br4nch.add.subject("Computer", "Gaming", "Monitors", "LG")
br4nch.add.subject("Computer", "Gaming", "Keyboard & Mouse", "Steel Series")
br4nch.add.subject("Computer", "Gaming", "Keyboard & Mouse", "Razer")
br4nch.add.object("Computer", "Gaming", "Monitors", "LG", "LG 27GN850 Ultragear")
br4nch.add.object("Computer", "Gaming", "Keyboard & Mouse", "Razer", "Razer Blackwindow Elite")
br4nch.add.object("Computer", "Gaming", "Keyboard & Mouse", "Steel Series", "SteelSeries Apex 3")
br4nch.add.object("Computer", "Gaming", "Keyboard & Mouse", "Steel Series", "SteelSeries Apex 5")

# Colors the Computer branch.
br4nch.set.color.branch("Computer", "blue", "bold")
br4nch.set.color.header("Computer", "red", "reversing", "bold", "underline")
br4nch.set.color.module("Computer", "Monitors", "yellow", "bold")
br4nch.set.color.module("Computer", "Keyboard & Mouse", "cyan", "underline")
br4nch.set.color.subject("Computer", "Razer", "blue", "underline", "bold")
br4nch.set.color.subject("Computer", "all", "green", "underline", "bold")
br4nch.set.color.subject("Computer", "LG", "red", "underline", "bold")
br4nch.set.color.object("Computer", "SteelSeries Apex 5", "red", "underline", "reversing")
br4nch.set.color.object("Computer", "LG 27GN850 Ultragear", "cyan", "", "bold")

# Creates the Mall branch.
br4nch.add.branch("Mall")
br4nch.add.header("Mall", "Food\nStore")
br4nch.add.module("Mall", "Food\nStore", "Meat")
br4nch.add.module("Mall", "Food\nStore", "Vegetarian")
br4nch.add.module("Mall", "Food\nStore", "Vegan\nVegy")
br4nch.add.subject("Mall", "Food\nStore", "Meat", "Cow")
br4nch.add.subject("Mall", "Food\nStore", "Meat", "Pig")
br4nch.add.subject("Mall", "Food\nStore", "Vegetarian", "Cheese")
br4nch.add.subject("Mall", "Food\nStore", "Vegetarian", "Milk")
br4nch.add.subject("Mall", "Food\nStore", "Vegetarian", "Bread")
br4nch.add.subject("Mall", "Food\nStore", "Vegan\nVegy", "Vegetables\nFruits")
br4nch.add.object("Mall", "Food\nStore", "Meat", "Cow", "Beef")
br4nch.add.object("Mall", "Food\nStore", "Meat", "Pig", "Pork")
br4nch.add.object("Mall", "Food\nStore", "Meat", "Pig", "Tail")
br4nch.add.object("Mall", "Food\nStore", "Vegetarian", "Cheese", "Goat Cheese\nMolten Goat Cheese")
br4nch.add.object("Mall", "Food\nStore", "Vegetarian", "Cheese", "Blue Cheese")
br4nch.add.object("Mall", "Food\nStore", "Vegetarian", "Milk", "Cow Milk\nGoat Milk")
br4nch.add.object("Mall", "Food\nStore", "Vegetarian", "Bread", "Brown Bread")
br4nch.add.object("Mall", "Food\nStore", "Vegetarian", "Bread", "White Bread")
br4nch.add.object("Mall", "Food\nStore", "Vegetarian", "Bread", "Baguette")
br4nch.add.object("Mall", "Food\nStore", "Vegan\nVegy", "Vegetables\nFruits", "Carrot")
br4nch.add.object("Mall", "Food\nStore", "Vegan\nVegy", "Vegetables\nFruits", "Potato")
br4nch.add.object("Mall", "Food\nStore", "Vegan\nVegy", "Vegetables\nFruits", "Onion")
br4nch.add.object("Mall", "Food\nStore", "Vegan\nVegy", "Vegetables\nFruits", "Broccoli")
br4nch.add.object("Mall", "Food\nStore", "Vegan\nVegy", "Vegetables\nFruits", "Tomato")
br4nch.add.object("Mall", "Food\nStore", "Vegan\nVegy", "Vegetables\nFruits", "Red Apple\nGreen Apple")

# Colors the Mall branch.
br4nch.set.color.branch("Mall", "magenta")
br4nch.set.color.header("Mall", "magenta", "bold")
br4nch.set.color.module("Mall", "Meat", "red", "bold", "underline")
br4nch.set.color.module("Mall", "Vegetarian", "green", "bold", "underline")
br4nch.set.color.module("Mall", "Vegan\nVegy", "cyan", "bold", "underline")
br4nch.set.color.subject("Mall", "Cheese", "yellow")
br4nch.set.color.subject("Mall", "all-Meat", "cyan")
br4nch.set.color.object("Mall", "all-Bread", "yellow", "bold")
br4nch.set.color.object("Mall", "Tomato", "red", "bold")
br4nch.set.color.object("Mall", "Broccoli", "green")
br4nch.set.color.object("Mall", "Blue Cheese", "blue", "underline")

# Displays the branches.
br4nch.run.display("all")
