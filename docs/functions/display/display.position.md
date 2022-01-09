# display.position

To display a position, use the **following function:**

> br4nch.**display**.**position**(*branch*, *position*, *beautify=True*)

**Required arguments:**

- branch - This is the argument where you specify the branch(es) to display an position for.
- position - This is the argument where you specify the position(s) that are displayed. For more information about positions, head to [positions](../../guides/positions.md).

**Optional arguments:**

- beautify - If this argument is 'True', then the result will be displayed with a special branch format.

Here's an example:

```python
>>> br4nch.display.position(branch="MyBranch", position="1")
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

>>> br4nch.display.position(branch="Streaming", position="1.2.1")
Get Position Result:
┗━ Branch: Streaming
   ┗━ Layer: Squid Game
      ┗━ Position: 1.2.1

>>> br4nch.display.position(branch="Streaming", position="1.2.1", beautify=False)
Squid Game
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- InstanceBooleanError
- InvalidPositionError
- NotExistingBranchError
