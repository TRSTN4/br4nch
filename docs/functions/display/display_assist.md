# display.Assist

To display a assist for an tree, use the **following function:**

> br4nch.**display**.**Assist**(*tree*)

**Required argument(s):**

- *tree* - The tree(s) to display an assist for.

**Guide:**

> To print a tree with all positions linked to the corresponding nodes, give the name of the tree in the `tree` argument. In this example we will print the tree`Stream`.
>
> ```python
> >>> br4nch.display.Assist(tree="Stream")
> 0: Movies & Series
> ┣━ 1: Netflix
> ┃ˑˑ┣━ 1.1: Movies
> ┃ˑˑ┃ˑˑ┗━ 1.1.1: Interstellar
> ┃ˑˑ┗━ 1.2: Series
> ┃ˑˑˑˑˑ┣━ 1.2.1: Squid Game
> ┃ˑˑˑˑˑ┗━ 1.2.2: The Crown
> ┗━ 2: Prime Video
> ˑˑˑ┣━ 2.1: Movies
> ˑˑˑ┃ˑˑ┣━ 2.1.1: Tenet
> ˑˑˑ┃ˑˑ┗━ 2.1.2: Parasite
> ˑˑˑ┗━ 2.2: Series
> ˑˑˑˑˑˑ┗━ 2.2.1: The Walking Dead
> ```
>
> To print an assist for multiple trees in the same function call, you can use a list for the `tree` argument.
>
> ```python
> >>> br4nch.display.Assist(tree=["Stream", "MyTree"])
> 0: Movies & Series
> ┣━ 1: Netflix
> ┃ˑˑ┣━ 1.1: Movies
> ┃ˑˑ┃ˑˑ┗━ 1.1.1: Interstellar
> ┃ˑˑ┗━ 1.2: Series
> ┃ˑˑˑˑˑ┣━ 1.2.1: Squid Game
> ┃ˑˑˑˑˑ┗━ 1.2.2: The Crown
> ┗━ 2: Prime Video
> ˑˑˑ┃ˑˑ┣━ 2.1.1: Tenet
> ˑˑˑ┃ˑˑ┗━ 2.1.2: Parasite
> ˑˑˑ┗━ 2.2: Series
> ˑˑˑˑˑˑ┗━ 2.2.1: The Walking Dead
> 0: My header!
> ┣━ 1: My Layer
> ┃ˑˑ┣━ 1.1: Sublayer One
> ┃ˑˑ┃ˑˑ┗━ 1.1.1: Last Layer
> ┃ˑˑ┗━ 1.2: Sublayer Two
> ┃ˑˑˑˑˑ┗━ 1.2.1: Last Layer
> ┗━ 2: One
> ˑˑˑˑˑˑTwo
> ˑˑˑˑˑˑThree
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- *InstanceStringError*
- *InstanceIntegerError*
- *InvalidSizeError*
- *NotExistingBranchError*

