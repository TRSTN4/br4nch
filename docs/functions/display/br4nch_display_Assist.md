# br4nch.display.Assist

To display a assist for an branch, use the **following function:**

> br4nch.**display**.**assist**(*branch*, *size=0*, *line=""*, *split=""*, *end=""*)

**Required argument(s):**

- *branch* - The branch(es) to display an assist for.

**Optional argument(s):**

- *size* - The size of the branch assist.
- *line* - The line symbol.
- *split* - The split symbol.
- *end* - The end symbol.

**Guide:**

> Prints the branch given in the `branch` argument with all positions linked to the corresponding layers. In this example we will print the branch `Stream`.
>
> ```python
> >>> br4nch.display.assist(branch="Stream")
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
> Prints the branch given in the `branch` argument with all positions linked to the corresponding layers with the given size, In this example `1`.
>
> ```python
> >>> br4nch.display.assist(branch="Stream", size=1)
> 0: Movies & Series
> ┃
> ┣━━ 1: Netflix
> ┃ˑˑˑ┃
> ┃ˑˑˑ┣━━ 1.1: Movies
> ┃ˑˑˑ┃ˑˑˑ┃
> ┃ˑˑˑ┃ˑˑˑ┗━━ 1.1.1: Interstellar
> ┃ˑˑˑ┃
> ┃ˑˑˑ┗━━ 1.2: Series
> ┃ˑˑˑˑˑˑˑ┃
> ┃ˑˑˑˑˑˑˑ┣━━ 1.2.1: Squid Game
> ┃ˑˑˑˑˑˑˑ┃
> ┃ˑˑˑˑˑˑˑ┗━━ 1.2.2: The Crown
> ┃
> ┗━━ 2: Prime Video
> ˑˑˑˑ┃
> ˑˑˑˑ┣━━ 2.1: Movies
> ˑˑˑˑ┃ˑˑˑ┃
> ˑˑˑˑ┃ˑˑˑ┣━━ 2.1.1: Tenet
> ˑˑˑˑ┃ˑˑˑ┃
> ˑˑˑˑ┃ˑˑˑ┗━━ 2.1.2: Parasite
> ˑˑˑˑ┃
> ˑˑˑˑ┗━━ 2.2: Series
> ˑˑˑˑˑˑˑˑ┃
> ˑˑˑˑˑˑˑˑ┗━━ 2.2.1: The Walking Dead
> ```
>
> Prints the branch given in the `branch` argument with all positions linked to the corresponding layers with custom `line`, `split` and `end` symbols.
>
> ```python
> >>> br4nch.display.assist(branch="Stream", line="║", split="╠═", end="╚═")
> 0: Movies & Series
> ╠═ 1: Netflix
> ║ˑˑ╠═ 1.1: Movies
> ║ˑˑ║ˑˑ╚═ 1.1.1: Interstellar
> ║ˑˑ╚═ 1.2: Series
> ║ˑˑˑˑˑ╠═ 1.2.1: Squid Game
> ║ˑˑˑˑˑ╚═ 1.2.2: The Crown
> ╚═ 2: Prime Video
> ˑˑˑ╠═ 2.1: Movies
> ˑˑˑ║ˑˑ╠═ 2.1.1: Tenet
> ˑˑˑ║ˑˑ╚═ 2.1.2: Parasite
> ˑˑˑ╚═ 2.2: Series
> ˑˑˑˑˑˑ╚═ 2.2.1: The Walking Dead
> ```
>
> To print an assist for multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.display.assist(branch=["Stream", "MyBranch"])
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

