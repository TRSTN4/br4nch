# reset.Size

To reset an size, use the **following function:**

> br4nch.**reset**.**Size**(*tree*)

**Required argument(s):**

- *tree* - The tree(s) whose size should be reset.

**Guide:**

> To reset the size of the tree, specify the tree name in the `tree` argument.
>
> ```python
> >>> br4nch.reset.Size(tree="MyTree")
> ```
>
> To reset the size for multiple trees in the same function call, you can use a list for the `tree` argument.
>
> ```python
> >>> br4nch.reset.Size(tree=["TreeOne", "TreeTwo"])
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- *InstanceStringError*
- *NotExistingBranchError*

