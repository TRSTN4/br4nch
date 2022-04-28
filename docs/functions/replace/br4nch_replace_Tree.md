# br4nch.replace.Tree

To replace a branch, use the **following function:**

> br4nch.**replace**.**branch**(*branch*, *replace*)

**Required argument(s):**

- *branch* - The name of the branch to be replaced.
- *replace* - The new name for the branch.

**Guide:**

> To replace the name of a branch, specify the branch name in the `branch` argument and the new name for the branch in the `replace` argument.
>
> ```python
> >>> br4nch.replace.branch(branch="MyBranch", replace="ReplacedBranch")
> 
> >>> br4nch.display.branch(branch="ReplacedBranch")
> Just a header
> ┣━ ABCD
> ┃ˑˑ┣━ Just text
> ┃ˑˑ┗━ Two lines
> ┗━ Second layer
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- *InstanceStringError*
- *InvalidBranchNameError*
- *NotExistingBranchError*
- *DuplicateBranchError*

