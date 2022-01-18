# reset.paint.header

To reset the paint of an header, use the **following function:**

> br4nch.**reset**.**paint**.**header**(*branch*)

**Required argument(s):**

- *branch* - This is the argument where you specify the name of the branch(es) to reset the header paint from.

**Guide:**

> To reset the header paint, specify the branch name in the `branch` argument.
>
> ```python
> >>> br4nch.reset.paint.header(branch="MyBranch")
> ```
>
> To reset the header paint in multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.reset.paint.header(branch=["BranchOne", "BranchTwo"])
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- NotExistingBranchError

