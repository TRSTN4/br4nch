# get.Data

To get the data from a tree, use the **following function:**

> br4nch.**get**.**Data**(*tree*, *include_header=False*)

**Required argument(s):**

- *tree* - The tree which data will be retrieved.

**Optional argument(s):**

- *include_header* - If this argument is True, then the header from the tree will be included in the data.

**Guide:**

> To export the data of a tree, first assign a variable to the function and specify the tree which data must be retrieved in the `tree` argument.
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
> >>> MyData = br4nch.get.Data(tree="MyData")
> >>> print(MyData)
> {'Users': {'Manager': 'Ben', 'Scientists': ['Jerry', 'Hank']}, 'Information': {'Temperature': '44', 'Statements': {'Content': 'None', 'Overheat': 'False', 'Active': 'True'}}}
> ```
>

> To retrieve te data with the header in the data, set the `include_header` argument to `True`.
>
> ```python
> >>> MyData = br4nch.get.Data(tree="MyData", include_header=True)
> >>> print(MyData)
> {'Database': {'Users': {'Manager': 'Ben', 'Scientists': ['Jerry', 'Hank']}, 'Information': {'Temperature': '44', 'Statements': {'Content': 'None', 'Overheat': 'False', 'Active': 'True'}}}}
> ```

> If there is a duplicate node in the tree, a number is added to each duplicate node in the data output.
>
> ```python
> {"Test#1": ["ABC",123], "Test#2": ["Hey","Hai"]}
> ```
> 

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- InstanceStringError
- NotExistingTreeError

