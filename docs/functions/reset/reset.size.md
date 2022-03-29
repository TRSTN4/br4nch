# reset.size

To reset an size, use the **following function:**

> br4nch.**reset**.**size**(*branch*)

**Required argument(s):**

- *branch* - The branch(es) whose size should be reset.

**Guide:**

> To reset the size of the branch, specify the branch name in the `branch` argument.
>
> ```python
> >>> br4nch.reset.size(branch="MyBranch")
> ```
>
> To reset the size for multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.reset.size(branch=["BranchOne", "BranchTwo"])
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- *InstanceStringError*
- *NotExistingBranchError*

