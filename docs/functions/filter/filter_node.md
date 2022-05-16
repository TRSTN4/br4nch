# filter.Node

To filter a node, use the **following function:**

> br4nch.**filter**.**Node**(*tree*, *include=""*, *exclude=""*, *match_include=False*, *match_exclude=False*)

**Required argument(s):**

- *tree* - The tree that will be filtered.

**Optional argument(s):**

- *include* - If the given word(s) are in the node, the node will be included. Else, it will not be excluded.
- *exclude* - If the given word(s) are in the node, the node will not be excluded. Else, it will be included.
- *match_include* - If this argument is 'True', then the filled in word(s) must be case-sensitive and words.
- *match_exclude* -  If this argument is 'True', then the filled in word(s) must be case-sensitive and words.

**Guide:**

> To filter only nodes with a certain word, put the word in the `include` argument.
>
> ```python
> >>> br4nch.display.Tree(tree="MyData")
> Database
> ┣━ Users
> ┃ˑˑ┣━ Manager
> ┃ˑˑ┃ˑˑ┗━ Ben
> ┃ˑˑ┗━ Scientists
> ┃ˑˑˑˑˑ┣━ Jerry
> ┃ˑˑˑˑˑ┗━ Hank
> ┗━ Information
> ˑˑˑ┣━ Temperature
> ˑˑˑ┃ˑˑ┗━ 44
> ˑˑˑ┗━ Statements
> ˑˑˑˑˑˑ┣━ Content
> ˑˑˑˑˑˑ┃ˑˑ┗━ None
> ˑˑˑˑˑˑ┣━ Overheat
> ˑˑˑˑˑˑ┃ˑˑ┗━ False
> ˑˑˑˑˑˑ┗━ Active
> ˑˑˑˑˑˑˑˑˑ┗━ True
> 
> >>> br4nch.filter.Node(tree="MyData", include="Scientists")
> 
> >>> br4nch.display.Tree(tree="MyData")
> Database
> ┗━ Scientists
> ˑˑˑ┣━ Jerry
> ˑˑˑ┗━ Hank
> ```

> To filter out only nodes with a certain word, put the word in the `exclude` argument.
>
> ```python
> >>> br4nch.display.Tree(tree="MyData")
> Database
> ┣━ Users
> ┃ˑˑ┣━ Manager
> ┃ˑˑ┃ˑˑ┗━ Ben
> ┃ˑˑ┗━ Scientists
> ┃ˑˑˑˑˑ┣━ Jerry
> ┃ˑˑˑˑˑ┗━ Hank
> ┗━ Information
> ˑˑˑ┣━ Temperature
> ˑˑˑ┃ˑˑ┗━ 44
> ˑˑˑ┗━ Statements
> ˑˑˑˑˑˑ┣━ Content
> ˑˑˑˑˑˑ┃ˑˑ┗━ None
> ˑˑˑˑˑˑ┣━ Overheat
> ˑˑˑˑˑˑ┃ˑˑ┗━ False
> ˑˑˑˑˑˑ┗━ Active
> ˑˑˑˑˑˑˑˑˑ┗━ True
> 
> >>> br4nch.filter.Node(tree="MyData", exclude="Scientists")
> 
> >>> br4nch.display.Tree(tree="MyData")
> Database
> ┣━ Users
> ┃ˑˑ┗━ Manager
> ┃ˑˑˑˑˑ┗━ Ben
> ┗━ Information
> ˑˑˑ┣━ Temperature
> ˑˑˑ┃ˑˑ┗━ 44
> ˑˑˑ┗━ Statements
> ˑˑˑˑˑˑ┣━ Content
> ˑˑˑˑˑˑ┃ˑˑ┗━ None
> ˑˑˑˑˑˑ┣━ Overheat
> ˑˑˑˑˑˑ┃ˑˑ┗━ False
> ˑˑˑˑˑˑ┗━ Active
> ˑˑˑˑˑˑˑˑˑ┗━ True
> ```

> To make the name of the node(s) for the `include` argument case-sensitive and words, set the `match_include` argument to True.
>
> ```python
> >>> br4nch.display.Tree(tree="MyData")
> Database
> ┣━ Users
> ┃ˑˑ┣━ Manager
> ┃ˑˑ┃ˑˑ┗━ Ben
> ┃ˑˑ┗━ Scientists
> ┃ˑˑˑˑˑ┣━ Jerry
> ┃ˑˑˑˑˑ┗━ Hank
> ┗━ Information
> ˑˑˑ┣━ Temperature
> ˑˑˑ┃ˑˑ┗━ 44
> ˑˑˑ┗━ Statements
> ˑˑˑˑˑˑ┣━ Content
> ˑˑˑˑˑˑ┃ˑˑ┗━ None
> ˑˑˑˑˑˑ┣━ Overheat
> ˑˑˑˑˑˑ┃ˑˑ┗━ False
> ˑˑˑˑˑˑ┗━ Active
> ˑˑˑˑˑˑˑˑˑ┗━ True
> 
> >>> br4nch.filter.Node(tree="MyData", include="scientists", match_include=True)
> 
> >>> br4nch.display.Tree(tree="MyData")
> 
> ```

