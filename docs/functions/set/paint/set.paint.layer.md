# set.paint.layer

To set the paint of an layer, use the **following function:**

> br4nch.**set**.**paint**.**layer**(*branch*, *position*, *paint*)

**Required argument(s):**

- *branch* - The name of the branch(s) where the layer paint will be applied.
- *position* - The position(s) where the layer paint will be applied.
- *paint* - The paint used for the layer(s).

**Guide:**

> To set the layer paint, you must specify the branch. You must also indicate the position(s) of the layer.
>
> *For more information about positions, head to [positions](../../../guides/positions.md).*
> *For more information about paint, head to [paint](../../../guides/paint.md).*
>
> ```python
> >>> br4nch.set.paint.layer(branch="MyBranch", position="1.2", paint="blue")
> ```
>
> To set the layer paint in multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.set.paint.layer(branch=["BranchOne", "BranchTwo"], position="1.2", paint="blue")
> ```
>
> To set the layer paint in multiple positions in the same function call, you can use a list for the `position` position.
>
> ```python
> >>> br4nch.set.paint.layer(branch="MyBranch", position=["1.2", "2.3"], paint="blue")
> ```
>
> To set the multiple paint in the same function call, you can use a list for the `paint` position.
>
> ```python
> >>> br4nch.set.paint.layer(branch="MyBranch", position="1.2", paint=["blue", "bold"])
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
For more information about errors, head to [errors](../../guides/errors.md).

- *InstanceStringError*
- *InvalidPositionError*
- *NotExistingBranchError*
- *NotExistingPaintError*
- *MaximumPaintSlotsError*
