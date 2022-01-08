# display.layer

To display a layer, use the **following function:**

> br4nch.**display**.**layer**(*branch*, *layer*, *sensitive=False*, *beautify=True*)

**Required arguments:**

- branch - This is the argument where you specify the branch(es) to display an layer for.
- layer - This is the argument where you specify the layer(s) that are displayed.

**Optional arguments:**

- sensitive - If this argument is 'True', then the layer is searched and compared with case-sensitive.
- beautify - If this argument is 'True', then the result will be displayed with a special branch format.

Here's an example:

```python
>>> br4nch.display.layer(branch="MyBranch", layer="MyLayer")
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

>>> br4nch.display.layer(branch="Streaming", layer="Squid Game")
Get Position Result:
┗━ Branch: Streaming
   ┗━ Layer: Squid Game
      ┗━ Position: 1.2.1

>>> br4nch.display.layer(branch="Streaming", layer="Squid Game", beautify=False)
1.2.1
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- InstanceBooleanError
- NotExistingBranchError

