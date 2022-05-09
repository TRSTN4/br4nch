# get.Position

To get any position, use the **following function:**

> br4nch.**get**.**Position**(*tree*, *position=""*, *include=""*, *exclude=""*, *beautify=True*)

**Required argument(s):**

- *tree* - The tree(s) to display an position for.

**Optional argument(s):**

- *position* - The position(s) that are displayed.
- *include* - If the given word(s) are in the node, the node will be displayed. Else, it will not be displayed.
- *exclude* - If the given word(s) are in the node, the node will not be displayed. Else, it will be displayed.
- *beautify* - If this argument is 'True', then the result will be displayed with a special tree format.

**Guide:**

> To print all positions in a tree, specify the tree name in the `tree` argument.
>
> ```python
> >>> br4nch.get.Position(tree="Test")
> Get Position Result:
> ┗━ Tree: Test
> ˑˑˑ┣━ Position: 1
> ˑˑˑ┃ˑˑ┗━ Node: First Node
> ˑˑˑ┣━ Position: 1.1
> ˑˑˑ┃ˑˑ┗━ Node: Second Node
> ˑˑˑ┣━ Position: 1.1.1
> ˑˑˑ┃ˑˑ┗━ Node: Third Node
> ˑˑˑ┣━ Position: 2
> ˑˑˑ┃ˑˑ┗━ Node: New Line One
> ˑˑˑ┃ˑˑˑˑˑNew Line Two
> ˑˑˑ┃ˑˑˑˑˑNew Line Three
> ˑˑˑ┗━ Position: 2.1
> ˑˑˑˑˑˑ┗━ Node: Sub Node One
> ˑˑˑˑˑˑˑˑˑSub Node Two
> ```
>

> To print the node of a position in a tree, specify the position in the `position` argument.
>
> *For more information about positions, head to [positions](../../guides/positions.md).*
>
> ```python
> >>> br4nch.get.Position(tree="Stream", position="1.2.1")
> Get Position Result:
> ┗━ Tree: Stream
> ˑˑˑ┗━ Position: 1.2.1
> ˑˑˑˑˑˑ┗━ Node: Squid Game
> ```
>

> To filter only nodes with a certain word, put the word in the `include` argument.
>
> ```python
> >>> br4nch.get.Position(tree="Test", include="Line")
> Get Position Result:
> ┗━ Tree: Test
> ˑˑˑ┗━ Position: 2
> ˑˑˑˑˑˑ┗━ Node: New Line One
> ˑˑˑˑˑˑˑˑˑNew Line Two
> ˑˑˑˑˑˑˑˑˑNew Line Three
> ```
>

> To filter out only nodes with a certain word, put the word in the `exclude` argument.
>
> ```python
> >>> br4nch.get.Position(tree="Test", exclude="Node")
> Get Position Result:
> ┗━ Tree: Test
> ˑˑˑ┗━ Position: 2
> ˑˑˑˑˑˑ┗━ Node: New Line One
> ˑˑˑˑˑˑˑˑˑNew Line Two
> ˑˑˑˑˑˑˑˑˑNew Line Three
> ```
>

> To print the result without a tree structure in the result, set the `beautify` argument to `False`.
>
> ```python
> >>> br4nch.get.Position(tree="Stream", beautify=False)
> Squid Game
> ```
>

> To print the position(s) in multiple trees in the same function call, you can use a list for the `tree` argument.
>
> ```python
> >>> br4nch.get.Position(tree=["Stream"], ["Stream2"], position="2.1.1")
> Get Position Result:
> ┣━ Tree: Stream
> ┃ˑˑ┗━ Position: 2.1.1
> ┃ˑˑˑˑˑ┗━ Node: The Walking Dead
> ┗━ Tree: Stream2
> ˑˑˑ┗━ Position: 2.1.1
> ˑˑˑˑˑˑ┗━ Node: The Walking Dead
> ```
>

> To print multiple positions in the same function call, you can use a list for the `position` argument.
>
> ```python
> >>> br4nch.get.Position(tree="Stream", position=["1.1.1", "1.2.1"])
> Get Position Result:
> ┗━ Tree: Stream
> ˑˑˑ┣━ Position: 1.1.1                
> ˑˑˑ┃ˑˑ┗━ Node: Interstellar
> ˑˑˑ┗━ Position: 1.2.1               
> ˑˑˑˑˑˑ┗━ Node: Squid Game
> ```
>

> To include multiple words in the same function call, you can use a list for the `include` argument.
>
> ```python
> >>> br4nch.get.Position(tree="Test", include=["Second", "Third"])
> Get Position Result:
> ┗━ Tree: Test
> ˑˑˑ┣━ Position: 1.1
> ˑˑˑ┃ˑˑ┗━ Node: Second Node
> ˑˑˑ┗━ Position: 1.1.1
> ˑˑˑˑˑˑ┗━ Node: Third Node
> ```
>

> To exclude multiple words in the same function call, you can use a list for the `exclude` argument.
>
> ```python
> >>> br4nch.get.Position(tree="Test", exclude=["Second", "Third"])
> Get Position Result:
> ┗━ Tree: Test
> ˑˑˑ┣━ Position: 1
> ˑˑˑ┃ˑˑ┗━ Node: First Node
> ˑˑˑ┣━ Position: 2
> ˑˑˑ┃ˑˑ┗━ Node: New Line One
> ˑˑˑ┃ˑˑˑˑˑNew Line Two
> ˑˑˑ┃ˑˑˑˑˑNew Line Three
> ˑˑˑ┗━ Position: 2.1
> ˑˑˑˑˑˑ┗━ Node: Sub Node One
> ˑˑˑˑˑˑˑˑˑSub Node Two
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- InstanceStringError
- InstanceBooleanError
- NotExistingTreeError
- InvalidPositionError
