# delete.Node

To delete an node, use the **following function:**

> br4nch.**delete**.**Node**(*tree*, *node*)

**Required argument(s):**

- *tree* - The name of the tree(s) where the node(s) will be deleted.
- *node* - The node(s) that will be deleted.

**Guide:**

> To delete a node, specify the node you want to delete.
>
> *For more information about node positions, head to [positions](../../guides/positions.md).*
>
> ```python
> >>> br4nch.display.Tree(tree="Board")
> Information
> ┣━ Animals
> ┃ˑˑ┣━ Dog
> ┃ˑˑ┗━ Cat
> ┣━ Food
> ┗━ Bread
> 
> >>> br4nch.delete.Node(tree="Board", node="Animals")
> 
> >>> br4nch.display.Tree(tree="Board")
> Information
> ┣━ Food
> ┗━ Bread
> ```
>

> To delete the given node(s) in multiple trees in the same function call, you can use a list for the `tree` argument.
>
> ```python
> >>> br4nch.delete.Node(tree=["TreeOne", "TreeTwo"], node="Test")
> ```
>

> To delete multiple nodes in the same function call, you can use a list for the `node` argument.
>
> ```python
> >>> br4nch.delete.Node(tree="TestTree", node=["First", "Second", "Third"])
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- InstanceStringError

- NotExistingTreeError

- InvalidPositionError

  

