# create.layer

To create a new layer, use the **following function:**

> br4nch.**create**.**layer**(*branch*, *layer*, *position*)

**Required arguments:**

- branch - This is the argument where you specify the name of the branch(es) to which the new layer will be created.
- layer - This is the argument where you specify the name for the new layer(s) that will be created.
- position - This is the argument where you specify the position where the layer(s) are created. For more information about positions, head to [positions](../../guides/positions.md).

Here's an example of the minimum/required arguments for this function:

```python
# Creates the layer 'MyLayer' in the branch 'MyBranch' at position '0'.
>>> br4nch.create.layer(branch="MyBranch", layer="MyLayer", position="0")
```

Here's an example for beginners:

```python
# First we need to create a branch, we will call the branch 'MyBranch' and the name of the header will be 'My custom header!'.
>>> br4nch.create.branch(branch="MyBranch", header="My custom header!")

# To create a layer to the branch, first specify the branch where the layer should be created, the name of the layer you want to create (we use the name 'Hello World!') and the position where the layer must be created. The position '0' indicates that the layer is created at the first height.
>>> br4nch.create.layer(branch="MyBranch", layer="Hello World!", position="0")

# To print the result of the branch created so far, specify the name of the branch you want to print. In this case the branch 'MyBranch'.
>>> br4nch.display.branch(branch="MyBranch")
My custom header!
┗━ Hello World!

# You can also create multiple layers at once by making a list and specifying it in the layer argument.
>>> br4nch.create.layer(branch="MyBranch", layer=["Apple", "Pear"], position="0")

>>> br4nch.display.branch(branch="MyBranch")
My custom header!
┣━ Hello World!
┣━ Apple
┗━ Pear

# To create a sublayer in for example the layer 'Hello World!', adjust the position to '1'. This is because the 'Hello World!' layer in place one is in the first height.
>>> br4nch.create.layer(branch="MyBranch", layer=["Checklist", "Tree"], position="1")

>>> br4nch.display.branch(branch="MyBranch")
My custom header!
┣━ Hello World!
┃  ┣━ Checklist
┃  ┗━ Tree
┣━ Apple
┗━ Pear

# To print the positions of all layers in a branch, the function 'display.assist' is used.
>>> br4nch.display.assist(branch="MyBranch")
0: My custom header!
┣━ 1: Hello World!
┃  ┣━ 1.1: Checklist
┃  ┗━ 1.2: Tree
┣━ 2: Apple
┗━ 3: Pear

# To create another sublayer in for example the layer 'Tree', adjust the position to '1.2'. (See example above).
>>> br4nch.create.layer(branch="MyBranch", layer="Birds", position="1.2")

>>> br4nch.display.branch(branch="MyBranch")
My custom header!
┣━ Hello World!
┃  ┣━ Checklist
┃  ┗━ Tree
┃     ┗━ Birds
┣━ Apple
┗━ Pear

# You can even use newlines/'\n' in a layer.
>>> br4nch.create.layer(branch="MyBranch", layer="One\nTwo\nThree", position="1.1")

>>> br4nch.display.branch(branch="MyBranch")
My custom header!
┣━ Hello World!
┃  ┣━ Checklist
┃  ┃  ┗━ One
┃  ┃     Two
┃  ┃     Three
┃  ┗━ Tree
┃     ┗━ Birds
┣━ Apple
┗━ Pear
```

Here's an example when the function is used in a real situation:

```python
# Creates the 'Stream' branch.
>>> br4nch.add.branch(branch="Stream", header="Movies & Series")

# Creates multiple layers in the 'Stream' branch.
>>> br4nch.add.layer(branch="Stream", layer=["Netflix", "Prime Video"], position="0")
>>> br4nch.add.layer(branch="Stream", layer=["Movies", "Series"], position="*")
>>> br4nch.add.layer(branch="Stream", layer="Interstellar", position="1.1")
>>> br4nch.add.layer(branch="Stream", layer=["Squid Game", "The Crown"], position="1.2")
>>> br4nch.add.layer(branch="Stream", layer=["Tenet", "Parasite"], position="2.1")
>>> br4nch.add.layer(branch="Stream", layer="The Walking Dead", position="2.2")

# Prints the 'Stream' branch.
>>> br4nch.display.branch(branch="Stream")
Movies & Series
┣━ Netflix
┃  ┣━ Movies
┃  ┃  ┗━ Interstellar
┃  ┗━ Series
┃     ┣━ Squid Game
┃     ┗━ The Crown
┗━ Prime Video
   ┣━ Movies
   ┃  ┣━ Tenet
   ┃  ┗━ Parasite
   ┗━ Series
      ┗━ The Walking Dead
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- InvalidPositionError
- NotExistingBranchError

