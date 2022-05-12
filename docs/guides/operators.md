# Operators

## Combinator - /

The operator 'Combinator' is used to perform multiple position actions at the same height as the current position.

**Guide:**

> Using the `/` aka `combinator` operator.
>
> ```python
> >>> br4nch.display.Tree(tree="Stream")
> Movies & Series
> ┣━ Netflix
> ┗━ Prime Video
> 
> >>> br4nch.add.Node(tree="Stream", node=["Movies", "Series"], parent="1/2")
> 
> >>> br4nch.display.Tree(tree="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
> ˑˑˑ┣━ Movies
> ˑˑˑ┗━ Series
> ```
>

> Using the `/` aka `combinator` operator followed by a position.
>
> ```python
> >>> br4nch.display.Tree(tree="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
> ˑˑˑ┣━ Movies
> ˑˑˑ┗━ Series
> 
> >>> br4nch.add.Node(tree="Stream", node=["The Hobbit"], parent="1/2.1")
> 
> >>> br4nch.display.Tree(tree="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┃ˑˑ┗━ The Hobbit
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
> ˑˑˑ┣━ Movies
> ˑˑˑ┃ˑˑ┗━ The Hobbit
> ˑˑˑ┗━ Series
> ```

## Selector - *

The operator 'selector' is used to include all positions at the same height as the current position.

**Guide**

> Using the `*` aka `selector` operator.
>
> ```python
> >>> br4nch.display.Tree(tree="Stream")
> Movies & Series
> ┣━ Netflix
> ┗━ Prime Video
> 
> >>> br4nch.add.Node(tree="Stream", node=["Movies", "Series"], parent="*")
> 
> >>> br4nch.display.Tree(tree="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
> ˑˑˑ┣━ Movies
> ˑˑˑ┗━ Series
> ```
>

> Using the `*` aka `selector` operator followed by a position.
>
> ```python
> >>> br4nch.display.Tree(tree="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
> ˑˑˑ┣━ Movies
> ˑˑˑ┗━ Series
> 
> >>> br4nch.add.Node(tree="Stream", node=["The Hobbit"], parent="*.1")
> 
> >>> br4nch.display.Tree(tree="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┃ˑˑ┗━ The Hobbit
> ┃ˑˑ┗━ Series
> ┗━ Prime Video
> ˑˑˑ┣━ Movies
> ˑˑˑ┃ˑˑ┗━ The Hobbit
> ˑˑˑ┗━ Series
> ```
>

> The `selector` operator can also be used to define all existing trees.
>
> For example to display all trees.
>
> ```python
> >>> br4nch.display.Tree(tree="*")
> ```
>

> For example to create a node in all trees on the position `0`.
>
> ```python
> >>> br4nch.add.Node(tree="*", node="Test", position="0")
> ```

## Inclusor - >

The operator 'inclusor' is used to include all positions between two values at the same height as the current position.

**Guide:**

> Using the `>` aka `inclusor` operator followed by a position.
>
> ```python
> >>> br4nch.display.Tree(tree="MyTree")
> My Header
> ┣━ Layer One
> ┣━ Layer Two
> ┗━ Layer Three
> 
> >>> br4nch.add.Node(tree="MyTree", node=["Sub Layer"], parent="2>3")
> 
> >>> br4nch.display.Tree(tree="MyTree")
> My Header
> ┣━ Layer One
> ┣━ Layer Two
> ┃ˑˑ┗━ Sub Layer
> ┗━ Layer Three
> ˑˑˑ┗━ Sub Layer
> ```
>
> And...
>
> ```python
> >>> br4nch.display.Tree(tree="MyTree")
> My Header
> ┣━ Layer One
> ┣━ Layer Two
> ┃ˑˑ┗━ Sub Layer
> ┗━ Layer Three
> ˑˑˑ┗━ Sub Layer
> 
> >>> br4nch.add.Node(tree="MyTree", node=["Final Layer"], parent="2>3.1")
> 
> >>> br4nch.display.Tree(tree="MyTree")
> My Header
> ┣━ Layer One
> ┣━ Layer Two
> ┃ˑˑ┗━ Sub Layer
> ┃ˑˑˑˑˑ┗━ Final Layer
> ┗━ Layer Three
> ˑˑˑ┗━ Sub Layer
> ˑˑˑˑˑˑ┗━ Final Layer
> ```

## Exclusor - <

The operator 'exclusor' is used to avoid using all positions between two values at the same height as the current position.

**Guide:**

> Using the `<` aka `exclusor` operator followed by a position.
>
> ```python
> >>> br4nch.display.Tree(tree="MyTree")
> My Header
> ┣━ Layer One
> ┣━ Layer Two
> ┗━ Layer Three
> 
> >>> br4nch.add.Node(tree="MyTree", node=["Sub Layer"], parent="2<3")
> 
> >>> br4nch.display.Tree(tree="MyTree")
> My Header
> ┣━ Layer One
> ┃ˑˑ┗━ Sub Layer
> ┣━ Layer Two
> ┗━ Layer Three
> ```
>
> And...
>
> ```python
> >>> br4nch.display.Tree(tree="MyTree")
> My Header
> ┣━ Layer One
> ┃ˑˑ┗━ Sub Layer
> ┣━ Layer Two
> ┗━ Layer Three
> 
> >>> br4nch.add.Node(tree="MyTree", node=["Final Layer"], parent="2<3.1")
> 
> >>> br4nch.display.Tree(tree="MyTree")
> My Header
> ┣━ Layer One
> ┃ˑˑ┗━ Sub Layer
> ┃ˑˑˑˑˑ┗━ Final Layer
> ┣━ Layer Two
> ┗━ Layer Three
> ```

## Combinations

Combinations can also be made with positions and operators together in the same height of the position. The 'combinator' operator is used for this.

**Here is an list for example:**

> - */1
> - 1>2/5>6
> - 1<2/3
> - 2/3/5/6
> - 2/5>7/9
>

## Serial - # #

The operator 'serial' is used to select a specific duplicate node.

**Guide:**

> If a node already exists in the tree, and you want to add a specific node in one of the two, use the `#` aka `serial` operator.
>
> **Example:**
> You want to add a node `Plant` to the node parent `Apple`, but you want to add it to the second `Apple` node. To do this, use the `#` after the node name with the number in the `parent` argument.
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
>
> Combined with other operators...
>
> ```python
> >>> br4nch.display.Tree(tree="ThirdExampleTree")
> Example
> ┣━ Hello World
> ┃ˑˑ┣━ Earth
> ┃ˑˑ┣━ Earth
> ┃ˑˑ┣━ Earth
> ┃ˑˑ┗━ Earth
> ┣━ Second node
> ┣━ Apple
> ┗━ Pear
> 
> >>> br4nch.create.Node(tree="ThirdExampleTree", node="Life", parent="Earth#1>2/4")
> 
> >>> br4nch.display.Tree(tree="ThirdExampleTree")
> Example
> ┣━ Hello World
> ┃ˑˑ┣━ Earth
> ┃ˑˑ┃ˑˑ┗━ Life
> ┃ˑˑ┣━ Earth
> ┃ˑˑ┃ˑˑ┗━ Life
> ┃ˑˑ┣━ Earth
> ┃ˑˑ┗━ Earth
> ┃ˑˑˑˑˑ┗━ Life
> ┣━ Second node
> ┣━ Apple
> ┗━ Pear
> ```

