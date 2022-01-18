# set.size

To set an size, use the **following function:**

> br4nch.**set**.**size**(*branch*, *size*)

**Required argument(s):**

- branch - The branch(es) where the symbols are added.
- size - The size of the space in the branch structure.

**Guide:**

> To add sizes, you must specify the name of the branch(es) and the size of the `size` argument.
>
> ```python
> >>> br4nch.set.size(branch="MyBranch", size=1)
> 
> >>> br4nch.display.branch(branch="MyBranch")
> Just a header
> ┃
> ┣━━ First layer
> ┃   ┃
> ┃   ┣━━ Just text
> ┃   ┃
> ┃   ┗━━ Two lines
> ┃
> ┗━━ Second layer
> ```
>
> To set the size for multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.set.size(branch=["BranchOne", "BranchTwo"], size=1)
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- InstanceIntegerError
- InvalidSizeError
- NotExistingBranchError

