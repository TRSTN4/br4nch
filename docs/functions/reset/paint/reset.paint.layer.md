# reset.paint.layer

To reset the paint of an layer, use the **following function:**

> br4nch.**reset**.**paint**.**layer**(*branch*, *position*)

**Required arguments:**

- branch - This is the argument where you specify the name of the branch(es) to reset the layer paint from.
- position - This is the argument where you specify the position(s) of the layer(s) to reset the paint from. For more information about positions, head to [positions](../../guides/positions.md).

Here's an example:

```python
>>> br4nch.reset.paint.layer(branch="MyBranch", position="1")
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../../guides/errors.md).

- InstanceStringError
- InvalidPositionError
- NotExistingBranchError
