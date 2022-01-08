# add.layer

To create a new layer, use the **following function:**

> br4nch.**add**.**layer**(*branch*, *layer*, *position*)

**Required arguments:**

- branch - This is the argument where you specify the name of the branch(es) to which the new layer will be added.
- layer - This is the argument where you specify the name for the new layer(s) that will be added.
- position - This is the argument where you specify the position where the layer(s) are added. For more information about positions, head to [positions](../../guides/positions.md).

Here's an example:

```python
>>> br4nch.add.layer(branch="MyBranch", layer="MyLayer", position="0")
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

>>> br4nch.display.branch(branch="Streaming")
Movies & Series
┣━ Netflix
┃  ┣━ Movies
┃  ┃  ┗━ Interstellar
┃  ┗━ Series
┃     ┣━ Squid Game
┃     ┗━ The Crown
┗━ Prime Video
   ┣━ Movies
   ┃  ┣━ Tenet
   ┃  ┗━ Parasite
   ┗━ Series
      ┗━ The Walking Dead
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- InvalidPositionError
- NotExistingBranchError

