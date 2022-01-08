# duplicate.layer

To duplicate a layer, use the **following function:**

> br4nch.**duplicate**.**layer**(*branch*, *duplicate*, *position*, *put=""*, *paint=False*, *delete=False*)

**Required arguments:**

- branch - This is the argument where you specify the name of the branch(es) where the layer(s) to be copied are located.
- duplicate - This is the argument where you specify the position(s) of the layer(s) to be duplicated. For more information about positions, head to [positions](../../guides/positions.md).
- position - This is the argument where you specify the position(s) where to add the duplicated layer(s). For more information about positions, head to [positions](../../guides/positions.md).

**Optional arguments:**

- put -  This is the argument where you specify the name of the branch(es) where the copied layer(s) will be placed at the chosen position(s).
- paint - If this argument is 'True', the paint is duplicated and linked to the duplicated layer(s).
- delete - If this argument is 'True', then the layer(s) in the original place will be deleted.

Here's an example:

```python
>>> br4nch.duplicate.layer(branch="MyBranch", duplicate="2", position="1.1")
```

Here is an example in realistic usage:

```python
>>> br4nch.add.branch(branch="MyBranch", header="Just a header")
>>> br4nch.add.layer(branch="MyBranch", layer=["First layer", "Second layer"], position="0")
>>> br4nch.add.layer(branch="MyBranch", layer=["Just text", "Two lines"], position="1")

>>> br4nch.display.branch(branch="MyBranch")
Just a header
┣━ First layer
┃  ┣━ Just text
┃  ┗━ Two lines
┗━ Second layer

>>> br4nch.duplicate.layer(branch="MyBranch", duplicate="1.1", position="0")

>>> br4nch.display.branch(branch="MyBranch")
Just a header
┣━ First layer
┃  ┣━ Just text
┃  ┗━ Two lines
┣━ Second layer
┗━ Just text

# Second branch.
>>> br4nch.add.branch(branch="Park", header="Zoo")
>>> br4nch.add.layer(branch="Park", layer=["Animals", "Tickets"], position="0")
>>> br4nch.add.layer(branch="Park", layer=["Koala", "Elephant"], position="1")
>>> br4nch.add.layer(branch="Park", layer="Regular", position="2")

>>> br4nch.display.branch(branch="*")
Zoo
┣━ Animals
┃  ┣━ Koala
┃  ┗━ Elephant
┗━ Tickets
   ┗━ Regular

# Using the put argument.
br4nch.duplicate.layer(branch="MyBranch", duplicate="1.2", position="2", put="Park")

>>> br4nch.display.branch(branch="*")
Just a header
┣━ First layer
┃  ┣━ Just text
┃  ┗━ Two lines
┗━ Second layer
Zoo
┣━ Animals
┃  ┣━ Koala
┃  ┗━ Elephant
┗━ Tickets
   ┣━ Regular
   ┗━ Two lines
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- InstanceBooleanError
- InvalidPositionError
- NotExistingBranchError
