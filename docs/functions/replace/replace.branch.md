# replace.branch

To replace a branch, use the **following function:**

> br4nch.**replace**.**branch**(*branch*, *name*)

**Required arguments:**

- branch - This is the argument where you specify the name of the branch that will be replaced with a new name.
- name - This is the argument where you specify the name of the new branch.

Here's an example:

```python
>>> br4nch.replace.branch(branch="MyBranch", name="MyNewBranch")
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- InvalidBranchNameError
- NotExistingBranchError
- DuplicateBranchError

