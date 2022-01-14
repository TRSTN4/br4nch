# delete.layer

To delete an layer, use the **following function:**

> br4nch.**delete**.**layer**(*branch*, *position*)

**Required arguments:**

- branch - This is the argument where you specify the name of the branch(es) to which the layer will be deleted.
- position - This is the argument where you specify the position(s) where the layer(s) will be deleted. For more information about positions, head to [positions](../../guides/positions.md).

Here's an example of the minimum/required arguments for this function:

```python
# Deletes the layer attatched to the position '1' in the branch 'MyBranch'.
>>> br4nch.delete.layer(branch="MyBranch", position="1")
```

Here's an example for beginners:

```python
# To delete a branch, specify the name of the branch in the branch argument.
>>> br4nch.delete.branch(branch="MyBranch")

# You can also delete multiple branches at once by making a list and specifying it in the branch argument.
>>> br4nch.delete.branch(branch=["BranchOne", "BranchTwo"])
```

Here's an example when the function is used in a real situation:

```python
# Creates the 'Board' branch.
>>> br4nch.create.branch(branch="Board", header="Information")

# Creates multiple layers in the 'Board' branch.
>>> br4nch.create.layer(branch="Board", layer=["Animals", "Food"], position="0")
>>> br4nch.create.layer(branch="Board", layer=["Dog", "Cat"], position="1")
>>> br4nch.create.layer(branch="Board", layer="Bread", position="2")

# Prints the 'Board' branch.
>>> br4nch.display.branch(branch="Board")
Information
┣━ Animals
┃  ┣━ Dog
┃  ┗━ Cat
┗━ Food
   ┗━ Bread

# Deletes the layer attatched to the position '1' in the branch 'Board'.
>>> br4nch.delete.layer(branch="Board", position="1")

# Prints the 'Board' branch.
>>> br4nch.display.branch(branch="Board")
Information
┗━ Food
   ┗━ Bread
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- InvalidPositionError
- NotExistingBranchError

