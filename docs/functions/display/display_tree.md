# display.Tree

To display a tree, use the **following function:**

> br4nch.**display**.**Tree**(*tree*, *delete=False*)

**Required argument(s):**

- *tree* - The tree(s) to display.

**Optional argument(s):**

- *delete* - If this argument is 'True', the tree(s) will be deleted after it is printed.

**Guide:**

> Prints the tree given in the `tree` argument. In this example we will print the tree `Stream`.
>
> ```python
> >>> br4nch.display.Tree(tree="Stream")
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┃ˑˑ┗━ Interstellar
> ┃ˑˑ┗━ Series
> ┃ˑˑˑˑˑ┣━ Squid Game
> ┃ˑˑˑˑˑ┗━ The Crown
> ┗━ Prime Video
> ˑˑˑ┣━ Movies
> ˑˑˑ┃ˑˑ┣━ Tenet
> ˑˑˑ┃ˑˑ┗━ Parasite
> ˑˑˑ┗━ Series
> ˑˑˑˑˑˑ┗━ The Walking Dead
> ```
>
> To print a tree and delete after printed, specify the value `True` in the `delete` argument.
>
> ```python
> >>> br4nch.display.Tree(tree="Stream", delete=True)
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┃ˑˑ┗━ Interstellar
> ┃ˑˑ┗━ Series
> ┃ˑˑˑˑˑ┣━ Squid Game
> ┃ˑˑˑˑˑ┗━ The Crown
> ┗━ Prime Video
> ˑˑˑ┣━ Movies
> ˑˑˑ┃ˑˑ┣━ Tenet
> ˑˑˑ┃ˑˑ┗━ Parasite
> ˑˑˑ┗━ Series
> ˑˑˑˑˑˑ┗━ The Walking Dead
> 
> >>> br4nch.display.Tree(tree="Stream")
> NotExistingTreeError: The tree: 'Stream' does not exists.
> ```
>
> To print multiple trees in the same function call, you can use a list for the `tree` argument.
>
> ```python
> >>> br4nch.display.Tree(tree=["Stream", "MyTree"])
> Movies & Series
> ┣━ Netflix
> ┃ˑˑ┣━ Movies
> ┃ˑˑ┃ˑˑ┗━ Interstellar
> ┃ˑˑ┗━ Series
> ┃ˑˑˑˑˑ┣━ Squid Game
> ┃ˑˑˑˑˑ┗━ The Crown
> ┗━ Prime Video
> ˑˑˑ┣━ Movies
> ˑˑˑ┃ˑˑ┣━ Tenet
> ˑˑˑ┃ˑˑ┗━ Parasite
> ˑˑˑ┗━ Series
> ˑˑˑˑˑˑ┗━ The Walking Dead
> My header!
> ┣━ My Layer
> ┃ˑˑ┣━ Sublayer One
> ┃ˑˑ┃ˑˑ┗━ Last Layer
> ┃ˑˑ┗━ Sublayer Two
> ┃ˑˑˑˑˑ┗━ Last Layer
> ┗━ One
> ˑˑˑTwo
> ˑˑˑThree
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- *InstanceStringError*
- *InstanceBooleanError*
- *NotExistingBranchError*

