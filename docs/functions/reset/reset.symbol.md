# reset.symbol

To reset one or multiple symbol(s), use the **following function:**

> br4nch.**reset**.**symbol**(*branch*, *line=True*, *split=True*, *end=True*)

**Required argument(s):**

- *branch* - The branch(es) whose symbol(s) should be reset.

**Optional argument(s):**

- *line* - If 'True', the line symbol is reset to the default line symbol.
- *split* - If 'True', the split symbol is reset to the default split symbol.
- *end* - If 'True', the end symbol is reset to the default end symbol.

**Guide:**

> To reset the symbols of the branch, specify the branch name in the `branch` argument.
>
> ```python
> >>> br4nch.reset.symbol(branch="MyBranch")
> ```
>
> For example, to reset only the `split` symbol, set the `line` and `end` symbols to 'False'.
>
> ```python
> >>> br4nch.reset.symbol(branch="MyBranch", line=False, end=False)
> ```
>
> To reset the symbols in multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.reset.symbol(branch=["BranchOne", "BranchTwo"])
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- InstanceBooleanError
- NotExistingBranchError

