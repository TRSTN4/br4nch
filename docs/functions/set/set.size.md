# set.size

To set an size, use the **following function:**

> br4nch.**set**.**size**(*branch*, *size*)

**Required arguments:**

- branch - This is the argument where you specify the branch(es) whose size should be reset.
- size - This is the argument where you specify the size of the branch(es).

Here's an example:

```python
>>> br4nch.set.size(branch="MyBranch", size=1)
```

Here is an example in realistic usage:

```python
>>> br4nch.add.branch(branch="MyBranch", header="Just a header")
>>> br4nch.add.layer(branch="MyBranch", layer=["First layer", "Second layer"], pos="0")
>>> br4nch.add.layer(branch="MyBranch", layer=["Just text", "Two lines"], pos="1")

>>> br4nch.set.size(branch="MyBranch", size=1)

>>> br4nch.display.branch(branch="MyBranch")
Just a header
┃
┣━━ First layer
┃   ┃
┃   ┣━━ Just text
┃   ┃
┃   ┗━━ Two lines
┃
┗━━ Second layer
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- InstanceIntegerError
- InvalidSizeError
- NotExistingBranchError

