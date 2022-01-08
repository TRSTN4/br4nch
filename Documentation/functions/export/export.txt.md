# export.txt

To export an branch to txt file, use the **following function:**

> br4nch.**export**.**txt**(*branch*, *directory*)

**Required arguments:**

- branch - This is the argument where you specify the branch(es) and the structure of that branch becomes the output.
- directory  - This is the argument where you specify the output for the txt file.

Here's an example:

```python
>>> br4nch.export.txt(branch="MyBranch", directory="D:/MyOutput")
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

>>> br4nch.export.txt(branch="Streaming", directory="D:/MyOutput")
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- NotExistingBranchError
- NotExistingDirectoryError

