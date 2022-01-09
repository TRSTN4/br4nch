# set.paint.header

To set the paint of an header, use the **following function:**

> br4nch.**set**.**paint**.**header**(*branch*, *paint*)

**Required arguments:**

- branch - This is the argument where you specify the name of the branch(es) to set the header paint from.
- paint - This is the argument where you specify the paint for the header. For more information about paint, head to [paint](../../../guides/paint.md).

Here's an example:

```python
>>> br4nch.set.paint.header(branch="MyBranch", paint=["blue", "bold"])
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../../guides/errors.md).

- InstanceStringError
- NotExistingBranchError
- NotExistingPaintError
- MaximumPaintSlotsError

