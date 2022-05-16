# get.Position

To get any position, use the **following function:**

> br4nch.**get**.**Position**(*tree*, *node=""*, *match_node=False*, *include=""*, *exclude=""*, *match_include=False*, *match_exclude=False*, *beautify=True*)

**Required argument(s):**

- *tree* - The tree(s) to display a position(s) for.

**Optional argument(s):**

- *node* - The node(s) to display the corresponding position(s).
- *match_node* - If this argument is 'True', then the filled in node(s) must be case-sensitive and words.
- *include* - If the given word(s) are in the node, the node will be displayed. Else, it will not be displayed.
- *exclude* - If the given word(s) are in the node, the node will not be displayed. Else, it will be displayed.
- *match_include* - If this argument is 'True', then the filled in word(s) must be case-sensitive and words.
- *match_exclude* -  If this argument is 'True', then the filled in word(s) must be case-sensitive and words.
- *beautify* - If this argument is 'True', then the result will be displayed with a special tree format.

**Guide:**

> To print all positions in a tree, specify the tree name in the `tree` argument.
>
> ```python
> >>> br4nch.get.Position(tree="Test")
> Get Position Result:
> ┗━ Tree: Test
> ˑˑˑ┣━ Node: First Node
> ˑˑˑ┃ˑˑ┗━ Position: 1
> ˑˑˑ┣━ Node: Second Node
> ˑˑˑ┃ˑˑ┗━ Position: 1.1
> ˑˑˑ┣━ Node: Third Node
> ˑˑˑ┃ˑˑ┗━ Position: 1.1.1
> ˑˑˑ┣━ Node: New Line One
> ˑˑˑ┃ˑˑ>>>>> New Line Two
> ˑˑˑ┃ˑˑ>>>>> New Line Three
> ˑˑˑ┃ˑˑ┗━ Position: 2
> ˑˑˑ┗━ Node: Sub Node One
> ˑˑˑˑˑˑ>>>>> Sub Node Two
> ˑˑˑˑˑˑ┗━ Position: 2.1
> ```
>

> To print the node of a position in a tree, specify the node in the `node` argument.
>
> ```python
>>>> br4nch.get.Position(tree="Stream", node="Squid Game")
> Get Position Result:
> ┗━ Tree: Stream
> ˑˑˑ┗━ Node: Squid Game                  
> ˑˑˑˑˑˑ┗━ Position: 1.2.1
> ```
> 

> To make the name of the node case-sensitive and words, set the `match_node` argument to True.
>
> ```python
> >>> br4nch.get.Position(tree="Stream", node="squid game", match_node=True)
> ```
>

> To filter only nodes with a certain word, put the word in the `include` argument.
>
> ```python
> >>> br4nch.get.Position(tree="Test", include="Line")
> Get Position Result:
> ┗━ Tree: Test
> ˑˑˑ┗━ Node: New Line One
> ˑˑˑˑˑˑ>>>>> New Line Two
> ˑˑˑˑˑˑ>>>>> New Line Three
> ˑˑˑˑˑˑ┗━ Position: 2
> ```
>

> To filter out only nodes with a certain word, put the word in the `exclude` argument.
>
> ```python
> >>> br4nch.get.Position(tree="Test", exclude="Node")
> Get Position Result:
> ┗━ Tree: Test
> ˑˑˑ┗━ Node: New Line One
> ˑˑˑˑˑˑ>>>>> New Line Two
> ˑˑˑˑˑˑ>>>>> New Line Three
> ˑˑˑˑˑˑ┗━ Position: 2
> ```
>

> To make the name of the word case-sensitive and words, set the `match_include` argument to True.
>
> ```python
> >>> br4nch.get.Position(tree="Stream", include="squid game", match_include=True)
> ```
>

> To make the name of the word case-sensitive and words, set the `match_exclude` argument to True.
>
> ```python
> >>> br4nch.get.Position(tree="Stream", exclude="squid game", match_exclude=True)
> ```
>

> To print the result without a tree structure in the result, set the `beautify` argument to `False`.
>
> ```python
> >>> br4nch.get.Position(tree="Stream", beautify=False)
> 1
> 1.1
> 1.1.1
> 1.2
> 1.2.1
> 1.2.2
> 2
> 2.1
> 2.1.1
> 2.1.2
> 2.2
> 2.2.1
> ```
>

> To print the position(s) in multiple trees in the same function call, you can use a list for the `tree` argument.
>
> ```python
> >>> br4nch.get.Position(tree=["Stream"], ["Stream2"], node="The Walking Dead")
> Get Position Result:
> ┣━ Tree: Stream
> ┃ˑˑ┗━ Node: The Walking Dead              
> ┃ˑˑˑˑˑ┗━ Position: 2.1.1
> ┗━ Tree: Stream2
> ˑˑˑ┗━ Node: The Walking Dead                
> ˑˑˑˑˑˑ┗━ Position: 2.1.1
> ```
>

> To print multiple positions in the same function call, you can use a list for the `node` argument.
>
> ```python
> >>> br4nch.get.Position(tree="Stream", node=["Interstellar", "Squid Game"])
> Get Position Result:
> ┗━ Tree: Stream
> ˑˑˑ┣━ Node: Interstellar                 
> ˑˑˑ┃ˑˑ┗━ Position: 1.1.1
> ˑˑˑ┗━ Node: Squid Game                  
> ˑˑˑˑˑˑ┗━ Position: 1.2.1
> ```
>

> To include multiple words in the same function call, you can use a list for the `include` argument.
>
> ```python
> >>> br4nch.get.Position(tree="Test", include=["Second", "Third"])
> Get Position Result:
> ┗━ Tree: Test
> ˑˑˑ┣━ Node: Second Node
> ˑˑˑ┃ˑˑ┗━ Position: 1.1
> ˑˑˑ┗━ Node: Third Node
> ˑˑˑˑˑˑ┗━ Position: 1.1.1
> ```
>

> To exclude multiple words in the same function call, you can use a list for the `exclude` argument.
>
> ```python
> >>> br4nch.get.Position(tree="Test", exclude=["Second", "Third"])
> Get Position Result:
> ┗━ Tree: Test
> ˑˑˑ┣━ Node: First Node
> ˑˑˑ┃ˑˑ┗━ Position: 1
> ˑˑˑ┣━ Node: New Line One
> ˑˑˑ┃ˑˑ>>>>> New Line Two
> ˑˑˑ┃ˑˑ>>>>> New Line Three
> ˑˑˑ┃ˑˑ┗━ Position: 2
> ˑˑˑ┗━ Node: Sub Node One
> ˑˑˑˑˑˑSub Node Two
> ˑˑˑˑˑˑ┗━ Position: 2.1
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- InstanceStringError
- InstanceBooleanError
- NotExistingTreeError
- InvalidPositionError
