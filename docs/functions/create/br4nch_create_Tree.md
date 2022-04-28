# br4nch.create.Tree

To create a new tree, use the **following function:**

> br4nch.**create**.**Tree**(*tree*, *header*)

**Required argument(s):**

- *tree* - The name for the tree.
- *header* - The header for the tree.

**Guide:**

> To create a new tree you have to give the tree a name, we call the tree `MyBranch`. You also need to add a header to the tree, we call the header `My Header!`.
>
> ```python
> >>> br4nch.create.Tree(tree="MyTree", header="My Header!")
> ```
>
> To create multiple trees in the same function call, you can use a list for the `tree` argument.
>
> ```python
> >>> br4nch.create.Tree(tree=["TreeOne", "TreeTwo"], header="My Header!")
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- *InstanceStringError*
- *InvalidBranchNameError*
- *NotExistingBranchError*
- *DuplicateBranchError*

