# add.branch

To create a new branch, use the **following function:**

> br4nch.**add**.**branch**(*branch*, *header*)

**Required arguments:**

- branch - This is the argument where you specify the name of the new branch(es) that will be created.
- header - This is the argument where you specify the header name for the branch.

Here's an example:

```python
>>> br4nch.add.branch(branch="MyBranch", header="MyHeader")
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError

- InvalidBranchNameError
- NotExistingBranchError
- DuplicateBranchError

