# delete.Tree

To delete a tree, use the **following function:**

> br4nch.**delete**.**Tree**(*tree*)

**Required argument(s):**

- *tree* - The name of the tree(s) that will be deleted.

**Guide:**

> To delete a tree, specify the tree name.
>
> ```python
> >>> br4nch.delete.Tree(tree="MyTree")
> 
> >>> br4nch.display.Tree(tree="MyTree")
> NotExistingTreeError: The tree: 'MyTree' does not exists.
> ```
>
> To delete multiple trees in the same function call, you can use a list for the `tree` argument.
>
> ```python
> >>> br4nch.delete.Tree(tree=["TreeOne", "TreeTwo"])
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- *InstanceStringError*
- *NotExistingBranchError*
