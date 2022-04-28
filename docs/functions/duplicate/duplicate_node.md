# duplicate.Node

To duplicate a node, use the **following function:**

> br4nch.**duplicate**.**Node**(*tree*, *duplicate_node*, *to_parent*, *target_tree=""*, *delete=False*)

**Required argument(s):**

- *tree* - The tree(s) where the node(s) to be copied are located.
- *duplicate_node* - The node(s) to be duplicated.

**Optional argument(s):**

- *to_parent* - The parent(s) where to add the duplicated node(s).
- *target_tree* -  The tree(s) where the copied node(s) will be placed at the chosen parents(s).
- *delete* - If this argument is 'True', then the node(s) in the original place will be deleted.

**Guide:**

> To copy a node, specify the tree name and the node you want to copy in the `duplicate_node` argument.
>
> ```python
> >>> br4nch.display.Tree(tree="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
> 
> >>> br4nch.duplicate.Node(tree="Stream", duplicate_node="Series")
> 
> >>> br4nch.display.Tree(tree="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┣━ Prime Video
> ┗━ Series
> ```
>
> You can also specify the parent where the node should be duplicated to in the tree using the `to_parent` argument. 
>
> *For more information about parents/positions, head to [positions](../../guides/positions.md).*
>
> ```python
> >>> br4nch.display.Tree(tree="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┣━ Prime Video
> ┗━ Series
> 
> >>> br4nch.duplicate.Node(tree="Stream", duplicate_node="Movies", to_parent="Prime Video")
> 
> >>> br4nch.display.Tree(tree="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┣━ Prime Video
> ┃ˑˑ┗━ Movies
> ┗━ Series
> ```
>
> To copy the node(s) to another existing tree, specify the tree(s) name in the `target_tree` argument.
>
> ```python
> >>> br4nch.display.Tree(tree=["Stream", "MyBranch"])
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┣━ Prime Video
> ┃ˑˑ┗━ Movies
> ┗━ Series
> My header
> ┗━ Grass
> ˑˑˑ┗━ Dirt
> ˑˑˑˑˑˑ┗━ Stone
> 
> >>> br4nch.duplicate.Node(tree="Stream", duplicate_node="Movies", target_tree="MyBranch")
> 
> >>> br4nch.display.Tree(tree=["Stream", "MyBranch"])
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┣━ Prime Video
> ┃ˑˑ┗━ Movies
> ┗━ Series
> My header
> ┣━ Grass
> ┃ˑˑ┗━ Dirt
> ┃ˑˑˑˑˑ┗━ Stone
> ┗━ Movies
> ```
>
> To copy the node(s) and then delete it directly from the original position(s), set the `delete` argument to `True`.
>
> ```python
> >>> br4nch.display.Tree(tree="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┣━ Prime Video
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┗━ Series
> 
> >>> br4nch.duplicate.Node(tree="Stream", duplicate_node="Prime Video", to_parent="Netflix", delete=True)
> 
> >>> br4nch.display.Tree(tree="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┣━ Series
> ┃ˑˑ┗━ Prime Video
> ┃ˑˑˑˑˑ┣━ Movies
> ┃ˑˑˑˑˑ┗━ Series
> ┗━ Series
> ```
>
> To duplicate the node(s) in multiple trees in the same function call, you can use a list for the `tree` argument.
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
> >>> br4nch.duplicate.Node(tree=["Cars", "Electronics"], duplicate_node="1.1", to_parent="2")
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
> To duplicate multiple nodes in the same function call, you can use a list for the `duplicate_node` argument.
>
> ```python
> >>> br4nch.display.Tree(tree="Fruits")
> Fruits
> ┣━ Trees
> ┃ˑˑ┣━ Apple
> ┃ˑˑ┗━ Pear
> ┗━ Plant
> 
> >>> br4nch.duplicate.Node(tree="Fruits", duplicate_node=["Apple", "Pear"], to_parent="Plant")
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
> To duplicate the node(s) to multiple parents in the same function call, you can use a list for the `to_parent` argument.
>
> ```python
> >>> br4nch.display.Tree(tree="Board")
> Info
> ┣━ USA
> ┃ˑˑ┣━ LA
> ┃ˑˑ┗━ Texas
> ┗━ Netherlands
> 
> >>> br4nch.duplicate.Node(tree="Board", duplicate_node="Texas", to_parent=["0", "Netherlands"])
> 
> >>> br4nch.display.Tree(tree="Board")
> Info
> ┣━ USA
> ┃ˑˑ┣━ LA
> ┃ˑˑ┗━ Texas
> ┣━ Netherlands
> ┃ˑˑ┗━ Texas
> ┗━ Texas
> ```
>
> To duplicate the node(s) to multiple diffrent trees in the same function call, you can use a list for the `target_tree` argument.
>
> ```python
> >>> br4nch.display.Tree(tree=["Parks", "Food"])
> Fruits
> ┣━ Vacation
> ┃ˑˑ┣━ Apple
> ┃ˑˑ┗━ Pear
> ┗━ Games
> ˑˑˑ┗━ Go Park
> Food
> ┣━ Pie
> ┃ˑˑ┣━ Crumble
> ┃ˑˑ┗━ Cream
> ┗━ Fruit
> ˑˑˑ┣━ Apple
> ˑˑˑ┗━ Pear
> 
> >>> br4nch.duplicate.Node(tree="Parks", duplicate_node="Go Park", target_tree=["Parks", "Food"])
> 
> >>> br4nch.display.Tree(tree=["Parks", "Food"])
> Fruits
> ┣━ Vacation
> ┃ˑˑ┣━ Apple
> ┃ˑˑ┗━ Pear
> ┣━ Games
> ┃ˑˑ┗━ Go Park
> ┗━ Go Park
> Food
> ┣━ Pie
> ┃ˑˑ┣━ Crumble
> ┃ˑˑ┗━ Cream
> ┣━ Fruit
> ┃ˑˑ┣━ Apple
> ┃ˑˑ┗━ Pear
> ┗━ Go Park
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- *InstanceStringError*
- *InstanceBooleanError*
- *InvalidPositionError*
- *NotExistingBranchError*
