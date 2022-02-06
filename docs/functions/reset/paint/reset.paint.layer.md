# reset.paint.layer

To reset the paint of an layer, use the **following function:**

> br4nch.**reset**.**paint**.**layer**(*branch*, *position*)

**Required argument(s):**

- *branch* - The name of the branch(es) to reset the layer paint from.
- *position* - The position(s) of the layer(s) to reset the paint from.

**Guide:**

> To reset the layer paint, specify the branch name in the `branch` argument and specify the position of the layer.
>
> *For more information about positions, head to [positions](../../guides/positions.md).*
>
> ```python
> >>> br4nch.reset.paint.layer(branch="MyBranch", position="1.2")
> ```
>
> To reset the layer paint for multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.reset.paint.layer(branch=["BranchOne", "BranchTwo"], position="1.2")
> ```
>
> To reset the layer paint for multiple positions in the same function call, you can use a list for the `positions` argument.
>
> ```python
> >>> br4nch.reset.paint.layer(branch="MyBranch", position=["1.2", "2.3"])
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
For more information about errors, head to [errors](../../guides/errors.md).

- *InstanceStringError*
- *InvalidPositionError*
- *NotExistingBranchError*
