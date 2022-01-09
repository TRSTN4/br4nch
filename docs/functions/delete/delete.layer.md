# delete.layer

To delete an layer, use the **following function:**

> br4nch.**delete**.**layer**(*branch*, *position*)

**Required arguments:**

- branch - This is the argument where you specify the name of the branch(es) to which the layer will be deleted.
- position - This is the argument where you specify the position(s) where the layer(s) will be deleted. For more information about positions, head to [positions](../../guides/positions.md).

Here's an example:

```python
>>> br4nch.delete.layer(branch="MyBranch", position="1")
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

>>> br4nch.delete.layer(branch="Streaming", position="1")

>>> br4nch.display.branch(branch="Streaming")
Movies & Series
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
