# set.paint.layer

To set the paint of an layer, use the **following function:**

> br4nch.**set**.**paint**.**layer**(*branch*, *position*, *paint*)

**Required arguments:**

- branch - This is the argument where you specify the name of the branch(es) to set the layer paint from.
- position - This is the argument where you specify the position(s) of the layer(s) to set the paint from. For more information about positions, head to [positions](../../../guides/positions.md).
- paint - This is the argument where you specify the paint for the layer. For more information about paint, head to [paint](../../../guides/paint.md).

Here's an example:

```python
>>> br4nch.set.paint.layer(branch="MyBranch", position="1", paint=["blue", "bold"])
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../../guides/errors.md).

- InstanceStringError
- InvalidPositionError
- NotExistingBranchError
- NotExistingPaintError
- MaximumPaintSlotsError
