# delete.branch

To delete a branch, use the **following function:**

> br4nch.**delete**.**branch**(*branch*)

**Required arguments:**

- branch - This is the argument where you specify the name of the branch(es) that will be deleted.

Here's an example:

```python
>>> br4nch.delete.branch(branch="MyBranch")
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- NotExistingBranchError

