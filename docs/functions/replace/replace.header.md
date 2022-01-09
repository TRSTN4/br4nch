# replace.header

To replace a header, use the **following function:**

> br4nch.**replace**.**header**(*branch*, *name*)

**Required arguments:**

- branch - This is the argument where you specify the name of the branch(es) whose header is replaced with a new name.
- name - This is the argument where you specify the name of the new header.

Here's an example:

```python
>>> br4nch.replace.header(branch="MyBranch", name="MyNewHeader")
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- NotExistingBranchError

