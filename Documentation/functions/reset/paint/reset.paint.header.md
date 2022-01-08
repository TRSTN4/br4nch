# reset.paint.header

To reset the paint of an header, use the **following function:**

> br4nch.**reset**.**paint**.**header**(*branch*)

**Required arguments:**

- branch - This is the argument where you specify the name of the branch(es) to reset the header paint from.

Here's an example:

```python
>>> br4nch.reset.paint.header(branch="MyBranch")
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../../guides/errors.md).

- InstanceStringError
- NotExistingBranchError

