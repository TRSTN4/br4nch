# set.paint.header

To set the paint of an header, use the **following function:**

> br4nch.**set**.**paint**.**header**(*branch*, *paint*)

**Required argument(s):**

- *branch* - The name of the branch(s) where the header paint will be applied.
- *paint* - The paint used for the header.

**Guide:**

> To set the header paint, first specify the branch name. Then you specify the paint in the `paint` argument.
>
> *For more information about paint, head to [paint](../../../guides/paint.md).*
>
> ```python
> >>> br4nch.set.paint.header(branch="MyBranch", paint="blue")
> ```
>
> To set the header paint in multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.set.paint.header(branch=["BranchOne", "BranchTwo"], paint="red")
> ```
>
> To use multiple types of paint in the same function call, you can use a list for the `paint` argument.
>
> ```python
> >>> br4nch.set.paint.header(branch="MyBranch", paint=["blue", "bold"])
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- NotExistingBranchError
- NotExistingPaintError
- MaximumPaintSlotsError

