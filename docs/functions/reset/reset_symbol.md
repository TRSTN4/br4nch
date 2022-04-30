# reset.Symbol

To reset one or multiple symbol(s), use the **following function:**

> br4nch.**reset**.**symbol**(*tree*, *line=True*, *split=True*, *end=True*)

**Required argument(s):**

- *tree* - The tree(s) whose symbol(s) should be reset.

**Optional argument(s):**

- *line* - If 'True', the line symbol is reset to the default line symbol.
- *split* - If 'True', the split symbol is reset to the default split symbol.
- *end* - If 'True', the end symbol is reset to the default end symbol.

**Guide:**

> To reset the symbols of the tree, specify the tree name in the `tree` argument.
>
> ```python
> >>> br4nch.reset.Symbol(tree="MyTree")
> ```
>
> For example, to reset only the `split` symbol, set the `line` and `end` symbols to 'False'.
>
> ```python
> >>> br4nch.reset.Symbol(tree="MyTree", line=False, end=False)
> ```
>
> To reset the symbols for multiple trees in the same function call, you can use a list for the `tree` argument.
>
> ```python
> >>> br4nch.reset.Symbol(tree=["TreeOne", "TreeTwo"])
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- InstanceBooleanError
- InstanceStringError
- NotExistingTreeError

