# replace.layer

To replace a layer, use the **following function:**

> br4nch.**replace**.**layer**(*branch*, *position*, *name*)

**Required arguments:**

- branch - This is the argument where you specify the name of the branch(es) whose layer(s) is replaced with a new name.
- position - This is the argument where you specify the position(s) where to replace the layer(s). For more information about positions, head to [positions](../../guides/positions.md).

- name - This is the argument where you specify the new name of the layer(s).

Here's an example:

```python
>>> br4nch.replace.layer(branch="MyBranch", position="1", name="ReplacedLayer")
```

Here is an example in realistic usage:

```python
# Original.
>> br4nch.add.branch(branch="MyBranch", header="Just a header")
>>> br4nch.add.layer(branch="MyBranch", layer=["First layer", "Second layer"], position="0")
>>> br4nch.add.layer(branch="MyBranch", layer=["Just text", "Two lines"], position="1")

>>> br4nch.display.branch(branch="MyBranch")
Just a header
┣━ First layer
┃  ┣━ Just text
┃  ┗━ Two lines
┗━ Second layer

# Replaced.
>>> br4nch.replace.layer(branch="MyBranch", position="1", name="Replaced Layer!!")

>>> br4nch.display.branch(branch="MyBranch")
Just a header
┣━ Replaced Layer!!
┃  ┣━ Just text
┃  ┗━ Two lines
┗━ Second layer
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- InvalidPositionError
- NotExistingBranchError
