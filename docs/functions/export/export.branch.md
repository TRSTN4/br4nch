# export.branch

To export an branch, use the **following function:**

> br4nch.**export**.**branch**(*branch*, *package=False*, *beautify=True*, *directory=""*)

**Required arguments:**

- branch - This is the argument where you specify the branch(es) and the structure of that branch becomes the output.

**Optional arguments:**

- package - If this argument is 'True', then the size, symbols and paint will also be exported.
- beautify - If this argument is 'True', then the result will be displayed with a special branch format.
- directory  - This is the argument where you specify the output directory.

Here's an example:

```python
>>> br4nch.export.branch(branch="MyBranch")
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

>>> br4nch.export.branch(branch="Streaming")
Export Result:
┗━ Branch: Streaming
   ┗━ Export: {'Streaming': {'Movies & Series': {'Netflix:uid=2176c8feb0': {'Movies:uid=81a3564e4b': {'Interstellar:uid=7146ab0e51': {}}, 'Series:uid=50d5b41788': {'Squid Game:uid=5066335af1': {}, 'The Crown:uid=b6ced91562': {}}}, 'Prime Video:uid=d9139fd0ed': {'Movies:uid=432e107f88': {'Tenet:uid=8f3d4b6b92': {}, 'Parasite:uid=f308d76354': {}}, 'Series:uid=6275151659': {'The Walking Dead:uid=a08ac0ed1d': {}}}}}}

>>> br4nch.export.branch(branch="Streaming", package=True)
Export Result:
┗━ Branch: Streaming
   ┣━ Export: {'Streaming': {'Movies & Series': {'Netflix:uid=a1d87bce71': {'Movies:uid=c34df53a8d': {'Interstellar:uid=61305cd343': {}}, 'Series:uid=14449b49c6': {'Squid Game:uid=fa7882ffe0': {}, 'The Crown:uid=601c5dd87a': {}}}, 'Prime Video:uid=941098fd75': {'Movies:uid=e310a99478': {'Tenet:uid=9c63c9ba71': {}, 'Parasite:uid=cb002cde10': {}}, 'Series:uid=9a1b5a7a3a': {'The Walking Dead:uid=8086de715e': {}}}}}}
   ┗━ Package: {'Streaming': [['a1d87bce71', '941098fd75', 'c34df53a8d', '14449b49c6', 'e310a99478', '9a1b5a7a3a', '61305cd343', 'fa7882ffe0', '601c5dd87a', '9c63c9ba71', 'cb002cde10', '8086de715e'], 0, {'line': '┃', 'split': '┣━', 'end': '┗━'}, [], [], {'Netflix:uid=a1d87bce71': [], 'Prime Video:uid=941098fd75': [], 'Movies:uid=c34df53a8d': [], 'Series:uid=14449b49c6': [], 'Movies:uid=e310a99478': [], 'Series:uid=9a1b5a7a3a': [], 'Interstellar:uid=61305cd343': [], 'Squid Game:uid=fa7882ffe0': [], 'The Crown:uid=601c5dd87a': [], 'Tenet:uid=9c63c9ba71': [], 'Parasite:uid=cb002cde10': [], 'The Walking Dead:uid=8086de715e': []}]}

>>> br4nch.export.branch(branch="Streaming", package=True, directory="D:/MyOutput")
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- InstanceBooleanError
- NotExistingBranchError
- NotExistingDirectoryError

