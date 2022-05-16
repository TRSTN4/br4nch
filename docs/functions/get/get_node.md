# get.Node

To get any node, use the **following function:**

> br4nch.**get**.**Node**(*tree*, *position=""*, *include=""*, *exclude=""*, *match_include=False*, *match_exclude=False*, *beautify=True*)

**Required argument(s):**

- *tree* - The tree(s) to display the node(s) for.

**Optional argument(s):**

- *position* - The position(s) to display the corresponding node(s).
- *include* - If the given word(s) are in the node, the node will be displayed. Else, it will not be displayed.
- *exclude* - If the given word(s) are in the node, the node will not be displayed. Else, it will be displayed.
- *match_include* - If this argument is 'True', then the filled in word(s) must be case-sensitive and words.
- *match_exclude* -  If this argument is 'True', then the filled in word(s) must be case-sensitive and words.
- *beautify* - If this argument is 'True', then the result will be displayed with a special tree format.

**Guide:**

> To print all nodes in a tree, specify the tree name in the `tree` argument.
>
> ```python
> >>> br4nch.get.Node(tree="Test")
> Get Node Result:
> ┗━ Tree: Test
> ˑˑˑ┣━ Position: 1
> ˑˑˑ┃ˑˑ┗━ Node: First Node
> ˑˑˑ┣━ Position: 1.1
> ˑˑˑ┃ˑˑ┗━ Node: Second Node
> ˑˑˑ┣━ Position: 1.1.1
> ˑˑˑ┃ˑˑ┗━ Node: Third Node
> ˑˑˑ┣━ Position: 2
> ˑˑˑ┃ˑˑ┗━ Node: New Line One
> ˑˑˑ┃ˑˑˑˑˑ>>>>> New Line Two
> ˑˑˑ┃ˑˑˑˑˑ>>>>> New Line Three
> ˑˑˑ┗━ Position: 2.1
> ˑˑˑˑˑˑ┗━ Node: Sub Node One
> ˑˑˑˑˑˑˑˑˑ>>>>> Sub Node Two
> ```
> 

> To print a position of a node in a tree, specify the name of the node in the `position` argument.
>
> *For more information about positions, head to [positions](../../guides/positions.md).*
>
> ```python
> >>> br4nch.get.Node(tree="Stream", position="1.2.1")
> Get Node Result:
> ┗━ Tree: Stream
> ˑˑˑ┗━ Position: 1.2.1
> ˑˑˑˑˑˑ┗━ Node: Squid Game
> ```
>

> To filter only nodes with a certain word, put the word in the `include` argument.
>
> ```python
> >>> br4nch.get.Node(tree="Test", include="Line")
> Get Node Result:
> ┗━ Tree: Test
> ˑˑˑ┗━ Position: 2
> ˑˑˑˑˑˑ┗━ Node: New Line One
> ˑˑˑˑˑˑˑˑˑ>>>>> New Line Two
> ˑˑˑˑˑˑˑˑˑ>>>>> New Line Three
> ```
>

> To filter out only nodes with a certain word, put the word in the `exclude` argument.
>
> ```python
> >>> br4nch.get.Node(tree="Test", exclude="Node")
> Get Node Result:
> ┗━ Tree: Test
> ˑˑˑ┗━ Position: 2
> ˑˑˑˑˑˑ┗━ Node: New Line One
> ˑˑˑˑˑˑˑˑˑ>>>>> New Line Two
> ˑˑˑˑˑˑˑˑˑ>>>>> New Line Three
> ```
>

> To make the name of the word case-sensitive and words, set the `match_include` argument to True.
>
> ```python
> >>> br4nch.get.Node(tree="Stream", include="squid game", match_include=True)
> ```

> To make the name of the word case-sensitive and words, set the `match_exclude` argument to True.
>
> ```python
> >>> br4nch.get.Node(tree="Stream", exclude="squid game", match_exclude=True)
> ```

> To print the result without a tree structure in the result, set the `beautify` argument to ˑFalseˑ.
>
> ```python
> >>> br4nch.get.Node(tree="Stream", beautify=False)
> Netflix
> Movies
> Interstellar
> Series
> Squid Game
> The Crown
> Prime Video
> Movies
> Tenet
> Parasite
> Series
> The Walking Dead
> ```
>

> To print the position(s) in multiple trees in the same function call, you can use a list for the `tree` argument.
>
> ```python
> >>> br4nch.get.Node(tree=["Stream"], ["Stream2"], position="2.1.1")
> Get Node Result:
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
> >>> br4nch.get.Node(tree="Stream", position=["1.1.1", "1.2.1"])
> Get Node Result:
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
> >>> br4nch.get.Node(tree="Test", include=["Second", "Third"])
> Get Node Result:
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
> >>> br4nch.get.Node(tree="Test", exclude=["Second", "Third"])
> Get Node Result:
> ┗━ Tree: Test
> ˑˑˑ┣━ Position: 1
> ˑˑˑ┃ˑˑ┗━ Node: First Node
> ˑˑˑ┣━ Position: 2
> ˑˑˑ┃ˑˑ┗━ Node: New Line One
> ˑˑˑ┃ˑˑˑˑˑ>>>>> New Line Two
> ˑˑˑ┃ˑˑˑˑˑ>>>>> New Line Three
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

