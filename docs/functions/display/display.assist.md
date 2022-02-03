# display.assist

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
> ┃‎‎┣━ 1.1: Movies
> ┃‎‎┃‎‎┗━ 1.1.1: Interstellar
> ┃‎‎┗━ 1.2: Series
> ┃‎‎‎‎‎┣━ 1.2.1: Squid Game
> ┃‎‎‎‎‎┗━ 1.2.2: The Crown
> ┗━ 2: Prime Video
>    ‎‎‎┣━ 2.1: Movies
>    ‎‎‎┃‎‎┣━ 2.1.1: Tenet
>    ‎‎‎┃‎‎┗━ 2.1.2: Parasite
>    ‎‎‎┗━ 2.2: Series
>    ‎‎‎‎‎‎┗━ 2.2.1: The Walking Dead
> ```
>
> Prints the branch given in the `branch` argument with all positions linked to the corresponding layers with the given size, In this example `1`.
>
> ```python
> >>> br4nch.display.assist(branch="Stream", size=1)
> 0: Movies & Series
> ┃
> ┣━━ 1: Netflix
> ┃‎‎‎┃
> ┃‎‎‎┣━━ 1.1: Movies
> ┃‎‎‎┃‎‎‎┃
> ┃‎‎‎┃‎‎‎┗━━ 1.1.1: Interstellar
> ┃‎‎‎┃
> ┃‎‎‎┗━━ 1.2: Series
> ┃‎‎‎‎‎‎‎┃
> ┃‎‎‎‎‎‎‎┣━━ 1.2.1: Squid Game
> ┃‎‎‎‎‎‎‎┃
> ┃‎‎‎‎‎‎‎┗━━ 1.2.2: The Crown
> ┃
> ┗━━ 2: Prime Video
>    ‎‎‎‎┃
>    ‎‎‎‎┣━━ 2.1: Movies
>    ‎‎‎‎┃‎‎‎┃
>    ‎‎‎‎┃‎‎‎┣━━ 2.1.1: Tenet
>    ‎‎‎‎┃‎‎‎┃
>    ‎‎‎‎┃‎‎‎┗━━ 2.1.2: Parasite
>    ‎‎‎‎┃
>    ‎‎‎‎┗━━ 2.2: Series
>    ‎‎‎‎‎‎‎‎┃
>    ‎‎‎‎‎‎‎‎┗━━ 2.2.1: The Walking Dead
> ```
>
> Prints the branch given in the `branch` argument with all positions linked to the corresponding layers with custom `line`, `split` and `end` symbols.
>
> ```python
> >>> br4nch.display.assist(branch="Stream", line="║", split="╠═", end="╚═")
> 0: Movies & Series
> ╠═ 1: Netflix
> ║‎‎╠═ 1.1: Movies
> ║‎‎║‎‎╚═ 1.1.1: Interstellar
> ║‎‎╚═ 1.2: Series
> ║‎‎‎‎‎╠═ 1.2.1: Squid Game
> ║‎‎‎‎‎╚═ 1.2.2: The Crown
> ╚═ 2: Prime Video
>    ‎‎‎╠═ 2.1: Movies
>    ‎‎‎║‎‎╠═ 2.1.1: Tenet
>    ‎‎‎║‎‎╚═ 2.1.2: Parasite
>    ‎‎‎╚═ 2.2: Series
>    ‎‎‎‎‎‎╚═ 2.2.1: The Walking Dead
> ```
>
> To print an assist for multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.display.assist(branch=["Stream", "MyBranch"])
> 0: Movies & Series
> ┣━ 1: Netflix
> ┃‎‎┣━ 1.1: Movies
> ┃‎‎┃‎‎┗━ 1.1.1: Interstellar
> ┃‎‎┗━ 1.2: Series
> ┃‎‎‎‎‎┣━ 1.2.1: Squid Game
> ┃‎‎‎‎‎┗━ 1.2.2: The Crown
> ┗━ 2: Prime Video
>    ‎‎‎┣━ 2.1: Movies
>    ‎‎‎┃‎‎┣━ 2.1.1: Tenet
>    ‎‎‎┃‎‎┗━ 2.1.2: Parasite
>    ‎‎‎┗━ 2.2: Series
>    ‎‎‎‎‎‎┗━ 2.2.1: The Walking Dead
> 0: My header!
> ┣━ 1: My Layer
> ┃‎‎┣━ 1.1: Sublayer One
> ┃‎‎┃‎‎┗━ 1.1.1: Last Layer
> ┃‎‎┗━ 1.2: Sublayer Two
> ┃‎‎‎‎‎┗━ 1.2.1: Last Layer
> ┗━ 2: One
>    ‎‎‎‎‎‎Two
>    ‎‎‎‎‎‎Three
> ```
>

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
For more information about errors, head to [errors](../../guides/errors.md).

- *InstanceStringError*
- *InstanceIntegerError*
- *InvalidSizeError*
- *NotExistingBranchError*

