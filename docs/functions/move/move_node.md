# move.Node

To move a node, use the **following function:**

> br4nch.**move**.**Node**(*tree*, *move_node*, *to_parent*, *target_tree=""*)

**Required argument(s):**

- *tree* - The tree(s) where the node(s) that will be moved are located.
- *move_node* - The position(s) of the node(s) that will be moved.

**Optional argument(s):**

- *to_parent* - The position/parent where to move the node(s) to.
- *target_tree* -  The tree where the copied node(s) will get placed at the chosen position.

**Guide:**

> To move a node, specify the tree name and the node you want to copy in the `move_node` argument.
>
> ```python
> >>> br4nch.display.Tree(tree="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
> 
> >>> br4nch.move.Node(tree="Stream", move_node="Movies")
> 
> >>> br4nch.display.Tree(tree="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┗━ Series
> ┣━ Prime Video
> ┗━ Movies
> ```
>
> You can also specify the parent where the node should be moved to in the tree using the `to_parent` argument. 
>
> *For more information about parents/positions, head to [positions](../../guides/positions.md).*
>
> ```python
> >>> br4nch.display.Tree(tree="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┗━ Series
> ┣━ Prime Video
> ┗━ Movies
> 
> >>> br4nch.move.Node(tree="Stream", move_node="Movies", to_parent="Prime Video")
> 
> >>> br4nch.display.Tree(tree="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
> ˑˑˑ┗━ Movies
> ```
>
> To move the node(s) to another existing tree, specify the tree name where the node(s) should go to in the `target_tree` argument.
>
> ```python
> >>> br4nch.display.Tree(tree=["Stream", "MyTree"])
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
> ˑˑˑ┗━ Movies
> My header
> ┗━ Grass
> ˑˑˑ┗━ Dirt
> ˑˑˑˑˑˑ┗━ Stone
> 
> >>> br4nch.move.Node(tree="Stream", move_node="Movies", target_tree="MyTree")
> 
> >>> br4nch.display.Tree(tree=["Stream", "MyTree"])
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
> ˑˑˑ┗━ Movies
> My header
> ┣━ Grass
> ┃ˑˑ┗━ Dirt
> ┃ˑˑˑˑˑ┗━ Stone
> ┗━ Movies
> ```
>
> To move the node(s) in multiple trees in the same function call, you can use a list for the `tree` argument.
>
> ```python
> >>> br4nch.display.Tree(tree=["Cars", "Electronics"])
> Garage
> ┗━ Cars
> ˑˑˑ┣━ Mercedes
> ˑˑˑ┗━ BMW
> PC
> ┣━ Mouses
> ┃ˑˑ┣━ Microsoft
> ┃ˑˑ┗━ Razer
> ┗━ Keyboards
> ˑˑˑ┣━ Steel Series
> ˑˑˑ┗━ Omen
> 
> >>> br4nch.move.Node(tree=["Cars", "Electronics"], move_node="1.1", to_parent="2")
> 
> >>> br4nch.display.Tree(tree="Cars")
> Garage
> ┣━ Cars
> ┃ˑˑ┣━ Mercedes
> ┃ˑˑ┗━ BMW
> ┗━ Mercedes
> PC
> ┣━ Mouses
> ┃ˑˑ┣━ Microsoft
> ┃ˑˑ┗━ Razer
> ┣━ Keyboards
> ┃ˑˑ┣━ Steel Series
> ┃ˑˑ┗━ Omen
> ┗━ Microsoft
> ```
>
> To move multiple nodes in the same function call, you can use a list for the `move_node` argument.
>
> ```python
> >>> br4nch.display.Tree(tree="Fruits")
> Fruits
> ┣━ Trees
> ┃ˑˑ┣━ Apple
> ┃ˑˑ┗━ Pear
> ┗━ Plant
> 
> >>> br4nch.move.Node(tree="Fruits", move_node=["Apple", "Pear"], to_parent="Plant")
> 
> >>> br4nch.display.Tree(tree="Fruits")
> Fruits
> ┣━ Trees
> ┃ˑˑ┣━ Apple
> ┃ˑˑ┗━ Pear
> ┗━ Plant
> ˑˑˑ┣━ Apple
> ˑˑˑ┗━ Pear
> ```
>

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- InstanceStringError
- InvalidPositionError
- NotExistingTreeError
- InvalidPositionError
