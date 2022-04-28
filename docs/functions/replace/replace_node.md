# replace.Node

To replace a node, use the **following function:**

> br4nch.**replace**.**Node**(*tree*, *new_node*, *target_node*)

**Required argument(s):**

- *tree* - The name of the tree(s) whose node(s) will be replaced.
- *new_node* - The new name for the node(s).
- *target_node* - The position(s) where the node(s) in the tree(s) will be replaced.

**Guide:**

> To replace the node(s) name(s), specify the tree name in the `tree` argument and the new name for the node(s) in the `new_node` argument. You also need to specify the target node(s) in the `target_node` argument.
>
> For more information about parents/positions, head to [positions](../../guides/positions.md).
>
> ```python
> >>> br4nch.replace.Node(tree="MyTree", new_node="Replaced layer!", target_node="First layer")
> 
> >>> br4nch.display.Tree(tree="MyTree")
> Replaced Header!
> ┣━ Replaced layer!
> ┃ˑˑ┣━ Just text
> ┃ˑˑ┗━ Two lines
> ┗━ Second layer
> ```
>
> To replace the node(s) for multiple trees in the same function call, you can use a list for the `tree` argument.
>
> ```python
> >>> br4nch.replace.Node(tree=["TreeOne", "TreeTwo"], new_node="Replaced layer!", target_node="Test Two")
> 
> >>> br4nch.display.Tree(tree=["TreeOne", "TreeTwo"])
> Tree One
> ┣━ Alpha
> ┃ˑˑ┣━ Test One
> ┃ˑˑ┗━ Replaced layer!
> ┗━ Beta
> Tree Two
> ┣━ Alpha
> ┃ˑˑ┣━ Test One
> ┃ˑˑ┗━ Replaced layer!
> ┗━ Beta
> ```
>
> To replace multiple target node(s) in the same function call, you can use a list for the `target_node` argument.
>
> ```python
> >>> br4nch.replace.Node(tree="MyTree", new_node="Replaced This layer too!", target_node=["ABC", "DEF"])
> 
> >>> br4nch.display.Tree(tree="MyTree")
> Replaced Header!
> ┣━ Replaced layer!
> ┃ˑˑ┣━ Replaced This layer too!
> ┃ˑˑ┗━ Replaced This layer too!
> ┗━ Second layer
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- *InstanceStringError*
- *InvalidPositionError*
- *NotExistingBranchError*
