# replace.layer

To replace a layer, use the **following function:**

> br4nch.**replace**.**layer**(*branch*, *replace*, *position*)

**Required argument(s):**

- *branch* - The name of branch(es) whose layer(s) is to be replaced.
- *position* - The position(s) where the layer(s) in the branch(es) are replaced.

- *replace* - The new name for the layer(s).

**Guide:**

> To replace the layer(s) name(s), specify the branch name in the `branch` argument and the new name for the layer(s) in the `replace` argument.
>
> For more information about positions, head to [positions](../../guides/positions.md).
>
> ```python
> >>> br4nch.replace.layer(branch="MyBranch", position="1", replace="Replaced layer!")
> 
> >>> br4nch.display.branch(branch="MyBranch")
> Replaced Header!
> ┣━ Replaced layer!
> ┃  ┣━ Just text
> ┃  ┗━ Two lines
> ┗━ Second layer
> ```
>
> To replace layers for multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.replace.layer(branch=["BranchOne", "BranchTwo"], position="1.2", replace="Replaced layer!")
> 
> >>> br4nch.display.branch(branch=["BranchOne", "BranchTwo"])
> Branch One
> ┣━ Alpha
> ┃  ┣━ Charlie
> ┃  ┗━ Replaced layer!
> ┗━ Beta
> Branch Two
> ┣━ Alpha
> ┃  ┣━ Charlie
> ┃  ┗━ Replaced layer!
> ┗━ Beta
> ```
>
> To replace the layer(s) for multiple position in the same function call, you can use a list for the `position` argument.
>
> ```python
> >>> br4nch.replace.layer(branch="MyBranch", position=["1.1", "1.2"], replace="Replaced This layer too!")
> 
> >>> br4nch.display.branch(branch="MyBranch")
> Replaced Header!
> ┣━ Replaced layer!
> ┃  ┣━ Replaced This layer too!
> ┃  ┗━ Replaced This layer too!
> ┗━ Second layer
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
For more information about errors, head to [errors](../../guides/errors.md).

- *InstanceStringError*
- *InvalidPositionError*
- *NotExistingBranchError*
