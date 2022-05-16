# get.Tree

To get any tree, use the **following function:**

> br4nch.**get**.**Tree**(*include=""*, *exclude=""*, *match_include=False*, *match_exclude=True*, *beautify=True*)

**Optional argument(s):**

- *include* - If the given word(s) are in the tree, the tree will be displayed. Else, it will not be displayed.
- *exclude* - If the given word(s) are in the tree, the tree will not be displayed. Else, it will be displayed.
- *match_include* - If this argument is 'True', then the filled in word(s) must be case-sensitive and words.
- *match_exclude* -  If this argument is 'True', then the filled in word(s) must be case-sensitive and words.
- *beautify* - If this argument is 'True', then the result will be displayed with a special branch format.

**Guide:**

> To print all trees, use this function.
>
> ```python
> >>> br4nch.get.Tree()
> Get Tree Result:
> ┣━ MyTree
> ┣━ Earth
> ┣━ SecondTree
> ┗━ Games
> ```
>

> To filter only trees with a certain word, put the word in the `include` argument.
>
> ```python
> >>> br4nch.get.Tree(include="Tree")
> Get Tree Result:
> ┣━ MyTree
> ┗━ SecondTree
> ```
>

> To filter out only trees with a certain word, put the word in the `exclude` argument.
>
> ```python
> >>> br4nch.get.Tree(exclude="Tree")
> Get Tree Result:
> ┣━ Earth
> ┗━ Games
> ```
>

> To make the name of the word case-sensitive and words, set the `match_include` argument to True.
>
> ```python
> >>> br4nch.get.Tree(include="stream", match_include=True)
> ```

> To make the name of the word case-sensitive and words, set the `match_exclude` argument to True.
>
> ```python
> >>> br4nch.get.Tree(exclude="stream", match_exclude=True)
> ```

> To print the result without a tree structure in the result, set the `beautify` argument to `False`.
>
> ```python
> >>> br4nch.get.Tree(beautify=False)
> MyTree
> Earth
> SecondTree
> Games
> ```
>

> To include multiple words in the same function call, you can use a list for the `include` argument.
>
> ```python
> >>> br4nch.get.Tree(include=["Earth", "Games"])
> Get Tree Result:
> ┣━ Earth
> ┗━ Games
> ```
>

> To exclude multiple words in the same function call, you can use a list for the `exclude` argument.
>
> ```python
> >>> br4nch.get.Tree(exclude=["Tree", "Earth"])
> Get Tree Result:
> ┗━ Games
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- InstanceStringError
- InstanceBooleanError

