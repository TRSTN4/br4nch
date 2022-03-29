# set.symbol

To set one or multiple symbol(s), use the **following function:**

> br4nch.**set**.**symbol**(*branch*, *line=""*, *split=""*, *end=""*)

**Required argument(s):**

- *branch* - The branch where the symbols are set.

**Optional argument(s):**

- *line* - The line symbol.
- *split* - The split symbol.
- *end* - The end symbol.

**Guide:**

> To add symbols, you must specify the name of the branch(es) and symbol(s) argument(s).
>
> ```python
> >>> br4nch.set.symbol(branch="Streaming", line="║", split="╠═", end="╚═")
> 
> >>> br4nch.display.branch(branch="Streaming")
> Movies & Series
> ╠═ Netflix
> ║ˑˑ╠═ Movies
> ║ˑˑ║ˑˑ╚═ Interstellar
> ║ˑˑ╚═ Series
> ║ˑˑˑˑˑ╠═ Squid Game
> ║ˑˑˑˑˑ╚═ The Crown
> ╚═ Prime Video
> ˑˑˑ╠═ Movies
> ˑˑˑ║ˑˑ╠═ Tenet
> ˑˑˑ║ˑˑ╚═ Parasite
> ˑˑˑ╚═ Series
> ˑˑˑˑˑˑ╚═ The Walking Dead
> ```
>
> To set the symbol(s) for multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.set.symbol(branch=["BranchOne", "BranchTwo"], line="║", split="╠═", end="╚═")
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- *InstanceStringError*
- *BooleanOnlyError*
- *NotExistingBranchError*
- *RequiredSymbolChangeError*

