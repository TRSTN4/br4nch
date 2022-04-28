# br4nch.duplicate.Tree

To duplicate a branch, use the **following function:**

> br4nch.**duplicate**.**branch**(*branch*, *name*, *package=False*)

**Required argument(s):**

- *branch* - The name of the branch being copied.
- *name* - The name for the new branch.

**Optional argument(s):**

- *package* - If this argument is True, then the size, symbols and paint are also copied and linked to the new branch.

**Guide:**

> To copy a branch, specify the name of the branch to be copied in the `branch` argument. You also specify the name of what the copied branch should be called in the `name` argument.
>
> ```python
> >>> br4nch.duplicate.branch(branch="MyBranch", name="CopiedOne")
> 
> >>> br4nch.display.branch(branch="CopiedOne")
> Copy Me!
> ┣━ First layer
> ┃ˑˑ┣━ Just text
> ┃ˑˑ┗━ Two lines
> ┗━ Second layer
> ˑˑˑ┣━ Just text
> ˑˑˑ┗━ Two lines
> ```
>
> If the argument package is `True`, then the `size`, `symbols` and `paint` are also copied and linked to the new branch.
>
> ```python
> >>> br4nch.duplicate.branch(branch="MyBranch", name="CopiedTwo", package=True)
> 
> >>> br4nch.display.branch(branch="CopiedTwo")
> Copy Me!
> ┃
> ┣━━ First layer
> ┃ˑˑˑ┃
> ┃ˑˑˑ┣━━ Just text
> ┃ˑˑˑ┃
> ┃ˑˑˑ┗━━ Two lines
> ┃
> ┗━━ Second layer
> ˑˑˑˑ┃
> ˑˑˑˑ┣━━ Just text
> ˑˑˑˑ┃
> ˑˑˑˑ┗━━ Two lines
> ```
>

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- *InstanceStringError*
- *InstanceBooleanError*
- *InvalidBranchNameError*
- *DuplicateBranchError*
- *NotExistingBranchError*

