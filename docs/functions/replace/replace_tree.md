# replace.Tree

To replace a tree, use the **following function:**

> br4nch.**replace**.**Tree**(*new_tree*, *target_tree*)

**Required argument(s):**

- *new_tree* - The name of the tree to be replaced.
- *target_tree* - The new name for the tree.

**Guide:**

> To replace the name of a tree, specify the new name for the tree in the `new_tree` argument and specify the target tree name in the `target_tree` argument.
>
> ```python
> >>> br4nch.replace.Tree(new_tree="ReplacedTree", target_tree="MyTree")
> 
> >>> br4nch.display.Tree(tree="ReplacedTree")
> Just a header
> ┣━ ABCD
> ┃ˑˑ┣━ Just text
> ┃ˑˑ┗━ Two lines
> ┗━ Second layer
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- InstanceStringError
- InvalidTreeNameError
- DuplicateTreeError
- NotExistingTreeError

