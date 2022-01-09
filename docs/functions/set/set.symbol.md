# set.symbol

To set one or multiple symbol(s), use the **following function:**

> br4nch.**set**.**symbol**(*branch*, *line=""*, *split=""*, *end=""*)

**Required arguments:**

- branch - This is the argument where you specify the branch(es) whose symbol(s) should be set.

**Optional arguments:**

- line - This is the argument where you specify the line symbol.
- split - This is the argument where you specify the split symbol.
- end - This is the argument where you specify the end symbol.

Here's an example:

```python
>>> br4nch.set.symbol(branch="MyBranch", line="║", split="╠═", end="╚═")
```

Here is an example in realistic usage:

```python
>>> br4nch.add.branch(branch="Streaming", header="Movies & Series")
>>> br4nch.add.layer(branch="Streaming", layer=["Netflix", "Prime Video"], pos="0")
>>> br4nch.add.layer(branch="Streaming", layer=["Movies", "Series"], pos="*")
>>> br4nch.add.layer(branch="Streaming", layer="Interstellar", pos="1.1")
>>> br4nch.add.layer(branch="Streaming", layer=["Squid Game", "The Crown"], pos="1.2")
>>> br4nch.add.layer(branch="Streaming", layer=["Tenet", "Parasite"], pos="2.1")
>>> br4nch.add.layer(branch="Streaming", layer="The Walking Dead", pos="2.2")

>>> br4nch.set.symbol(branch="Streaming", line="║", split="╠═", end="╚═")

>>> br4nch.display.branch(branch="Streaming")
Movies & Series
╠═ Netflix
║  ╠═ Movies
║  ║  ╚═ Interstellar
║  ╚═ Series
║     ╠═ Squid Game
║     ╚═ The Crown
╚═ Prime Video
   ╠═ Movies
   ║  ╠═ Tenet
   ║  ╚═ Parasite
   ╚═ Series
      ╚═ The Walking Dead
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- BooleanOnlyError
- NotExistingBranchError
- RequiredSymbolChangeError

