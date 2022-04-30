# Getting Started

## Step 1

**Guide:**

> First we need to create a tree, we will call the tree `MyTree` and the name of the header will be `My Header!`.
>
> ```python
> >>> br4nch.create.Tree(tree="MyTree", header="My Header!")
> ```

## Step 2

**Guide:**

> To print the result of the tree created so far, specify the name of the tree you want to print. In this case the tree `MyTree`.
>
> ```python
> >>> br4nch.display.Tree(tree="MyTree")
> My Header!
> ```

## Step 3

**Guide:**

> To create a node to the tree, first specify the tree where the node should be created, the name of the node you want to create (we use the name `Hello World`).
>
> ```python
> >>> br4nch.create.Node(tree="MyTree", node="Hello World")
> 
> >>> br4nch.display.Tree(tree="MyTree")
> My Header!
> ┗━ Hello World
> ```
>
> To place a node in a specific position, use the argument `parent`. The position `0` indicates that the node will be created at the first height (to create nodes at the first height, you can leave out the `parent` argument).
>
> *For more information about parents/positions, head to [positions](../guides/positions.md).*
>
> ```python
> >>> br4nch.create.Node(tree="MyTree", node="Second node", parent="0")
> 
> >>> br4nch.display.Tree(tree="MyTree")
> My Header!
> ┣━ Hello World
> ┗━ Second node
> ```
>
> To create multiple nodes in the same function call, you can use list for the `layer` argument.
>
> ```python
> >>> br4nch.create.Node(tree="MyTree", node=["Apple", "Pear"], parent="0")
> 
> >>> br4nch.display.Tree(tree="MyTree")
> My Header!
> ┣━ Hello World
> ┣━ Second node
> ┣━ Apple
> ┗━ Pear
> ```

## Step 4

**Guide:**

> To create a child in for example the parent node `Hello World`, indicate the name of the node in the `parent` argument.
>
> ```python
> >>> br4nch.create.Node(tree="MyTree", node="Earth", parent="Hello World")
> 
> >>> br4nch.display.Tree(tree="MyTree")
> My Header!
> ┣━ Hello World
> ┃ˑˑ┗━ Earth
> ┣━ Second node
> ┣━ Apple
> ┗━ Pear
> ```
>
> You can also adjust the position to `1`. This is because the `Hello World` node is in the first place and in the first height.
>
> ```python
> >>> br4nch.create.Node(tree="MyTree", node="Moon", parent="1")
> 
> >>> br4nch.display.Tree(tree="MyTree")
> My Header!
> ┣━ Hello World
> ┃ˑˑ┣━ Earth
> ┃ˑˑ┗━ Moon
> ┣━ Second node
> ┣━ Apple
> ┗━ Pear
> ```
>
> To create a node at multiple parents/positions in the same function call, you can use list for the `parent` argument.
>
> ```python
> >>> br4nch.create.Node(tree="MyTree", node="Plant", parent=["Apple", "Pear"])
> 
> >>> br4nch.display.Tree(tree="MyTree")
> My Header!
> ┣━ Hello World
> ┃ˑˑ┣━ Earth
> ┃ˑˑ┗━ Moon
> ┣━ Second node
> ┣━ Apple
> ┃ˑˑ┗━ Plant
> ┗━ Pear
> ˑˑˑ┗━ Plant
> ```
>
> *Need help with the positions? then use the function [display.Assist](../functions/display/display_assist.md).*
>
> ```python
> >>> br4nch.display.Assist(tree="MyTree")
> 0: My Header!
> ┣━ 1: Hello World
> ┃ˑˑ┣━ 1.1: Earth
> ┃ˑˑ┗━ 1.2: Moon
> ┣━ 2: Second node
> ┣━ 3: Apple
> ┃ˑˑ┗━ 3.1: Plant
> ┗━ 4: Pear
> ˑˑˑ┗━ 4.1: Plant
> ```

## Step 5

**Guide:**

> To create another child in for example the node `Earth`, adjust the parent to `Earth`.
>
> ```python
> >>> br4nch.create.Node(tree="MyTree", node="Life", parent="Earth")
> 
> >>> br4nch.display.Tree(tree="MyTree")
> My Header!
> ┣━ Hello World
> ┃ˑˑ┣━ Earth
> ┃ˑˑ┃ˑˑ┗━ Life
> ┃ˑˑ┗━ Moon
> ┣━ Second node
> ┣━ Apple
> ┃ˑˑ┗━ Plant
> ┗━ Pear
> ˑˑˑ┗━ Plant
> ```
>
> You can also adjust the position to `1.1`. This is because the `Hello World` node is in place the first place in the first height and the `Earth` node is in the first place in the second height.
>
> ```python
> >>> br4nch.display.Assist(tree="MyTree")
> 0: My Header!
> ┣━ 1: Hello World
> ┃ˑˑ┣━ 1.1: Earth
> ┃ˑˑ┃ˑˑ┗━ 1.1.1: Life
> ┃ˑˑ┗━ 1.2: Moon
> ┣━ 2: Second node
> ┣━ 3: Apple
> ┃ˑˑ┗━ 3.1: Plant
> ┗━ 4: Pear
> ˑˑˑ┗━ 4.1: Plant
> 
> >>> br4nch.create.Node(tree="MyTree", node="Asteroid", parent="1.1")
> 
> >>> br4nch.display.Tree(tree="MyTree")
> My Header!
> ┣━ Hello World
> ┃ˑˑ┣━ Earth
> ┃ˑˑ┃ˑˑ┣━ Life
> ┃ˑˑ┃ˑˑ┗━ Astertoid
> ┃ˑˑ┗━ Moon
> ┣━ Second node
> ┣━ Apple
> ┃ˑˑ┗━ Plant
> ┗━ Pear
> ˑˑˑ┗━ Plant
> ```
>

