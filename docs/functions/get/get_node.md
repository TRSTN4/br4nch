# get.Node

To get any node, use the **following function:**

> br4nch.**get**.**Node**(*tree*, *node=""*, *sensitive=False*, *include=""*, *exclude=""*, *beautify=True*)

**Required argument(s):**

- *tree* - The tree(s) to display the node(s) for.

**Optional argument(s):**

- *node* - The node(s) that are displayed.
- *sensitive* - If this argument is 'True', then the filled in node must be case-sensitive.
- *include* - If the given word(s) are in the node, the node will be displayed. Else, it will not be displayed.
- *exclude* - If the given word(s) are in the node, the node will not be displayed. Else, it will be displayed.
- *beautify* - If this argument is 'True', then the result will be displayed with a special tree format.

**Guide:**

> To print all nodes in a tree, specify the tree name in the `tree` argument.
>
> ```python
> >>> br4nch.get.Node(tree="Test")
> Get Node Result:
> ┗━ Tree: Test
> ˑˑˑ┣━ Node: First Node
> ˑˑˑ┃ˑˑ┗━ Position: 1
> ˑˑˑ┣━ Node: Second Node
> ˑˑˑ┃ˑˑ┗━ Position: 1.1
> ˑˑˑ┣━ Node: Third Node
> ˑˑˑ┃ˑˑ┗━ Position: 1.1.1
> ˑˑˑ┣━ Node: New Line One
> ˑˑˑ┃ˑˑNew Line Two
> ˑˑˑ┃ˑˑNew Line Three
> ˑˑˑ┃ˑˑ┗━ Position: 2
> ˑˑˑ┗━ Node: Sub Node One
> ˑˑˑˑˑˑSub Node Two
> ˑˑˑˑˑˑ┗━ Position: 2.1
> ```
>
> To print a specfic position of node in a tree, specify the name of the node in the `node` argument.
>
> ```python
> >>> br4nch.get.Node(tree="Stream", node="Squid Game")
> Get Node Result:
> ┗━ Tree: Stream
> ˑˑˑ┗━ Node: Squid Game                  
> ˑˑˑˑˑˑ┗━ Position: 1.2.1
> ```
>
> To make the name of the node case-sensitive, set the `sensitive` argument to True.
>
> ```python
> >>> br4nch.get.Node(tree="Stream", node="squid game", sensitive=True)
> ```
>
> To filter only nodes with a certain word, put the word in the `include` argument.
>
> ```python
> >>> br4nch.get.Node(tree="Test", include="Line")
> Get Node Result:
> ┗━ Tree: Test
> ˑˑˑ┗━ Node: New Line One
> ˑˑˑˑˑˑNew Line Two
> ˑˑˑˑˑˑNew Line Three
> ˑˑˑˑˑˑ┗━ Position: 2
> ```
>
> To filter out only nodes with a certain word, put the word in the `exclude` argument.
>
> ```python
> >>> br4nch.get.Node(tree="Test", exclude="Node")
> Get Node Result:
> ┗━ Tree: Test
> ˑˑˑ┗━ Node: New Line One
> ˑˑˑˑˑˑNew Line Two
> ˑˑˑˑˑˑNew Line Three
> ˑˑˑˑˑˑ┗━ Position: 2
> ```
>
> To print the result without a tree structure in the result, set the `beautify` argument to ˑFalseˑ.
>
> ```python
> >>> br4nch.get.Node(tree="Stream", beautify=False)
> 1
> 1.1
> 1.1.1
> 2
> 2.1
> ```
>
> To print the position(s) in multiple trees in the same function call, you can use a list for the `tree` argument.
>
> ```python
> >>> br4nch.get.Node(tree=["Stream"], ["Stream2"], node="The Walking Dead")
> Get Node Result:
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
> >>> br4nch.get.Node(tree="Stream", node=["Interstellar", "Squid Game"])
> Get Node Result:
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
> >>> br4nch.get.Node(tree="Test", include=["Second", "Third"])
> Get Node Result:
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
> >>> br4nch.get.Node(tree="Test", exclude=["Second", "Third"])
> Get Node Result:
> ┗━ Tree: Test
> ˑˑˑ┣━ Node: First Node
> ˑˑˑ┃ˑˑ┗━ Position: 1
> ˑˑˑ┣━ Node: New Line One
> ˑˑˑ┃ˑˑNew Line Two
> ˑˑˑ┃ˑˑNew Line Three
> ˑˑˑ┃ˑˑ┗━ Position: 2
> ˑˑˑ┗━ Node: Sub Node One
> ˑˑˑˑˑˑSub Node Two
> ˑˑˑˑˑˑ┗━ Position: 2.1
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- *InstanceStringError*
- *InstanceBooleanError*
- *NotExistingBranchError*

