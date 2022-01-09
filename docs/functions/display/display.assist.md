# display.assist

To display a assist for an branch, use the **following function:**

> br4nch.**display**.**assist**(*branch*, *size=0*, *line=""*, *split=""*, *end=""*)

**Required arguments:**

- branch - This is the argument where you specify the branch(es) to display an assist for.

**Optional arguments:**

- size - This is the argument where you specify the size of the branch assist.
- line - This is the argument where you specify the line symbol.
- split - This is the argument where you specify the split symbol.
- end - This is the argument where you specify the end symbol.


Here's an example:

```python
>>> br4nch.display.assist(branch="MyBranch")
```

Here is an example in realistic usage:

```python
>>> br4nch.add.branch(branch="Streaming", header="Movies & Series")
>>> br4nch.add.layer(branch="Streaming", layer=["Netflix", "Prime Video"], position="0")
>>> br4nch.add.layer(branch="Streaming", layer=["Movies", "Series"], position="*")
>>> br4nch.add.layer(branch="Streaming", layer="Interstellar", position="1.1")
>>> br4nch.add.layer(branch="Streaming", layer=["Squid Game", "The Crown"], position="1.2")
>>> br4nch.add.layer(branch="Streaming", layer=["Tenet", "Parasite"], position="2.1")
>>> br4nch.add.layer(branch="Streaming", layer="The Walking Dead", position="2.2")

>>> br4nch.display.assist(branch="Streaming")
0: Movies & Series
┣━ 1: Netflix
┃   ┣━ 1.1: Movies
┃   ┃   ┗━ 1.1.1: Interstellar
┃   ┗━ 1.2: Series
┃       ┣━ 1.2.1: Squid Game
┃       ┗━ 1.2.2: The Crown
┗━━ 2: Prime Video
    ┣━ 2.1: Movies
    ┃   ┣━ 2.1.1: Tenet
    ┃   ┗━ 2.1.2: Parasite
    ┗━ 2.2: Series
        ┗━ 2.2.1: The Walking Dead

>>> br4nch.display.assist(branch="Streaming", size=1)
0: Movies & Series
┃
┣━━ 1: Netflix
┃   ┃
┃   ┣━━ 1.1: Movies
┃   ┃   ┃
┃   ┃   ┗━━ 1.1.1: Interstellar
┃   ┃
┃   ┗━━ 1.2: Series
┃       ┃
┃       ┣━━ 1.2.1: Squid Game
┃       ┃
┃       ┗━━ 1.2.2: The Crown
┃
┗━━ 2: Prime Video
    ┃
    ┣━━ 2.1: Movies
    ┃   ┃
    ┃   ┣━━ 2.1.1: Tenet
    ┃   ┃
    ┃   ┗━━ 2.1.2: Parasite
    ┃
    ┗━━ 2.2: Series
        ┃
        ┗━━ 2.2.1: The Walking Dead

>>> br4nch.display.assist(branch="Streaming", line="║", split="╠═", end="╚═")
0: Movies & Series
╠═ 1: Netflix
║  ╠═ 1.1: Movies
║  ║  ╚═ 1.1.1: Interstellar
║  ╚═ 1.2: Series
║     ╠═ 1.2.1: Squid Game
║     ╚═ 1.2.2: The Crown
╚═ 2: Prime Video
   ╠═ 2.1: Movies
   ║  ╠═ 2.1.1: Tenet
   ║  ╚═ 2.1.2: Parasite
   ╚═ 2.2: Series
      ╚═ 2.2.1: The Walking Dead
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- InstanceIntegerError
- InvalidSizeError
- NotExistingBranchError
