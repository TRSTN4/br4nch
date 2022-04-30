# set.Size

To set an size, use the **following function:**

> br4nch.**set**.**Size**(*tree*, *size*)

**Required argument(s):**

- *tree* - The tree(s) where the symbols are added.
- *size* - The size of the space in the tree structure.

**Guide:**

> To add sizes, you must specify the name of the tree(s) and the size of the `size` argument.
>
> ```python
> >>> br4nch.set.Size(tree="MyTree", size=1)
> 
> >>> br4nch.display.Tree(tree="MyTree")
> Just a header
> ┃
> ┣━━ First layer
> ┃ˑˑˑ┃
> ┃ˑˑˑ┣━━ Just text
> ┃ˑˑˑ┃
> ┃ˑˑˑ┗━━ Two lines
> ┃
> ┗━━ Second layer
> ```
>
> To set the size for multiple trees in the same function call, you can use a list for the `tree` argument.
>
> ```python
> >>> br4nch.set.Size(tree=["TreeOne", "TreeTwo"], size=1)
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- InstanceIntegerError
- InstanceStringError
- InvalidSizeError
- NotExistingTreeError
- NotSizeableError

