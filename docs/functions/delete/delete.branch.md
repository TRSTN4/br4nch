# delete.branch

To delete a branch, use the **following function:**

> br4nch.**delete**.**branch**(*branch*)

**Required argument(s):**

- *branch* - The name of the branch(es) that will be deleted.

**Guide:**

> To delete a branch, specify the branch name.
>
> ```python
> >>> br4nch.delete.branch(branch="MyBranch")
> 
> >>> br4nch.display.branch(branch="MyBranch")
> NotExistingBranchError: The branch: 'MyBranch' does not exists.
> ```
>
> To delete multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.delete.branch(branch=["BranchOne", "BranchTwo"])
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- NotExistingBranchError
