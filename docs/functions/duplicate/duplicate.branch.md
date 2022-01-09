# duplicate.branch

To duplicate a branch, use the **following function:**

> br4nch.**duplicate**.**branch**(*branch*, *name*, *package=False*)

**Required arguments:**

- branch - This is the argument where you specify the name of the branch to duplicate.
- name - This is the argument where you specify the name of the new branch.

**Optional arguments:**

- package - If this argument is 'True', then the size, symbols and paint are also duplicated and linked to the duplicated branch.

Here's an example:

```python
>>> br4nch.duplicate.branch(branch="MyBranch", name="MyCopiedBranch")
```

Here is an example in realistic usage:

```python
>>> br4nch.add.branch(branch="MyBranch", header="Copy Me!")
>>> br4nch.add.layer(branch="MyBranch", layer=["First layer", "Second layer"], position="0")
>>> br4nch.add.layer(branch="MyBranch", layer=["Just text", "Two lines"], position="*")

>>> br4nch.set.size(branch="MyBranch", size=1)

>>> br4nch.duplicate.branch(branch="MyBranch", name="MyBranchCopied", package=True)
>>> br4nch.duplicate.branch(branch="MyBranch", name="MyBranchCopiedTwo")

>>> br4nch.display.branch(branch="*")
Copy Me!
┃
┣━━ First layer
┃   ┃
┃   ┣━━ Just text
┃   ┃
┃   ┗━━ Two lines
┃
┗━━ Second layer
    ┃
    ┣━━ Just text
    ┃
    ┗━━ Two lines
Copy Me!
┃
┣━━ First layer
┃   ┃
┃   ┣━━ Just text
┃   ┃
┃   ┗━━ Two lines
┃
┗━━ Second layer
    ┃
    ┣━━ Just text
    ┃
    ┗━━ Two lines
Copy Me!
┣━ First layer
┃  ┣━ Just text
┃  ┗━ Two lines
┗━ Second layer
   ┣━ Just text
   ┗━ Two lines
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- InstanceBooleanError
- NotExistingBranchError

