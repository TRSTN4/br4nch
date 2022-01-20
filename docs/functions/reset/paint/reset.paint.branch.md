# reset.paint.branch

To reset the paint of an branch, use the **following function:**

> br4nch.**reset**.**paint**.**branch**(*branch*)

**Required argument(s):**

- *branch* - This name of the branch(es) to reset the branch paint from.

**Guide:**

> To reset the branch paint, specify the branch name in the `branch` argument.
>
> ```python
> >>> br4nch.reset.paint.branch(branch="MyBranch")
> ```
>
> To reset the branch paint for multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.reset.paint.branch(branch=["BranchOne", "BranchTwo"])
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
For more information about errors, head to [errors](../../guides/errors.md).

- *InstanceStringError*
- *NotExistingBranchError*

