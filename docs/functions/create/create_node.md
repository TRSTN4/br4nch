# create.Node

To create a new node, use the **following function:**

> br4nch.**create**.**Node**(*tree*, *node*, *parent=""*)

**Required argument(s):**

- *tree* - The name of the tree(s) where the node(s) will be created.
- *node* - The name for the node(s).

**Optional argument(s):**

- *parent* - The parent(s) where the node(s) in the tree(s) are created.

**Guide:**

> To add a new node for a tree, first indicate in which tree the node should be created, We use the tree `MyTree`. Then you specify the name of the node(s) you want to create.
>
> ```python
> >>> br4nch.create.Node(tree="MyTree", node="My Node")
> 
> >>> br4nch.display.Tree(tree="MyTree")
> My header!
> ┗━ My Node
> ```
>

> You can also specify the parent where the node should be created in the tree. 
>
> *For more information about parents/positions, head to [positions](../../guides/positions.md).*
>
> ```python
> >>> br4nch.create.Node(tree="MyTree", node="Set node", parent="My node")
> 
> >>> br4nch.display.Tree(tree="MyTree")
> My header!
> ┗━ My Node
> ˑˑˑ┗━ Set node
> ```
>

> You can also use `\n` in a node name.
>
> ```python
> >>> br4nch.create.Node(tree="MyTree", node="One\nTwo\nThree")
> 
> >>> br4nch.display.Tree(tree="MyTree")
> My header!
> ┣━ My node
> ┃ˑˑ┗━ Set node
> ┗━ One
> ˑˑˑTwo
> ˑˑˑThree
> ```
>

> To create the node(s) in multiple trees in the same function call, you can use a list for the `tree` argument.
>
> ```python
> >>> br4nch.create.Node(tree=["ZooA", "ZooB"], node="Animals")
> 
> >>> br4nch.display.Tree(tree=["ZooA", "ZooB"])
> Zoo Alpha
> ┗━ Animals
> Zoo Beta
> ┗━ Animals
> ```
>

> To create multiple node in the same function call, you can use list for the `node` argument.
>
> ```python
> >>> br4nch.create.Node(tree="MyTree", node=["Subnode One", "Subnode Two"], parent="My node")
> 
> >>> br4nch.display.Tree(tree="MyTree")
> My header!
> ┣━ My node
> ┃ˑˑ┣━ Set node
> ┃ˑˑ┣━ Subnode One
> ┃ˑˑ┗━ Subnode Two
> ┗━ One
> ˑˑˑTwo
> ˑˑˑThree
> ```
>

> To create the node(s) for multiple parents in the same function call, you can use a list for the `parent` argument.
>
> ```python
> >>> br4nch.create.Node(tree="MyTree", node="Last Node", parent=["Subnode One", "Subnode Two"])
> 
> >>> br4nch.display.Tree(tree="MyTree")
> My header!
> ┣━ My node
> ┃ˑˑ┣━ Set node
> ┃ˑˑ┣━ Subnode One
> ┃ˑˑ┃ˑˑ┗━ Last node
> ┃ˑˑ┗━ Subnode Two
> ┃ˑˑˑˑˑ┗━ Last node
> ┗━ One
> ˑˑˑTwo
> ˑˑˑThree
> ```
>

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- InstanceStringError,
- NotExistingTreeError
- InvalidPositionError

