# create.branch

To create a new branch, use the **following function:**

> br4nch.**create**.**branch**(*branch*, *header*)

**Required argument(s):**

- *branch* - The name for the branch(es).
- *header* - The header for the branch(es).

**Step(s) to reproduce the function:**

> To create a new branch you have to give the branch a name, we call the branch `MyBranch`. You also need to add a header to the branch, we call the header `My Header!`.
>
> ```python
> >>> br4nch.create.branch(branch="MyBranch", header="My Header!")
> ```
>
> To create multiple branches in the same function call, you can use a list for the branch argument.
>
> ```python
> >>> br4nch.create.branch(branch=["BranchOne", "BranchTwo"], header="My Header!")
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- InvalidBranchNameError
- NotExistingBranchError
- DuplicateBranchError