> To make the name of the node(s) for the `exclude` argument case-sensitive and words, set the `match_exclude` argument to True.
>
> ```python
> >>> br4nch.display.Tree(tree="MyData")
> Database
> ┣━ Users
> ┃ˑˑ┣━ Manager
> ┃ˑˑ┃ˑˑ┗━ Ben
> ┃ˑˑ┗━ Scientists
> ┃ˑˑˑˑˑ┣━ Jerry
> ┃ˑˑˑˑˑ┗━ Hank
> ┗━ Information
> ˑˑˑ┣━ Temperature
> ˑˑˑ┃ˑˑ┗━ 44
> ˑˑˑ┗━ Statements
> ˑˑˑˑˑˑ┣━ Content
> ˑˑˑˑˑˑ┃ˑˑ┗━ None
> ˑˑˑˑˑˑ┣━ Overheat
> ˑˑˑˑˑˑ┃ˑˑ┗━ False
> ˑˑˑˑˑˑ┗━ Active
> ˑˑˑˑˑˑˑˑˑ┗━ True
> 
> >>> br4nch.filter.Node(tree="MyData", exclude="scientists", match_exclude=True)
> 
> >>> br4nch.display.Tree(tree="MyData")
> ```

> To include multiple words in the same function call, you can use a list for the `include` argument.
>
> ```python
> >>> br4nch.display.Tree(tree="MyData")
> Database
> ┣━ Users
> ┃ˑˑ┣━ Manager
> ┃ˑˑ┃ˑˑ┗━ Ben
> ┃ˑˑ┗━ Scientists
> ┃ˑˑˑˑˑ┣━ Jerry
> ┃ˑˑˑˑˑ┗━ Hank
> ┗━ Information
> ˑˑˑ┣━ Temperature
> ˑˑˑ┃ˑˑ┗━ 44
> ˑˑˑ┗━ Statements
> ˑˑˑˑˑˑ┣━ Content
> ˑˑˑˑˑˑ┃ˑˑ┗━ None
> ˑˑˑˑˑˑ┣━ Overheat
> ˑˑˑˑˑˑ┃ˑˑ┗━ False
> ˑˑˑˑˑˑ┗━ Active
> ˑˑˑˑˑˑˑˑˑ┗━ True
> 
> >>> br4nch.filter.Node(tree="MyData", include=["Temperature", "Statements"])
> 
> >>> br4nch.display.Tree(tree="MyData")
> Database
> ┣━ Temperature
> ┃ˑˑ┗━ 44
> ┗━ Statements
> ˑˑˑ┣━ Content
> ˑˑˑ┃ˑˑ┗━ None
> ˑˑˑ┣━ Overheat
> ˑˑˑ┃ˑˑ┗━ False
> ˑˑˑ┗━ Active
> ˑˑˑˑˑˑ┗━ True
> ```

> To exclude multiple words in the same function call, you can use a list for the `exclude` argument.
>
> ```python
> >>> br4nch.display.Tree(tree="MyData")
> Database
> ┣━ Users
> ┃ˑˑ┣━ Manager
> ┃ˑˑ┃ˑˑ┗━ Ben
> ┃ˑˑ┗━ Scientists
> ┃ˑˑˑˑˑ┣━ Jerry
> ┃ˑˑˑˑˑ┗━ Hank
> ┗━ Information
> ˑˑˑ┣━ Temperature
> ˑˑˑ┃ˑˑ┗━ 44
> ˑˑˑ┗━ Statements
> ˑˑˑˑˑˑ┣━ Content
> ˑˑˑˑˑˑ┃ˑˑ┗━ None
> ˑˑˑˑˑˑ┣━ Overheat
> ˑˑˑˑˑˑ┃ˑˑ┗━ False
> ˑˑˑˑˑˑ┗━ Active
> ˑˑˑˑˑˑˑˑˑ┗━ True
> 
> >>> br4nch.filter.Node(tree="MyData", exclude=["Temperature", "Statements"])
> 
> >>> br4nch.display.Tree(tree="MyData")
> Database
> ┣━ Users
> ┃ˑˑ┣━ Manager
> ┃ˑˑ┃ˑˑ┗━ Ben
> ┃ˑˑ┗━ Scientists
> ┃ˑˑˑˑˑ┣━ Jerry
> ┃ˑˑˑˑˑ┗━ Hank
> ┗━ Information
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- InstanceStringError,
- NotExistingTreeError
- InstanceBooleanError

