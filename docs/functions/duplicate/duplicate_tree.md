# duplicate.Tree

To duplicate a tree, use the **following function:**

> br4nch.**duplicate**.**Tree**(*new_tree*, *target_tree*, *attributes=False*)

**Required argument(s):**

- *new_tree* - The name for the new tree.
- *target_tree* - The target tree that wil be copied.

**Optional argument(s):**

- *attributes* - If this argument is True, then the size and symbols are copied and linked to the new tree.

**Guide:**

> Specify the name for the new tree in the `new_tree` argument. To copy a tree, specify the name of the tree to be copied in the `target_tree` argument.
>
> ```python
> >>> br4nch.duplicate.Tree(new_tree="Copied", target_tree="MyBranch")
> 
> >>> br4nch.display.Tree(tree="Copied")
> Copy Me!
> ┣━ First layer
> ┃ˑˑ┣━ Just text
> ┃ˑˑ┗━ Two lines
> ┗━ Second layer
> ˑˑˑ┣━ Just text
> ˑˑˑ┗━ Two lines
> ```
>
> If the argument attributes is `True`, then the `size` and`symbols` are copied and linked to the new tree.
>
> ```python
> >>> br4nch.duplicate.branch(new_tree="CopiedAttr", target_tree="MyBranch", attributes=True)
> 
> >>> br4nch.display.branch(branch="CopiedAttr")
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

- InstanceStringError
- InstanceBooleanError
- InvalidTreeNameError
- DuplicateTreeError
- NotExistingTreeError

