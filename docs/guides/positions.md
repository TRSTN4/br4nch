# Positions

*It is recommended to use operators. For more information about operators, head to [operators](../guides/operators.md).*

## Adding the first layers

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

## Adding sublayers

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
> ┗━ Pear
> ```
>
> You can also adjust the position to `1.1`. This is because the `Hello World` node is in place the first place in the first height and the `Earth` node is in the first place in the second height.
>
> ```python
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
> ┗━ Pear
> ```
> 

## Branch assist

**Guide:**

> One of the many useful functions out there is the [display.Assist](../functions/display/display.assist.md) function. This function shows to which nodes the corresponding position belongs.
>
> ```python
> >>> br4nch.display.Assist(tree="MyTree")
> 0: My Header!
> ┣━ 1: Hello World
> ┃ˑˑ┣━ 1.1: Earth
> ┃ˑˑ┃ˑˑ┣━ 1.1.1: Life
> ┃ˑˑ┃ˑˑ┗━ 1.1.2: Astertoid
> ┃ˑˑ┗━ 1.2: Moon
> ┣━ 2: Second node
> ┣━ 3: Apple
> ┗━ 4: Pear
> ```
> 

## Duplicate nodes

**Guide:**

> If a node already exists in the tree, and you want to add a specific node in one of the two, use the `#` character.
>
> **Example:**
> You want to add a node `Plant` to the node parent `Apple`, but you want to add it to the second `Apple` node. To do this, use the `#` after the node name with the quantity in the `parent` argument.
>
> ```python
> >>> br4nch.display.Tree(tree="ExampleTree")
> Example
> ┣━ Apple
> ┣━ Apple
> ┗━ Apple
> 
> >>> br4nch.create.Node(tree="ExampleTree", node="Plant", parent="Apple#2")
> 
> >>> br4nch.display.Tree(tree="ExampleTree")
> Example
> ┣━ Apple
> ┣━ Apple
> ┃ˑˑ┗━ Plant
> ┗━ Apple
> ```
>
> And...
>
> ```python
> >>> br4nch.display.Tree(tree="SecondExampleTree")
> Example
> ┣━ Hello World
> ┃ˑˑ┣━ Earth
> ┃ˑˑ┗━ Earth
> ┣━ Second node
> ┣━ Apple
> ┗━ Pear
> 
> >>> br4nch.create.Node(tree="SecondExampleTree", node="Life", parent="Earth#1")
> 
> >>> br4nch.display.Tree(tree="SecondExampleTree")
> Example
> ┣━ Hello World
> ┃ˑˑ┣━ Earth
> ┃ˑˑ┃ˑˑ┗━ Life
> ┃ˑˑ┗━ Earth
> ┣━ Second node
> ┣━ Apple
> ┗━ Pear
> ```

